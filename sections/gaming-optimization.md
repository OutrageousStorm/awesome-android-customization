# Gaming & Performance Optimization

Squeeze the most performance from your Android device for gaming.

## Game launchers

| Tool | Features | Link |
|------|----------|------|
| **Armada** | Game center, performance profiles | Play Store |
| **Nova Launcher Prime** | Custom gestures, per-app profiles | Play Store |
| **Game Launcher** | Samsung/OEM built-in tool | Pre-installed |

## Performance tools (no root)

- **Cooler Master** — thermal management
- **Game Booster** — RAM cleaner, notification blocker
- **FPS Counter** — in-game overlay FPS monitor

## With root (Magisk)

- **Performance Profiles** — CPU governor/freq scaling
- **Advanced Thermal Tweaks** — custom throttle thresholds
- **Gaming Mode** (via LSPosed) — block notifications, lock FPS, disable background

## Network optimization

For competitive games (PUBG, COD, etc):
```bash
adb shell settings put global network_access_timeout_ms 1000
adb shell settings put global http_socket_timeout_ms 2000
adb shell pm grant com.example.game android.permission.CHANGE_NETWORK_STATE
```

## GPU optimization

```bash
# Check GPU
adb shell getprop ro.hardware.keystore
adb shell getprop ro.opengles.version

# Vulkan support (API 24+)
adb shell dumpsys SurfaceFlinger | grep "GLES"
```

---
[← Back to Index](../README.md)
