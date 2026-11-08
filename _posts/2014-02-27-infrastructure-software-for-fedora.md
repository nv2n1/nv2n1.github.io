---
title: "Essential Tools and Infrastructure for Fedora Development"
date: 2014-02-27 08:37:44 +0000
modified: 2026-04-11 16:40:30 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /infrastructure-software-for-fedora/
---

Fedora is a cutting-edge distribution sponsored by Red Hat that serves as a testing ground for technologies eventually stabilized in RHEL. This guide covers essential infrastructure, system administration, and desktop tools for modern Fedora systems, with practical installation and usage examples.

## Desktop Environment Setup

### GNOME Configuration

Modern GNOME desktops (GNOME 40+) use dconf for configuration, with the GNOME Settings application handling most user-facing options. GNOME Tweaks provides access to advanced settings not exposed in the main settings panel.

Install GNOME Tweaks:

``` bash
sudo dnf install gnome-tweaks
gnome-tweaks
```

Common customizations via dconf include window manager button layouts:

``` bash
dconf write /org/gnome/desktop/wm/preferences/button-layout "appmenu:minimize,maximize,close"
```

For a graphical dconf browser, install dconf-editor:

``` bash
sudo dnf install dconf-editor
```

Query existing settings without opening the GUI:

``` bash
dconf read /org/gnome/desktop/wm/preferences/button-layout
dconf list /org/gnome/desktop/
```

### MATE Desktop Configuration

If running MATE (common on Fedora spins), use mate-tweak for customization:

``` bash
sudo dnf install mate-tweak
mate-tweak
```

## Screenshot and Screen Capture Tools

### GNOME Screenshot

GNOME’s built-in screenshot tool handles standard use cases efficiently:

``` bash
# Full screen screenshot
gnome-screenshot

# Area selection (interactive)
gnome-screenshot -a

# Screenshot with 5-second delay
gnome-screenshot -d 5

# Save to specific file
gnome-screenshot -f ~/Pictures/screenshot.png

# Copy to clipboard instead of saving
gnome-screenshot -c
```

### Flameshot (Recommended for Advanced Features)

Flameshot provides superior screenshot annotation, editing, and sharing capabilities:

``` bash
sudo dnf install flameshot

# Launch GUI mode
flameshot gui

# Fullscreen mode
flameshot full

# Interactive area selection
flameshot region

# Screenshot with 2-second delay
flameshot gui --delay 2000
```

Configure Flameshot to launch with a keyboard shortcut by adding to your desktop environment’s keyboard settings, or via command line on GNOME:

``` bash
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/flameshot/']"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/flameshot/ name 'Flameshot'
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/flameshot/ command 'flameshot gui'
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/flameshot/ binding 'Print'
```

### Wayland Considerations

GNOME on Wayland (the default in recent Fedora releases) works with modern screenshot tools. If you encounter issues with area selection under X11, Flameshot is a reliable alternative. For remote X11 forwarding scenarios, ensure your forwarding supports the necessary protocols.

## Package Management

Use dnf for all package operations on current Fedora:

``` bash
# Synchronize package cache and upgrade all packages
sudo dnf upgrade

# Install a package (or multiple: dnf install pkg1 pkg2 pkg3)
sudo dnf install package-name

# Search for packages by name or description
dnf search keyword

# Show detailed package information
dnf info package-name

# List installed packages with filtering
dnf list installed | grep pattern

# Remove a package and dependencies
sudo dnf remove package-name

# Check for available updates without installing
dnf check-update

# Clean package cache to free disk space
sudo dnf clean all
```

Enable third-party repositories when needed:

``` bash
# Example: RPM Fusion (for multimedia and other packages)
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

# Verify installed repositories
dnf repolist
```

## Essential System Administration Tools

### System Monitoring and Information

``` bash
# Install system monitor GUI
sudo dnf install gnome-system-monitor

# Command-line alternatives
sudo dnf install htop          # Interactive process monitor
sudo dnf install bottom        # Modern system resource viewer
sudo dnf install nvtop         # GPU monitoring
```

### Terminal and File Management

``` bash
# Enhanced terminal emulator
sudo dnf install gnome-terminal

# File manager with admin features
sudo dnf install nautilus-admin

# Lightweight alternative file managers
sudo dnf install pcmanfm-qt     # Qt-based file manager
sudo dnf install thunar         # Xfce file manager (lightweight)
```

### System and Power Management

``` bash
# Power profiles management
sudo dnf install power-profiles-daemon

# Query current power profile
powerprofilesctl get

# Switch to performance mode
sudo powerprofilesctl set performance

# Switch back to balanced
sudo powerprofilesctl set balanced

# System information and diagnostics
sudo dnf install inxi          # Hardware inventory tool
```

## Verify Your System

Check your Fedora version and installed packages:

``` bash
# Fedora version
cat /etc/fedora-release
hostnamectl

# DNF version
dnf --version

# List all installed packages with version info
dnf list installed

# Find packages matching a pattern
dnf list "gnome*"

# Check disk usage by package
dnf repoquery --querytags | grep size
```

## Common Infrastructure Tasks

### Enable SSH

``` bash
sudo dnf install openssh-server openssh-clients

# Enable and start SSH
sudo systemctl enable sshd
sudo systemctl start sshd

# Check service status
systemctl status sshd
```

### Install Development Tools

``` bash
# Install build essentials
sudo dnf groupinstall "Development Tools"
sudo dnf groupinstall "C Development Tools and Libraries"

# Install additional development utilities
sudo dnf install git cmake ninja-build
```

### Configure Firewall

``` bash
# Check firewall status
sudo firewall-cmd --state

# List active zones and services
sudo firewall-cmd --list-all

# Open SSH port (if not already open)
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

For current Fedora documentation and release notes, refer to the <a href="https://docs.fedoraproject.org" rel="nofollow noopener" target="_blank">official Fedora documentation</a>.
