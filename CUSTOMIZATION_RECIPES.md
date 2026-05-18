# Customization Recipes

Copy-paste ADB recipes for common mods.

## Hide status bar clock

```bash
adb shell settings put secure hide_status_bar_clock 1
```

## Disable haptic feedback globally

```bash
adb shell settings put system haptic_feedback_enabled 0
```

## Remove carrier name from status bar

```bash
adb shell settings put secure show_operator_name 0
```

## Full screen gestures (force on)

```bash
adb shell settings put secure gesture_navigation_enabled 1
adb shell settings put global navigation_bar_gesture_height 40
```

## Lock screen shortcuts

Add custom apps to lock screen (varies by ROM):

```bash
# LineageOS
adb shell settings put secure lock_screen_custom_message "Custom Text"
```

## Always-on display brightness

```bash
# AOD minimum brightness
adb shell settings put secure aod_tap_to_show_screen 1
adb shell settings put system aod_brightness_percent 20
```

## Notification LED control

```bash
# Enable LED
adb shell settings put secure notification_light_pulse 1

# Custom colors (if ROM supports)
adb shell settings put secure notification_light_color -16776961  # Blue
```

## Quick settings order

```bash
# Rearrange quick tiles (stock Android 12+)
adb shell cmd statusbar panel-gravity top
```

## Developer options — hide in settings

```bash
adb shell setprop persist.sys.usb.config adb,midi
adb shell settings put global development_settings_enabled 0
```

## Volume key behavior

Change long-press:

```bash
# Volume up = next track
adb shell settings put system volume_key_cursor_control 1
```

## Immersive mode (hide UI elements)

```bash
adb shell settings put global policy_control immersive.navigation=*
```

---

**Pro tip:** Combine with Tasker or Automation app to apply profiles on boot.
