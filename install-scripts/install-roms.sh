#!/bin/bash
# install-roms.sh -- Download latest LineageOS, GrapheneOS, crDroid for your device
# Usage: ./install-roms.sh <device_codename>
# Example: ./install-roms.sh alioth   (POCO F3)

DEVICE="${1:?Usage: $0 <device_codename>}"
OUTDIR="./roms_$DEVICE"
mkdir -p "$OUTDIR"

echo "📥 Fetching custom ROMs for $DEVICE..."

# LineageOS
echo "  Checking LineageOS..."
LOS_URL=$(curl -s "https://download.lineageos.org/api/v1/$DEVICE/latest/download" | jq -r '.url' 2>/dev/null)
if [[ ! -z "$LOS_URL" ]]; then
  echo "  ✓ Found LineageOS"
  curl -# -L -o "$OUTDIR/lineageos.zip" "$LOS_URL" &
fi

# crDroid
echo "  Checking crDroid..."
CRDROID_URL=$(curl -s "https://crdroid.net/api/v2/$DEVICE" | jq -r '.response[0].url' 2>/dev/null)
if [[ ! -z "$CRDROID_URL" ]]; then
  echo "  ✓ Found crDroid"
  curl -# -L -o "$OUTDIR/crdroid.zip" "$CRDROID_URL" &
fi

# PixelOS
echo "  Checking PixelOS..."
PIXEL_URL=$(curl -s "https://api.pixelos.net/?json&device=$DEVICE" 2>/dev/null | jq -r '.devices[0].builds[0].download' 2>/dev/null)
if [[ ! -z "$PIXEL_URL" ]]; then
  echo "  ✓ Found PixelOS"
  curl -# -L -o "$OUTDIR/pixelos.zip" "$PIXEL_URL" &
fi

wait
echo "✅ ROMs saved to $OUTDIR"
ls -lh "$OUTDIR"
