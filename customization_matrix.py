#!/usr/bin/env python3
"""Android customization feature matrix by ROM/tool"""
MATRIX = {
    'Icon packs': ['Nova Launcher', 'KWGT', 'Zooper Widget'],
    'Launchers': ['Nova', 'KISS', 'Librefy'],
    'Status bar': ['GravityBox', 'xStana', 'Custom ROM'],
    'Navigation': ['NavBar', 'Edge Gestures', 'Full Gesture Nav'],
}
if __name__ == '__main__':
    print("\n📊 Android Customization Features\n")
    for category, tools in MATRIX.items():
        print(f"{category}:")
        for tool in tools:
            print(f"  • {tool}")
