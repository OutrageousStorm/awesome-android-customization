#!/usr/bin/env python3
"""Matrix of Android customization tools by feature"""
import json

TOOLS = {
    'Magisk': {'root': True, 'modules': True, 'flashing': True, 'ease': 9},
    'Xposed': {'root': True, 'modules': True, 'flashing': False, 'ease': 7},
    'KernelSU': {'root': True, 'modules': True, 'flashing': True, 'ease': 8},
    'LSPosed': {'root': False, 'modules': True, 'flashing': False, 'ease': 6},
    'EdXposed': {'root': False, 'modules': True, 'flashing': False, 'ease': 5},
}

print("Customization Tool Feature Matrix\n")
print(f"{'Tool':<15} {'Root':<6} {'Modules':<8} {'Flash':<6} {'Ease (1-10)'}")
print("─" * 45)
for tool, features in TOOLS.items():
    print(f"{tool:<15} "
          f"{'Yes' if features['root'] else 'No':<6} "
          f"{'Yes' if features['modules'] else 'No':<8} "
          f"{'Yes' if features['flashing'] else 'No':<6} "
          f"{features['ease']}")
