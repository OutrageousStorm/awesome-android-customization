#!/usr/bin/env python3
"""Device Permission Auditor - scan for over-privileged apps via ADB"""
import json
import subprocess

def scan():
    try:
        pkgs = subprocess.run(["adb", "shell", "pm", "list", "packages"],
                            capture_output=True, text=True, timeout=5).stdout
        packages = [p.replace("package:", "").strip() for p in pkgs.split("\n") if p]
        
        findings = {"CRITICAL": [], "HIGH": []}
        critical = ["android.permission.INSTALL_PACKAGES"]
        high = ["android.permission.CAMERA", "android.permission.RECORD_AUDIO"]
        
        for pkg in packages[:30]:
            try:
                dump = subprocess.run(["adb", "shell", "dumpsys", "package", pkg],
                                    capture_output=True, text=True, timeout=2).stdout
                for perm in critical:
                    if perm in dump:
                        findings["CRITICAL"].append(pkg)
                        break
                for perm in high:
                    if perm in dump:
                        findings["HIGH"].append(pkg)
                        break
            except: pass
        
        return findings
    except Exception as e:
        return {"error": str(e)}

print(json.dumps(scan(), indent=2))
