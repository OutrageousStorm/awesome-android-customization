# Recommended Customization Path

A roadmap for different use cases based on your goals.

## 🎮 Gaming Setup

1. **Custom Kernel** — Lower latency, higher GPU performance
   - KernelSU for root
   - Gaming-optimized kernel (POCO Kernel, Mochi Kernel)

2. **UI Tweaks** — Smooth animations, responsive feel
   - Iconify for custom icon pack
   - QuickSwitch for custom recents provider
   - System UI Tuner for extra settings

3. **Performance Optimization**
   - Disable background services (see android-tweaks-toolkit)
   - Set battery profile to Performance
   - Install Game Space or Gamer's Toolkit module

## 🔒 Privacy Hardening

1. **ROM**
   - GrapheneOS (Pixel only) or LineageOS for microG
   - CalyxOS if you want balance

2. **Apps**
   - Replace Chrome → Vanadium/Brave
   - Replace Gmail → FairEmail
   - Replace Maps → OsmAnd / Organic Maps
   - Use F-Droid for FOSS apps

3. **ADB Hardening** (see android-privacy-hardener)
   - Run `python3 harden.py --level 3`
   - Install NetGuard for per-app firewall
   - Use DNS.QUAD9.net encrypted DNS

## 📱 Daily Driver Optimization

1. **Stability First**
   - Use a stable ROM: LineageOS, crDroid, or stock
   - Minimal Magisk modules (core: PlayIntegrityFix only)

2. **Quality of Life**
   - Magisk modules: ACC (battery health), Universal GMS Doze
   - System tweaks: reduce animations, increase touch responsiveness
   - Dock app switcher for faster app switching

3. **Backup & Recovery**
   - Regular TWRP backups (see android-rom-guide)
   - Backup APKs (android-toolkit-scripts)

## 🛠️ Developer Setup

1. **ADB + Scripting**
   - Master ADB commands (see android-adb-cheatsheet)
   - Use android-toolkit-scripts for automation

2. **App Testing**
   - Custom ROM with USB debugging always available
   - scrcpy for screen mirroring (android-scrcpy-tools)
   - Frida for dynamic analysis (frida-scripts-android)

3. **CI/CD**
   - GitHub Actions for app builds
   - fastlane for automation

---

**See also:** [android-rom-guide](https://github.com/OutrageousStorm/android-rom-guide), [grapheneos-guide](https://github.com/OutrageousStorm/grapheneos-guide), [android-privacy-guide](https://github.com/OutrageousStorm/android-privacy-guide)
