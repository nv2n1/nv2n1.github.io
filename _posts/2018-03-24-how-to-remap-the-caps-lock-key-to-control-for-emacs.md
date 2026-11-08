---
title: "Remapping Caps Lock to Control on Linux: X11 and Wayland"
date: 2018-03-24 08:22:04 +0000
modified: 2026-04-11 16:03:02 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-remap-the-caps-lock-key-to-control-for-emacs/
---

Remapping Caps Lock to Control is a worthwhile investment if you spend significant time in Emacs or vim. Your pinky will benefit from years of reduced strain.

## Desktop Environment Settings (Easiest)

Most modern desktop environments include a built-in option for this remapping.

**GNOME (40+):**

- Open Settings → Keyboard → Special Character Options
- Toggle “Make Caps Lock an additional Control”

**KDE Plasma:**

- Open System Settings → Input Devices → Keyboard
- Go to the Advanced tab and find the Caps Lock option
- Select “Make Caps Lock an additional Control”

**XFCE:**

- Settings → Keyboard → Layout tab
- Click “Layout Options” button
- Under “Caps Lock behavior”, select “Make it an additional Control”

This is the simplest approach and works across both X11 and Wayland. If your DE supports it, use this first.

## X11: setxkbmap (Recommended for X11)

For X11 systems where DE settings don’t suffice, `setxkbmap` is cleaner than the older `xmodmap` approach:

``` bash
setxkbmap -option ctrl:nocaps
```

Verify it’s active:

``` bash
setxkbmap -query
```

To revert:

``` bash
setxkbmap -option ''
```

### Making it Persistent on X11

Add the command to your X11 startup. Choose one based on your setup:

**For startx users**, add to `~/.xinitrc`:

``` bash
setxkbmap -option ctrl:nocaps
```

**For display managers (GDM, LightDM, SDDM)**, create `~/.xsession`:

``` bash
#!/bin/bash
setxkbmap -option ctrl:nocaps
exec dbus-launch --exit-with-session your-window-manager
```

Make it executable:

``` bash
chmod +x ~/.xsession
```

**For systemd user sessions**, create `~/.config/autostart/setxkbmap.desktop`:

``` ini
[Desktop Entry]
Type=Application
Exec=setxkbmap -option ctrl:nocaps
Hidden=false
Name=Caps Lock Remapping
```

## X11: xmodmap (Legacy, When setxkbmap Won’t Work)

If `setxkbmap` doesn’t work for your keyboard layout, `xmodmap` provides lower-level control.

First, find the Caps Lock keycode:

``` bash
xev | grep -A 2 "KeyPress"
```

Press Caps Lock and look for output like:

    state 0x0, keycode 66 (keysym 0xffe5, Caps_Lock)

Create or edit `~/.Xmodmap`:

    clear Lock
    keycode 66 = Control_L
    add Control = Control_L Control_R

Apply immediately:

``` bash
xmodmap ~/.Xmodmap
```

Make it persistent using the same `~/.xinitrc`, `~/.xsession`, or `~/.config/autostart/` methods shown above, but call `xmodmap ~/.Xmodmap` instead.

## Wayland: systemd-localed

On Wayland, neither `xmodmap` nor `setxkbmap` work. Instead, use `localectl`:

``` bash
sudo localectl set-x11-keymap us '' '' ctrl:nocaps
```

Replace `us` with your keyboard layout if needed. This persists across reboots on systemd systems.

Verify the setting:

``` bash
localectl status
```

If you want to also apply it to the current Wayland session immediately (on GNOME or KDE), also run through your DE’s Settings as shown above.

## Testing and Troubleshooting

After applying any method, test in Emacs or a text editor:

``` bash
C-a   # Move to beginning of line
C-e   # Move to end of line
C-k   # Kill to end of line
```

**Settings don’t persist after reboot:**

- Verify your script is executable: `ls -l ~/.xsession` or `ls -l ~/.Xmodmap`
- Check that your shell is sourcing startup files: `echo $SHELL` and verify `~/.bashrc` sources `~/.bash_profile` if needed
- For systemd user sessions, ensure `~/.config/autostart/` is correct and verify with `systemctl --user status graphical-session.target`

**Changes don’t take effect immediately:**

- Log out and back in, or restart your display server (`killall X` for X11, then log out)
- For Wayland, changes from `localectl` require a full logout/login cycle

**Keycode varies by keyboard:**\
The keycode shown above (66) is standard for most keyboards, but ergonomic or international layouts may differ. Always verify with `xev` first.

## Muscle Memory Across Systems

If you frequently switch between machines where Caps Lock isn’t remapped, expect a transition period. Muscle memory typically adapts within 2–4 weeks. Consider remapping on all your regular systems to avoid constant context-switching.
