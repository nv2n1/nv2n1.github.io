---
title: "Creating a Bootable Fedora Live USB"
date: 2013-07-12 16:32:16 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/creating-fedora-live-usb-media/
---

A Fedora Live USB lets you boot directly into a Fedora environment without modifying your hard drive. You can use it to test Fedora, troubleshoot your system, or perform a fresh installation. This guide covers modern tools and workflows for creating bootable USB media.

**Back up any data on your USB stick first — the creation process will overwrite everything.**

## Download the ISO

Get the Live ISO from <a href="https://fedoraproject.org/workstation/download/" rel="nofollow noopener" target="_blank">Fedora’s download page</a>. You’ll find options for Fedora Workstation (GNOME desktop), Fedora KDE Plasma, Fedora Server, and other variants. Choose the architecture matching your hardware — most modern systems use x86_64.

If you want a smaller download, grab the netinst ISO instead. It’s a minimal installer that fetches packages during installation, useful for slow connections or when disk space is tight.

Verify the ISO checksum after downloading:

``` bash
sha256sum -c Fedora-Workstation-Live-x86_64-*.iso.sha256
```

## Command Line Method Using `dd`

This is the fastest and most straightforward approach if you’re comfortable with the command line. The `dd` tool performs a direct block-level copy of the ISO to your USB device.

First, identify your USB device:

``` bash
lsblk
```

Look for your USB stick in the output. It’ll be something like `/dev/sdc` or `/dev/sdd` — the key is that it’s a device name, not a partition (so `sdc` not `sdc1`).

Unmount the device if it’s already mounted:

``` bash
sudo umount /dev/sdX*
```

Replace `/dev/sdX` with your actual device name. The `*` ensures all partitions are unmounted.

Write the ISO:

``` bash
sudo dd if=Fedora-Workstation-Live-x86_64-*.iso of=/dev/sdX bs=4M status=progress && sync
```

Key parameters:

- `if=` input file (your ISO)
- `of=` output file (your USB device — use the device name like `/dev/sdc`, not a partition like `/dev/sdc1`)
- `bs=4M` block size of 4MB (speeds up the copy)
- `status=progress` shows the operation’s progress
- `sync` ensures all data is written to disk before returning

The process typically takes 1–5 minutes depending on ISO size and USB speed.

## Using GNOME Disks (GUI Method)

Most Linux desktops have a graphical tool built in. GNOME Disks (included in Fedora by default) works well:

1.  Plug in your USB stick
2.  Open **Disks** (search for it in your applications menu)
3.  Select your USB device from the left sidebar
4.  Click the menu button (three dots) and select **Restore Disk Image**
5.  Browse to your downloaded ISO file
6.  Click **Start Restoring** and confirm

Disks handles the write and verification automatically.

## Testing the Live USB

Before relying on the USB for an install or troubleshooting, test it in a virtual machine:

``` bash
sudo qemu-system-x86_64 -m 2048 -usb -drive file=/dev/sdX,format=raw
```

Replace `/dev/sdX` with your USB device. The `-m 2048` allocates 2GB of RAM to the VM. This ensures the ISO was written correctly and boots as expected.

Alternatively, reboot your physical machine, enter the BIOS/UEFI boot menu (usually F12, F2, or Del during startup), and select your USB device. If the live environment loads, you’re good.

## Booting the Live USB on UEFI Systems

Modern systems use UEFI firmware. Your USB stick needs to be bootable under UEFI, which the ISO already supports. If the USB doesn’t appear in your UEFI boot menu:

- Ensure **Secure Boot is disabled** in UEFI settings (or enroll the Fedora signing key)
- Check that your USB device is listed as a bootable option
- Try a different USB port (some legacy ports may not be UEFI-bootable)

## Troubleshooting

**USB not recognized after creation:** Use `sudo fdisk -l` to verify the device shows up. If not, try a different USB stick or port.

**Won’t boot:** Double-check you used the device name (`/dev/sdc`) not a partition name (`/dev/sdc1`). Re-run the `dd` command if unsure.

**Slow USB boot:** This is normal for older USB 2.0 sticks. USB 3.0 devices are significantly faster and worth the investment if you create live media frequently.

**Checksum mismatch:** If your ISO’s checksum doesn’t match the official one, your download corrupted. Delete it and download again.
