---
title: "Resetting Your Linux Keyboard Layout with xmodmap and setxkbmap"
date: 2018-03-24 08:22:17 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-reset-the-keyboard-set-by-xmodmap-on-linux/
---

When you’ve modified your keyboard layout or key bindings using xmodmap and need to revert to the default, setxkbmap is your primary tool. However, the approach depends on whether you’re running X11 or Wayland, and what aspects of the configuration you want to reset.

## Check Your Session Type

Before attempting any resets, verify whether you’re on X11 or Wayland:

``` bash
echo $XDG_SESSION_TYPE
```

If this returns `wayland`, most of the xmodmap and setxkbmap commands below won’t work. Wayland sessions use the display server’s native input handling, so you’ll need to use your desktop environment’s keyboard settings (GNOME Settings, KDE System Settings, etc.) instead.

## Basic Reset on X11

The simplest approach is to run setxkbmap without arguments:

``` bash
setxkbmap
```

This resets your keyboard to the default layout for your locale, typically US English unless configured otherwise.

## Check Current Configuration

Before resetting, see what’s currently active:

``` bash
setxkbmap -query
```

This shows your active layout, variant, and options. Example output:

    layout:     us
    variant:    
    options:    caps:escape

## Granular Resets

If you only want to reset certain aspects while keeping others:

``` bash
# Reset to a specific layout
setxkbmap us

# Reset to a specific layout with variant
setxkbmap us dvorak

# Clear only options while keeping layout
setxkbmap -option

# Clear all options explicitly
setxkbmap -option ""
```

## Remove xmodmap Files

If you’ve created custom xmodmap rules in `~/.Xmodmap` or `~/.xmodmaprc`, these files won’t be automatically cleared when you run setxkbmap. Prevent them from loading on session start:

``` bash
# Rename for backup
mv ~/.Xmodmap ~/.Xmodmap.bak

# Or remove entirely
rm ~/.Xmodmap
```

Then reload your X session by logging out and back in, or restart your X server.

## Stop xmodmap from Auto-Loading

Check these locations and remove any xmodmap calls:

- `~/.xinitrc`
- `~/.xsession`
- `~/.xprofile`
- `~/.bashrc` or `~/.bash_profile` (if xmodmap is called here)

Look for lines like:

``` bash
xmodmap ~/.Xmodmap
xmodmap -e "keycode 66 = Escape"
```

Delete or comment out these lines. The changes take effect on your next login.

## Test Changes Without Persistence

To test a configuration change temporarily without affecting your saved setup:

``` bash
# Apply temporarily for this session only
setxkbmap us -option ctrl:nocaps
```

Changes revert when you log out. This is useful for testing before making permanent changes.

## Advanced: Multiple Keyboard Configuration

If you have multiple keyboards connected and want to configure them separately, use xinput on X11:

``` bash
# List input devices
xinput list

# Set layout for specific device
setxkbmap -device 12 us dvorak
```

Replace `12` with the device ID from the list output.

## Persistent Configuration for X11

To make changes survive a reboot, add to your `~/.xprofile`:

``` bash
setxkbmap -layout us -option ctrl:nocaps
```

This executes before your window manager starts. For systems without `~/.xprofile`, create one.

## Wayland Keyboard Configuration

On Wayland systems, keyboard configuration is handled by the display server and desktop environment. GNOME and KDE don’t use xmodmap or setxkbmap. Instead:

- **GNOME**: Settings \> Keyboard \> Input Sources or Keyboard Shortcuts
- **KDE Plasma**: System Settings \> Input Devices \> Keyboard
- **Sway/Wlroots**: Configure in `~/.config/sway/config` with `input` blocks

Example Sway configuration:

    input * {
        xkb_layout us
        xkb_options caps:escape
    }

## Troubleshooting

If setxkbmap produces no visible effect:

1.  Verify X11 is running: `echo $XDG_SESSION_TYPE` should return `x11`
2.  Confirm X is accessible: `echo $DISPLAY` should show something like `:0` or `:1`
3.  Check for conflicting configuration in startup scripts
4.  Some desktop environments override xkb settings after login — check your DE’s keyboard settings

If you’re certain X11 is running but changes don’t persist, the issue is usually an auto-loading xmodmap or xkb configuration file that reapplies your old settings on each login. Find and remove it.
