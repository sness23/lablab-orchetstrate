#!/usr/bin/env python3
"""
Simple test to verify we can connect to Chrome and advance one slide
"""

import json
import websocket
import requests
import time

def test_slide_advance():
    print("Testing Chrome slide control...")
    print("-" * 40)

    # Get Chrome tabs
    try:
        response = requests.get("http://localhost:9222/json")
        tabs = response.json()
        print(f"Found {len(tabs)} tabs")

        if not tabs:
            print("No tabs found!")
            return

        # Find the tab with slides
        slide_tab = None
        for tab in tabs:
            print(f"  Tab: {tab.get('title', 'Untitled')[:50]}")
            if 'slides' in tab.get('url', '').lower() or 'slide' in tab.get('title', '').lower():
                slide_tab = tab
                print(f"    ✓ Using this tab for slides")
                break

        # If no slide tab found, use the first regular tab
        if not slide_tab:
            for tab in tabs:
                if tab.get('type') == 'page' and not tab.get('url', '').startswith('chrome-extension'):
                    slide_tab = tab
                    print(f"  Using first available tab: {tab.get('title', 'Untitled')[:50]}")
                    break

        if not slide_tab:
            print("No suitable tab found!")
            return

        ws_url = slide_tab['webSocketDebuggerUrl']
        print(f"\nConnecting to: {ws_url}")

        # Connect with origin header
        ws = websocket.create_connection(
            ws_url,
            origin="http://localhost:9222"
        )
        print("✅ Connected!")

        print("\nWaiting 2 seconds...")
        time.sleep(2)

        print("Sending Arrow Right key...")

        # Send keyDown
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
        result = ws.recv()
        print(f"KeyDown response: {result}")

        # Small delay between down and up
        time.sleep(0.05)

        # Send keyUp
        command["id"] = 2
        command["params"]["type"] = "keyUp"

        ws.send(json.dumps(command))
        result = ws.recv()
        print(f"KeyUp response: {result}")

        print("\n✅ Arrow Right key sent!")
        print("Check if the slide advanced in Chrome")

        ws.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_slide_advance()