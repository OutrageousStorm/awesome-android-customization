#!/bin/bash
# Install LineageOS on a given device (interactive guide + auto-flash)
set -e
echo "🔄 LineageOS Flash Helper"
read -p "Device codename (e.g. coral, bluejay): " DEVICE
read -p "Path to lineage-XX.X-$DEVICE.zip: " ZIP

[[ ! -f "$ZIP" ]] && echo "File not found" && exit 1

echo "Device: $DEVICE"
echo "File: $ZIP"
echo "Unlocking bootloader (wipes data)..."
adb reboot bootloader
sleep 3
fastboot flashing unlock
sleep 2

echo "Flashing recovery (TWRP)..."
read -p "Path to twrp.img: " TWRP
fastboot flash recovery "$TWRP"

echo "Booting into recovery..."
fastboot boot "$TWRP"
sleep 3

echo "Sideloading ROM..."
adb sideload "$ZIP"
echo "✅ Done! Device will auto-reboot"
