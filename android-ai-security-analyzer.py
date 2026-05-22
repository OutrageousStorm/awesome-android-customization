#!/usr/bin/env python3
"""
AI-powered Android app security analyzer.
Detects suspicious patterns in APK bytecode using pattern matching + heuristics.
No ML models required — pure Python.
"""
import sys, json, subprocess, re, hashlib
from dataclasses import dataclass
from enum import Enum

class RiskLevel(Enum):
    CRITICAL = "🔴 CRITICAL"
    HIGH = "🟠 HIGH"
    MEDIUM = "🟡 MEDIUM"
    LOW = "🔵 LOW"
    INFO = "ℹ️ INFO"

@dataclass
class SecurityFinding:
    name: str
    level: RiskLevel
    description: str
    affected_classes: list

class APKSecurityAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.findings = []
        
    def extract_dex_strings(self):
        """Extract all strings from DEX file"""
        try:
            result = subprocess.run(
                ['strings', self.apk_path],
                capture_output=True, text=True, timeout=30
            )
            return result.stdout.split('\n')
        except:
            return []
    
    def detect_crypto_hardcoding(self, strings):
        """Detect hardcoded encryption keys/secrets"""
        patterns = [
            r'[0-9a-f]{32}',  # MD5
            r'[0-9a-f]{40}',  # SHA1
            r'[0-9a-f]{64}',  # SHA256
            r'-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY',
            r'aws_secret_access_key',
            r'sk_live_[0-9a-z]{20,}',  # Stripe
            r'AIza[0-9A-Za-z_-]{35}',  # Google API key
        ]
        
        findings = []
        for line in strings:
            for pattern in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append(line[:100])
        
        if findings:
            self.findings.append(SecurityFinding(
                name="Hardcoded Secrets Detected",
                level=RiskLevel.CRITICAL,
                description="Potential API keys, tokens, or encryption keys found in APK",
                affected_classes=findings[:5]
            ))
    
    def detect_risky_permissions(self, strings):
        """Check for dangerous permission usage patterns"""
        risky_perms = [
            'READ_PHONE_STATE', 'ACCESS_FINE_LOCATION', 
            'RECORD_AUDIO', 'CAMERA', 'READ_CONTACTS',
            'READ_SMS', 'SEND_SMS'
        ]
        
        found_risky = []
        for perm in risky_perms:
            if any(perm in s for s in strings):
                found_risky.append(perm)
        
        if len(found_risky) > 3:
            self.findings.append(SecurityFinding(
                name="Excessive Sensitive Permissions",
                level=RiskLevel.HIGH,
                description=f"App requests {len(found_risky)} sensitive permissions",
                affected_classes=found_risky
            ))
    
    def detect_reflection_abuse(self, strings):
        """Detect excessive use of reflection (code obfuscation indicator)"""
        reflection_apis = [
            'getMethod', 'getDeclaredMethod', 'invoke',
            'forName', 'getDeclaredField'
        ]
        
        count = sum(1 for s in strings if any(api in s for api in reflection_apis))
        
        if count > 20:
            self.findings.append(SecurityFinding(
                name="Heavy Reflection Usage",
                level=RiskLevel.MEDIUM,
                description=f"Detected {count} reflection calls — possible code obfuscation",
                affected_classes=[f"{count} reflection API calls"]
            ))
    
    def detect_native_code(self, strings):
        """Detect native library usage"""
        native_patterns = ['.so', 'dlopen', 'JNI', 'native']
        native_count = sum(1 for s in strings if any(p in s for p in native_patterns))
        
        if native_count > 5:
            self.findings.append(SecurityFinding(
                name="Native Code Detected",
                level=RiskLevel.INFO,
                description=f"APK uses {native_count} native libraries — harder to reverse engineer",
                affected_classes=["Performance/Security boost"]
            ))
    
    def analyze(self):
        """Run full security analysis"""
        print(f"🔍 Analyzing {self.apk_path}...")
        strings = self.extract_dex_strings()
        
        if not strings:
            print("⚠️  Could not extract strings from APK")
            return
        
        self.detect_crypto_hardcoding(strings)
        self.detect_risky_permissions(strings)
        self.detect_reflection_abuse(strings)
        self.detect_native_code(strings)
        
        self.report()
    
    def report(self):
        """Print security report"""
        if not self.findings:
            print("✅ No major security issues detected")
            return
        
        print(f"\n{'='*60}")
        print(f"🚨 Security Analysis Report")
        print(f"{'='*60}\n")
        
        by_level = {}
        for f in self.findings:
            level = f.level.value.split()[0]
            if level not in by_level:
                by_level[level] = []
            by_level[level].append(f)
        
        for level in ['🔴', '🟠', '🟡', '🔵', 'ℹ️']:
            if level in by_level:
                for finding in by_level[level]:
                    print(f"{finding.level.value}")
                    print(f"  Name: {finding.name}")
                    print(f"  Description: {finding.description}")
                    if finding.affected_classes:
                        print(f"  Examples: {', '.join(finding.affected_classes[:3])}")
                    print()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 android_ai_security_analyzer.py <apk_path>")
        sys.exit(1)
    
    analyzer = APKSecurityAnalyzer(sys.argv[1])
    analyzer.analyze()
