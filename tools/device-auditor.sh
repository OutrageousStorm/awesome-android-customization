#!/bin/bash
# device-auditor.sh -- Full device security and customization audit
# Usage: ./device-auditor.sh

echo "📋 Android Device Audit Report"
echo "=========================================="

model=$(adb shell getprop ro.product.model)
android=$(adb shell getprop ro.build.version.release)
patch=$(adb shell getprop ro.build.version.security_patch)

echo "Device: $model | Android $android | Patch: $patch"
echo ""

# Check security properties
echo "Security Status:"
echo "  Build tags: $(adb shell getprop ro.build.tags)"
echo "  Bootloader: $(adb shell getprop ro.boot.verifiedbootstate)"
echo "  SELinux: $(adb shell getenforce 2>/dev/null || echo 'N/A')"
echo "  Root: $(adb shell which su 2>/dev/null && echo 'YES ⚠️' || echo 'No')"
echo "  Magisk: $(adb shell ls /sbin/.magisk 2>/dev/null && echo 'YES' || echo 'No')"

# Check device tree encryption
echo ""
echo "Encryption:"
echo "  /system: $(adb shell stat -c %a /system | grep -q 'rw' && echo 'RW (unusual)' || echo 'RO')"
echo "  /data: $(adb shell getprop ro.crypto.state)"
echo "  FBE: $(adb shell getprop ro.crypto.type)"

# Check for suspicious packages
echo ""
echo "Tracking apps:"
count=$(adb shell pm list packages | grep -E 'facebook|google\.gms|twitter|tiktok' | wc -l)
echo "  Found: $count social/tracker packages"

# Permission audit
echo ""
echo "Dangerous permissions granted:"
perms=$(adb shell dumpsys package | grep 'granted=true' | grep -E 'LOCATION|CONTACTS|CAMERA|MICROPHONE' | wc -l)
echo "  Total: $perms"

echo ""
echo "=========================================="
echo "✅ Audit complete"
