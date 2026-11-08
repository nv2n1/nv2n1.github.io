---
title: "Installing MATE Desktop on Fedora 17"
date: 2018-03-24 07:54:05 +0000
author: "Q A"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-install-the-mate-fork-of-gnome-2-on-fedora-17/
---

MATE is a continuation of GNOME 2, maintained by the MATE Desktop Environment project. It’s included in Fedora’s official repositories and is a supported desktop option.

### Install MATE Desktop

MATE is available as a desktop environment group in Fedora 41’s repositories. Install the base desktop with:

``` bash
sudo dnf install @mate-desktop
```

The `@mate-desktop` group installs the core components needed for a functional MATE session.

### Install Additional MATE Applications

Beyond the base desktop, you’ll want several standard applications. Install them with:

``` bash
sudo dnf install mate-media \
  mate-screensaver \
  mate-system-monitor \
  mate-power-manager \
  mate-utils \
  mate-image-viewer \
  mate-terminal
```

These provide common functionality like volume control, screensaver, system monitoring, terminal access, and image viewing.

### MATE Forked Applications

MATE maintains its own versions of several GNOME applications, keeping them aligned with GNOME 2 design principles:

- **Caja** – File manager (GNOME Nautilus fork)
- **Pluma** – Text editor (gedit fork)
- **Eye of MATE** – Image viewer (Eye of GNOME fork)
- **Atril** – Document viewer (Evince fork)
- **Engrampa** – Archive manager (File Roller fork)
- **MATE Terminal** – Terminal emulator (GNOME Terminal fork)
- **Marco** – Window manager (Metacity fork)

### Set MATE as Default Desktop

After installation, log out and select MATE from the session menu at the login screen. Most display managers (GDM, SDDM, LightDM) show this option near your username.

### Remove GNOME Applications (Optional)

If you want to clean up GNOME packages and use MATE equivalents exclusively:

``` bash
sudo dnf remove eog \
  file-roller \
  nautilus \
  gedit \
  gnome-terminal \
  gnome-screensaver \
  gnome-media \
  gnome-system-monitor \
  gnome-power-manager \
  gnome-utils
```

Be cautious—verify that nothing else depends on these packages before removing them.

### Remove GNOME Core (Advanced)

To remove the GNOME desktop environment entirely:

``` bash
sudo dnf remove gnome-session \
  gnome-desktop3 \
  gnome-session-xsession \
  gnome-shell
```

Remove additional GNOME packages if desired:

``` bash
sudo dnf remove gnome-themes \
  gnome-menus \
  gnome-search-tool \
  gnome-video-effects \
  gnome-bluetooth \
  gnome-screenshot
```

### Troubleshooting

If MATE doesn’t appear as a session option after installation, restart the display manager:

``` bash
sudo systemctl restart display-manager
```

For Wayland-based systems, MATE may still be X11-only. Check your session type and switch back to X11 if needed.

### Additional Resources

For a full list of available MATE applications and community extensions, check the <a href="https://mate-desktop.org/" rel="nofollow noopener" target="_blank">MATE Desktop project page</a>.

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
