---
title: "How to Enable Natural Scrolling on MATE Linux Touchpads"
date: 2018-03-24 11:49:54 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-enable-natual-scroll-of-touchpad-in-mate-on-linux/
---

MATE’s mouse settings don’t include a graphical toggle for natural (or inverted) scrolling on touchpads, unlike GNOME or Cinnamon. You’ll need to configure it through the command line or configuration files.

## Using synclient

If your system uses Synaptics touchpad driver, you can invert scrolling direction with `synclient`:

``` bash
synclient VertScrollDelta=-111
synclient HorizScrollDelta=-111
```

Verify the change took effect:

``` bash
synclient | grep ScrollDelta
```

However, `synclient` changes are temporary and reset on reboot. To make them permanent, add these commands to your session startup script.

## Permanent configuration via xorg.conf

For a persistent solution, create or edit `/etc/X11/xorg.conf.d/70-synaptics.conf`:

``` bash
sudo nano /etc/X11/xorg.conf.d/70-synaptics.conf
```

Add this configuration block:

    Section "InputClass"
        Identifier "Synaptics Touchpad"
        Driver "synaptics"
        MatchProduct "Synaptics"
        Option "VertScrollDelta" "-111"
        Option "HorizScrollDelta" "-111"
    EndSection

Restart X or reboot for changes to take effect. Adjust the delta values (the negative numbers) to control scroll sensitivity—higher absolute values mean more sensitivity.

## Using libinput instead

Modern systems often use `libinput` instead of Synaptics. Check which driver your touchpad uses:

``` bash
xinput list-props "$(xinput list | grep -i touchpad | awk '{print $NF}' | tr -d '[]')"
```

If you see `libinput` properties, natural scrolling is configured differently. Create `/etc/X11/xorg.conf.d/30-libinput.conf`:

    Section "InputClass"
        Identifier "libinput touchpad catchall"
        Driver "libinput"
        MatchProduct "touchpad|Touchpad"
        Option "NaturalScrolling" "true"
    EndSection

For `libinput`, you can also adjust it at runtime with `xinput`:

``` bash
xinput set-prop "$(xinput list | grep -i touchpad | awk '{print $NF}' | tr -d '[]')" "libinput Natural Scrolling Enabled" 1
```

Replace `1` with `0` to disable.

## Making changes persistent via startup script

If you prefer not to modify Xorg configs, add synclient or xinput commands to your MATE session startup. Open MATE Session Properties:

``` bash
mate-session-properties
```

Click “Add” and enter:

    /usr/bin/synclient VertScrollDelta=-111 HorizScrollDelta=-111

Or for libinput:

    xinput set-prop "Touchpad Name" "libinput Natural Scrolling Enabled" 1

Replace “Touchpad Name” with the actual device name from `xinput list`.

## Troubleshooting

If `synclient` isn’t installed, install it:

``` bash
sudo apt install xserver-xorg-input-synaptics
```

For Fedora/RHEL:

``` bash
sudo dnf install xorg-x11-drv-synaptics
```

If neither `synclient` nor `xinput` work, check your touchpad driver:

``` bash
xinput list
```

Look for your touchpad device name and verify it shows `Synaptics` or `libinput` in the properties output. Some newer trackpads use the `evdev` driver, which may have different configuration options.

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
