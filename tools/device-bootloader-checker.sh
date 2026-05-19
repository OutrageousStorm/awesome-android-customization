#!/bin/bash
# device-bootloader-checker.sh - Check bootloader lock status and security posture
# Usage: ./device-bootloader-checker.sh

set -e
echo "🔒 Android Bootloader & Security Checker"
echo "========================================="

# Bootloader status
echo -e "\n[Bootloader]"
adb shell getprop ro.boot.verifiedbootstate
adb shell getprop ro.boot.veritymode
adb shell getprop ro.secure
adb shell getprop ro.debuggable

# Encryption
echo -e "\n[Encryption]"
adb shell getprop ro.crypto.state
adb shell getprop ro.crypto.type

# Kernel hardening
echo -e "\n[Kernel Hardening]"
adb shell cat /proc/cmdline | grep -o "selinux=\|dm-verity=\|root=" || echo "(basic cmdline)"

# AVB (Android Verified Boot) status
echo -e "\n[AVB Status]"
adb shell avbctl get-state 2>/dev/null || echo "AVB not available or locked"

# Summary
echo -e "\n[Security Posture]"
SECURE=$(adb shell getprop ro.secure)
if [[ "$SECURE" == "1" ]]; then
    echo "✅ ro.secure = 1 (production build)"
else
    echo "⚠️  ro.secure = 0 (test/userdebug build)"
fi
