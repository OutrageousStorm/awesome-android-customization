#!/usr/bin/env python3
"""
systemui_customizer.py -- Customize SystemUI via ADB settings
Changes statusbar, navbar, lockscreen appearance without overlays.
Usage: python3 systemui_customizer.py --statusbar-color FF0000 --navbar-hide
"""
import subprocess, argparse

def adb(cmd):
    subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True)

def main():
    parser = argparse.ArgumentParser(description="Customize SystemUI appearance")
    parser.add_argument("--statusbar-color", help="Statusbar color (hex, e.g. FF0000)")
    parser.add_argument("--navbar-color", help="Navbar color (hex)")
    parser.add_argument("--navbar-hide", action="store_true", help="Hide navbar")
    parser.add_argument("--clock-format", choices=["12h", "24h"], help="Clock format")
    parser.add_argument("--battery-style", choices=["default", "circle", "percentage"], help="Battery icon style")
    parser.add_argument("--show-seconds", action="store_true", help="Show seconds in statusbar clock")
    args = parser.parse_args()

    if args.statusbar_color:
        color = int(args.statusbar_color, 16)
        adb(f"settings put secure status_bar_background_color {color}")
        print(f"✓ Statusbar color: #{args.statusbar_color}")

    if args.navbar_color:
        color = int(args.navbar_color, 16)
        adb(f"settings put secure navigation_bar_color {color}")
        print(f"✓ Navbar color: #{args.navbar_color}")

    if args.navbar_hide:
        # Requires Magisk module or root
        adb("settings put secure navigation_bar_show 0")
        adb("settings put global force_fsg_nav_bar 0")
        print("✓ Navbar hidden (requires system app or root)")

    if args.clock_format:
        format_24h = "1" if args.clock_format == "24h" else "0"
        adb(f"settings put system time_12_24 {format_24h}")
        print(f"✓ Clock format: {args.clock_format}")

    if args.show_seconds:
        adb("settings put secure status_bar_clock_seconds 1")
        print("✓ Seconds enabled in statusbar")

    if args.battery_style:
        styles = {"default": "0", "circle": "1", "percentage": "2"}
        adb(f"settings put secure status_bar_battery_style {styles[args.battery_style]}")
        print(f"✓ Battery style: {args.battery_style}")

    print("\nNote: Some changes require reboot or SystemUI restart")
    print("  adb shell am force-stop com.android.systemui")
    print("  adb shell am start -n com.android.systemui/.SystemUIService")

if __name__ == "__main__":
    main()
