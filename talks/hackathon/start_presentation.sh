#!/bin/bash
# Start script for the automated presentation

echo "=================================================="
echo "  TechBio Lead Gen - Presentation Setup"
echo "=================================================="
echo ""

# Check if Chrome is already running with debug port
if curl -s http://localhost:9222/json > /dev/null 2>&1; then
    echo "✅ Chrome is already running with remote debugging"
else
    echo "Starting Chrome with remote debugging..."
    echo ""
    echo "Please run this command in a separate terminal:"
    echo ""
    echo "google-chrome --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir=/home/sness/chrome/9222"
    echo ""
    echo "Or for a cleaner presentation mode:"
    echo "google-chrome --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir=/home/sness/chrome/9222 --kiosk"
    echo ""
    echo "Press Enter once Chrome is running..."
    read
fi

echo ""
echo "📋 Presentation Setup:"
echo "1. Open your slides in Chrome (e.g., http://localhost:3000 for Marp)"
echo "2. Navigate to the first slide"
echo "3. Press F11 for fullscreen (optional)"
echo ""
echo "Press Enter when ready..."
read

echo ""
echo "Select presentation mode:"
echo "1. Automatic - Full presentation with timed slides"
echo "2. Interactive - Manual control with audio sections"
echo "3. Test only - Test Chrome connection"
echo ""
read -p "Choice (1-3): " choice

case $choice in
    1)
        echo "Starting automatic presentation..."
        python auto_present.py
        ;;
    2)
        echo "Starting interactive mode..."
        python present.py
        ;;
    3)
        echo "Testing Chrome connection..."
        python test_chrome.py
        ;;
    *)
        echo "Invalid choice"
        ;;
esac