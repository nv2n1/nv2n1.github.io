---
title: "Dual Boot GNOME and MATE on Ubuntu"
date: 2018-07-31 02:27:48 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-gnome-3-in-ubuntu-mate-18-04/
---

Ubuntu MATE ships with the MATE desktop environment, but you might prefer GNOME’s modern interface and tighter integration with system tools. Installing GNOME alongside MATE is straightforward and lets you switch between them at login without removing either one.

## Installation

Update your package list and install the GNOME desktop package:

``` bash
sudo apt update
sudo apt install ubuntu-gnome-desktop
```

The package pulls in GNOME Shell, Mutter window manager, and standard GNOME applications. During installation, you’ll be prompted to select a display manager — this handles your login screen and session startup.

## Choosing a Display Manager

**GDM3 (GNOME Display Manager)**

- Modern, polished login screen with GNOME branding
- Better integration with GNOME Settings and Wayland sessions
- Slightly higher memory footprint (~50-100MB more than LightDM)
- Required for seamless Wayland support

**LightDM (MATE’s default)**

- Minimal, fast login experience
- Lower resource usage (important on older hardware)
- More easily customizable through configuration files
- Better compatibility if you’re switching desktops frequently

Choose GDM3 if you’re primarily using GNOME. Choose LightDM if you value speed or run on constrained hardware. You can change your selection later by running:

``` bash
sudo dpkg-reconfigure gdm3
```

Or to switch to LightDM:

``` bash
sudo apt remove gdm3
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

## Switching Between Desktops

Once both desktops are installed, log out from your current session. On the login screen, look for a menu or gear icon (⚙) — typically in the bottom-right or top-right corner, though placement depends on your display manager.

Click it to select your desired desktop environment (usually listed as “GNOME” or “Ubuntu” for GNOME, and “MATE” for MATE). Enter your credentials and you’ll boot into your chosen desktop.

Your session choice persists for future logins unless you change it again at the login screen.

## Performance and Display Protocol Considerations

Modern GNOME (version 46+) has seen substantial optimization work. While MATE remains lighter-weight, the performance gap on hardware from the last 5+ years is negligible in real-world usage. Both handle daily tasks smoothly.

GNOME offers superior Wayland support, which improves performance on newer GPUs and fixes many X11-era graphics quirks. Wayland eliminates screen tearing, improves touchpad responsiveness, and provides better security isolation. MATE still uses X11 primarily, which may feel more responsive in some edge cases but lacks modern display protocol benefits.

If you’re running modern hardware (within the last 3-4 years), Wayland is worth trying. Switch to Wayland at the login screen by selecting “GNOME on Wayland” instead of the default “GNOME” option.

## Removing GNOME

If you decide GNOME isn’t for you, cleanly remove it while preserving MATE:

``` bash
sudo apt remove ubuntu-gnome-desktop gnome-shell
sudo apt autoremove
```

This removes GNOME packages while leaving your system stable. Your MATE desktop remains untouched. If you also want to remove GDM3 and revert to LightDM:

``` bash
sudo apt remove gdm3
sudo apt install lightdm
sudo dpkg-reconfigure lightdm
```

## Troubleshooting

**Session won’t start after switching desktops**

Clear your session cache and try again:

``` bash
rm -rf ~/.local/share/gnome-shell/
rm -rf ~/.cache/gnome-shell/
```

Verify both desktops are fully installed:

``` bash
apt list --installed | grep -E "gnome-shell|mate-desktop"
```

If packages are missing, reinstall the desktop metapackage:

``` bash
sudo apt install --reinstall ubuntu-gnome-desktop
```

**Keyboard shortcuts differ between desktops**

GNOME uses different default bindings than MATE. This is expected behavior. Check Settings → Keyboard in each environment to customize, or copy your preferred keybindings between them. GNOME stores settings in `~/.config/dconf/` and MATE uses `~/.config/mate-settings-daemon/`.

**High CPU usage after switching**

New sessions sometimes spawn extra processes during initialization. Log out and back in to clean up. If the issue persists, restart your system:

``` bash
sudo systemctl reboot
```

**Login screen appears frozen or unresponsive**

If GDM3 hangs, switch to a virtual terminal and restart the display manager:

``` bash
Ctrl+Alt+F3
sudo systemctl restart gdm3
Ctrl+Alt+F1
```

**Can’t find the session selector at login**

Some older versions of GDM3 hide the session selector. Click the user account to expand options, or look for an icon or menu in the window title bar. If using LightDM, the session selector typically appears as a dropdown in the bottom-left corner of the login window.
