---
title: "Converting Linux from BIOS to UEFI Boot Mode"
date: 2018-03-24 11:42:25 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-turn-a-bios-based-linux-mint-17-installation-to-uefi-booting/
---

If you installed Linux in BIOS (Legacy) mode but need to boot alongside Windows in UEFI mode, converting an existing installation is possible but complex. This guide covers the process for modern systems while preserving your existing Linux installation and Windows setup.

**Before starting:** Back up your data. This procedure involves disk partitioning and bootloader reconfiguration, and mistakes can be costly.

## Check Your Current Setup

First, verify your current boot mode:

``` bash
[ -d /sys/firmware/efi ] && echo "UEFI" || echo "BIOS"
```

Check your partition table:

``` bash
sudo parted -l | grep "Partition Table"
```

BIOS installations typically use MBR (msdos) partition tables, while UEFI requires GPT.

## Key Prerequisites

- Your motherboard supports UEFI
- Your disk has free space for an EFI System Partition (ESP)
- Your Linux system uses a bootloader like GRUB2

## Step 1: Convert MBR to GPT

**Warning:** This is destructive. Back up everything first.

``` bash
sudo gdisk /dev/sdX
```

Replace `sdX` with your actual disk. In gdisk:

- Type `w` to write the MBR→GPT conversion
- Type `y` to confirm
- The tool preserves existing partitions during conversion

Alternatively, use parted (less recommended but simpler):

``` bash
sudo parted /dev/sdX mklabel gpt
```

This will erase all partitions. Only use this if you’re willing to repartition from scratch.

## Step 2: Create an EFI System Partition

You need a dedicated EFI System Partition (ESP) of at least 260 MB, ideally 512 MB or 1 GB.

``` bash
sudo parted /dev/sdX mkpart ESP fat32 1MiB 512MiB
sudo parted /dev/sdX set 1 esp on
```

Format the new partition:

``` bash
sudo mkfs.fat -F 32 /dev/sdXY
```

(Replace `sdXY` with your new partition number, e.g., `sda1`)

## Step 3: Mount and Install GRUB2 for UEFI

Mount the ESP:

``` bash
sudo mount /dev/sdXY /boot/efi
```

Make sure `/boot/efi` exists:

``` bash
sudo mkdir -p /boot/efi
```

Install GRUB2 in UEFI mode:

``` bash
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Linux
```

Update the GRUB configuration:

``` bash
sudo update-grub
```

## Step 4: Update fstab

Add the ESP to your `/etc/fstab` permanently:

``` bash
echo "/dev/sdXY /boot/efi vfat umask=0077 0 1" | sudo tee -a /etc/fstab
```

Verify the entry was added correctly:

``` bash
cat /etc/fstab
```

## Step 5: Reboot and Change Firmware Settings

Reboot into your system BIOS/UEFI firmware (usually F2, F10, Del, or Esc during startup—check your motherboard manual).

- Disable Legacy/BIOS boot mode
- Enable UEFI boot mode
- Set the UEFI boot order to prioritize your Linux installation

Save and exit. The system should boot into Linux via UEFI.

## Verify UEFI Boot

Once booted, confirm you’re in UEFI mode:

``` bash
[ -d /sys/firmware/efi ] && echo "UEFI" || echo "BIOS"
efibootmgr
```

The `efibootmgr` output should show your Linux entry in the boot order.

## Troubleshooting

**Black screen after reboot:** Your firmware may not recognize the GRUB UEFI entry. Reboot into firmware, select the EFI partition directly, or use UEFI shell to manually locate and run the bootloader.

**Windows won’t boot:** Ensure the Windows EFI partition is still intact. Boot into Windows recovery and run:

``` bash
bootrec /fixboot
bootrec /rebuildbcd
```

**GRUB doesn’t show Windows:** Update GRUB and rerun detection:

``` bash
sudo update-grub
```

## Modern Alternative: Reinstall

Converting BIOS→UEFI on an existing system is error-prone. If you encounter major issues, consider a fresh UEFI installation on a separate partition and migrating your data. Modern Linux distributions (Ubuntu 22.04 LTS, Linux Mint 21.x) install in UEFI by default on UEFI systems.
