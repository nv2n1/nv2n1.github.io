---
title: "Installing Fedora on MBR Disks"
date: 2018-03-24 08:21:51 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-fedora-20-on-a-mbr-ms-dos-disk/
---

If you’re working with legacy BIOS systems and MBR partition tables, Fedora’s installer can sometimes misdetect your firmware mode and attempt UEFI/GPT setup on hardware that only supports legacy BIOS. This guide covers the proper approach for Fedora 39+ on MBR systems.

## Prerequisites

Before starting, verify your system configuration:

- Boot the installer in legacy BIOS mode, not UEFI
- Confirm your disk uses MBR/MS-DOS partition table, not GPT
- Enable CSM (Compatibility Support Module) or legacy boot in firmware settings
- Disable Secure Boot in BIOS/UEFI firmware to prevent boot mode conflicts

## Configuring the Installer for MBR

When the Fedora installer boots, you’ll reach the boot menu. Press Tab (or the appropriate key for your system) to edit the kernel command line and add the `noefi` parameter:

    inst.noefi

This explicitly disables UEFI detection. Some systems may also benefit from adding:

    inst.noefi inst.gpt=0

The `inst.gpt=0` parameter explicitly directs the installer to use MBR partitioning. Boot with these parameters and proceed through the installer normally.

## Manual Partitioning

If the installer still auto-detects incorrectly, use manual partitioning:

1.  At the storage configuration screen, select “Custom” or “Advanced Partitioning”
2.  Delete any auto-created GPT partition table
3.  Create a new MBR/MS-DOS partition table
4.  Create your partitions:
    - `/boot` — 1 GiB, Linux (type 83)
    - `/` — remaining space, Linux (type 83)
    - Optionally swap — Linux Swap (type 82)
5.  Mark the `/boot` partition as bootable (set the boot flag)
6.  Do not create an ESP (EFI System Partition)

Proceed with installation. The installer will use GRUB2 in MBR mode automatically.

## GRUB2 Installation and Configuration

After installation completes, verify GRUB2 was installed to the MBR correctly. Boot into your installed system and run:

``` bash
sudo grub2-install /dev/sda
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

Check your GRUB configuration:

``` bash
cat /etc/default/grub
```

Verify the output does not contain `UEFI_ARCH=x86_64` or EFI-related boot entries. A typical MBR-based GRUB config will look like:

``` bash
GRUB_TIMEOUT=5
GRUB_DEFAULT=saved
GRUB_SAVEDEFAULT=true
GRUB_DISABLE_SUBMENU=true
```

## Troubleshooting

**Installer boots into UEFI mode despite noefi parameter**

The firmware itself may be forcing UEFI. Reboot into firmware settings and explicitly disable:

- UEFI Boot
- Secure Boot
- Fast Boot

Some systems require saving settings and cold-booting (power off completely, then power on) for changes to take effect.

**System won’t boot after installation**

GRUB may not have been installed to the MBR. Boot from the Fedora installation media, select “Troubleshooting,” then “Rescue a Fedora system.” Once in the rescue environment:

``` bash
sudo grub2-install /dev/sda
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
exit
reboot
```

**Partition table shows corruption or mixed MBR/GPT**

Use `parted` to inspect and fix the partition table:

``` bash
sudo parted /dev/sda print
```

If you see both MBR and GPT markers, remove the GPT table:

``` bash
sudo parted /dev/sda mklabel msdos
```

This will destroy the partition table—back up your data first. Repartition and reinstall if necessary.

**BIOS not recognizing the boot partition**

Ensure the boot flag is set on your `/boot` partition:

``` bash
sudo parted /dev/sda set 1 boot on
```

Replace `1` with your `/boot` partition number if different.

## When to Use MBR

MBR remains relevant for:

- Older hardware without UEFI support
- Virtualized legacy BIOS environments
- Embedded or appliance systems with firmware constraints
- Dual-boot scenarios with Windows XP/Vista-era systems

For new installations on modern hardware, GPT is the recommended standard. However, Fedora continues to support MBR installations when your specific hardware or use case requires it.
