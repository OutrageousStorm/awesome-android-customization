# Game Mode & Performance Tuning

Optimize Android for gaming — disable background processes, boost GPU, reduce latency.

## Game Mode (built-in)
Settings → Display → Game Booster / Game Space / Game Launcher
- Freezes background apps
- Boosts GPU clock
- Disables notifications
- Reduces touch latency to 20-60ms

## ADB tweaks for gaming
```bash
# Disable background animations
adb shell settings put global animator_duration_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global window_animation_scale 0

# Disable WiFi scanning (reduces latency)
adb shell settings put global wifi_scan_always_enabled 0

# Disable touch vibration feedback
adb shell settings put system haptic_feedback_enabled 0

# Lock to 120 FPS (if available)
adb shell dumpsys SurfaceFlinger | grep DesiredMode
adb shell settings put secure user_refresh_rate 120

# Disable thermal throttling (⚠️ risky, monitor temps)
# (device-specific, usually in vendor partition)
```

## Per-game tuning
Use Game Launcher profiles or Tasker to:
- Kill specific background services before launching game
- Disable WiFi/Bluetooth
- Force highest performance mode
- Disable always-on display
- Mute all notifications
