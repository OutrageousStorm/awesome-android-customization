# Android 16 Theme System

Material You on Android 16+ — dynamic theming from wallpaper and system colors.

## Programmatic theming

```kotlin
// Get system colors in Material You
val colorScheme = MaterialYou.getColorScheme(context)
val primary = colorScheme.primary
val secondary = colorScheme.secondary

// Custom Material 3 theme
val theme = dynamicColorScheme(context, isLight = true)
```

## ADB tweaks
```bash
# Force Material You colors to regenerate
adb shell settings put secure theme_customization_overlay_packages "com.android.theme.overlay.system"

# Switch to light/dark Material theme
adb shell settings put system theme_mode 2  # 0=light, 1=dark, 2=auto

# Custom accent color (requires Material 3)
adb shell settings put secure accent_color_overtake "0xFF4285F4"
```

## Resources
- Material Design 3: https://m3.material.io
- Material Design System: android.resource://com.android.theme
