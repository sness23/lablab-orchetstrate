#!/usr/bin/env python3
"""
Simple automated presentation player for the hackathon demo.
Plays the full presentation audio while advancing slides at specific timestamps.

Setup:
1. Start Chrome: google-chrome --remote-debugging-port=9222 --user-data-dir=/home/sness/chrome/9222
2. Open your slides in Chrome
3. Run: python auto_present.py
"""

import json
import time
import pygame
import websocket
import requests
from pathlib import Path
import sys

# Slide transition times (in seconds from start)
SLIDE_TRANSITIONS = [
    (0, "Slide 1: Title"),
    (20, "Slide 2: The Problem"),
    (45, "Slide 3: Solution - 4 AI Agents"),
    (75, "Slide 4: Alex Rives Introduction"),
    (90, "Slide 5: Lead Discovery Score"),
    (105, "Slide 6: Profile Builder - Pain Point"),
    (135, "Slide 7: Product Match - Rigaku"),
    (165, "Slide 8: SMYKM Email"),
    (195, "Slide 9: Personalization Hooks"),
    (225, "Slide 10: Bonus Features"),
    (255, "Slide 11: Technical Architecture"),
    (270, "Slide 12: ROI Impact"),
    (285, "Slide 13: Thank You"),
]

def connect_to_chrome(port=9222):
    """Connect to Chrome DevTools"""
    try:
        response = requests.get(f"http://localhost:{port}/json")
        pages = response.json()
        if not pages:
            return None
        return websocket.create_connection(pages[0]['webSocketDebuggerUrl'])
    except Exception as e:
        print(f"Error connecting to Chrome: {e}")
        return None

def send_arrow_right(ws):
    """Send right arrow key to advance slide"""
    command = {
        "id": 1,
        "method": "Input.dispatchKeyEvent",
        "params": {
            "type": "keyDown",
            "key": "ArrowRight",
            "code": "ArrowRight",
            "windowsVirtualKeyCode": 39,
            "nativeVirtualKeyCode": 39
        }
    }
    ws.send(json.dumps(command))

    command["params"]["type"] = "keyUp"
    ws.send(json.dumps(command))

def main():
    print("=" * 60)
    print("  🎭 TechBio Lead Gen - Automated Presentation Player")
    print("=" * 60)
    print()

    # Check audio file
    audio_path = Path(__file__).parent / "audio" / "full_presentation.mp3"
    if not audio_path.exists():
        print(f"❌ Audio file not found: {audio_path}")
        print("Please run generate_speech.py first to create the audio files.")
        return

    # Connect to Chrome
    print("📡 Connecting to Chrome on port 9222...")
    ws = connect_to_chrome()
    if not ws:
        print("❌ Failed to connect to Chrome.")
        print("Make sure Chrome is running with:")
        print("google-chrome --remote-debugging-port=9222 --user-data-dir=/home/sness/chrome/9222")
        return

    print("✅ Connected to Chrome")
    print()
    print("📋 Instructions:")
    print("1. Make sure your slides are open in Chrome")
    print("2. Click on the Chrome window to focus it")
    print("3. Press F11 for fullscreen (optional)")
    print("4. Press Home key to go to first slide")
    print()
    input("Press Enter when ready to start the presentation...")
    print()

    # Initialize pygame for audio
    pygame.mixer.init()

    # Countdown
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    print()
    print("🎬 Starting presentation!")
    print("-" * 40)

    # Play audio
    sound = pygame.mixer.Sound(str(audio_path))
    sound.play()
    start_time = time.time()

    # Track slide transitions
    transition_index = 0
    current_slide = 1

    try:
        while pygame.mixer.get_busy():
            elapsed = time.time() - start_time

            # Check for next transition
            if transition_index < len(SLIDE_TRANSITIONS):
                transition_time, slide_name = SLIDE_TRANSITIONS[transition_index]

                if elapsed >= transition_time:
                    if transition_index > 0:  # Don't advance on first slide
                        send_arrow_right(ws)
                        current_slide += 1

                    # Display progress
                    minutes = int(elapsed // 60)
                    seconds = int(elapsed % 60)
                    print(f"[{minutes:02d}:{seconds:02d}] → {slide_name}")

                    transition_index += 1

            # Small delay to prevent busy-waiting
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n\n⚠️ Presentation interrupted by user")
        sound.stop()

    finally:
        # Cleanup
        ws.close()
        pygame.mixer.quit()

        # Final message
        elapsed_total = time.time() - start_time
        minutes = int(elapsed_total // 60)
        seconds = int(elapsed_total % 60)
        print("-" * 40)
        print(f"✅ Presentation complete!")
        print(f"⏱️ Total time: {minutes:02d}:{seconds:02d}")
        print(f"📊 Slides shown: {current_slide}/{len(SLIDE_TRANSITIONS)}")

if __name__ == "__main__":
    main()