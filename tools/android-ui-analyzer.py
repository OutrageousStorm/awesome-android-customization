#!/usr/bin/env python3
"""
Android System UI Customization Analyzer
Detects installed overlays, custom launchers, themes, and modifications.
Requires: adb, Python 3.6+
"""

import subprocess
import sys
import json
import re
from typing import Dict, List

def run_adb(cmd: str) -> str:
    """Execute ADB command and return output."""
    try:
        result = subprocess.run(['adb'] + cmd.split(), 
                              capture_output=True, text=True, timeout=5)
        return result.stdout.strip()
    except FileNotFoundError:
        print("ERROR: adb not found. Install Android SDK Platform Tools.", file=sys.stderr)
        sys.exit(1)

def get_device_info() -> Dict[str, str]:
    """Get basic device info."""
    return {
        'android_version': run_adb('shell getprop ro.build.version.release'),
        'device_model': run_adb('shell getprop ro.product.model'),
        'rom_name': run_adb('shell getprop ro.build.display.id'),
    }

def get_custom_launchers() -> List[str]:
    """List installed third-party launchers."""
    packages = run_adb('shell cmd package list packages').split('\n')
    launcher_keywords = ['launcher', 'nova', 'pixel', 'poco']
    return [p.replace('package:', '') for p in packages 
            if any(kw in p for kw in launcher_keywords) and 'com.android' not in p]

def get_system_overlays() -> List[str]:
    """Get installed RRO overlays (Android 8+)."""
    overlays = run_adb('shell cmd overlay list').split('\n')
    return [o.split('\t')[0] for o in overlays if o.startswith('[x]')]

def get_installed_themes() -> List[str]:
    """Detect theme apps and frameworks."""
    packages = run_adb('shell cmd package list packages').split('\n')
    theme_patterns = ['theme', 'substratum', 'magisk_module']
    return [p.replace('package:', '') for p in packages
            if any(pat in p for pat in theme_patterns)]

def check_magisk() -> Dict[str, str]:
    """Check Magisk installation and module status."""
    version = run_adb('shell getprop ro.magisk.version')
    modules = run_adb('shell ls /data/adb/modules/ 2>/dev/null').split('\n')
    return {
        'installed': 'Yes' if version else 'No',
        'version': version or 'N/A',
        'module_count': len([m for m in modules if m.strip()])
    }

def analyze():
    """Run full customization analysis."""
    print("=" * 60)
    print("Android System UI Customization Analyzer")
    print("=" * 60)
    
    # Device info
    device = get_device_info()
    print(f"\n[Device Info]")
    for k, v in device.items():
        print(f"  {k}: {v}")
    
    # Launchers
    launchers = get_custom_launchers()
    print(f"\n[Custom Launchers] ({len(launchers)} found)")
    for launcher in launchers:
        print(f"  - {launcher}")
    
    # RRO Overlays
    overlays = get_system_overlays()
    print(f"\n[RRO Overlays] ({len(overlays)} active)")
    for overlay in overlays[:10]:  # Show top 10
        print(f"  - {overlay}")
    
    # Themes
    themes = get_installed_themes()
    print(f"\n[Theme Apps] ({len(themes)} found)")
    for theme in themes:
        print(f"  - {theme}")
    
    # Magisk
    magisk = check_magisk()
    print(f"\n[Magisk Status]")
    for k, v in magisk.items():
        print(f"  {k}: {v}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    analyze()
