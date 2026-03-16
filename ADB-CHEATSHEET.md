# Android ADB Cheat Sheet 2026
Complete ADB command reference for power users. No root required.

## Setup

**Install ADB**
- Windows: `winget install Google.PlatformTools`
- macOS: `brew install android-platform-tools`
- Linux: `sudo apt install adb`

**Enable USB Debugging**: Settings → About Phone → tap Build Number 7x → Developer Options → USB Debugging

**Wireless ADB (Android 11+)**:
```bash
adb pair 192.168.1.x:PORT
adb connect 192.168.1.x:PORT
```

## Performance
```bash
adb shell settings put global animator_duration_scale 0.5
adb shell settings put global transition_animation_scale 0.5
adb shell settings put global window_animation_scale 0.5
```

## Display
```bash
adb shell wm density 390        # change DPI (reset: wm density reset)
adb shell wm size 1080x2400     # change resolution (reset: wm size reset)
adb shell cmd uimode night yes  # dark mode
adb shell settings put system font_scale 0.9
```

## App Management
```bash
adb shell pm list packages -3               # user-installed apps
adb shell pm disable-user --user 0 com.pkg  # disable system app
adb shell pm enable com.pkg                 # re-enable
adb shell pm uninstall --user 0 com.pkg     # remove for current user
adb shell cmd package install-existing com.pkg  # restore
adb shell pm clear com.pkg                  # clear data/cache
```

## Privacy
```bash
adb shell pm revoke com.facebook.katana android.permission.ACCESS_FINE_LOCATION
adb shell pm revoke com.instagram.android android.permission.ACCESS_FINE_LOCATION
adb shell pm revoke com.zhiliaoapp.musically android.permission.ACCESS_FINE_LOCATION
adb shell pm revoke com.facebook.katana android.permission.RECORD_AUDIO
```

## Samsung Debloat
```bash
adb shell pm disable-user --user 0 com.samsung.android.bixby.agent
adb shell pm disable-user --user 0 com.samsung.android.bixbyvision.framework
adb shell pm disable-user --user 0 com.hiya.star
adb shell pm disable-user --user 0 com.samsung.android.app.tips
```

## Backup
```bash
adb pull /sdcard/DCIM/ ~/Desktop/photos/
adb pull /sdcard/Android/media/com.whatsapp/WhatsApp/ ~/Desktop/WhatsApp/
adb backup -apk -f myapp.ab com.package.name
```

## Screenshots & Recording
```bash
adb shell screencap /sdcard/s.png && adb pull /sdcard/s.png
adb shell screenrecord --time-limit 60 /sdcard/video.mp4 && adb pull /sdcard/video.mp4
```

## System Info
```bash
adb shell getprop ro.product.model
adb shell getprop ro.build.version.release
adb shell dumpsys battery
adb shell df -h
```

## Related Tools
- [android-adb-toolkit](https://github.com/OutrageousStorm/android-adb-toolkit) — Web GUI for all the above
- [android-tweaks-toolkit](https://github.com/OutrageousStorm/android-tweaks-toolkit) — Automated scripts
- [shizuku-apps-root-alternative](https://github.com/OutrageousStorm/shizuku-apps-root-alternative) — Do this without a PC
- [UAD-NG](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) — GUI debloater

*Maintained by [Tom | Android Intelligence](https://github.com/OutrageousStorm) — March 2026*
