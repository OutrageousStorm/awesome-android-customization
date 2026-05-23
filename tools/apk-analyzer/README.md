# APK Analyzer Tool

Fast Java CLI to analyze Android APK structure, permissions, and signatures.

## Usage

```bash
# Compile
javac APKAnalyzer.java

# Basic analysis
java APKAnalyzer app.apk

# Verbose output
java APKAnalyzer app.apk --verbose

# JSON output
java APKAnalyzer app.apk --json
```

## Features
- APK structure inspection
- File count and size analysis
- Native library detection
- Resource detection
- Permission enumeration
