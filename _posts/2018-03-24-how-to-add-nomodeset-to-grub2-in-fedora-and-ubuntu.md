---
title: "Adding nomodeset to GRUB2 on Fedora and Ubuntu"
date: 2018-03-24 11:47:46 +0000
layout: post
canonical: https://www.systutorials.com/how-to-add-nomodeset-to-grub2-in-fedora-and-ubuntu/
---

The `nomodeset` kernel parameter tells Linux to disable kernel mode setting (KMS), forcing the graphics driver to use basic VESA modes instead of native driver features. This is useful for troubleshooting display issues during boot or installation.

## When You Need nomodeset

Common scenarios that require `nomodeset`:

- Black screen during boot with certain GPUs (especially Nvidia and some AMD cards)
- Display freezes when the kernel loads the graphics driver
- Installer shows a blank screen after the initial menu
- System boots fine in text mode but hangs when starting the display manager
- Virtual machines with GPU passthrough configuration issues

## Adding nomodeset Temporarily (One Boot)

**On Fedora (GRUB2):**

1.  Boot the system and wait for the GRUB menu
2.  Select the kernel you want to boot
3.  Press **e** to edit the boot entry
4.  Find the line starting with `linux` or `linux16`
5.  Add `nomodeset` at the end of that line
6.  Press **Ctrl+X** or **F10** to boot

**On Ubuntu (GRUB2):**

1.  Same process — press **e** at the GRUB menu
2.  Find the line starting with `linux`
3.  Add `nomodeset` after `quiet splash` (or wherever in the parameter list)
4.  Press **F10** to boot

## Making nomodeset Permanent

**Fedora / RHEL:**

```wp-block-code
# Edit the GRUB default config
sudo nano /etc/default/grub

# Add nomodeset to GRUB_CMDLINE_LINUX
GRUB_CMDLINE_LINUX="...existing params... nomodeset"

# Rebuild GRUB config
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

# For UEFI systems:
sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
```

**Ubuntu / Debian:**

```wp-block-code
sudo nano /etc/default/grub
# Add nomodeset to GRUB_CMDLINE_LINUX_DEFAULT
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"

sudo update-grub
```

## What nomodeset Actually Does

Without KMS (`nomodeset` active):

- The kernel doesn’t initialize the GPU
- X11/Wayland uses the VESA or fbdev driver (basic, low resolution)
- No hardware-accelerated graphics
- Higher power consumption (GPU not properly managed)

With KMS (default, no nomodeset):

- The kernel initializes the GPU early in boot
- Native resolution console from boot
- Hardware-accelerated graphics in the desktop
- Proper power management for the GPU

## After Boot: Fix the Real Issue

`nomodeset` is a workaround, not a fix. After booting successfully, address the root cause:

**Nvidia GPUs:** Install the proprietary driver:

```wp-block-code
# Fedora
sudo dnf install akmod-nvidia
sudo akmods --force
sudo dracut --force

# Ubuntu
sudo ubuntu-drivers autoinstall
```

**AMD GPUs:** Usually work with open-source drivers. Update your kernel and mesa:

```wp-block-code
sudo dnf update kernel mesa-dri-drivers   # Fedora
sudo apt update && sudo apt upgrade       # Ubuntu
```

**Intel GPUs:** Generally well-supported. If issues persist, try `i915.modeset=0` instead of `nomodeset` for Intel-specific troubleshooting.

## Removing nomodeset

Once you’ve installed proper graphics drivers, remove `nomodeset` from GRUB:

```wp-block-code
sudo nano /etc/default/grub
# Remove nomodeset from GRUB_CMDLINE_LINUX

# Rebuild GRUB
sudo grub2-mkconfig -o /boot/grub2/grub.cfg    # Fedora
sudo update-grub                                 # Ubuntu
```

Running with `nomodeset` long-term means no GPU acceleration, poor display performance, and higher power usage. Always fix the underlying driver issue.

## Related Kernel Parameters

Several other kernel parameters can help with graphics troubleshooting:

- `video=1024x768` — Force a specific resolution during boot
- `vesafb.mtrr=3 vesafb.ywrap=1` — Improve VESA framebuffer performance
- `drm_kms_helper.edid_firmware=edid/1024x768.bin` — Override EDID data for monitors that report wrong resolutions
- `gpu_sched.enable_scheduler=0` — Disable the GPU scheduler (AMD debugging)

Combine parameters as needed:

```wp-block-code
nomodeset video=1024x768 vga=792
```

The `vga=` parameter sets the console resolution before KMS loads. Common values:

- `vga=791` — 1024x768x16
- `vga=792` — 1024x768x24
- `vga=794` — 1280x1024x16
- `vga=795` — 1280x1024x24

## Debugging Graphics Issues

If you’re still having problems after installing drivers, gather debug info:

```wp-block-code
# Check which GPU driver is loaded
lspci -k | grep -A3 VGA

# Check kernel DRM messages
dmesg | grep drm

# Check X11 log (if using X11)
cat /var/log/Xorg.0.log | grep EE

# List available DRM drivers
ls /lib/modules/$(uname -r)/kernel/drivers/gpu/drm/
```

These logs help identify whether the issue is with the driver, firmware, or hardware detection.
