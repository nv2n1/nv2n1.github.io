---
title: "GRUB Not Detecting Windows on UEFI Systems"
date: 2018-03-24 11:41:40 +0000
modified: 2026-04-11 16:00:18 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /fix-the-grub-issue-with-windows-8-uefi-after-installing-fedora-20/
---

When you install Fedora (or other Linux distributions) alongside Windows on a UEFI system, GRUB sometimes fails to generate a functional boot entry for Windows. The symptom is a missing or non-working “Windows Boot Manager” entry in the GRUB menu, or GRUB drops you to a shell prompt when you select it.

## Why This Happens

Modern systems use UEFI with GPT partitioning. GRUB needs to explicitly load the correct partition table driver and filesystem driver, then point to the Windows EFI bootloader. Without proper configuration, GRUB can’t locate the Windows boot files on the EFI System Partition (ESP).

## Step 1: Check If GRUB Can Auto-Detect Windows

First, let GRUB attempt automatic detection. This works on GRUB 2.06+, which includes improved Windows detection:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Reboot and check if a Windows entry now appears in the GRUB menu:

``` bash
sudo reboot
```

If Windows appears and boots successfully, you’re done. If not, proceed to manual configuration.

## Step 2: Identify Your EFI Partition

Find the EFI System Partition on your system:

``` bash
sudo fdisk -l
```

Look for a partition marked “EFI System” — it’s typically small (100–550 MB) and usually `/dev/nvme0n1p1` or `/dev/sda1` on newer systems.

Verify the ESP exists and contains Windows boot files:

``` bash
sudo mount /dev/nvme0n1p1 /mnt
ls -la /mnt/EFI/Microsoft/Boot/
```

The file `bootmgfw.efi` must be present. If it’s not, Windows installation is corrupted or the wrong partition was identified.

## Step 3: Manually Add Windows to GRUB

Open the custom GRUB configuration file:

``` bash
sudo nano /etc/grub.d/40_custom
```

Add a Windows Boot Manager entry. Replace `hd0,gpt1` with your actual partition (see the conversion table below):

``` bash
menuentry 'Windows Boot Manager' {
    insmod part_gpt
    insmod fat
    set root='hd0,gpt1'
    chainloader /EFI/Microsoft/Boot/bootmgfw.efi
    boot
}
```

Save and exit (Ctrl+X, then Y in nano).

## Partition Notation Conversion

GRUB uses a different naming scheme than Linux. Convert your device to GRUB notation:

| Linux Device     | GRUB Notation |
|------------------|---------------|
| `/dev/sda1`      | `hd0,gpt1`    |
| `/dev/sda2`      | `hd0,gpt2`    |
| `/dev/nvme0n1p1` | `hd0,gpt1`    |
| `/dev/nvme0n1p2` | `hd0,gpt2`    |

If your system uses legacy MBR (rare for Windows 8+), use `part_msdos` instead of `part_gpt`.

## Step 4: Regenerate GRUB Configuration

After editing, regenerate the main GRUB config file:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

On some Fedora installations, the output path may be `/boot/efi/EFI/fedora/grub.cfg` — check your actual GRUB location first:

``` bash
sudo find /boot -name grub.cfg
```

## Step 5: Test the Boot Entry

Reboot and select “Windows Boot Manager” from the GRUB menu:

``` bash
sudo reboot
```

If Windows boots successfully, the fix is complete. If GRUB still fails to boot Windows, verify the chainloader path is correct:

``` bash
sudo mount /dev/nvme0n1p1 /mnt
file /mnt/EFI/Microsoft/Boot/bootmgfw.efi
```

The file should be identified as a PE executable. If it’s missing or corrupted, use `bootrec.exe` from a Windows recovery environment to repair the bootloader.

## Troubleshooting Secure Boot Issues

If Windows is registered in firmware but not loading from GRUB:

``` bash
sudo efibootmgr -v
```

This shows EFI boot entries. If Windows appears here but fails when chainloaded from GRUB, your system may have Secure Boot enabled and GRUB may not be signed correctly. Options:

- Disable Secure Boot in UEFI firmware settings and retest
- Boot Windows directly from the UEFI firmware menu (hold Del, F2, or F10 during startup) to verify Windows bootloader itself is intact
- Use `efibootmgr` to set Windows as the default boot entry and bypass GRUB entirely

## Important: Never Edit grub.cfg Directly

The main config file (`/boot/grub2/grub.cfg`) regenerates automatically during kernel updates. Always place custom entries in `/etc/grub.d/40_custom`, then run `grub2-mkconfig` to update the main file. This ensures your Windows entry persists across system updates.
