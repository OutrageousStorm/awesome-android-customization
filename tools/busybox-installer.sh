#!/bin/bash
# busybox-installer.sh -- Download, push, and install busybox on Android
# Adds essential Linux utilities: grep, awk, sed, find, etc.
# Usage: ./busybox-installer.sh
set -e

ARCH=$(adb shell getprop ro.product.cpu.abi)
BUSYBOX_URL="https://busybox.net/downloads/binaries"

case "$ARCH" in
  arm64-v8a)  URL="$BUSYBOX_URL/1.35.0-arm64/busybox" ;;
  armeabi-v7a) URL="$BUSYBOX_URL/1.35.0-arm/busybox" ;;
  x86_64)     URL="$BUSYBOX_URL/1.35.0-x86_64/busybox" ;;
  *)          echo "Unsupported arch: $ARCH"; exit 1 ;;
esac

echo "📦 Installing busybox for $ARCH"
echo "Downloading from: $URL"

# Download
if ! curl -L -o busybox "$URL" 2>/dev/null; then
  echo "Failed to download. Try manual download from busybox.net"
  exit 1
fi

chmod +x busybox
echo "✓ Downloaded"

# Push to device
adb push busybox /data/local/tmp/
echo "✓ Pushed to device"

# Install
adb shell "chmod +x /data/local/tmp/busybox && /data/local/tmp/busybox --install -s /data/local/bin"
echo "✓ Installed to /data/local/bin"

# Verify
if adb shell /data/local/bin/grep --version &>/dev/null; then
  echo "✅ grep works! Other tools available:"
  adb shell /data/local/bin/busybox --list | head -20
  echo "..."
  echo "Add to PATH: adb shell 'echo export PATH=/data/local/bin:\$PATH >> /data/local/tmp/shell.rc'"
else
  echo "⚠️  Installation may have failed. Check manually."
fi

rm busybox
