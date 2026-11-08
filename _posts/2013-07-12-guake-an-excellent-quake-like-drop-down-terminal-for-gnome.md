---
title: "Guake: A Quake-Style Dropdown Terminal for GNOME"
date: 2013-07-12 16:31:57 +0000
layout: post
canonical: https://www.systutorials.com/guake-an-excellent-quake-like-drop-down-terminal-for-gnome/
---

Guake is a drop-down terminal emulator for GNOME that brings the Quake-style console experience to Linux desktops. When you press a hotkey (F12 by default), a terminal slides down from the top of the screen. Press it again and it retracts. It’s fast, minimal, and designed purely around keyboard efficiency.

### Installation

On Fedora/RHEL-based systems:

``` bash
sudo dnf install guake
```

On Debian/Ubuntu:

``` bash
sudo apt install guake
```

On Arch:

``` bash
sudo pacman -S guake
```

After installation, start it with:

``` bash
guake
```

To enable it at login, add it to your GNOME startup applications or use:

``` bash
systemctl --user enable --now guake
```

### Core Features

**Hotkey Activation**

The default hotkey is F12. When pressed, Guake appears from the top of the screen. Press F12 again and it disappears. This is the core feature — you never need to click or minimize/maximize windows.

**Tab Management**

Create tabs with Ctrl+Shift+T. Navigate between them using Ctrl+Page Up/Page Down or by clicking. Each tab maintains its own shell session and working directory.

**Fullscreen Mode**

Press F11 to toggle fullscreen mode. This gives you a full-screen terminal without closing the application, letting you switch back to the desktop instantly with your hotkey.

**Transparency and Colors**

Configure transparency, fonts, and color schemes in the preferences (Ctrl+comma). The settings are stored in `~/.config/guake/` in JSON format if you need to manage them manually.

### Configuration

Access preferences with Ctrl+comma. Key settings:

- **Hotkey**: Rebind the activation key if F12 conflicts with other applications
- **Scrollback Lines**: Set how many lines of history to keep (default 5000)
- **Window Width**: Set percentage of screen width (default 100%)
- **Font and Colors**: Choose from built-in themes or create custom ones
- **Tab Position**: Tabs can appear at the top or bottom

Edit the config file directly for advanced settings:

``` bash
nano ~/.config/guake/guake.json
```

### Comparison with Alternatives

**Yakuake** (KDE Plasma) works similarly but is heavier and slower. It’s tied to KDE’s infrastructure.

**Tilda** is another drop-down terminal but is less stable and receives infrequent updates. Guake is actively maintained and more reliable.

**Kitty** with tmux or shell aliases can replicate some functionality but requires more setup and doesn’t provide the same seamless drop-down experience.

### Common Use Cases

**Quick Command Execution**

Press F12, run a command, press F12 again. Your workspace is unchanged and the terminal is out of the way.

**Monitoring Tasks**

Keep one tab open for `watch` or `tail` commands while working in other applications. Switch to it instantly without window management.

**SSH Sessions**

Each tab can hold a persistent SSH connection. Press F12 to access your remote session anytime.

**Development Workflow**

Use one tab for your editor/IDE, another for git commands, another for logs. Navigate with hotkeys instead of managing windows.

### Tips and Tricks

**Multiple Workspaces**

Run separate Guake instances on different workspaces by launching `guake &` multiple times. Each maintains its own settings independently.

**Scripting**

Open a terminal and run commands directly:

``` bash
guake --show
guake --hide
guake --toggle-visibility
```

**Keybindings Beyond the Default**

If F12 conflicts with your application, reconfigure it in preferences. Common alternatives: Ctrl+Grave, Super+T, or Ctrl+Alt+T.

**Session Persistence**

Guake doesn’t automatically restore tabs on restart. Use `tmux` or `screen` within Guake tabs for persistent session management across reboots.

### When NOT to Use Guake

Guake works best in GNOME and Wayland-aware systems (GNOME 40+). On other desktop environments, Yakuake (KDE), Tint2 with a terminal plugin, or WezTerm with your window manager’s keybindings may be better choices.

If you regularly need terminal windows alongside desktop applications (not overlaid), a traditional terminal emulator is more practical than a drop-down terminal.

### Bottom Line

Guake delivers exactly what it promises: instant terminal access without window clutter. It won’t replace your main terminal, but it eliminates friction for quick commands, monitoring, and multi-tasking. The simplicity is the feature.
