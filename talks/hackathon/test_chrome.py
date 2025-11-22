#!/usr/bin/env python3
"""
Test Chrome remote control connection
"""

import json
import websocket
import requests
import time

def test_chrome_connection():
    """Test connection to Chrome DevTools"""
    print("Testing Chrome DevTools connection...")
    print("-" * 40)

    try:
        # Get list of tabs
        response = requests.get("http://localhost:9222/json")
        tabs = response.json()

        print(f"✅ Found {len(tabs)} open tabs:")
        for i, tab in enumerate(tabs, 1):
            print(f"  {i}. {tab.get('title', 'Untitled')[:50]}")
            print(f"     URL: {tab.get('url', 'N/A')[:60]}")

        if tabs:
            # Connect to first tab
            ws_url = tabs[0]['webSocketDebuggerUrl']
            print(f"\n📡 Connecting to WebSocket...")
            print(f"   {ws_url}")

            # Try to connect with origin header
            ws = websocket.create_connection(
                ws_url,
                origin="http://localhost:9222"
            )
            print("✅ WebSocket connected!")

            # Send a test command (get page info)
            command = {
                "id": 1,
                "method": "Page.getNavigationHistory"
            }
            ws.send(json.dumps(command))
            response = ws.recv()
            print("\n✅ Successfully sent and received DevTools command")

            ws.close()
            print("\n🎉 All tests passed! Chrome automation is ready.")
            return True

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Chrome on port 9222")
        print("\nMake sure Chrome is running with:")
        print("google-chrome --remote-debugging-port=9222 --user-data-dir=/home/sness/chrome/9222")
        return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_chrome_connection()