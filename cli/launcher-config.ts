#!/usr/bin/env ts-node
/**
 * launcher-config.ts -- Generate Android launcher shortcut configs
 * Usage: npx ts-node launcher-config.ts
 */

interface LauncherConfig {
  name: string;
  icon: string;
  apps: { label: string; package: string }[];
}

const configs: Record<string, LauncherConfig> = {
  "gaming": {
    name: "Gaming Hub",
    icon: "🎮",
    apps: [
      { label: "Call of Duty Mobile", package: "com.activision.callofduty.shooter" },
      { label: "PUBG Mobile", package: "com.tencent.ig" },
      { label: "Genshin Impact", package: "com.mihoyo.genshin" },
      { label: "Game Booster", package: "com.limbgamer.gametuner" }
    ]
  },
  "work": {
    name: "Productivity",
    icon: "💼",
    apps: [
      { label: "Gmail", package: "com.google.android.gm" },
      { label: "Google Drive", package: "com.google.android.apps.docs" },
      { label: "Slack", package: "com.slack" },
      { label: "Notion", package: "com.notion" }
    ]
  },
  "dev": {
    name: "Developer Tools",
    icon: "👨‍💻",
    apps: [
      { label: "VS Code Server", package: "com.microsoft.vscode" },
      { label: "Git apps", package: "com.github.android" },
      { label: "SSH Terminal", package: "com.termux" },
      { label: "ADB Helper", package: "com.example.adbhelper" }
    ]
  }
};

function generateLauncherScript(configName: string): string {
  const config = configs[configName];
  if (!config) return "Config not found";
  
  let script = `#!/bin/bash
# ${config.name} launcher setup
`;
  script += `# Generated at ${new Date().toISOString()}

`;
  
  for (const app of config.apps) {
    script += `# ${app.label}
`;
    script += `adb shell am start -n ${app.package}/.MainActivity

`;
  }
  
  return script;
}

// Main
const args = process.argv.slice(2);
const configName = args[0] || "gaming";
const script = generateLauncherScript(configName);
console.log(script);
