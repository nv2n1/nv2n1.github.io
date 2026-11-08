---
title: "Fix GNOME Natural Scrolling on Mouse and Touchpad"
date: 2018-07-31 10:00:03 +0000
layout: post
canonical: https://www.systutorials.com/gnome-3-natural-scrolling-mouse-option-does-not-work/
---

GNOME’s natural scrolling setting can be frustrating — especially when the GUI option is missing or doesn’t apply to your mouse while leaving your touchpad alone. The issue usually comes down to your session type, GNOME version, and how input devices are registered on your system.

## Check your session type first

Before troubleshooting, verify whether you’re on Wayland or X11:

``` bash
echo $XDG_SESSION_TYPE
```

This matters significantly. Wayland (the default on Ubuntu 22.04+, Fedora 36+, and modern Arch installs) applies input settings immediately. X11 requires a full logout/login cycle to pick up changes. Knowing which you’re using saves time when testing fixes.

## Configure via GNOME Settings

Recent GNOME versions (45+) separate mouse and touchpad settings:

1.  Open Settings → Mouse & Touchpad
2.  Locate the Natural Scrolling toggle under Mouse
3.  Toggle as needed

If the toggle is missing or greyed out, either your GNOME version is older than expected or your distribution has customized the build. Move on to the dconf method.

## Use dconf for direct control

When the GUI fails, manage settings from the command line:

``` bash
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll true
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll false
```

Check the current setting:

``` bash
gsettings get org.gnome.desktop.peripherals.mouse natural-scroll
```

Touchpads use a separate key, allowing independent control:

``` bash
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true
gsettings get org.gnome.desktop.peripherals.touchpad natural-scroll
```

This separation is the key to having natural scrolling on your touchpad but standard scrolling on your mouse — or vice versa.

## Verify device registration with libinput

GNOME relies on libinput for input handling. Check how your devices are recognized:

``` bash
libinput list-devices
```

Look for entries with “Scroll” support. The output includes vendor/product IDs and capabilities:

    Device:           Logitech USB Optical Mouse
    Kernel:           /dev/input/event5
    Scroll:           wheel
      Wheel: ↑ ↓ ←→

If your mouse and touchpad aren’t properly separated in this output, they may not be individually configurable through GNOME settings.

## Per-device libinput quirks for fine control

For granular control over specific devices, create or edit `/etc/libinput/local-overrides.quirks`:

``` bash
[Logitech USB Mouse]
MatchName=Logitech USB Optical Mouse
MatchProduct=046D*
AttrNaturalScrolling=0

[Synaptics Touchpad]
MatchName=Synaptics TM3289
MatchProduct=*
AttrNaturalScrolling=1
```

Reload the libinput daemon:

``` bash
sudo systemctl restart libinput
```

Verify the quirks took effect:

``` bash
libinput list-devices | grep -A 5 "Natural scrolling"
```

Order matters — libinput matches quirks top-to-bottom, so place more specific device entries before general ones.

## Troubleshooting common issues

**Settings don’t persist after reboot**

Your distribution may have removed the dconf key entirely. Check if it exists:

``` bash
dconf list org.gnome.desktop.peripherals.mouse
```

If `natural-scroll` is absent, file an issue with your distribution’s GNOME package maintainers. Some minimal builds strip less-common settings.

**Both mouse and touchpad behave identically**

GNOME may be applying a global setting. Reset and reconfigure:

``` bash
dconf reset org.gnome.desktop.peripherals.mouse.natural-scroll
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll false
```

**Changes don’t apply on Wayland**

Restart GNOME Shell without logging out:

``` bash
killall -9 gnome-shell
```

GNOME Shell restarts automatically. On X11, a full logout/login cycle is necessary since X11 doesn’t hot-reload input settings reliably.

**Wavy or unresponsive scrolling**

This is usually a device driver problem, not a GNOME setting issue. Check kernel input logs:

``` bash
dmesg | grep -i input
```

Look for firmware errors or device initialization failures. Try a different USB port if applicable. For persistent issues, verify whether the mouse manufacturer provides Linux driver support.

**dconf changes revert after the next session**

Ensure you’re editing the correct dconf database. Check what’s actually stored:

``` bash
dconf list org.gnome.desktop.peripherals.
```

If keys don’t appear, rebuild the schema cache:

``` bash
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
dconf update
```

This recompiles the GSettings schema and ensures dconf can read and persist your changes.

## Quick reference

``` bash
# Check current settings
gsettings get org.gnome.desktop.peripherals.mouse natural-scroll
gsettings get org.gnome.desktop.peripherals.touchpad natural-scroll

# Enable natural scroll on touchpad only
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll false

# Reset to defaults
dconf reset org.gnome.desktop.peripherals.mouse.natural-scroll
dconf reset org.gnome.desktop.peripherals.touchpad.natural-scroll

# List your input devices
libinput list-devices
```
