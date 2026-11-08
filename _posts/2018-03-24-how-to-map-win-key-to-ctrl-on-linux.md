---
title: "Remapping Windows Key to Ctrl on Linux"
date: 2018-03-24 08:22:23 +0000
layout: post
canonical: https://www.systutorials.com/how-to-map-win-key-to-ctrl-on-linux/
---

The Windows (Super) key can be remapped to function as an additional Ctrl key, useful if you work across multiple systems or prefer the extra modifier. The approach varies significantly by display server and desktop environment.

## GNOME (Wayland and X11)

GNOME 3.38 and later have built-in remapping through Settings:

1.  Open Settings → Keyboard → Special Character Key Handling
2.  Under “Alt/Win Key Behavior”, select “Ctrl (L)” for the left Super key or “Ctrl (R)” for the right Super key
3.  Changes apply immediately

This is the simplest approach on modern GNOME and works identically on Wayland and X11.

## X11 with xmodmap

For X11 environments (KDE, i3, OpenBox, XFCE, or older GNOME), use xmodmap:

First, identify your Super key codes:

``` bash
xmodmap -pke | grep Super
```

You’ll likely see output like:

    keycode 133 = Super_L ...
    keycode 134 = Super_R ...

Create or edit `~/.Xmodmap`:

``` bash
keycode 133 = Control_L
keycode 134 = Control_R
```

Ensure it loads at startup by adding this to `~/.xinitrc`:

``` bash
if [ -f ~/.Xmodmap ]; then
    xmodmap ~/.Xmodmap
fi
```

Or if you’re using a display manager (gdm, sddm, lightdm), add it to `~/.xprofile` instead. Test the mapping immediately with:

``` bash
xmodmap ~/.Xmodmap
```

## Wayland with evremap

xmodmap doesn’t work on Wayland. Use **evremap**, a modern remapper that works across Wayland and X11:

Install on Arch:

``` bash
sudo pacman -S evremap
```

On Debian/Ubuntu:

``` bash
sudo apt install evremap
```

Create `~/.config/evremap/config.toml`:

``` toml
[[remaps]]
input = "Super_L"
output = "Control_L"

[[remaps]]
input = "Super_R"
output = "Control_R"
```

Enable and start the systemd service:

``` bash
systemctl --user enable --now evremap.service
```

Check status:

``` bash
systemctl --user status evremap.service
```

If evremap isn’t in your repos, build from source:

``` bash
cargo install evremap
sudo setcap cap_sys_admin=ep ~/.cargo/bin/evremap
```

## KDE Plasma

In System Settings → Keyboard → Advanced → Key Bindings, search for “Super” or “Meta” key bindings and modify as needed.

Alternatively, edit `~/.config/kwinrc`:

``` ini
[ModifierOnlyShortcuts]
Meta=
```

Then restart KDE or the session.

## TTY Console (Before X11/Wayland)

To remap at the TTY level, use loadkeys:

``` bash
echo "keycode 125 = Control" | sudo tee /tmp/winkey.map
sudo loadkeys /tmp/winkey.map
```

For persistence across reboots, edit your distribution’s keyboard configuration. On Debian/Ubuntu, add the mapping to `/etc/console-setup/boottime.kmap.gz`:

``` bash
sudo bash -c 'echo "keycode 125 = Control" >> /etc/console-setup/boottime.kmap'
sudo update-initramfs -u
```

On Fedora/RHEL, modify `/etc/vconsole.conf`:

``` ini
KEYMAP=us
FONT=latarcyrheb-sun16
```

Then add your custom keymap file and reference it.

## Verification

For X11, use xev to see key events:

``` bash
xev
```

Press the Win key and verify it reports as `Control_L` or `Control_R`. For Wayland, check `journalctl`:

``` bash
journalctl --user -u evremap.service -f
```

Press the Win key and watch the logs confirm the remap.

## Caveats

- Some applications (browsers, IDEs) may hardcode Super key behavior and ignore remaps
- Wayland support through evremap is mature, but some edge cases exist
- If using a desktop environment, always prefer Settings over manual config — they survive updates and usually override manual files
- Remapping at the TTY level affects all sessions but persists through kernel updates less reliably

## Troubleshooting

**evremap fails to start on Wayland:**\
Ensure you have `cap_sys_admin` capability:

``` bash
sudo setcap cap_sys_admin=ep $(which evremap)
```

**xmodmap changes don’t persist:**\
Verify your startup file is being sourced. Check `~/.bashrc` vs `~/.bash_profile` — graphical sessions use the latter. Alternatively, place a desktop file in `~/.config/autostart/`:

``` ini
[Desktop Entry]
Type=Application
Exec=xmodmap /home/username/.Xmodmap
Hidden=false
Name=xmodmap
```

**Mapping works in one app but not another:**\
Some applications intercept Super before the window manager sees it. Check the application’s preferences for keybinding configuration or file a bug report.
