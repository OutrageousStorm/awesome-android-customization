# Android Launcher Comparison

Most popular custom launchers with feature matrix.

| Launcher | Stars | Material You | Gesture | Dev Drawer | Icon Pack | Free |
|----------|-------|------------|---------|-----------|-----------|------|
| [Lawnchair](https://github.com/LawnchairLauncher/Lawnchair) | ⭐⭐⭐⭐⭐ | ✓ | ✓ | ✓ | ✓ | Yes |
| [Niagara](https://niagara.launcher) | ⭐⭐⭐⭐ | ✓ | ✓ | ✗ | ~ | $4.99 |
| [Sesame](https://github.com/aashishksinha/Sesame) | ⭐⭐⭐ | ✓ | ✓ | ✓ | ✓ | Yes |
| [POCO Launcher](https://play.google.com/store/apps/details?id=com.mi.home) | ⭐⭐⭐⭐ | ~ | ✓ | ✓ | ✓ | Yes |
| [Nova Launcher](https://www.novalauncher.com) | ⭐⭐⭐⭐ | ✗ | ✓ | ✓ | ✓ | Free/Prime |

## Recommended setups

**Performance-first:**
- Launcher: Lawnchair (lightweight, open source)
- Icon pack: Pix (Material Design)
- Grid: 4×6 (fewer icons = faster scrolling)

**Minimal aesthetic:**
- Launcher: Sesame
- Wallpaper: solid color
- App drawer: gesture swipe-up
- Hidden status bar: YES

**Power user:**
- Launcher: Nova Prime
- Gesture: Swipe-down = notification panel, swipe-up = app drawer
- Shortcuts: custom app pairs (e.g., long-press home = lock screen)
- Grid: 5×6 or custom

## Installation

```bash
# Via ADB to set default launcher
adb shell cmd package set-default-home <package.name>

# Example: set Lawnchair as default
adb shell cmd package set-default-home ch.deletescape.lawnchair
```

*Tip: Lawnchair + Pix icon pack + 4×6 grid = best performance/looks ratio*
