#!/usr/bin/env python3
"""
Automated presentation player that synchronizes audio playback with slide transitions
through a Chrome browser with remote debugging enabled.

Usage:
    1. Start Chrome with remote debugging:
       google-chrome --remote-debugging-port=9222 --user-data-dir=/home/sness/chrome/9222

    2. Open your slide presentation in Chrome (e.g., localhost:3000 with Marp slides)

    3. Run this script:
       python present.py
"""

import asyncio
import json
import time
import pygame
from pathlib import Path
import websocket
import requests
from typing import Dict, List, Optional
import threading
import sys

# Configuration
CHROME_DEBUG_PORT = 9222
AUDIO_DIR = Path(__file__).parent / "audio"

# Timing for each audio section (in seconds)
# These timings control when to advance slides
SECTION_TIMINGS = [
    # (audio_file, duration_seconds, slide_number)
    ("01_intro.mp3", 45, 1),           # Slide 1-2: Title & Problem
    ("02_solution.mp3", 30, 3),        # Slide 3: Solution
    ("03_lead_discovery.mp3", 30, 4),  # Slide 4-5: Alex Rives & Lead Discovery
    ("04_profile_builder.mp3", 30, 6), # Slide 6: Profile Builder
    ("05_product_match.mp3", 30, 7),   # Slide 7: Product Match
    ("06_smykm_outreach.mp3", 60, 8),  # Slide 8-9: SMYKM Email & Personalization
    ("07_bonus_features.mp3", 30, 10), # Slide 10: Bonus Features
    ("08_technical_roi.mp3", 30, 11),  # Slide 11-12: Technical & ROI
    ("09_closing.mp3", 15, 13),        # Slide 13: Thank You
]

# Alternative: Use full presentation with specific slide transition times
FULL_PRESENTATION_TIMINGS = [
    # (time_in_seconds, action)
    (0, "start"),           # Start presentation
    (20, "next"),          # Go to slide 2 (Problem)
    (45, "next"),          # Go to slide 3 (Solution)
    (75, "next"),          # Go to slide 4 (Alex Rives)
    (90, "next"),          # Go to slide 5 (Lead Discovery)
    (105, "next"),         # Go to slide 6 (Profile Builder)
    (135, "next"),         # Go to slide 7 (Product Match)
    (165, "next"),         # Go to slide 8 (SMYKM Email)
    (195, "next"),         # Go to slide 9 (Personalization Hooks)
    (225, "next"),         # Go to slide 10 (Bonus Features)
    (255, "next"),         # Go to slide 11 (Technical)
    (270, "next"),         # Go to slide 12 (ROI)
    (285, "next"),         # Go to slide 13 (Thank You)
]

class ChromeController:
    """Controls Chrome browser via DevTools Protocol"""

    def __init__(self, port: int = 9222):
        self.port = port
        self.ws = None
        self.current_id = 1

    def connect(self) -> bool:
        """Connect to Chrome DevTools"""
        try:
            # Get WebSocket debugger URL
            response = requests.get(f"http://localhost:{self.port}/json")
            pages = response.json()

            if not pages:
                print("No tabs open in Chrome")
                return False

            # Use the first tab
            ws_url = pages[0]['webSocketDebuggerUrl']
            print(f"Connecting to: {ws_url}")

            self.ws = websocket.create_connection(ws_url)
            return True

        except Exception as e:
            print(f"Failed to connect to Chrome: {e}")
            return False

    def send_command(self, method: str, params: Dict = None) -> Dict:
        """Send command to Chrome DevTools"""
        if not self.ws:
            return None

        command = {
            "id": self.current_id,
            "method": method,
            "params": params or {}
        }

        self.current_id += 1
        self.ws.send(json.dumps(command))

        # Wait for response
        response = json.loads(self.ws.recv())
        return response

    def press_key(self, key: str):
        """Simulate key press in Chrome"""
        # Key codes for navigation
        key_codes = {
            "ArrowRight": 39,
            "ArrowLeft": 37,
            "ArrowDown": 40,
            "ArrowUp": 38,
            "Space": 32,
            "Enter": 13,
            "PageDown": 34,
            "PageUp": 33,
            "Home": 36,
            "End": 35,
            "f": 70,  # Fullscreen in many presentation tools
            "Escape": 27
        }

        if key not in key_codes:
            print(f"Unknown key: {key}")
            return

        code = key_codes[key]

        # Send keydown event
        self.send_command("Input.dispatchKeyEvent", {
            "type": "keyDown",
            "key": key,
            "code": key,
            "windowsVirtualKeyCode": code,
            "nativeVirtualKeyCode": code
        })

        # Send keyup event
        self.send_command("Input.dispatchKeyEvent", {
            "type": "keyUp",
            "key": key,
            "code": key,
            "windowsVirtualKeyCode": code,
            "nativeVirtualKeyCode": code
        })

    def next_slide(self):
        """Go to next slide"""
        self.press_key("ArrowRight")
        print("→ Next slide")

    def prev_slide(self):
        """Go to previous slide"""
        self.press_key("ArrowLeft")
        print("← Previous slide")

    def go_to_start(self):
        """Go to first slide"""
        self.press_key("Home")
        print("⏮ First slide")

    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self.press_key("f")
        print("🖥 Toggled fullscreen")

    def close(self):
        """Close WebSocket connection"""
        if self.ws:
            self.ws.close()

class AudioPlayer:
    """Handles audio playback"""

    def __init__(self):
        pygame.mixer.init()
        self.current_sound = None

    def play_file(self, file_path: Path):
        """Play an audio file"""
        if self.current_sound:
            self.current_sound.stop()

        print(f"🔊 Playing: {file_path.name}")
        self.current_sound = pygame.mixer.Sound(str(file_path))
        self.current_sound.play()

    def stop(self):
        """Stop current playback"""
        if self.current_sound:
            self.current_sound.stop()

    def is_playing(self) -> bool:
        """Check if audio is still playing"""
        return pygame.mixer.get_busy()

    def wait_for_finish(self):
        """Wait for current audio to finish"""
        while self.is_playing():
            time.sleep(0.1)

class PresentationController:
    """Main presentation controller"""

    def __init__(self):
        self.chrome = ChromeController(CHROME_DEBUG_PORT)
        self.audio = AudioPlayer()
        self.running = False

    def run_individual_sections(self):
        """Play individual audio sections with timed slide transitions"""
        print("\n🎭 Starting presentation with individual sections...\n")

        # Connect to Chrome
        if not self.chrome.connect():
            print("Failed to connect to Chrome. Make sure Chrome is running with --remote-debugging-port=9222")
            return

        # Go to first slide
        self.chrome.go_to_start()
        time.sleep(1)

        # Optional: Enter fullscreen
        print("Press 'f' in Chrome to enter fullscreen mode, then press Enter here...")
        input()

        current_slide = 1

        for audio_file, duration, target_slide in SECTION_TIMINGS:
            audio_path = AUDIO_DIR / audio_file

            if not audio_path.exists():
                print(f"⚠️ Audio file not found: {audio_path}")
                continue

            # Navigate to target slide if needed
            while current_slide < target_slide:
                self.chrome.next_slide()
                current_slide += 1
                time.sleep(0.5)

            # Play audio
            self.audio.play_file(audio_path)

            # Wait for audio to finish or duration to pass
            start_time = time.time()
            while self.audio.is_playing() and (time.time() - start_time) < duration:
                time.sleep(0.1)

            # Small pause between sections
            time.sleep(0.5)

        print("\n✅ Presentation complete!")
        self.chrome.close()

    def run_full_presentation(self):
        """Play full presentation audio with precisely timed slide transitions"""
        print("\n🎭 Starting full presentation...\n")

        # Connect to Chrome
        if not self.chrome.connect():
            print("Failed to connect to Chrome. Make sure Chrome is running with --remote-debugging-port=9222")
            return

        # Go to first slide
        self.chrome.go_to_start()
        time.sleep(1)

        # Optional: Enter fullscreen
        print("Press 'f' in Chrome to enter fullscreen mode, then press Enter here...")
        input()

        # Play full audio
        audio_path = AUDIO_DIR / "full_presentation.mp3"
        if not audio_path.exists():
            print(f"⚠️ Full presentation audio not found: {audio_path}")
            return

        self.audio.play_file(audio_path)
        start_time = time.time()

        # Schedule slide transitions
        transition_index = 0

        while self.audio.is_playing():
            elapsed = time.time() - start_time

            # Check if we need to transition
            if transition_index < len(FULL_PRESENTATION_TIMINGS):
                transition_time, action = FULL_PRESENTATION_TIMINGS[transition_index]

                if elapsed >= transition_time:
                    if action == "next":
                        self.chrome.next_slide()
                    elif action == "start":
                        print("🎬 Presentation started")

                    transition_index += 1

            time.sleep(0.1)

        print("\n✅ Presentation complete!")
        self.chrome.close()

    def run_interactive(self):
        """Interactive mode for testing"""
        print("\n🎮 Interactive Mode\n")
        print("Commands:")
        print("  n/right  - Next slide")
        print("  p/left   - Previous slide")
        print("  s/home   - Start (first slide)")
        print("  f        - Toggle fullscreen")
        print("  1-9      - Play audio section")
        print("  0        - Play full presentation")
        print("  q        - Quit\n")

        if not self.chrome.connect():
            print("Failed to connect to Chrome")
            return

        while True:
            cmd = input("Command: ").strip().lower()

            if cmd in ['n', 'right']:
                self.chrome.next_slide()
            elif cmd in ['p', 'left']:
                self.chrome.prev_slide()
            elif cmd in ['s', 'home']:
                self.chrome.go_to_start()
            elif cmd == 'f':
                self.chrome.toggle_fullscreen()
            elif cmd in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                section_num = int(cmd)
                audio_file = f"0{section_num}_*.mp3"
                files = list(AUDIO_DIR.glob(audio_file))
                if files:
                    self.audio.play_file(files[0])
                else:
                    print(f"Audio section {section_num} not found")
            elif cmd == '0':
                audio_path = AUDIO_DIR / "full_presentation.mp3"
                if audio_path.exists():
                    self.audio.play_file(audio_path)
                else:
                    print("Full presentation audio not found")
            elif cmd == 'q':
                break
            else:
                print("Unknown command")

        self.audio.stop()
        self.chrome.close()

def main():
    """Main entry point"""
    print("=" * 50)
    print("  TechBio Lead Gen - Presentation Automator")
    print("=" * 50)

    controller = PresentationController()

    print("\nSelect mode:")
    print("1. Full presentation (automatic)")
    print("2. Individual sections (automatic)")
    print("3. Interactive mode (manual control)")
    print("4. Exit")

    choice = input("\nChoice (1-4): ").strip()

    if choice == '1':
        controller.run_full_presentation()
    elif choice == '2':
        controller.run_individual_sections()
    elif choice == '3':
        controller.run_interactive()
    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        pygame.mixer.quit()
        sys.exit(0)