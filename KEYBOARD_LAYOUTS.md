# Custom Keyboard Layouts for Android

Swappable keyboard layouts without root — tested on Android 12–15.

## System keyboards with layout support

| Keyboard | Layout selection | Root needed |
|----------|-----------------|-------------|
| **AOSP Keyboard** | Settings → Languages → Keyboard layout | No |
| **Google Keyboard (Gboard)** | Gboard Settings → Languages & layouts | No |
| **AnySoftKeyboard** | Settings → Keyboards menu | No |
| **OpenBoard** | Settings → Keyboard layouts | No |
| **Swiftkey** | Settings → Keyboards & layouts | No |

## Popular layouts

- **QWERTY** (default)
- **DVORAK** (efficiency)
- **Colemak** (modern optimized)
- **Workman** (ergonomic)
- **AZERTY** (French)
- **QWERTZ** (German/Czech)

## Install custom layouts

```bash
# Via ADB settings:
adb shell settings put secure default_input_method com.android.inputmethod.latin/.LatinIME
```

## AnySoftKeyboard custom addons

Download packs: https://anysoftkeyboard.github.io/

Popular: Colemak, Dvorak, Workman, Hebrew, Arabic.
