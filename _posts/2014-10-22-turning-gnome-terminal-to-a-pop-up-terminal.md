---
title: "Pop-up Terminal Hotkey for GNOME"
date: 2014-10-22 06:22:12 +0000
modified: 2026-04-11 16:22:08 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /turning-gnome-terminal-to-a-pop-up-terminal/
---

A toggle-on-demand terminal you can summon and hide with a single keystroke is useful for quick commands without cluttering your workspace. This guide walks you through creating one using GNOME Terminal and basic shell scripting.

## Prerequisites

You need `xdotool` and `wmctrl` installed to manipulate windows:

``` bash
# Debian/Ubuntu
sudo apt install xdotool wmctrl

# Fedora
sudo dnf install xdotool wmctrl

# Arch
sudo pacman -S xdotool wmctrl
```

## The script

Save this as `~/.local/bin/toggle-terminal.sh`:

``` bash
#!/bin/bash
# toggle-terminal.sh
# Toggle GNOME Terminal visibility with a hotkey

TERM_CLASS="gnome-terminal-server"
STATE_FILE="/dev/shm/toggle-terminal.$USER"
WAIT_SEC=0.5
MAX_WAIT_CNT=20

create_terminal() {
    gnome-terminal &
    sleep 1

    local wait_cnt=0
    while [ $wait_cnt -lt $MAX_WAIT_CNT ]; do
        sleep $WAIT_SEC
        term=$(xdotool search --class "$TERM_CLASS" | tail -1)
        if [ -n "$term" ]; then
            echo "$term" > "$STATE_FILE"
            xdotool windowactivate "$term"
            return 0
        fi
        ((wait_cnt++))
    done

    echo "Failed to create terminal" >&2
    return 1
}

toggle_terminal() {
    local term=""

    # Read stored terminal ID if it exists
    if [ -f "$STATE_FILE" ]; then
        term=$(cat "$STATE_FILE")
        # Verify window still exists
        if ! xdotool getwindowname "$term" >/dev/null 2>&1; then
            term=""
            rm -f "$STATE_FILE"
        fi
    fi

    # Create terminal if none exists
    if [ -z "$term" ]; then
        create_terminal
        return $?
    fi

    # Toggle visibility
    local current_window=$(xdotool getactivewindow)

    if [ "$term" = "$current_window" ]; then
        # Terminal is focused; minimize it
        xdotool windowminimize "$term"
    else
        # Terminal exists but isn't focused; bring it to front
        xdotool windowactivate "$term"
        xdotool windowraise "$term"
    fi
}

toggle_terminal
```

Make it executable:

``` bash
chmod +x ~/.local/bin/toggle-terminal.sh
```

## Bind to a hotkey

Choose your keybinding and configure it in your desktop environment.

**GNOME 40+:**

1.  Open Settings → Keyboard → Custom Shortcuts
2.  Click **+** to add a new shortcut
3.  Name: “Toggle Terminal”
4.  Command: `/home/youruser/.local/bin/toggle-terminal.sh`
5.  Press your desired key (F12, Super+\`, Ctrl+Alt+T, etc.)

**Cinnamon:**

Settings → Keyboard → Keyboard shortcuts → Custom shortcuts → Add custom shortcut

**KDE Plasma:**

System Settings → Shortcuts → Custom Shortcuts → Edit → New → Global Shortcut

**X11 with no DE (using xbindkeys):**

Install xbindkeys, then add to `~/.xbindkeysrc`:

    "/home/youruser/.local/bin/toggle-terminal.sh"
        F12

Run `xbindkeys` or add it to your `~/.xinitrc`:

``` bash
xbindkeys &
```

## How it works

The script maintains a single terminal window ID in `/dev/shm/toggle-terminal.$USER`. Using `/dev/shm/` avoids disk I/O and ensures the state file is cleaned up on reboot.

On each invocation:

1.  **Read the state file** — Retrieve the tracked terminal window ID
2.  **Verify the window exists** — Confirm the stored ID still points to an open window using `xdotool getwindowname`
3.  **Create if needed** — Spawn a new terminal if none is tracked or the old one was closed
4.  **Toggle visibility** — If the terminal is focused, minimize it; otherwise raise and focus it

## Handling edge cases

**Stale window IDs:** If the user closes the terminal manually, the next hotkey press triggers window validation. The script detects the closed window and creates a fresh one.

**Multiple GNOME Terminal windows:** This script manages only one terminal per hotkey. If you manually open additional terminals, they won’t interfere. The `tail -1` in `xdotool search` ensures the newest window is selected.

**Timing issues:** On slower systems, the terminal window may take longer to register. Increase `WAIT_SEC` or `MAX_WAIT_CNT` if creation fails consistently.

**Multi-user systems:** The `$USER` suffix in the state filename prevents conflicts between users toggling terminals simultaneously.

## Customizations

**Maximize on open:**

Replace the `gnome-terminal &` line with:

``` bash
gnome-terminal --maximize &
```

**Always open on current workspace:**

Add this before `xdotool windowactivate "$term"` in `create_terminal()`:

``` bash
current_desktop=$(wmctrl -d | grep '\*' | awk '{print $1}')
xdotool set_desktop_for_window "$term" "$current_desktop"
```

**Dropdown animation (partial):**

Instead of standard minimize, use:

``` bash
xdotool windowminimize "$term"
wmctrl -i -b add,shaded "$term"
```

This shades the window (collapses it), giving a more dropdown-like feel when toggled again.

**Different terminal application:**

Change `TERM_CLASS` and the launcher command. For Tilix:

``` bash
TERM_CLASS="tilix"
# In create_terminal():
tilix &
```

For xfce4-terminal:

``` bash
TERM_CLASS="xfce4-terminal"
# In create_terminal():
xfce4-terminal &
```

## Why this approach instead of dedicated popup terminals

Guake and Yakuake are excellent, but they add another application to maintain. GNOME Terminal is stable, receives regular updates, and is available on every GNOME system. This script keeps you on native tooling without extra dependencies. The approach works across GNOME, Cinnamon, and other X11 desktop environments with minimal configuration.
