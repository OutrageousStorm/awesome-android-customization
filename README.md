# 📱 Awesome Android Customization

Curated list of the best Android customization tools, ROMs, kernels, and tweaks.

## 🔝 Top picks

**Custom ROMs** → [LineageOS](lineageos.org), [GrapheneOS](grapheneos.org), [crDroid](crdroid.net)  
**Launchers** → Lawnchair, KISS, Nova, Niagra  
**Magisk** → [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk)  
**Kernel** → [KernelSU](https://kernelsu.org), [franco Kernel](https://franco-kernel.com)  
**Themes** → [Iconify](https://github.com/Mahmud0808/Iconify), [Material You](https://www.bing.com/ck/a?!&&p=8f8c8c8c)

## Launchers

| Launcher | Features | Link |
|----------|----------|------|
| **Lawnchair** | Icon pack support, Material You | [GitHub](https://github.com/LawnchairLauncher/Lawnchair) |
| **KISS** | Ultra-minimal, search-first | [GitHub](https://github.com/Neamar/KISS) |
| **Niagra** | Gesture-driven, pocket-friendly | [Website](https://niagra.toolbxforever.com) |
| **Nova** | Feature-rich, customizable grid | [Play Store](https://play.google.com/store/apps/details?id=com.teslacoilsw.launcher) |

## Icon packs

| Pack | Style | Source |
|------|-------|--------|
| **Material Icons** | Official Google | [GitHub](https://github.com/google/material-design-icons) |
| **Arcticons** | Minimalist outlines | [F-Droid](https://f-droid.org/en/packages/com.donnnno.arcticons) |
| **Icalendar** | Functional, calendar | [GitHub](https://github.com/danziger/Icalendar) |

## System UI tweaks

| Tool | Does | Root |
|------|------|------|
| **GravityBox** (LSPosed) | Status bar, buttons, animations | No |
| **Iconify** (LSPosed) | Full UI theming | No |
| **Customization Sideload** | Pixel UI features | No |

## ADB tweaks

| Tweak | Command |
|-------|---------|
| Hide navigation bar | `adb shell settings put secure navigation_bar_visible 0` |
| Increase animation speed | `adb shell settings put global animator_duration_scale 0.5` |
| Immersive mode | `adb shell settings put global immersive_mode_confirmations confirmed` |
| Disable bloatware | `adb shell pm uninstall -k --user 0 <package>` |

## Kernel customizers

| Tool | Purpose | Link |
|------|---------|------|
| **Kernel Adiutor** | CPU, GPU, I/O tuning | [GitHub](https://github.com/grarak/KernelAdiutor) |
| **FKM Kernel Manager** | Franco Kernel control | [XDA](https://forum.xda-developers.com/t/app-2-9-fkm-kernel-manager.3437207/) |

See full guide → [android-rom-guide](https://github.com/OutrageousStorm/android-rom-guide)
