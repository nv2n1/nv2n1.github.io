---
title: "Making Your Linux Keyboard Work Like macOS"
date: 2024-06-25 14:03:20 +0000
layout: post
canonical: https://www.systutorials.com/making-linux-keyboard-similar-to-macos-keyboard/
---

If you regularly switch between macOS and Linux, having consistent keyboard behavior across platforms cuts down cognitive load and keeps your muscle memory intact. The main difference is that macOS uses Command (⌘) for most shortcuts, while Linux defaults to Ctrl. You can remap your Linux keyboard to behave like macOS by making Alt function like Ctrl, effectively simulating Command key behavior.

## Why Remap Your Keyboard

**Consistency across platforms**: Using the same modifier key across macOS and Linux eliminates the mental tax of context-switching between systems.

**Muscle memory**: Once you’ve built habits around Command+C, Command+V, and Command+W on macOS, forcing yourself to use Ctrl on Linux wastes mental cycles. Remapping preserves your automatic keybindings.

**Workflow efficiency**: Fewer mistakes and faster navigation when the muscle memory works the same way everywhere.

## Installing and Configuring input-remapper

`input-remapper` is the standard tool for persistent keyboard remapping on Linux. It runs as a daemon and survives reboots, unlike temporary solutions like `xmodmap`.

Install it:

``` bash
sudo apt install input-remapper-daemon input-remapper-gtk
```

For Fedora/RHEL:

``` bash
sudo dnf install input-remapper
```

For Arch:

``` bash
sudo pacman -S input-remapper
```

Start the daemon:

``` bash
sudo systemctl enable --now input-remapper
```

Open the GUI application (search for “Input Remapper” in your application menu or run `input-remapper-gtk` from the terminal).

## Remapping Alt to Ctrl

In the input-remapper GUI:

1.  Select your keyboard from the device list on the left
2.  Click the input field at the bottom and press the key you want to remap (left Alt)
3.  In the “Map to” field on the right, select or type `ctrl`
4.  Click “Apply” to test the mapping
5.  Click “Save” to persist it across reboots

If you use multiple keyboards, you’ll need to create separate profiles for each device. input-remapper applies mappings per-device automatically.

For systems where the GUI isn’t available, you can configure remappings via the config file at `~/.config/input-remapper/profiles/` or use the CLI:

``` bash
input-remapper-control --command set-preset --device "Your Keyboard Name" --preset default
```

## Adjusting Application Shortcuts

Many applications already use Ctrl for their common shortcuts (Ctrl+C, Ctrl+V, Ctrl+W), so remapping Alt to Ctrl usually “just works.” However, some Linux applications may still use Alt-based shortcuts that will now conflict.

Check your desktop environment’s keyboard settings:

**GNOME**: `Settings > Keyboard > Keyboard Shortcuts`\
**KDE Plasma**: `System Settings > Shortcuts > Standard Shortcuts`\
**XFCE**: `Settings > Keyboard > Application Shortcuts`

Look for shortcuts using Alt and either disable them or rebind them to something less common. Window manager shortcuts (Alt+Tab, Alt+F4) typically don’t conflict since you’re mapping both modifier and key combination together, but verify they work as expected after remapping.

## Handling Special Cases

**Right Alt/AltGr**: If you need AltGr for special characters (common in non-US layouts), only remap the left Alt key. Modify your input-remapper settings to specifically target `alt+l` (left Alt only).

**Gaming and applications that need both Ctrl and Alt**: Some games capture raw keyboard input and won’t respect remappings. For these, create a separate input-remapper profile and toggle it on/off as needed, or keep a second USB keyboard without remapping.

**Virtual machines**: Remappings apply at the Linux host level. Inside VirtualBox or KVM guests, the VM sees the remapped keys. If the guest is also Linux, this usually works fine. For Windows guests expecting different behavior, you may need to disable remapping within the VM settings.

## Additional Keyboard Tweaks

**Enable key repeat at macOS speeds**: macOS has slower key repeat by default. In GNOME/Wayland:

``` bash
gsettings set org.gnome.desktop.input-sources repeat-interval 30
gsettings set org.gnome.desktop.input-sources delay 660
```

For X11, modify `~/.xbindkeysrc` or use `xset r rate 660 30`.

**Map Caps Lock to Control**: Many macOS users remap Caps Lock to Control system-wide. In input-remapper, map `caps_lock` to `ctrl`.

**Invert scrolling direction**: If you’re accustomed to macOS’s “natural” scrolling:

**GNOME**: `Settings > Mouse & Touchpad > Natural Scrolling > On`\
**KDE**: `System Settings > Input Devices > Mouse > Pointer > Scrolling direction`

Or via command line for GNOME:

``` bash
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll true
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true
```

**Swap Ctrl and Alt completely**: If you want full macOS key layout (Alt as Command, Ctrl as Option), remap both directions:

- Left Alt → Ctrl
- Left Ctrl → Alt
- Right Alt → Ctrl (if needed)

## Persistence and Troubleshooting

input-remapper persists mappings by default, but verify the daemon runs on boot:

``` bash
sudo systemctl status input-remapper
```

If mappings aren’t applying after reboot, check that your keyboard is included in the device list and that the profile is marked as active.

For external keyboards, the mapping applies only to that specific device. If you use multiple keyboards, input-remapper creates device-specific profiles automatically.

If input-remapper conflicts with your desktop environment, fall back to `xmodmap` (X11 only) as a temporary workaround:

``` bash
echo "keycode 64 = Control_L" | xmodmap -
```

However, this doesn’t persist across reboots and doesn’t work on Wayland. input-remapper is the modern, maintainable approach.
