#!/usr/bin/env python3
"""
Android Theme & Overlay Detector
Detects installed themes, overlays, icon packs, launchers, and customization packages via ADB.
Real-time detection without root.
"""

import subprocess
import json
import sys
import re
from typing import Dict, List, Tuple

class AndroidThemeDetector:
    def __init__(self, device_id: str = None):
        self.device_id = device_id
        self.adb_cmd = ["adb"]
        if device_id:
            self.adb_cmd.extend(["-s", device_id])
    
    def run_adb(self, *args) -> str:
        """Execute ADB command and return output."""
        try:
            result = subprocess.run(
                self.adb_cmd + list(args),
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout.strip()
        except Exception as e:
            print(f"❌ ADB error: {e}", file=sys.stderr)
            return ""
    
    def detect_launchers(self) -> Dict[str, str]:
        """Detect installed launcher apps."""
        launchers = {}
        launcher_packages = [
            "com.android.launcher",
            "com.google.android.apps.nexuslauncher",
            "com.sec.android.app.launcher",
            "org.adwfrw.launcher",
            "com.teslacoilsw.launcher",
            "com.motorola.launcher",
            "com.oppo.launcher",
            "com.vivo.launcher",
        ]
        
        for pkg in launcher_packages:
            output = self.run_adb("shell", "pm", "list", "package", pkg)
            if output:
                name = self.run_adb("shell", "pm", "dump", pkg, "|", "grep", "versionName")
                launchers[pkg] = name if name else "Installed"
        
        return launchers
    
    def detect_icon_packs(self) -> Dict[str, str]:
        """Detect icon pack applications."""
        icon_packs = {}
        output = self.run_adb("shell", "pm", "list", "packages", "-f")
        
        icon_keywords = ["icon", "pack", "theme", "deco"]
        for line in output.split('\n'):
            if any(kw in line.lower() for kw in icon_keywords):
                match = re.search(r'=(.+?)$', line)
                if match:
                    pkg = match.group(1)
                    icon_packs[pkg] = "Icon/Theme Package"
        
        return icon_packs
    
    def detect_overlays(self) -> List[str]:
        """Detect system UI overlays (requires Android 8+)."""
        overlays = []
        output = self.run_adb("shell", "cmd", "overlay", "list")
        
        for line in output.split('\n'):
            if "enabled" in line.lower() or "disabled" in line.lower():
                overlays.append(line.strip())
        
        return overlays
    
    def detect_themes(self) -> List[str]:
        """Detect theme packages."""
        themes = []
        output = self.run_adb("shell", "pm", "list", "packages")
        
        theme_keywords = ["theme", "miui", "oneui", "coloros"]
        for pkg in output.split('\n'):
            if any(kw in pkg.lower() for kw in theme_keywords):
                themes.append(pkg.replace("package:", ""))
        
        return themes
    
    def detect_customization(self) -> Dict:
        """Get all customization data."""
        return {
            "launchers": self.detect_launchers(),
            "icon_packs": self.detect_icon_packs(),
            "themes": self.detect_themes(),
            "overlays": self.detect_overlays(),
        }

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Detect Android themes, overlays, and customization packages")
    parser.add_argument("-s", "--serial", help="Device serial (optional)")
    parser.add_argument("-j", "--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()
    
    detector = AndroidThemeDetector(args.serial)
    
    print("🎨 Android Theme & Overlay Detector")
    print("=" * 50)
    
    customization = detector.detect_customization()
    
    if args.json:
        print(json.dumps(customization, indent=2))
    else:
        print(f"\n📱 Launchers ({len(customization['launchers'])}):")
        for pkg, version in customization['launchers'].items():
            print(f"  • {pkg}: {version}")
        
        print(f"\n🎯 Icon Packs ({len(customization['icon_packs'])}):")
        for pkg, desc in customization['icon_packs'].items():
            print(f"  • {pkg}")
        
        print(f"\n🌈 Themes ({len(customization['themes'])}):")
        for theme in customization['themes']:
            print(f"  • {theme}")
        
        print(f"\n⚙️ Overlays ({len(customization['overlays'])}):")
        for overlay in customization['overlays']:
            print(f"  • {overlay}")

if __name__ == "__main__":
    main()
