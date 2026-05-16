# Custom Boot Animations

Replace the stock Android boot animation with custom ones.

## How to flash

**Via TWRP:**
1. Download `.zip` boot animation
2. Wipe Dalvik/ADB Cache
3. Install the zip
4. Reboot

**Via Magisk:**
1. Download Magisk module `.zip`
2. Install via Magisk Manager
3. Reboot

## Popular sources

- **XDA Boot Animations**: https://forum.xda-developers.com (search "boot animation")
- **BESTiphone Animations**: iPhone-style boot logos and animations
- **Minimal Flats**: Clean, minimalist boot loops
- **LineageOS Animations**: Official LineageOS boot animations
- **Custom Pixel Animations**: Google Pixel boot screen ports

## Create your own

```bash
# Boot animation directory structure:
# bootanimation.zip
# ├── part0/  (image files in sequence)
# │   ├── 0.png
# │   ├── 1.png
# │   └── ...
# ├── part1/  (second part, optional)
# └── desc.txt

# desc.txt format:
# 1080 1920 20
# p 1 0 part0
# p 0 0 part1
# (width, height, fps on first line, then parts)
```

Replace stock animation:
```bash
adb push bootanimation.zip /system/media/bootanimation.zip
adb shell chmod 644 /system/media/bootanimation.zip
```
