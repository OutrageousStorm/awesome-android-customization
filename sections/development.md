# Development & Advanced

Tools for Android developers and power users who want to code on their device.

---

## Terminal & Linux

- **Termux** — Full Linux environment on Android (no root)
  - https://termux.dev
  - Package manager: pkg install <tool>
  - SSH, Python, Node, Rust available

- **Termux:API** — Access Android APIs from Termux shell
  - Notifications, sensors, SMS, contacts

- **vim/nano/micro** — Text editors in Termux
  - `pkg install vim`

---

## Development IDEs

- **Visual Studio Code Server** — Run VS Code on Android (via Termux)
  ```bash
  # In Termux:
  npm install -g code-server
  code-server
  # Access on http://localhost:8080
  ```

- **Android Studio** — Full IDE (requires 2GB+ RAM)
  - https://developer.android.com/studio

- **AIDE** — Java/C++ IDE on Android
  - Play Store: AIDE - C/C++/Java IDE
  - Lightweight alternative to Android Studio

---

## Version Control

- **Git via Termux**
  ```bash
  pkg install git
  git clone <repo>
  git commit -am "message"
  git push
  ```

- **GitHub CLI**
  ```bash
  pkg install gh
  gh repo create my-app
  ```

---

## Build Tools

- **Gradle** (via Termux)
  ```bash
  pkg install gradle
  gradle build
  ```

- **Apache Maven**
  ```bash
  pkg install maven
  mvn compile
  ```

---

## Programming Languages (Termux)

- **Python**: `pkg install python` + `pip install requests`
- **Node.js**: `pkg install nodejs` + `npm install`
- **Rust**: `pkg install rust` + `cargo build`
- **Go**: `pkg install golang` + `go run main.go`
- **Ruby**: `pkg install ruby`

---

## Debugging & Analysis

- **frida** — Dynamic instrumentation
  - `pip install frida-tools`
  - https://frida.re

- **strace** — System call tracer
  - `pkg install strace`
  - `strace -f ls`

- **ltrace** — Library call tracer
  - `pkg install ltrace`

---

## Testing

- **pytest** — Python testing
  - `pip install pytest`

- **JUnit** — Java testing framework
  - Via Gradle/Maven

---

See also: [android-toolkit-scripts](https://github.com/OutrageousStorm/android-toolkit-scripts)
