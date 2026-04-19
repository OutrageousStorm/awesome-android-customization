#!/bin/bash
set -e
OEM="$1"
echo "Debloating $OEM..."
adb shell pm uninstall -k --user 0 com.samsung.android.bixby.agent 2>/dev/null || true
