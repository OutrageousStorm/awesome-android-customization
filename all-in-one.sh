#!/bin/bash
# all-in-one.sh -- Router script for all OutrageousStorm Android tools
# Downloads and runs any tool in one command
# Usage: ./all-in-one.sh toolkit permission-audit
#        ./all-in-one.sh frida-scripts ssl-bypass.js
#        ./all-in-one.sh help

set -e

REPO_URL="https://github.com/OutrageousStorm"
TOOLS_DIR="${HOME}/.outrageous-android-tools"

mkdir -p "$TOOLS_DIR"

case "$1" in
  toolkit)
    echo "📦 Downloading android-toolkit-scripts..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/android-toolkit-scripts.git" 2>/dev/null || cd android-toolkit-scripts && git pull
    cd android-toolkit-scripts
    python3 "${2:-device_info.py}"
    ;;
  
  permission-audit)
    echo "🔍 Downloading android-permission-auditor..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/android-permission-auditor.git" 2>/dev/null || cd android-permission-auditor && git pull
    cd android-permission-auditor
    python3 "audit.py"
    ;;
  
  privacy-harden)
    echo "🔏 Downloading android-privacy-hardener..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/android-privacy-hardener.git" 2>/dev/null || cd android-privacy-hardener && git pull
    cd android-privacy-hardener
    python3 "${2:-harden.py}" --level 2
    ;;
  
  debloat)
    echo "🗑️  Downloading android-debloat-lists..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/android-debloat-lists.git" 2>/dev/null || cd android-debloat-lists && git pull
    cd android-debloat-lists
    bash debloat.sh "lists/${2:-universal.txt}"
    ;;
  
  frida)
    echo "💉 Downloading frida-scripts-android..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/frida-scripts-android.git" 2>/dev/null || cd frida-scripts-android && git pull
    echo "Scripts ready in: $(pwd)/scripts"
    echo "Run: frida -U -f <app> -l scripts/$2"
    ;;
  
  apk-patch)
    echo "🩹 Downloading apk-patcher..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/apk-patcher.git" 2>/dev/null || cd apk-patcher && git pull
    cd apk-patcher
    python3 patch.py --apk "$2" --ssl-bypass --root-bypass --sign
    ;;
  
  scrcpy)
    echo "🖥️  Downloading android-scrcpy-tools..."
    cd "$TOOLS_DIR"
    git clone --depth 1 "$REPO_URL/android-scrcpy-tools.git" 2>/dev/null || cd android-scrcpy-tools && git pull
    cd android-scrcpy-tools
    python3 launch.py "${2:-default}"
    ;;
  
  list)
    echo "Available tools:"
    echo "  toolkit              - Device info, permission audit, extraction, debloat"
    echo "  permission-audit     - Scan and revoke dangerous permissions"
    echo "  privacy-harden       - Multi-level privacy hardening"
    echo "  debloat [list]       - Remove bloatware (universal, samsung, xiaomi)"
    echo "  frida [script]       - Run Frida scripts (ssl-bypass, root-bypass, etc.)"
    echo "  apk-patch <file>     - Patch APK for SSL/root detection bypass"
    echo "  scrcpy [profile]     - Screen mirror profiles (gaming, record, etc.)"
    echo ""
    echo "All tools are cached in: $TOOLS_DIR"
    ;;
  
  *)
    echo "OutrageousStorm Android Toolkit Launcher"
    echo "Usage: $0 <tool> [args...]"
    echo ""
    echo "Run: $0 list"
    ;;
esac
