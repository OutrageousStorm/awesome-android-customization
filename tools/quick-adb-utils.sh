#!/bin/bash
# Quick ADB Utilities - Fast access to common Android device operations

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Get device ID
DEVICE=$(adb devices | grep -v "^$" | tail -1 | awk '{print $1}')

if [ -z "$DEVICE" ] || [ "$DEVICE" = "List" ]; then
    echo -e "${RED}❌ No device connected${NC}"
    exit 1
fi

# Colors for device
echo -e "${BLUE}📱 Device: $DEVICE${NC}\n"

case "$1" in
    "battery")
        echo -e "${YELLOW}🔋 Battery Info:${NC}"
        adb -s "$DEVICE" shell dumpsys battery | grep -E "level|temperature|status"
        ;;
    
    "storage")
        echo -e "${YELLOW}💾 Storage Usage:${NC}"
        adb -s "$DEVICE" shell df /data | tail -1
        ;;
    
    "memory")
        echo -e "${YELLOW}🧠 Memory Usage:${NC}"
        adb -s "$DEVICE" shell cat /proc/meminfo | head -3
        ;;
    
    "processes")
        echo -e "${YELLOW}⚙️  Top Processes:${NC}"
        adb -s "$DEVICE" shell ps -ef | head -10
        ;;
    
    "apps")
        echo -e "${YELLOW}📦 Installed Apps:${NC}"
        adb -s "$DEVICE" shell pm list packages | wc -l
        ;;
    
    "screen-on")
        echo -e "${YELLOW}🔆 Turning screen ON${NC}"
        adb -s "$DEVICE" shell input keyevent 26
        ;;
    
    "screen-off")
        echo -e "${YELLOW}🌙 Turning screen OFF${NC}"
        adb -s "$DEVICE" shell input keyevent 26
        ;;
    
    "reboot")
        echo -e "${RED}🔄 Rebooting device...${NC}"
        adb -s "$DEVICE" reboot
        echo -e "${GREEN}✅ Device rebooting${NC}"
        ;;
    
    "logcat")
        echo -e "${YELLOW}📜 Logcat (Press Ctrl+C to exit):${NC}"
        adb -s "$DEVICE" logcat
        ;;
    
    "push")
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: quick-adb-utils.sh push <local_path> <device_path>"
            exit 1
        fi
        echo -e "${YELLOW}📤 Pushing $2 to $3${NC}"
        adb -s "$DEVICE" push "$2" "$3"
        echo -e "${GREEN}✅ Push complete${NC}"
        ;;
    
    "pull")
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: quick-adb-utils.sh pull <device_path> <local_path>"
            exit 1
        fi
        echo -e "${YELLOW}📥 Pulling $2 to $3${NC}"
        adb -s "$DEVICE" pull "$2" "$3"
        echo -e "${GREEN}✅ Pull complete${NC}"
        ;;
    
    *)
        echo -e "${BLUE}Quick ADB Utilities${NC}"
        echo ""
        echo "Usage: quick-adb-utils.sh <command>"
        echo ""
        echo "Commands:"
        echo "  battery      - Show battery info"
        echo "  storage      - Show storage usage"
        echo "  memory       - Show memory usage"
        echo "  processes    - List top processes"
        echo "  apps         - Count installed apps"
        echo "  screen-on    - Turn screen on"
        echo "  screen-off   - Turn screen off"
        echo "  reboot       - Reboot device"
        echo "  logcat       - Stream device logs"
        echo "  push <local> <remote>  - Push file to device"
        echo "  pull <remote> <local>  - Pull file from device"
        ;;
esac
