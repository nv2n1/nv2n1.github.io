---
title: "Remapping Alt and Ctrl Keys in Linux for Emacs"
date: 2018-03-24 08:22:11 +0000
layout: post
canonical: https://www.systutorials.com/how-to-swap-alt-and-ctrl-on-linux-for-emacs/
---

Emacs makes heavy use of Ctrl, and many users find it ergonomically difficult to hit Ctrl repeatedly, especially on modern keyboards where Ctrl is placed far from home row. Swapping Alt and Ctrl can make Emacs navigation more comfortable. This guide covers modern approaches for different desktop environments and input systems.

## Emacs-Only Configuration (Simplest)

If you only want this behavior in Emacs and don’t need system-wide remapping, configure it directly in your init file:

```elisp
(setq x-alt-keysym 'control)
(setq x-ctrl-keysym 'meta)
```

This keeps your system keybindings unchanged while giving Emacs the remapped behavior. This is the least disruptive approach and works across all Linux desktop environments.

## Using XKB (Recommended for Modern Systems)

XKB is the standard keyboard configuration system on modern Linux desktops and works with both X11 and Wayland (through the compositor layer).

Create a custom keyboard layout file at `~/.config/xkb/symbols/custom`:

    xkb_symbols "altctrl" {
        key <LALT> { [ Control_L, Control_L ] };
        key <LCTL> { [ Alt_L, Meta_L ] };
        key <RALT> { [ Control_R, Control_R ] };
        key <RCTL> { [ Alt_R, Meta_R ] };
    };

Create `~/.config/xkb/keymap/custom`:

    xkb_keymap {
        xkb_keycodes { include "evdev" };
        xkb_types { include "complete" };
        xkb_compat { include "complete" };
        xkb_symbols { include "pc+us+custom(altctrl)" };
        xkb_geometry { include "pc(pc104)" };
    };

Load it immediately:

``` bash
setxkbmap -I$HOME/.config/xkb custom
```

To make this persistent, add the command to your session startup. For X11, place it in `~/.xinitrc` or `~/.xprofile`. For Wayland sessions with GNOME or KDE, create `~/.config/autostart/xkbmap-swap.desktop`:

``` ini
[Desktop Entry]
Type=Application
Exec=setxkbmap -I$HOME/.config/xkb custom
NoDisplay=true
```

## Desktop Environment GUI Methods

### GNOME (X11 and Wayland)

GNOME provides built-in keyboard option names for common swaps:

``` bash
gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swap_lalt_lctl']"
```

Available options:

- `ctrl:swap_lalt_lctl` — swap left Alt and left Ctrl
- `ctrl:swap_ralt_rctl` — swap right Alt and right Ctrl
- `ctrl:swapcaps` — swap Caps Lock and Ctrl (useful alternative)

To verify the setting:

``` bash
gsettings get org.gnome.desktop.input-sources xkb-options
```

### KDE Plasma

1.  Open System Settings
2.  Navigate to Input Devices → Keyboard → Advanced
3.  Enable “Ctrl position” and select your preferred swap option
4.  Click Apply

## Legacy: xmodmap (X11 Only)

xmodmap works only with X11 and is not recommended for new setups, but remains useful for legacy systems. Create `~/.xmodmap`:

    clear control
    clear mod1

    keycode  64 = Control_L NoSymbol Control_L
    keycode  37 = Alt_L Meta_L Alt_L Meta_L
    keycode 108 = Control_R NoSymbol Control_R
    keycode 105 = Alt_R Meta_R Alt_R Meta_R

    add mod1 = Alt_R Alt_L Meta_R Meta_L
    add control = Control_R Control_L

Apply it:

``` bash
xmodmap ~/.xmodmap
```

For persistence, add to `~/.xinitrc`:

``` bash
xmodmap ~/.xmodmap
```

## Finding Your Keyboard’s Keycodes

Keycodes vary by keyboard layout and hardware. Find the correct codes for your keyboard:

``` bash
xmodmap -pke | grep -E '(Control|Alt)'
```

This shows all current mappings. Look for `Control_L`, `Control_R`, `Alt_L`, and `Alt_R`, then note their keycodes and adjust your configuration accordingly.

## Testing Before Permanent Changes

Always test remapping before making it permanent:

``` bash
xmodmap ~/.xmodmap
xev
```

Use `xev` to verify correct key mappings by pressing keys in the window and watching the output. This prevents accidentally breaking your keyboard.

## Troubleshooting

**Mappings reset after login:** Ensure your startup file is executable and placed in the correct location. For display managers, `~/.xprofile` is more reliable than `~/.xinitrc`.

**Wayland session ignores xmodmap:** Wayland doesn’t use xmodmap. Use XKB method or your desktop environment’s settings instead.

**Keycodes differ between login sessions:** Some display managers source files differently. Test your configuration in a virtual terminal (Ctrl+Alt+F2) before relying on GUI startup.

**Emacs still sees old bindings:** If using the Emacs-only approach, ensure you’ve restarted Emacs after adding the configuration, and verify with `C-h k` (describe-key) to check what Emacs sees.
