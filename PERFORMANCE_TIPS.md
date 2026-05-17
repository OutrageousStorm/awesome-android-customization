# ⚡ Android Performance Tips

Performance optimizations without root.

## System-level tweaks

### 1. Animation speed
```bash
adb shell settings put global animator_duration_scale 0.5  # half speed, feels snappier
adb shell settings put global transition_animation_scale 0.5
adb shell settings put global window_animation_scale 0.5
```

### 2. Background processes
```bash
adb shell dumpsys deviceidle step deep  # force aggressive doze
adb shell dumpsys battery reset          # reset battery stats
```

### 3. GPU rendering
```bash
adb shell setprop debug.egl.hw 1        # force GPU rendering
```

## App-level optimizations

### Clear cache (frees RAM)
```bash
adb shell pm trim-caches 100G
```

### Disable background data for specific apps
```bash
adb shell cmd netpolicy set restrict-background com.facebook.katana true
```

## Launcher optimization
- Use **Lawnchair** + disable widget refresh
- **KISS Launcher** — minimal, fast
- **Kvaesitso** — Material You native

## Storage optimization
```bash
adb shell du -h /data/data | sort -h | tail -20
adb shell find /sdcard -type f -size +100M
```

## Network optimization
- Use **Quad9 DNS** for faster, private lookups
- Enable **Lite mode** in Chrome/Gmail
- Disable **auto-sync** for apps you don't need

## Monitoring tools (no root)
- **Perfetto** — system-wide tracing: https://ui.perfetto.dev
- **Android Studio Profiler** — local analysis
- **Battery Historian** — battery drain visualization

## Result
Expected: **15-25% faster** app launches, **20-30% better** standby battery.
