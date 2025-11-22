#!/usr/bin/env python3
"""
Automatic presentation player - starts immediately without prompts
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
        tabs = response.json()
        if not tabs:
            return None

        # Find the tab with slides
        slide_tab = None
        for tab in tabs:
            if 'slides' in tab.get('url', '').lower() or 'slide' in tab.get('title', '').lower():
                slide_tab = tab
                print(f"  Found slide tab: {tab.get('title', 'Untitled')[:50]}")
                break

        # If no slide tab found, use the first regular tab
        if not slide_tab:
            for tab in tabs:
                if tab.get('type') == 'page' and not tab.get('url', '').startswith('chrome-extension'):
                    slide_tab = tab
                    break

        if not slide_tab:
            return None

        ws_url = slide_tab['webSocketDebuggerUrl']
        return websocket.create_connection(
            ws_url,
            origin="http://localhost:9222"
        )
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
            "nativeVirtualKeyCode": 39,
            "text": "",
            "unmodifiedText": "",
            "autoRepeat": False,
            "isKeypad": False,
            "isSystemKey": False
        }
    }
    ws.send(json.dumps(command))
    ws.recv()  # Wait for response

    time.sleep(0.05)  # Small delay between down and up

    command["id"] = 2
    command["params"]["type"] = "keyUp"
    ws.send(json.dumps(command))
    ws.recv()  # Wait for response

def send_home_key(ws):
    """Send Home key to go to first slide"""
    command = {
        "id": 1,
        "method": "Input.dispatchKeyEvent",
        "params": {
            "type": "keyDown",
            "key": "Home",
            "code": "Home",
            "windowsVirtualKeyCode": 36,
            "nativeVirtualKeyCode": 36,
            "text": "",
            "unmodifiedText": "",
            "autoRepeat": False,
            "isKeypad": False,
            "isSystemKey": False
        }
    }
    ws.send(json.dumps(command))
    ws.recv()  # Wait for response

    time.sleep(0.05)  # Small delay between down and up

    command["id"] = 2
    command["params"]["type"] = "keyUp"
    ws.send(json.dumps(command))
    ws.recv()  # Wait for response

def main():
    print("=" * 60)
    print("  🎭 TechBio Lead Gen - Starting Presentation NOW!")
    print("=" * 60)
    print()

    # Check audio file
    audio_path = Path(__file__).parent / "audio" / "full_presentation.mp3"
    if not audio_path.exists():
        print(f"❌ Audio file not found: {audio_path}")
        return

    # Connect to Chrome
    print("📡 Connecting to Chrome...")
    ws = connect_to_chrome()
    if not ws:
        print("❌ Failed to connect to Chrome.")
        return

    print("✅ Connected to Chrome")
    print()

    # Go to first slide
    print("⏮ Going to first slide...")
    send_home_key(ws)
    time.sleep(1)

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