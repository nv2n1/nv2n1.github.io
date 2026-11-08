---
title: "Remapping Modifier Keys on Linux"
date: 2018-03-24 08:22:23 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-rearrange-alt-ctrl-and-win-keys-on-linux-win-as-alt-and-ctrl-alt-as-ctrl/
---

Remapping modifier keys on Linux makes sense if you’re an Emacs power user, prefer ergonomic hand positioning, or simply don’t use the Win key. The standard approach moves frequently-used modifiers closer to your thumbs by trading the underutilized Super/Win key for additional Ctrl or Alt access.

A typical remapped layout looks like:

    |Ctrl|Alt|Ctrl|     Space Bar      |Ctrl|Menu|Ctrl|

## Using xmodmap (X11 Only)

The traditional approach uses xmodmap, which reads key mapping definitions from a configuration file. This works only on X11 sessions, not Wayland.

Create `~/.Xmodmap`:

    ! Swap left Alt and left Ctrl
    keycode 64 = Control_L
    keycode 37 = Alt_L

    ! Map Super (Win) to Alt
    keycode 133 = Alt_L

    ! Map right Alt to Ctrl
    keycode 108 = Control_L

Check your actual keycodes first:

``` bash
xmodmap -pke | grep -E "(Alt|Control|Super)"
```

Apply changes immediately:

``` bash
xmodmap ~/.Xmodmap
```

Verify the mapping worked:

``` bash
xmodmap -pm
```

For X11 session persistence, add to `~/.xinitrc`:

``` bash
xmodmap ~/.Xmodmap
```

For display managers (GDM, LightDM, SDDM), create `~/.config/autostart/xmodmap-load.desktop`:

``` ini
[Desktop Entry]
Type=Application
Exec=xmodmap /home/yourusername/.Xmodmap
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Load Xmodmap
```

## Using xkb (X11 and Better Wayland Support)

The xkb (X Keyboard Extension) approach is more robust and works better across modern systems. Create a custom symbols file at `~/.config/xkb/symbols/custom`:

    xkb_symbols "ctrl_alt_swap" {
        replace key <LALT> { [ Control_L ] };
        replace key <LCTL> { [ Alt_L ] };
        replace key <RALT> { [ Control_L ] };
        replace key <LWIN> { [ Alt_L ] };
    };

Then load it with setxkbmap:

``` bash
setxkbmap -I~/.config/xkb -symbols "pc+us+custom(ctrl_alt_swap)"
```

Test it works:

``` bash
xkbcomp -xkb $DISPLAY -
```

For persistence, add the setxkbmap command to your session startup. On GNOME/systemd-based systems, create `~/.config/systemd/user/xkb-custom.service`:

``` ini
[Unit]
Description=Load custom xkb keymap
After=graphical-session-pre.target
PartOf=graphical-session.target

[Service]
Type=oneshot
ExecStart=%h/.config/xkb/load-xkb.sh
RemainAfterExit=yes

[Install]
WantedBy=graphical-session.target
```

Create the script `~/.config/xkb/load-xkb.sh`:

``` bash
#!/bin/bash
setxkbmap -I~/.config/xkb -symbols "pc+us+custom(ctrl_alt_swap)"
```

Make it executable:

``` bash
chmod +x ~/.config/xkb/load-xkb.sh
```

Enable the service:

``` bash
systemctl --user enable xkb-custom.service
```

## GNOME Settings (GUI Approach)

Modern GNOME versions (42+) expose modifier key remapping through the Settings application:

1.  Open Settings → Keyboard
2.  Scroll down to Special Character Key Handling
3.  Remap Ctrl, Alt, and Super keys as needed

This GUI approach is easier but limited to GNOME’s supported remappings. It doesn’t handle all edge cases that xkb or xmodmap can.

## KDE Plasma

KDE provides modifier key remapping through the system settings:

1.  Open System Settings → Input Devices → Keyboard
2.  Go to the Advanced tab
3.  Select Modifier Keys
4.  Configure your preferred layout

KDE persists these settings automatically.

## Wayland Considerations

Wayland doesn’t use X11’s input system, so xmodmap doesn’t work. Check your session type:

``` bash
echo $XDG_SESSION_TYPE
```

If it returns `wayland`, use one of these approaches:

- GNOME/KDE Settings (both have native Wayland support)
- Sway: Edit `~/.config/sway/config` with `input * xkb_options "ctrl:swap_lalt_lctl"` and similar
- Hyprland: Edit `~/.config/hyprland/hyprland.conf` with `input { kb_options = ctrl:swap_lalt_lctl }`
- Systemd user service with setxkbmap if your Wayland compositor supports XWayland

## Troubleshooting

**Remapping doesn’t persist after logout:**

- Verify the startup script/service is enabled: `systemctl --user list-unit-files | grep xkb`
- Check file permissions: `ls -la ~/.Xmodmap ~/.config/xkb/load-xkb.sh`
- Review logs: `journalctl --user -u xkb-custom.service`

**Keys feel unresponsive or mapped incorrectly:**

- Reload the keymap: `setxkbmap -I~/.config/xkb -symbols "pc+us+custom(ctrl_alt_swap)"`
- Test in a terminal: `xev` shows keycodes and current mappings
- Restart your session (logout/login) if changes don’t apply

**Conflicting with application-level bindings:**

- Emacs users should verify `M-x` and `C-x` work correctly
- Some applications (browsers, terminals) may have hardcoded Alt behavior—test in your primary use cases
- If conflicts occur, adjust your xkb symbols file rather than relying on application settings

**Partial remapping not working:**

- Keycodes vary by keyboard layout and hardware—always run `xmodmap -pke` to find your actual keycodes
- Some laptop keyboards have special firmware-level key handling that bypasses userspace remapping

Test your final configuration in Emacs, your terminal, and text editor before considering it production-ready.
