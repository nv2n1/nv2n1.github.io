---
title: "Booting an Older Kernel Version with GRUB2 on Ubuntu 20.04"
date: 2020-06-07 11:59:27 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/how-to-make-grub2-boot-to-older-kernel-version-in-ubuntu-20-04/
---

Start by viewing the GRUB menu entries that will be generated during the next boot:

``` bash
sudo grub-mkconfig | grep -E 'submenu |menuentry '
```

This will output something like:

    menuentry 'Ubuntu' --class ubuntu --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-simple-...' {
    submenu 'Advanced options for Ubuntu' $menuentry_id_option 'gnulinux-advanced-...' {
        menuentry 'Ubuntu, with Linux 6.8.0-45-generic' --class ubuntu --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-6.8.0-45-generic-advanced-...' {
        menuentry 'Ubuntu, with Linux 6.8.0-45-generic (recovery mode)' ...
        menuentry 'Ubuntu, with Linux 5.15.0-120-generic' --class ubuntu --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-5.15.0-120-generic-advanced-...' {
        menuentry 'Ubuntu, with Linux 5.15.0-120-generic (recovery mode)' ...

You can also see installed kernels directly:

``` bash
ls -la /boot/vmlinuz-*
```

This lists all available kernel images. The naming convention is `vmlinuz-VERSION-generic`, where VERSION represents the kernel release number.

## Configuring the default kernel

GRUB’s default boot entry is controlled by `/etc/default/grub`. Open this file with your preferred editor:

``` bash
sudo nano /etc/default/grub
```

Find the `GRUB_DEFAULT` variable. By default it’s set to `0`, which boots the first menu entry (the latest kernel).

To boot an older kernel, set `GRUB_DEFAULT` to a nested menu path using `>` as a separator:

``` bash
GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.15.0-120-generic"
```

Replace the kernel version with your target kernel. The first part before `>` is the submenu name, and the second part is the specific menu entry.

If you want to boot a recovery mode kernel instead, use:

``` bash
GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.15.0-120-generic (recovery mode)"
```

## Alternative: Using numeric indexing

You can also reference menu entries by index number instead of name. The first level is the primary menu, and submenus are referenced as `level>index`:

``` bash
GRUB_DEFAULT="1>2"
```

This boots the 3rd entry (index 2) in the 2nd menu (index 1). However, this approach is fragile—if you install new kernels, the indexes shift. The named approach is more reliable.

## Updating GRUB configuration

After modifying `/etc/default/grub`, regenerate the GRUB configuration:

``` bash
sudo update-grub
```

This command calls `grub-mkconfig` internally and writes the output to `/boot/grub/grub.cfg`. You should see output confirming it found your kernels:

    Sourcing file `/etc/default/grub'
    Generating grub configuration from /etc/default/grub...
    Found linux image: /boot/vmlinuz-6.8.0-45-generic
    Found initrd image: /boot/initrd.img-6.8.0-45-generic
    Found linux image: /boot/vmlinuz-5.15.0-120-generic
    Found initrd image: /boot/initrd.img-5.15.0-120-generic
    done

## Verifying the change

You can verify the change was applied by checking the generated GRUB config:

``` bash
grep "^set default=" /boot/grub/grub.cfg
```

Or by examining the full configuration:

``` bash
sudo grep -A 5 "submenu 'Advanced options" /boot/grub/grub.cfg
```

## Booting temporarily into a different kernel

If you just need to test a kernel once without changing the default, you don’t need to modify the configuration. At the GRUB boot menu (hold Shift during startup if it doesn’t display), select your desired kernel and press Enter. This is useful for troubleshooting before making a permanent change.

## Removing old kernels

Once you’ve confirmed your older kernel works reliably, you can remove unnecessary newer kernels to save space:

``` bash
sudo apt remove linux-image-6.8.0-45-generic linux-headers-6.8.0-45-generic
sudo update-grub
```

Use `apt autoremove` afterward to clean up related packages:

``` bash
sudo apt autoremove
```

Always keep at least two working kernel versions available until you’re certain one is stable for your hardware and workload.
