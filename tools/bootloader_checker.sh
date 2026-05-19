#!/bin/bash
# bootloader_checker.sh -- Check bootloader unlock status and security
# Usage: ./bootloader_checker.sh
adb_check() {
  adb shell getprop "$1"
}
echo "🔓 Bootloader Status Check"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━"
LOCKED=$(adb_check ro.boot.verifiedbootstate)
BL_STATE=$(adb_check ro.boot.bootloader)
SELINUX=$(adb_check ro.build.selinux)
echo "  Bootloader state: $LOCKED"
echo "  Bootloader ver:   $BL_STATE"
echo "  SELinux:          $SELINUX"
[[ "$LOCKED" == "green" ]] && echo "  ✓ Secure Boot enabled" || echo "  ⚠️  Bootloader unlocked"
