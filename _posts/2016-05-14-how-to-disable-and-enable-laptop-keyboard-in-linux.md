---
title: "How to Enable and Disable Your Laptop Keyboard in Linux"
date: 2016-05-14 02:45:52 +0000
modified: 2026-04-11 16:21:32 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-disable-and-enable-laptop-keyboard-in-linux/
---

When you dock a laptop with an external USB keyboard, the built-in keyboard becomes a nuisance—it’s too easy to brush keys while typing and trigger unwanted input. Rather than disabling the keyboard at the BIOS level or physically disconnecting it, you can use the `xinput` tool to disable and re-enable it from within your Linux session.

## Prerequisites

You’ll need:

- `xinput` installed (included by default on most X11 desktop environments)
- An external USB keyboard connected before disabling the laptop keyboard
- Access to a terminal or SSH session to re-enable if needed

If `xinput` isn’t installed, grab it from your distro’s repos:

``` bash
# Debian/Ubuntu
sudo apt install x11-utils

# Fedora
sudo dnf install xorg-x11-utils

# Arch
sudo pacman -S xorg-xinput
```

## Finding Your Keyboard IDs

First, list all input devices to identify your laptop keyboard:

``` bash
xinput list
```

You’ll see output like this:

    ⎡ Virtual core pointer                      id=2    [master pointer  (3)]
    ⎜ ↳ Virtual core XTEST pointer                  id=4    [slave pointer   (2)]
    ⎜ ↳ Logitech USB Mouse                          id=9    [slave pointer   (2)]
    ⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
      ↳ Virtual core XTEST keyboard                 id=5    [slave keyboard  (3)]
      ↳ Power Button                                id=6    [slave keyboard  (3)]
      ↳ AT Translated Set 2 keyboard                id=10   [slave keyboard  (3)]
      ↳ HP WMI hotkeys                              id=12   [slave keyboard  (3)]

The `AT Translated Set 2 keyboard` is almost always your built-in laptop keyboard. Note its ID (in this example, `id=10`). The `Virtual core keyboard` is the master device (typically `id=3`).

Automate finding the laptop keyboard ID:

``` bash
LAPTOP_KB_ID=$(xinput list | grep 'AT Translated Set 2' | sed -n 's/.*id=\([0-9]*\).*/\1/p')
echo "Laptop keyboard ID: $LAPTOP_KB_ID"
```

## Disabling the Keyboard

To disable the laptop keyboard, detach it from the master keyboard device:

``` bash
xinput float <ID>
```

Replace `<ID>` with your laptop keyboard’s ID. For example:

``` bash
xinput float 10
```

The `float` command detaches the device from its master, effectively disabling it. You should immediately stop receiving input from the laptop keyboard. Test by pressing keys—they won’t register.

## Re-enabling the Keyboard

To bring the keyboard back online, reattach it to the master keyboard device:

``` bash
xinput reattach <ID> <MASTER_ID>
```

For example:

``` bash
xinput reattach 10 3
```

The keyboard becomes functional again.

## Automated Scripts

Create a reusable script pair for convenience. Save this as `disable-laptop-kb.sh`:

``` bash
#!/bin/bash
LAPTOP_KB_ID=$(xinput list | grep 'AT Translated Set 2' | sed -n 's/.*id=\([0-9]*\).*/\1/p')

if [ -z "$LAPTOP_KB_ID" ]; then
    echo "Error: Could not find laptop keyboard"
    exit 1
fi

echo "Disabling laptop keyboard (ID: $LAPTOP_KB_ID)..."
xinput float "$LAPTOP_KB_ID"
echo "Done. Keyboard disabled."
```

And `enable-laptop-kb.sh`:

``` bash
#!/bin/bash
LAPTOP_KB_ID=$(xinput list | grep 'AT Translated Set 2' | sed -n 's/.*id=\([0-9]*\).*/\1/p')
MASTER_ID=3

if [ -z "$LAPTOP_KB_ID" ]; then
    echo "Error: Could not find laptop keyboard"
    exit 1
fi

echo "Enabling laptop keyboard (ID: $LAPTOP_KB_ID)..."
xinput reattach "$LAPTOP_KB_ID" "$MASTER_ID"
echo "Done. Keyboard enabled."
```

Make them executable:

``` bash
chmod +x disable-laptop-kb.sh enable-laptop-kb.sh
```

Then run them as needed:

``` bash
./disable-laptop-kb.sh
./enable-laptop-kb.sh
```

## Desktop Environment Integration

You can bind these scripts to keyboard shortcuts in your desktop environment for one-key toggling:

**GNOME/MATE:** Settings → Keyboard Shortcuts → Custom Shortcuts
**KDE Plasma:** System Settings → Shortcuts → Custom Shortcuts
**Xfce:** Settings → Keyboard → Application Shortcuts

## Important Notes

- The master keyboard device ID is usually `3`, but verify with `xinput list` if the re-enable script fails.
- Changes persist only during your X11 session. Rebooting resets everything.
- If you disable the keyboard without an external keyboard connected, you’ll need to SSH in or restart to recover.
- Some hybrid-sleep or hibernation events may require you to run the disable script again after resuming.

## Alternatives

If you prefer permanent solutions, check your laptop’s BIOS settings—many allow disabling internal keyboards entirely. Alternatively, use your desktop environment’s accessibility settings under “Physical Keyboard” if available, though `xinput` is more reliable and reversible.
