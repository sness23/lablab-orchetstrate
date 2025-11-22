#!/usr/bin/env python3
"""
Synchronized presentation player that plays each slide's audio
and advances automatically to the next slide.
Perfect synchronization between narration and slides.
"""

import json
import time
import pygame
import websocket
import requests
from pathlib import Path
import sys

# Audio files for each slide (in order)
SLIDE_AUDIO_FILES = [
    "slide_01_title.mp3",
    "slide_02_problem.mp3",
    "slide_03_solution.mp3",
    "slide_04_alex_rives.mp3",
    "slide_05_lead_discovery.mp3",
    "slide_06_profile_builder.mp3",
    "slide_07_product_match.mp3",
    "slide_08_smykm_outreach.mp3",
    "slide_09_personalization.mp3",
    "slide_10_bonus_features.mp3",
    "slide_11_technical.mp3",
    "slide_12_roi.mp3",
    "slide_13_thank_you.mp3",
]

# Slide titles for display
SLIDE_TITLES = [
    "Slide 1: TechBio Lead Gen and SMYKM - Title",
    "Slide 2: The Problem - 80% Research Time",
    "Slide 3: Our Solution - 4 AI Agents",
    "Slide 4: Demo - Alex Rives Target Lead",
    "Slide 5: Step 1 - Lead Discovery",
    "Slide 6: Step 2 - Profile Builder",
    "Slide 7: Step 3 - Product Match",
    "Slide 8: Step 4 - SMYKM Outreach",
    "Slide 9: Key Personalization Hooks",
    "Slide 10: Bonus Features - Sales Toolkit",
    "Slide 11: Technical Implementation",
    "Slide 12: ROI Impact - The Numbers",
    "Slide 13: Thank You",
]

class ChromeSlideController:
    """Controls Chrome browser for slide navigation"""

    def __init__(self):
        self.ws = None

    def connect(self):
        """Connect to Chrome DevTools"""
        try:
            response = requests.get("http://localhost:9222/json")
            tabs = response.json()

            if not tabs:
                print("❌ No tabs found in Chrome")
                return False

            # Find the tab with slides - look for localhost:3000 or slides in URL/title
            slide_tab = None
            for tab in tabs:
                url = tab.get('url', '').lower()
                title = tab.get('title', '').lower()
                # Check for React app on port 3000 or slides in URL/title
                if 'localhost:3000' in url or ':3000' in url or 'slides' in url or 'slide' in title:
                    slide_tab = tab
                    print(f"✓ Found slide tab: {tab.get('title', 'Untitled')[:50]}")
                    print(f"  URL: {tab.get('url', '')}")
                    break

            # If no slide tab found, use the first regular tab
            if not slide_tab:
                for tab in tabs:
                    if tab.get('type') == 'page' and not tab.get('url', '').startswith('chrome-extension'):
                        slide_tab = tab
                        print(f"  Using tab: {tab.get('title', 'Untitled')[:50]}")
                        break

            if not slide_tab:
                print("❌ No suitable tab found")
                return False

            # Connect with origin header
            self.ws = websocket.create_connection(
                slide_tab['webSocketDebuggerUrl'],
                origin="http://localhost:9222"
            )

            print("✅ Connected to Chrome")
            return True

        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            return False

    def send_key(self, key, key_code):
        """Send a keyboard key to Chrome"""
        if not self.ws:
            return

        # Send keydown
        command = {
            "id": 1,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "keyDown",
                "key": key,
                "code": key,
                "windowsVirtualKeyCode": key_code,
                "nativeVirtualKeyCode": key_code,
                "text": "",
                "unmodifiedText": "",
                "autoRepeat": False,
                "isKeypad": False,
                "isSystemKey": False
            }
        }
        self.ws.send(json.dumps(command))
        self.ws.recv()  # Wait for response

        time.sleep(0.05)  # Small delay

        # Send keyup
        command["id"] = 2
        command["params"]["type"] = "keyUp"
        self.ws.send(json.dumps(command))
        self.ws.recv()  # Wait for response

    def next_slide(self):
        """Advance to next slide"""
        self.send_key("ArrowRight", 39)

    def go_to_first_slide(self):
        """Go to first slide"""
        self.send_key("Home", 36)

    def close(self):
        """Close connection"""
        if self.ws:
            self.ws.close()

class SlidePresentation:
    """Main presentation controller"""

    def __init__(self):
        self.chrome = ChromeSlideController()
        self.audio_dir = Path(__file__).parent / "slide_audio"
        pygame.mixer.init()

    def play_audio(self, filename):
        """Play an audio file and wait for it to finish"""
        audio_path = self.audio_dir / filename

        if not audio_path.exists():
            print(f"⚠️ Audio file not found: {filename}")
            return 0

        # Load and play
        sound = pygame.mixer.Sound(str(audio_path))
        duration = sound.get_length()
        sound.play()

        return duration

    def wait_for_audio(self):
        """Wait for current audio to finish playing"""
        while pygame.mixer.get_busy():
            time.sleep(0.1)

    def run(self):
        """Run the complete presentation"""
        print("=" * 60)
        print("  🎭 Synchronized Slide Presentation")
        print("=" * 60)
        print()

        # Check if audio files exist
        missing_files = []
        for audio_file in SLIDE_AUDIO_FILES:
            if not (self.audio_dir / audio_file).exists():
                missing_files.append(audio_file)

        if missing_files:
            print("❌ Missing audio files:")
            for f in missing_files:
                print(f"  - {f}")
            print("\nPlease run: python split_audio_by_slide.py")
            return

        # Connect to Chrome
        if not self.chrome.connect():
            print("\n❌ Could not connect to Chrome")
            print("Make sure Chrome is running with:")
            print("google-chrome --remote-debugging-port=9222 '--remote-allow-origins=*' --user-data-dir=/home/sness/chrome/9222")
            return

        print("\n📋 Instructions:")
        print("1. Make sure your slides are visible in Chrome")
        print("2. Press F11 for fullscreen (optional)")
        print("3. The presentation will start in 3 seconds...")
        print()

        # Go to first slide
        print("⏮ Going to first slide...")
        self.chrome.go_to_first_slide()
        time.sleep(1)

        # Countdown
        for i in range(3, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)

        print("\n🎬 Starting presentation!")
        print("-" * 50)

        start_time = time.time()
        total_slides = len(SLIDE_AUDIO_FILES)

        try:
            for i, (audio_file, title) in enumerate(zip(SLIDE_AUDIO_FILES, SLIDE_TITLES), 1):
                # Show progress
                elapsed = time.time() - start_time
                minutes = int(elapsed // 60)
                seconds = int(elapsed % 60)
                print(f"[{minutes:02d}:{seconds:02d}] → {title}")

                # Play audio for this slide
                duration = self.play_audio(audio_file)

                # Wait for audio to complete
                self.wait_for_audio()

                # Small pause between slides
                if i < total_slides:
                    time.sleep(0.3)
                    # Advance to next slide
                    self.chrome.next_slide()
                    time.sleep(0.2)  # Give slide time to transition

        except KeyboardInterrupt:
            print("\n\n⚠️ Presentation interrupted")
            pygame.mixer.stop()

        finally:
            # Cleanup
            self.chrome.close()
            pygame.mixer.quit()

            # Summary
            total_time = time.time() - start_time
            minutes = int(total_time // 60)
            seconds = int(total_time % 60)
            print("-" * 50)
            print(f"✅ Presentation complete!")
            print(f"⏱️ Total time: {minutes:02d}:{seconds:02d}")

def main():
    presentation = SlidePresentation()
    presentation.run()

if __name__ == "__main__":
    main()