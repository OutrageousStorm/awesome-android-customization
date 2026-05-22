#!/bin/bash
# Batch ADB Command Executor for Multiple Devices

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get connected devices
get_devices() {
    adb devices | grep -v "^$" | grep -v "List" | awk '{print $1}' | grep -v "device$" | head -1
}

# Execute command on all devices
batch_exec() {
    local cmd=$1
    local devices=$(adb devices | grep -v "^$" | grep "device$" | awk '{print $1}')
    
    if [ -z "$devices" ]; then
        echo -e "${RED}No devices found${NC}"
        return 1
    fi
    
    while IFS= read -r device; do
        echo -e "${YELLOW}[${device}]${NC} Executing: $cmd"
        adb -s "$device" shell $cmd 2>&1 | sed 's/^/  /' || true
    done <<< "$devices"
}

# Get all device properties
device_info() {
    local device=$1
    echo -e "${GREEN}Device: $device${NC}"
    echo "  Model: $(adb -s $device shell getprop ro.product.model)"
    echo "  Android: $(adb -s $device shell getprop ro.build.version.release)"
    echo "  API Level: $(adb -s $device shell getprop ro.build.version.sdk)"
    echo "  Battery: $(adb -s $device shell dumpsys battery | grep 'level:' | awk '{print $2}')%"
}

# List all connected devices with info
list_devices() {
    local devices=$(adb devices | grep -v "^$" | grep "device$" | awk '{print $1}')
    if [ -z "$devices" ]; then
        echo -e "${RED}No devices found${NC}"
        return 1
    fi
    while IFS= read -r device; do
        device_info "$device"
    done <<< "$devices"
}

# Install APK on all devices
batch_install() {
    local apk=$1
    if [ ! -f "$apk" ]; then
        echo -e "${RED}APK not found: $apk${NC}"
        return 1
    fi
    batch_exec "pm install -r -g $(basename $apk)" || batch_exec "install -r -g $apk"
}

# Uninstall package from all devices
batch_uninstall() {
    local pkg=$1
    batch_exec "pm uninstall $pkg"
}

# Main menu
if [ $# -eq 0 ]; then
    echo "ADB Batch Command Executor"
    echo ""
    echo "Usage:"
    echo "  $0 list                    List all connected devices"
    echo "  $0 exec '<command>'        Execute command on all devices"
    echo "  $0 install <apk>           Install APK on all devices"
    echo "  $0 uninstall <package>     Uninstall package from all devices"
    echo ""
    echo "Examples:"
    echo "  $0 exec 'settings get global adb_enabled'"
    echo "  $0 install app.apk"
    echo "  $0 uninstall com.example.app"
    exit 0
fi

case "$1" in
    list)
        list_devices
        ;;
    exec)
        batch_exec "$2"
        ;;
    install)
        batch_install "$2"
        ;;
    uninstall)
        batch_uninstall "$2"
        ;;
    *)
        echo "Unknown command: $1"
        exit 1
        ;;
esac
