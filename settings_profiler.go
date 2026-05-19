package main

import (
	"fmt"
	"os/exec"
	"strings"
	"time"
)

// SettingsProfiler measures Android settings read/write performance
func main() {
	fmt.Println("⚙️  Android Settings Profiler\n")
	
	settings := []string{
		"system", "secure", "global",
	}
	
	for _, ns := range settings {
		start := time.Now()
		cmd := exec.Command("adb", "shell", "settings", "list", ns)
		out, err := cmd.Output()
		elapsed := time.Since(start)
		
		if err == nil {
			lines := len(strings.Split(string(out), "\n"))
			fmt.Printf("[%s] %d settings in %v\n", ns, lines, elapsed)
		}
	}
}
