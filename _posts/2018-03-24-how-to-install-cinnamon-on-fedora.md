---
title: "Installing Cinnamon Desktop on Fedora"
date: 2018-03-24 08:18:57 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-cinnamon-on-fedora/
---

Cinnamon is a modern, feature-rich desktop environment forked from GNOME. It’s lightweight compared to full GNOME installations and offers a traditional taskbar-based interface. Installing it on Fedora is straightforward.

### Basic Installation

Use `dnf` (the modern package manager) with group install:

``` bash
sudo dnf groupinstall 'Cinnamon Desktop'
```

This installs the complete Cinnamon desktop environment along with necessary dependencies and core applications.

If you prefer a minimal installation without extra applications, install just the core components:

``` bash
sudo dnf install cinnamon cinnamon-session cinnamon-control-center
```

### Selecting the Cinnamon Session

After installation, log out of your current session. At the login screen:

1.  Click your username to proceed to the password prompt
2.  Before entering your password, look for the session selector (usually a gear icon or dropdown menu in the bottom-right or top-right corner)
3.  Select “Cinnamon” from the available sessions
4.  Enter your password and log in

Your session choice typically persists across logins, so you won’t need to repeat this step.

### Verifying Your Installation

Once logged in, confirm Cinnamon is running:

``` bash
echo $DESKTOP_SESSION
```

This should output `cinnamon`.

You can also check the version:

``` bash
cinnamon --version
```

### Troubleshooting Common Issues

**Black screen after login**: This sometimes happens on fresh installations. Try pressing `Alt+F2` to open the run dialog and type `cinnamon --replace` to restart the Cinnamon session.

**Applets or extensions not loading**: Restart Cinnamon with:

``` bash
killall cinnamon; cinnamon &
```

**Missing themes or icons**: Install additional Cinnamon themes and icon packs:

``` bash
sudo dnf install cinnamon-themes
```

### Customizing Cinnamon

Access the Cinnamon Settings application (usually available in your application menu) to configure:

- Appearance (themes, icons, fonts)
- Panel settings and applet management
- Window behavior and effects
- Power management
- Keyboard shortcuts

You can also edit the configuration files directly in `~/.config/cinnamon-session/` for advanced customization.

### Switching Back to GNOME or Another Desktop

If you decide to switch to GNOME or another desktop environment, you don’t need to uninstall Cinnamon—just select a different session at the login screen. To remove Cinnamon entirely:

``` bash
sudo dnf groupremove 'Cinnamon Desktop'
```

This removes the group but may leave some dependencies behind. For a clean removal:

``` bash
sudo dnf remove cinnamon\* --noautoremove
```

The `--noautoremove` flag prevents DNF from removing shared dependencies that other applications might need.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
