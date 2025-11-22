#!/bin/bash
# Start Chrome with proper remote debugging flags

echo "Starting Chrome with remote debugging enabled..."
echo ""

# Method 1: Using quotes (recommended)
google-chrome --remote-debugging-port=9222 '--remote-allow-origins=*' --user-data-dir=/home/sness/chrome/9222

# Alternative methods that also work:
# Method 2: Backslash escape
# google-chrome --remote-debugging-port=9222 --remote-allow-origins=\* --user-data-dir=/home/sness/chrome/9222

# Method 3: Double quotes
# google-chrome --remote-debugging-port=9222 "--remote-allow-origins=*" --user-data-dir=/home/sness/chrome/9222

# Method 4: Full path with all origins
# google-chrome --remote-debugging-port=9222 --remote-allow-origins=http://localhost:9222,http://127.0.0.1:9222 --user-data-dir=/home/sness/chrome/9222