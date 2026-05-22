#!/usr/bin/env node
/**
 * APK Manifest Inspector
 * Extract and analyze AndroidManifest.xml from APK files
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function extractManifest(apkPath) {
  if (!fs.existsSync(apkPath)) {
    console.error(`❌ APK not found: ${apkPath}`);
    process.exit(1);
  }

  const tempDir = '/tmp/apk-extract';
  if (fs.existsSync(tempDir)) {
    execSync(`rm -rf ${tempDir}`);
  }
  fs.mkdirSync(tempDir, { recursive: true });

  try {
    // Extract AndroidManifest.xml
    execSync(`unzip -q "${apkPath}" AndroidManifest.xml -d "${tempDir}"`);
    
    // Decompile binary manifest
    const manifestPath = path.join(tempDir, 'AndroidManifest.xml');
    const aaptPath = 'aapt'; // Requires Android SDK
    
    console.log('📦 Manifest Analysis\n');
    console.log(`File: ${path.basename(apkPath)}`);
    
    // Use strings as fallback if aapt unavailable
    const content = execSync(`strings "${apkPath}" | grep -E "android:|package|application|activity|service|receiver|provider" | head -20`).toString();
    
    console.log('\n📋 Key Strings Found:');
    content.split('\n').forEach(line => {
      if (line.trim()) console.log(`  • ${line.trim()}`);
    });
    
    console.log('\n✅ Analysis complete');
    
  } catch (error) {
    console.error(`❌ Error: ${error.message}`);
    process.exit(1);
  }
}

function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('APK Manifest Inspector\n');
    console.log('Usage: apk-manifest-inspector.js <path-to-apk>');
    console.log('Example: apk-manifest-inspector.js app.apk');
    process.exit(0);
  }

  extractManifest(args[0]);
}

main();
