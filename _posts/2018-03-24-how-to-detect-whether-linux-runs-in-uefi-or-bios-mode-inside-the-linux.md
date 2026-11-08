---
title: "How to Check If Linux Is Running in UEFI or BIOS Mode"
date: 2018-03-24 11:48:19 +0000
layout: post
canonical: https://www.systutorials.com/how-to-detect-whether-linux-runs-in-uefi-or-bios-mode-inside-the-linux/
---

The simplest way to detect whether your Linux system booted in UEFI or BIOS (Legacy) mode is to check for the existence of the EFI firmware directory.

## Check for EFI Directory

The `/sys/firmware/efi/` directory only exists when the system has booted in UEFI mode. If it’s absent, the system is running in BIOS/Legacy mode.

``` bash
[ -d /sys/firmware/efi/ ] && echo "UEFI" || echo "BIOS"
```

This is the most reliable method and works on all modern Linux distributions.

## Using `efibootmgr`

If you have `efibootmgr` installed (available in the efibootmgr package on most distributions), it will only function on UEFI systems:

``` bash
efibootmgr
```

On a BIOS system, this command will fail with an error like “EFI variables are not supported on this system.” On UEFI systems, it displays the boot entries.

You can use this for detection:

``` bash
if efibootmgr &>/dev/null; then
    echo "UEFI"
else
    echo "BIOS"
fi
```

## Check Boot Partition Type

You can also inspect the disk partition table to identify the boot mode:

``` bash
sudo parted -l | grep -i "Partition Table"
```

UEFI systems typically use GPT (GUID Partition Table), while BIOS systems use MBR (Master Boot Record). However, this isn’t foolproof—modern BIOS systems can boot from GPT, and UEFI systems can technically use MBR.

## Check `/proc/cmdline`

Examine the kernel command line to see if EFI-related parameters are present:

``` bash
cat /proc/cmdline | grep -i efi
```

If output appears, the kernel detected EFI. No output indicates BIOS mode.

## Check EFI Variables

List EFI variables to confirm UEFI:

``` bash
ls -la /sys/firmware/efi/efivars/ 2>/dev/null && echo "UEFI" || echo "BIOS"
```

Note that on some hardened systems, the `efivars` directory may not be readable by non-root users even on UEFI systems.

## Practical Shell Function

For scripting purposes, create a reusable function:

``` bash
detect_boot_mode() {
    if [ -d /sys/firmware/efi/ ]; then
        echo "uefi"
        return 0
    else
        echo "bios"
        return 1
    fi
}

# Usage
BOOT_MODE=$(detect_boot_mode)
echo "System booted in: $BOOT_MODE mode"
```

## Why This Matters

Knowing your boot mode is essential for:

- **Bootloader configuration**: GRUB2, systemd-boot, and other bootloaders handle UEFI and BIOS differently
- **Partition scheme decisions**: UEFI requires an EFI System Partition (ESP)
- **Kernel parameters**: Some firmware-related kernel options are UEFI-specific
- **System migration**: Converting between boot modes requires specific procedures

The `/sys/firmware/efi/` method is the most direct and reliable approach used by system tools and frameworks like GRUB2, Anaconda installer, and systemd.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
