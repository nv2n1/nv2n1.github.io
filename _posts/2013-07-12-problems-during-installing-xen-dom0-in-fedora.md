---
title: "Installing Xen Dom0 on Fedora: Common Issues and Fixes"
date: 2013-07-12 16:32:15 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /problems-during-installing-xen-dom0-in-fedora/
---

Xen remains relevant in production environments (AWS EC2, Citrix Hypervisor), though KVM has become the default for most Linux distributions. This guide covers frequent installation and configuration issues specific to Fedora Dom0 setups, with many tips applicable to other Linux platforms.

## BIOS Configuration

If Xen fails with “I/O virtualization disabled,” you need to enable virtualization support in BIOS. Required options vary by CPU vendor:

**Intel systems:**

- Intel Virtualization Technology (VT-x)
- Intel VT for Directed I/O (VT-d)
- Interrupt Remapping
- Coherency Support
- ATS Support

**AMD systems:**

- AMD-V
- AMD-Vi (IOMMU)
- Interrupt Remapping

Verify BIOS changes took effect by checking `/proc/cpuinfo` for `vmx` (Intel) or `svm` (AMD) flags, and confirm IOMMU via `dmesg | grep -i iommu`.

## Loop Device Limitations

The default kernel configuration provides only 8 loop devices. When using blkback-backed virtual block devices with more than 8 VMs, increase this limit by passing a kernel parameter at boot:

Edit your bootloader configuration (GRUB2: `/etc/default/grub`) and add `max_loop=32` to the kernel command line:

    GRUB_CMDLINE_LINUX="... max_loop=32"

Then rebuild the GRUB configuration:

``` bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

Verify the change with:

``` bash
cat /sys/module/loop/parameters/max_loop
```

## Initramfs Issues

On some systems, dracut-generated initramfs images fail to boot. If you encounter boot hangs or kernel panics, try recreating the initramfs with dracut’s verbose output:

``` bash
dracut -f --verbose /boot/initramfs-$(uname -r).img $(uname -r)
```

If issues persist, check boot logs with `journalctl -b` and consider adding debug parameters to the kernel command line:

    rd.debug rd.shell=1

For persistent issues, you can try generating an older-style initramfs (though dracut is preferred in modern Fedora):

``` bash
dracut --hostonly-cmdline /boot/initramfs-custom.img $(uname -r)
```

## GPU and DRM Issues

Graphics-related crashes during boot—particularly with AMD Radeon, Intel i915, or NVIDIA cards—often stem from DRM (Direct Rendering Manager) conflicts with Xen’s console handling.

### Quick Fix: Disable Modesetting

Add `nomodeset` to the kernel command line in `/etc/default/grub`:

    GRUB_CMDLINE_LINUX="... nomodeset"

Then regenerate GRUB config and reboot:

``` bash
grub2-mkconfig -o /boot/grub2/grub.cfg
reboot
```

### Alternative: Force Xen Graphics Mode

If `nomodeset` fails, configure Xen to handle video directly. Edit `/etc/default/grub` and modify the Xen hypervisor options (the `module` line in GRUB config):

    GRUB_CMDLINE_XEN="vga=gfx-1280x1024x32"

This forces Xen to use graphics mode before Dom0 kernel boot, bypassing DRM initialization.

**Xen video mode syntax:**

    vga=ask                          # Interactive mode selection menu
    vga=text-80x25                   # Text mode (25, 28, 30, 34, 43, 50, or 60 rows)
    vga=gfx-1024x768x16              # Graphics mode (width x height x depth)
    vga=mode-0x318                   # Specific hex mode from 'vga=ask' menu
    vga=gfx-1280x1024x32,keep        # Graphics mode with persistent Xen console output

The `keep` option is useful for debugging—it preserves Xen hypervisor messages on the console even after Dom0 starts.

## 32-bit Kernel Configuration

If building a 32-bit Dom0 kernel, you must enable Physical Address Extension (PAE) support. Without it, Xen options won’t appear in the kernel configuration menu.

Enable PAE in `make menuconfig`:

    Processor type and features → High Memory Support (64GB) → PAE (Physical Address Extension)

After enabling PAE, Xen build options become available in the same menu. Additionally, add the `clocksource=jiffies` parameter to the kernel command line if you encounter time-related issues:

    GRUB_CMDLINE_LINUX="... clocksource=jiffies"

Note: 32-bit Dom0 is rarely tested in modern Xen deployments. Test thoroughly before production use.

## KSM (Kernel Samepage Merging) Errors

Excessive KSM error messages often indicate compatibility issues between Xen and the KSM daemon. Disable both services:

``` bash
systemctl disable ksm
systemctl disable ksmtuned
systemctl stop ksm
systemctl stop ksmtuned
```

Check that they’re stopped:

``` bash
systemctl status ksm ksmtuned
```

## Netplugd Conflicts with Xend

The netplugd daemon (network plug event daemon) conflicts with Xen’s network bridge configuration. When both are running, you’ll see errors like:

    /etc/xen/scripts/network-bridge: command not found

And bridge creation fails, with physical interfaces renaming unpredictably (e.g., `eth0` → `peth0`).

**Solution:** Disable netplugd:

``` bash
systemctl disable netplugd
systemctl stop netplugd
```

Modern Fedora systems typically use NetworkManager or systemd-networkd, making netplugd obsolete. Verify it’s disabled and confirm your bridge persists across reboots with:

``` bash
ip link show | grep -i bridge
```

## Troubleshooting Checklist

Before concluding Xen won’t work on your system:

1.  Verify BIOS virtualization is enabled: `grep -E 'vmx|svm' /proc/cpuinfo`
2.  Check IOMMU status: `dmesg | grep -i iommu`
3.  Review Xen boot messages: `xl dmesg`
4.  Test Dom0 with minimal kernel parameters (remove debugging options, custom vga settings, etc.)
5.  Try latest Fedora kernel: `dnf update kernel`
6.  Check for BIOS/firmware updates from your hardware vendor

If you’re experiencing persistent issues on modern systems, consider KVM as an alternative—it’s better integrated into Fedora and receives more active development.
