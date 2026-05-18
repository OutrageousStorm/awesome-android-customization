package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func adb(args ...string) (string, error) {
	cmd := exec.Command("adb", args...)
	out, err := cmd.CombinedOutput()
	return string(out), err
}

func main() {
	fmt.Println("🚀 Interactive Launcher Switcher")
	fmt.Println("================================")

	// List installed launchers
	out, _ := adb("shell", "pm", "list", "packages")
	launchers := []string{}
	for _, line := range strings.Split(out, "\n") {
		pkg := strings.TrimPrefix(line, "package:")
		if strings.Contains(pkg, "launcher") || strings.Contains(pkg, "home") {
			launchers = append(launchers, pkg)
		}
	}

	if len(launchers) == 0 {
		fmt.Println("No launchers found")
		return
	}

	fmt.Println("\nAvailable launchers:")
	for i, l := range launchers {
		fmt.Printf("%d. %s\n", i+1, l)
	}

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("\nSelect launcher (number): ")
	scanner.Scan()
	input := scanner.Text()

	var idx int
	fmt.Sscanf(input, "%d", &idx)
	if idx < 1 || idx > len(launchers) {
		fmt.Println("Invalid selection")
		return
	}

	pkg := launchers[idx-1]
	fmt.Printf("Setting default launcher to: %s\n", pkg)

	// Find main activity
	out, _ = adb("shell", "pm", "dump", pkg)
	var mainActivity string
	for _, line := range strings.Split(out, "\n") {
		if strings.Contains(line, "android.intent.action.MAIN") {
			parts := strings.Fields(line)
			if len(parts) > 0 {
				mainActivity = parts[0]
				break
			}
		}
	}

	if mainActivity == "" {
		fmt.Println("Could not find main activity")
		return
	}

	// Launch
	adb("shell", "cmd", "package", "set-home-activity", fmt.Sprintf("%s/%s", pkg, mainActivity))
	fmt.Println("✓ Launcher switched!")
}
