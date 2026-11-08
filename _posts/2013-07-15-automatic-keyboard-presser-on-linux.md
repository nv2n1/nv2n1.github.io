---
title: "Automating Keyboard Input in Linux: xvkbd and Alternatives"
date: 2013-07-15 12:53:02 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/automatic-keyboard-presser-on-linux/
---

On most distributions:

``` bash
# Debian/Ubuntu
sudo apt install xvkbd

# Fedora/RHEL
sudo dnf install xvkbd

# Arch
sudo pacman -S xvkbd
```

xvkbd is an X11 tool for sending keyboard and mouse input to the focused window. It’s lightweight and useful for straightforward automation tasks, but has significant limitations that make it unsuitable for critical workflows.

## Text Input Syntax

The `-text` option sends strings to the active window. Use escape sequences for modifiers and special keys:

| Sequence | Function |
|----|----|
| `\Cr` | Ctrl+R |
| `\Ax` | Alt+X |
| `\Sr` | Shift+R |
| `\r` | Return/Enter |
| `\t` | Tab |
| `\e` | Escape |
| `\b` | Backspace |
| `\d` | Delete |
| `\[Left]`, `\[Right]`, `\[Up]`, `\[Down]` | Arrow keys |
| `\{Control_L}` | Press Control (raw keysym) |
| `\{+Control_L}` | Press and hold Control |
| `\{-Control_L}` | Release Control |
| `\Ddigit` | Delay digit × 100ms (e.g., `\D5` = 500ms) |
| `\mdigit` | Click mouse button (1=left, 2=middle, 3=right) |
| `\xvalue` | Move mouse X (use +/- for relative) |
| `\yvalue` | Move mouse Y (use +/- for relative) |

## Basic Usage Examples

Type a string with Return:

``` bash
xvkbd -text "echo hello\r"
```

Send Ctrl+A followed by Ctrl+C with a 200ms delay:

``` bash
xvkbd -text "\Ca\D2\Cc"
```

Tab between form fields:

``` bash
xvkbd -text "username\tpassword\r"
```

Combine modifiers for Ctrl+Shift+P:

``` bash
xvkbd -text "\C\Sp"
```

Note: Some applications ignore shift combinations. Test thoroughly with your target application before relying on complex modifier sequences.

## Automating Repetitive Tasks

For pressing the same key multiple times, use a loop:

``` bash
# Refresh browser (F5) 10 times with 1-second intervals
for i in {1..10}; do
  xvkbd -text "\[F5]"
  sleep 1
done
```

Type a command repeatedly:

``` bash
# Execute uptime 5 times with 2-second delays
for i in {1..5}; do
  xvkbd -text "uptime\r"
  sleep 2
done
```

## Robust Automation with Error Handling

Wrap xvkbd in a script with proper error handling and delays:

``` bash
#!/bin/bash

auto_type() {
  local text="$1"
  local delay="${2:-0}"

  if (( delay > 0 )); then
    echo "Waiting ${delay}s before sending: $text"
    sleep "$delay"
  fi

  echo "Sending: $text"
  xvkbd -text "$text" || {
    echo "Failed to send input" >&2
    return 1
  }
}

# Example: Fill a login form with delays between fields
auto_type "admin" 0
auto_type "\t" 0.5
auto_type "password123" 0.5
auto_type "\r" 1
```

Save as `auto_type.sh`, make executable with `chmod +x auto_type.sh`, and run it.

## Practical Example: Auto-Refresh Browser

Monitor a webpage for changes by refreshing every 5 seconds:

``` bash
while true; do
  xvkbd -text "\Cr"
  sleep 5
done
```

Focus your browser window and the refresh will run automatically. Press Ctrl+C to stop.

## Critical Limitations

**Window focus is essential** — Input goes to whatever window has focus when the command runs. If the user switches windows, your script will type into the wrong place. Always verify the target window is active before sending input. This makes xvkbd unsuitable for unattended automation.

**X11 only** — xvkbd doesn’t work on Wayland. Modern systems increasingly use Wayland, making xvkbd less viable for new deployments.

**Hard-coded delays are fragile** — If the system is slow or an application takes longer to respond than expected, timing breaks. There’s no reliable way to detect when a window is ready for input with xvkbd alone.

**Application-dependent behavior** — Terminal emulators, web browsers, and text editors all handle keyboard input differently. Testing is mandatory for each target application.

**Security risk** — Never embed passwords or API keys in xvkbd scripts. This creates a serious vulnerability. Use credential managers, environment variables, or secure vaults instead.

## Better Alternatives

For most automation needs, use these more reliable tools:

### xdotool — Mature keyboard/mouse automation

``` bash
xdotool type "hello"
xdotool key ctrl+c
xdotool search --name "Firefox" windowactivate
xdotool getactivewindow
```

xdotool is more mature than xvkbd and handles complex sequences better. It also has better Wayland support through XWayland.

### Python with pynput — Complex cross-platform automation

``` python
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()

keyboard.type('hello')
keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release('c')
keyboard.release(Key.ctrl)

mouse.position = (100, 200)
mouse.click(Button.left)
```

pynput is better for complex logic and works across Linux, macOS, and Windows.

### Window manager keybindings — Native tiling WM automation

If automating i3, Sway, or other tiling window managers, use native configuration instead of simulating keypresses. This is far more reliable and doesn’t depend on focus or timing.

### Desktop environment APIs — DBus for GNOME/KDE

GNOME and KDE expose DBus interfaces for specific tasks like opening applications, controlling media, or managing windows. This is more reliable than simulating keypresses:

``` bash
# Open an application via GNOME
dbus-send --session --print-reply --dest=org.freedesktop.DBus /org/freedesktop/DBus org.freedesktop.DBus.ListNames
```

### Ansible or configuration management — System-wide automation

For automating tasks across multiple machines, use proper orchestration tools like Ansible, Puppet, or Chef instead of keyboard simulation.

Choose the tool that matches your use case. xvkbd works for simple, locally-focused tasks where window focus is guaranteed and timing is predictable. For anything more complex, one of these alternatives will be more reliable and maintainable.
