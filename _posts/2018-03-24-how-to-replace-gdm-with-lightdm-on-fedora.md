---
title: "Replacing GDM with LightDM on Fedora"
date: 2018-03-24 08:19:02 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-replace-gdm-with-lightdm-on-fedora/
---

LightDM is a lighter alternative to GDM (GNOME Display Manager). If GDM is causing issues, you prefer a simpler login screen, or you’re running a lightweight desktop environment, here’s how to switch to LightDM on Fedora.

## Install LightDM

```wp-block-code
sudo dnf install lightdm lightdm-gtk-greeter
```

The `lightdm-gtk-greeter` provides the graphical login screen. Other greeter options include:

- `lightdm-gtk-greeter` — Simple, GTK-based, fast loading (recommended for most users)
- `lightdm-webkit2-greeter` — Themeable with HTML, CSS, and JavaScript for custom login screens
- `lightdm-kde-greeter` — KDE Plasma integration with Plasma-style branding
- `lightdm-another-greeter` — Minimal, keyboard-driven greeter

## Switch Default Display Manager

Fedora uses systemd to manage which display manager loads at boot:

```wp-block-code
# Disable GDM (current display manager)
sudo systemctl disable gdm

# Enable LightDM
sudo systemctl enable lightdm

# Switch immediately without rebooting
sudo systemctl stop gdm
sudo systemctl start lightdm
```

When you stop GDM, the current desktop session ends. LightDM starts with the login greeter. This change persists across reboots.

## Configure LightDM

The main configuration file is `/etc/lightdm/lightdm.conf`:

```wp-block-code
[SeatDefaults]
greeter-session=lightdm-gtk-greeter
user-session=gnome
session-wrapper=/etc/lightdm/Xsession
allow-guest=false
xserver-command=Xorg
```

Key settings:

- `greeter-session` — Which greeter to display
- `user-session` — Default desktop session (gnome, plasma, xfce, etc.)
- `allow-guest` — Enable or disable guest login
- `autologin-user` — Skip login for a specific user (see below)

## Customize the Greeter Appearance

Edit `/etc/lightdm/lightdm-gtk-greeter.conf`:

```wp-block-code
[greeter]
theme-name = Adwaita
icon-theme-name = Adwaita
background = /usr/share/backgrounds/fedora/default/standard/fedora.png
font-name = Cantarell 11
clock-format = %H:%M
show-clock = true
show-user-image = true
```

Set the background to any image file. For a solid color background instead:

```wp-block-code
background = #2c2c2c
```

## Autologin Configuration

To automatically log in a user without a password prompt:

```wp-block-code
# Edit /etc/lightdm/lightdm.conf
[SeatDefaults]
autologin-user=yourusername
autologin-user-timeout=0
```

Add the user to the autologin group:

```wp-block-code
sudo groupadd -r autologin
sudo usermod -aG autologin yourusername
```

Autologin is convenient for single-user machines but reduces physical security. Anyone with access to the machine gets a full desktop session.

## Switch Back to GDM

```wp-block-code
sudo systemctl disable lightdm
sudo systemctl enable gdm
sudo systemctl start gdm
```

GDM takes over immediately. If the switch doesn’t work cleanly, reboot.

## Troubleshooting Common Issues

**Black screen after switching:**

```wp-block-code
# Switch to a TTY (Ctrl+Alt+F2)
# Check LightDM logs
sudo journalctl -u lightdm --since "10 minutes ago"

# Verify the greeter is installed
rpm -qa | grep lightdm
ls /usr/share/xgreeters/
```

**Login loop (returns to login screen after entering password):**

```wp-block-code
# Check for Xsession errors
cat ~/.xsession-errors

# Verify the desktop session file exists
ls /usr/share/xsessions/
ls /usr/share/wayland-sessions/

# Try a different session
# At the login screen, look for a session dropdown (usually near username)
```

**LightDM doesn’t start after reboot:**

```wp-block-code
# Verify the service is enabled
systemctl is-enabled lightdm

# Ensure graphical target is set
sudo systemctl set-default graphical.target

# Manually start if needed
sudo systemctl start lightdm
```

## LightDM vs GDM Comparison

**Choose LightDM when:**

- Running lightweight desktops (Xfce, LXQt, MATE, i3)
- You need custom login screen theming
- GDM has bugs or conflicts with your setup
- Running on older hardware where every MB of RAM counts

**Choose GDM when:**

- Running GNOME desktop (tighter integration)
- You need Wayland support out of the box
- Accessibility features are important
- You use GNOME’s screen recording, remote login, or multi-seat features

GDM and GNOME are developed together, so GDM has better support for GNOME-specific features. LightDM is more flexible and desktop-agnostic.

## Quick Reference

- `sudo dnf install lightdm lightdm-gtk-greeter` — Install
- `sudo systemctl enable lightdm` — Set as default
- `/etc/lightdm/lightdm.conf` — Main config
- `/etc/lightdm/lightdm-gtk-greeter.conf` — Greeter appearance
- `sudo systemctl disable lightdm && sudo systemctl enable gdm` — Switch back
