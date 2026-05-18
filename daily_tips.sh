#!/bin/bash
# daily_tips.sh — Random Android customization tips
# Run as cron job: 0 9 * * * /path/to/daily_tips.sh
TIPS=(
  "Disable WiFi scanning when off: settings put global wifi_scan_always_enabled 0"
  "Aggressive doze: dumpsys deviceidle step deep"
  "Disable bloatware: pm uninstall -k --user 0 <package>"
  "Root detector bypass: Hide My AppList + Shamiko modules"
  "Battery: limit charge to 80% with ACC Magisk module"
  "Privacy: use GrapheneOS or DivestOS for baseline security"
  "Launchers: Lawnchair, KISS, Kvaesitso all lightweight"
  "Xposed modules: RootBeer patcher, Xprivacy, GravityBox"
  "ADB tips: enable TCP debugging for wireless adb"
  "ROM flashing: always backup with TWRP first"
)
TIP=\${TIPS[\$RANDOM % \${#TIPS[@]}]}
echo "💡 Android Tip: \$TIP" | notify-send -
