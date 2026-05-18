# Android Overlays (RRO)

Runtime Resource Overlays — the proper way to theme Android without modifying system files.

## What are overlays?

Overlays allow you to override resources (colors, strings, dimensions, drawables) system-wide without touching `/system`. Changes apply at runtime.

## Types

- **Framework overlays** — theme system UI (StatusBar, SystemUI)
- **App overlays** — override specific app resources
- **Signature overlays** — require matching signature

## Quick start

```bash
# Enable overlay
adb shell cmd overlay enable com.example.overlay

# List all overlays
adb shell cmd overlay list

# Get priority
adb shell cmd overlay dump --target com.android.settings
```

## Build an overlay

```
overlay/
├── Android.bp
├── res/
│   ├── values/
│   │   └── colors.xml  (override colors)
│   └── drawable/
│       └── ic_launcher.xml
└── AndroidManifest.xml
```

**colors.xml:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="primary_dark">#FF1A1A</color>
    <color name="accent">#00FF00</color>
</resources>
```

**AndroidManifest.xml:**
```xml
<manifest package="com.example.overlay" android:versionCode="1">
    <overlay android:targetPackage="android" android:priority="50" />
</manifest>
```

**Android.bp:**
```
runtime_resource_overlay {
    name: "com.example.overlay",
    manifest: "AndroidManifest.xml",
}
```

Build:
```bash
m com.example.overlay
adb push out/target/product/*/system/product/overlay/com.example.overlay.apk /tmp/
adb shell cmd overlay enable com.example.overlay
```

## Popular overlays

- **Substratum** — overlay manager (requires compatible ROM)
- **Layers** — GrapheneOS overlay system
- **OMS (Oxygen OS Manager)** — OnePlus overlay system

## Resources

- [AOSP Overlays](https://source.android.com/docs/core/ota/nonab/ab_implement)
- [RRO Guide](https://github.com/LineageOS/android_packages_apps_Layers)
