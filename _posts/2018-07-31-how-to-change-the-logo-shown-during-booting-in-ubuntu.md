---
title: "Customizing the Plymouth Boot Logo in Ubuntu"
date: 2018-07-31 10:32:47 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-logo-shown-during-booting-in-ubuntu/
---

Plymouth manages the splash screen (boot logo) displayed during Ubuntu startup and shutdown. Switching themes involves selecting a Plymouth theme, regenerating the initramfs, and verifying the change takes effect on reboot.

## List available themes

Check what Plymouth themes are installed and available:

``` bash
apt search plymouth-theme
```

To see only installed themes:

``` bash
apt list --installed | grep plymouth-theme
```

Common Ubuntu themes include `plymouth-theme-ubuntu-logo`, `plymouth-theme-ubuntu-text`, and variants for other flavors like `plymouth-theme-kubuntu-logo` or `plymouth-theme-xubuntu-logo`.

## Install additional themes

If the default themes don’t suit you, install alternatives:

``` bash
sudo apt install plymouth-theme-ubuntu-text
```

The Ubuntu repositories include several built-in options. Third-party themes exist on GitHub and other sources, though the standard themes usually provide reliable boot experiences. Community themes may lack maintenance—stick with official or well-maintained options if you want stability.

## Select the active theme

Use `update-alternatives` to switch between installed themes:

``` bash
sudo update-alternatives --config default.plymouth
```

This displays all available themes with priorities:

    There are 3 choices for the alternative default.plymouth.

      Selection    Path                                                      Priority   Status
    ------------------------------------------------------------
      0            /usr/share/plymouth/themes/ubuntu-logo/ubuntu-logo.plymouth   100       auto
      1            /usr/share/plymouth/themes/spinner/spinner.plymouth           70       manual
    * 2            /usr/share/plymouth/themes/ubuntu-text/ubuntu-text.plymouth   100       manual

    Press <enter> to keep the current choice[*], or type selection number:

Enter the number of your preferred theme, or set it programmatically:

``` bash
sudo update-alternatives --set default.plymouth /usr/share/plymouth/themes/ubuntu-text/ubuntu-text.plymouth
```

## Regenerate the initramfs

Plymouth loads during boot via the initramfs, so you must regenerate it after changing themes:

``` bash
sudo update-initramfs -u
```

For a specific kernel version:

``` bash
sudo update-initramfs -u -k 6.12.0-1-generic
```

If you run multiple kernels, update all of them:

``` bash
sudo update-initramfs -u -k all
```

The process takes about a minute and outputs:

    update-initramfs: Generating /boot/initrd.img-6.12.0-1-generic

## Verify the change

Confirm which theme is active:

``` bash
cat /etc/alternatives/default.plymouth
```

Check that Plymouth is present in the initramfs:

``` bash
lsinitramfs /boot/initrd.img-$(uname -r) | grep -i plymouth
```

The new theme appears after your next reboot. If you see no change, verify the symlink actually updated:

``` bash
ls -l /etc/alternatives/default.plymouth
```

## Troubleshooting

**Theme doesn’t appear on boot:**

Verify the theme package is installed:

``` bash
apt list --installed | grep plymouth-theme-NAME
```

If it’s not there, reinstall it and regenerate the initramfs again. Double-check that `update-initramfs -u` completed without errors.

**Black screen during boot:**

The splash screen may fail to initialize, though this rarely affects functionality. Check the kernel log:

``` bash
dmesg | grep -i plymouth
```

Some custom themes have broken dependencies. Try an official Ubuntu theme instead. If you’re on a fresh system, this usually resolves itself on the next boot cycle.

**Changes don’t take effect:**

Confirm you ran `update-initramfs -u` after selecting the new theme. Verify the symlink points to the correct theme:

``` bash
cat /etc/alternatives/default.plymouth
```

If it still shows the old path, the `update-alternatives` command may not have completed. Run it again and verify with the `cat` command before rebooting.

**Encrypted disk (LUKS) password prompt overlays the splash:**

This is expected behavior with encrypted systems. Plymouth displays a password prompt over the splash screen. Some themes handle this better than others—the `ubuntu-text` theme typically provides a cleaner experience for encrypted disks.

**Stuck on splash screen during boot:**

If the system hangs rather than continuing, you may have selected a broken or incompatible theme. Hold `Shift` during boot to access the GRUB menu, then edit the kernel command line to add `splash=off` or `quiet` to disable Plymouth temporarily. After booting, switch back to a standard theme like `ubuntu-logo` or `ubuntu-text` and regenerate the initramfs.

## Create custom themes

Themes live in `/usr/share/plymouth/themes/`. To create a custom theme, copy an existing one as a template:

``` bash
sudo cp -r /usr/share/plymouth/themes/ubuntu-logo /usr/share/plymouth/themes/my-custom-theme
```

Edit the `.plymouth` configuration file:

``` bash
sudo nano /usr/share/plymouth/themes/my-custom-theme/my-custom-theme.plymouth
```

You can adjust image paths, animation speeds, text colors, and other properties. The configuration format is straightforward key-value pairs. After editing, set it as active and regenerate the initramfs:

``` bash
sudo update-alternatives --set default.plymouth /usr/share/plymouth/themes/my-custom-theme/my-custom-theme.plymouth
sudo update-initramfs -u
```

Custom theming requires familiarity with Plymouth’s structure and is only necessary if standard themes don’t meet your needs. Study an existing theme before building from scratch.
