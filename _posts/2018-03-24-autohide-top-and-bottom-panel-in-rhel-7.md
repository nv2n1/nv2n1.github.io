---
title: "Auto-hiding Panels in RHEL 7: A Setup Guide"
date: 2018-03-24 11:54:26 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/autohide-top-and-bottom-panel-in-rhel-7/
---

GNOME 3 and GNOME Classic don’t provide built-in autohide functionality for the top panel or taskbar. Unlike some lightweight desktop environments, this feature isn’t available through the standard settings or extensions in recent GNOME versions.

If you need panels that automatically hide when applications are running, you have several options:

### GNOME Extensions (limited approach)

While GNOME itself lacks native autohide for panels, you can explore extensions on <a href="https://extensions.gnome.org" rel="nofollow noopener" target="_blank">extensions.gnome.org</a>. Search for “autohide” or “panel” to see if community-maintained extensions are available for your GNOME version. Keep in mind that extensions can be fragile across updates and may break after GNOME releases.

To install an extension:

``` bash
# Install GNOME Extensions CLI tool
sudo dnf install gnome-shell-extension-manager

# Or use the web interface at extensions.gnome.org
# Click "Install" on an extension (requires native connector)
sudo dnf install chrome-gnome-shell
```

After installation, you’ll need to restart GNOME Shell:

``` bash
# Alt+F2, type 'r', then Enter
# Or log out and log back in
```

### MATE Desktop (recommended alternative)

MATE provides built-in autohide for panels without requiring extensions. To switch:

``` bash
# Install MATE
sudo dnf install @mate-desktop

# Select MATE at the login screen, or start it directly
startx /usr/bin/mate-session
```

To enable autohide in MATE:

1.  Right-click on a panel → Panel Settings
2.  Check “Autohide”
3.  Adjust hide delay if needed

### Other lightweight alternatives

For comparable autohide functionality:

- **Xfce**: Lightweight, has panel autohide built-in
- **KDE Plasma**: Full-featured, supports panel autohiding
- **i3/sway**: Window managers with complete configurability (advanced)

``` bash
# Install Xfce
sudo dnf install @xfce-desktop-environment

# Install KDE Plasma
sudo dnf install @kde-desktop-environment
```

### If you must stay on GNOME

If you’re locked into GNOME for other reasons, consider:

- **Using fullscreen applications** — GNOME hides the top panel in fullscreen mode
- **Disabling the top panel entirely** via `gsettings` (loses clock and system menu):

``` bash
gsettings set org.gnome.shell enable-hot-corners false
```

- **Using keyboard shortcuts** to maximize window space (`Super+H` or `Super+Up` for window snapping)

The practical reality: GNOME prioritizes a consistent, persistent interface. If autohiding panels is a workflow requirement, switching to MATE or Xfce is the most straightforward solution.

## Troubleshooting Common Issues

If you encounter problems during installation, check these common solutions:

- Ensure your system packages are up to date before installing new software
- Check for conflicting packages that might prevent installation
- Verify network connectivity if downloading packages from external repositories
- Review system logs in /var/log/ for detailed error messages

## Verification Steps

After installation, verify everything is working correctly by checking the installed version and running basic functionality tests. Most command-line tools respond to the –version or -v flag to display their version information.

## Keeping Your Installation Updated

Regularly update your system to receive security patches and bug fixes. On Fedora, use dnf update. On Ubuntu and Debian, use apt update followed by apt upgrade. For software installed via language-specific package managers like pip, npm, or gem, check their respective update commands.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
