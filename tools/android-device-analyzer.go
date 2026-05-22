package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

type DeviceInfo struct {
	Model        string
	Build        string
	AndroidVer   string
	BootLoader   string
	SerialNumber string
	Security     string
}

func executeADB(args ...string) string {
	cmd := exec.Command("adb", args...)
	output, err := cmd.Output()
	if err != nil {
		return ""
	}
	return strings.TrimSpace(string(output))
}

func getDeviceInfo() DeviceInfo {
	info := DeviceInfo{
		Model:        executeADB("shell", "getprop", "ro.product.model"),
		Build:        executeADB("shell", "getprop", "ro.build.fingerprint"),
		AndroidVer:   executeADB("shell", "getprop", "ro.build.version.release"),
		BootLoader:   executeADB("shell", "getprop", "ro.bootloader"),
		SerialNumber: executeADB("shell", "getprop", "ro.serialno"),
		Security:     executeADB("shell", "getprop", "ro.build.version.security_patch"),
	}
	return info
}

func checkDeviceState() {
	// Check if device is connected
	output := executeADB("devices")
	scanner := bufio.NewScanner(strings.NewReader(output))
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "device") && !strings.Contains(line, "offline") {
			fmt.Println("✅ Device is connected")
			return
		}
	}
	fmt.Println("❌ No device connected")
}

func analyzeSystemHealth() {
	fmt.Println("\n🔍 System Health Check:")
	
	// Battery
	battery := executeADB("shell", "dumpsys", "battery")
	if strings.Contains(battery, "level:") {
		fmt.Println("  📊 Battery info available")
	}
	
	// Storage
	storage := executeADB("shell", "df", "/data")
	if storage != "" {
		fmt.Println("  💾 Storage info available")
	}
	
	// Memory
	meminfo := executeADB("shell", "cat", "/proc/meminfo")
	if meminfo != "" {
		fmt.Println("  🧠 Memory info available")
	}
}

func main() {
	fmt.Println("📱 Android Device Analyzer\n")
	
	checkDeviceState()
	
	info := getDeviceInfo()
	fmt.Println("\n📋 Device Information:")
	fmt.Printf("  Model: %s\n", info.Model)
	fmt.Printf("  Android: %s\n", info.AndroidVer)
	fmt.Printf("  Build: %s\n", info.Build)
	fmt.Printf("  Security Patch: %s\n", info.Security)
	fmt.Printf("  Serial: %s\n", info.SerialNumber)
	
	analyzeSystemHealth()
}
