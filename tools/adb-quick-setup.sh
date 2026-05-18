#!/bin/bash
# adb-quick-setup.sh -- Enable USB debugging and set up ADB in one command
# Usage: ./adb-quick-setup.sh
# Guides user through the UI since it must be done manually
set -e

echo "🔧 Android USB Debugging Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "This will guide you through enabling USB debugging on your Android device."
echo "Make sure your device is connected via USB cable."
echo ""

# Check if adb is available
if ! command -v adb &> /dev/null; then
    echo "❌ adb not found in PATH"
    echo "Install: apt install android-tools-adb (Linux) or brew install android-platform-tools (Mac)"
    exit 1
fi

# Wait for device
echo "📱 Waiting for device connection..."
timeout=30
while ! adb devices | grep -q "device$"; do
    ((timeout--))
    [[ $timeout -lt 0 ]] && echo "❌ No device found after 30 seconds" && exit 1
    sleep 1
done

echo "✓ Device found!"
echo ""
echo "Now follow these steps on your device:"
echo "1. Go to Settings > About Phone"
echo "2. Tap 'Build Number' 7 times (until 'You are a developer' appears)"
echo "3. Go to Settings > Developer Options"
echo "4. Enable 'USB Debugging'"
echo "5. Allow the USB Debugging permission prompt"
echo ""
read -p "Press Enter once you've enabled USB Debugging on the device..."

# Verify
adb devices
adb shell getprop ro.product.model && echo "✅ ADB setup complete!" || echo "⚠️  Still not responding"
