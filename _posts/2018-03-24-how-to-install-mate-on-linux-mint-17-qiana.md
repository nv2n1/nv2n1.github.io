---
title: "Installing MATE Desktop on Linux Mint 17 Qiana"
date: 2018-03-24 11:49:54 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-mate-on-linux-mint-17-qiana/
---

MATE Desktop provides a traditional GNOME 2-style interface that many users prefer over modern GNOME Shell. Here’s how to install it on Linux Mint 17 Qiana.

## Install MATE Desktop

```wp-block-code
sudo apt-get update
sudo apt-get install mate-desktop-environment
```

For the full MATE experience with extras:

```wp-block-code
sudo apt-get install mate-desktop-environment-extras
```

This adds additional applets, themes, and utilities not included in the base package.

## Switch to MATE

1.  Log out of your current session
2.  At the login screen, click the session icon (usually near your username)
3.  Select **MATE** from the list of available desktop environments
4.  Enter your password to log in

Linux Mint will remember your choice for future logins.

## Configure MATE Panels

MATE uses a traditional panel system similar to GNOME 2. Customize panels by right-clicking them:

- **Add applets:** Right-click panel → Add to Panel
- **Move applets:** Alt+right-click and drag
- **Remove applets:** Right-click the applet → Remove from Panel
- **Panel properties:** Right-click panel → Properties (adjust size, position, auto-hide)

Recommended applets to add:

- **CPU Frequency Scaling Monitor** — Shows and controls CPU governor
- **System Monitor** — Graphs CPU, memory, and network usage
- **Weather Report** — Current conditions in your panel
- **Workspace Switcher** — Navigate virtual desktops

## Customize MATE Themes

Install additional themes for MATE:

```wp-block-code
sudo apt-get install mate-themes
```

Change the theme in **System → Preferences → Appearance**. You can also install themes manually by extracting them to `~/.themes/` or `/usr/share/themes/`.

For a modern look with traditional layout, try these themes:

- **Adwaita** — Clean GNOME-style theme
- **TraditionalOk** — Classic green Mint look
- **BlueMenta** — Blue variant of the Menta theme

## MATE vs Cinnamon on Linux Mint

Linux Mint 17 offers three desktop environments:

- **Cinnamon** — Modern, GNOME 3-based, Mint’s default. Best for users who want a contemporary desktop with traditional elements.
- **MATE** — GNOME 2 fork, lightweight, traditional. Best for users who prefer the classic GNOME 2 layout or have older hardware.
- **Xfce** — Even lighter than MATE, good for very old hardware or minimal resource usage.

MATE uses fewer resources than Cinnamon, making it better suited for machines with less than 2GB RAM.

## MATE Tweak Tool

The MATE Tweak tool provides advanced desktop configuration:

```wp-block-code
sudo apt-get install mate-tweak
```

Use it to:

- Switch between traditional and modern panel layouts
- Enable/disable window snapping and tiling
- Configure button layout (close/minimize/maximize order)
- Manage workspace settings

## Keyboard Shortcuts

Configure shortcuts in **System → Preferences → Hardware → Keyboard Shortcuts**:

- `Alt+F1` — Open main menu
- `Alt+F2` — Run command
- `Ctrl+Alt+D` — Show desktop
- `Ctrl+Alt+Arrow` — Switch workspaces
- `Alt+Tab` — Switch windows

Note: Linux Mint 17 is based on Ubuntu 14.04 LTS and reached end-of-life in 2019. If you’re still running it, consider upgrading to a current Linux Mint version for security updates and continued package support.

## Upgrading from Linux Mint 17

If you’re still on Mint 17 with MATE, the upgrade path goes through several intermediate versions:

```wp-block-code
# Mint 17 -> 18 -> 19 -> 20 -> 21 -> 22
# Each step requires a full upgrade

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install mintupgrade
sudo mintupgrade check
sudo mintupgrade upgrade
```

Alternatively, do a clean install of the latest Linux Mint MATE edition — this is faster and avoids potential issues from accumulated configuration changes across multiple upgrades.

Modern Linux Mint 22 with MATE provides the same traditional desktop experience but with updated packages, better hardware support, and security updates through 2029.
