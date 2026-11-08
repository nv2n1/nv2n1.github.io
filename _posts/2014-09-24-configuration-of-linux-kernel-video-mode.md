---
title: "Configuring Video Modes on UEFI and Legacy BIOS Systems"
date: 2014-09-24 16:58:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /configuration-of-linux-kernel-video-mode/
---

The Linux kernel handles video mode configuration through bootloader parameters and kernel graphics drivers. Modern UEFI systems use Kernel Mode Setting (KMS) automatically, but you can override modes when needed. Legacy BIOS systems still use older mechanisms if you’re maintaining older hardware.

## UEFI Systems: Modern Video Mode Configuration

On UEFI systems with GRUB2, add video parameters to the kernel command line in `/etc/default/grub`:

``` bash
GRUB_CMDLINE_LINUX="video=1920x1080-32@60"
```

The syntax format is:

    video=<connector>:<xres>x<yres>[M][R][-<bpp>][@<refresh>][i][m][eDd]

Where:

- `<connector>`: Optional display connector name (HDMI-1, DP-2, eDP-1, LVDS-1, etc.)
- `<xres>x<yres>`: Resolution in pixels
- `M`: Reduced blanking
- `R`: CVT reduced blanking v2 (more aggressive reduction)
- `-<bpp>`: Bits per pixel (8, 16, 24, 32)
- `@<refresh>`: Refresh rate in Hz
- `i`: Interlaced mode
- `m`: Margins around the display
- `e`, `D`, `d`: Enable/disable output or deep color

For multi-monitor setups, specify modes per connector:

``` bash
GRUB_CMDLINE_LINUX="video=HDMI-1:1920x1080-32@60 video=DP-2:3840x2160-32@60"
```

To force a specific connector when detection fails:

``` bash
GRUB_CMDLINE_LINUX="video=eDP-1:1366x768-32@60"
```

### Configuring GRUB Graphics Mode

Improve boot-time visuals by setting GRUB’s graphics terminal:

``` bash
GRUB_GFXMODE=1920x1080x32
GRUB_GFXPAYLOAD_LINUX=keep
GRUB_TERMINAL=gfxterm
```

The `GRUB_GFXPAYLOAD_LINUX=keep` option preserves the GRUB resolution throughout the kernel boot process, eliminating display flicker as the kernel takes over.

After editing `/etc/default/grub`, regenerate the configuration:

``` bash
# Debian/Ubuntu
sudo update-grub

# RHEL/Fedora/CentOS
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

# Systems with separate EFI partition
sudo grub2-mkconfig -o /boot/efi/EFI/ubuntu/grub.cfg
```

## Legacy BIOS Systems: vga Parameter

Older BIOS systems use the 16-bit boot protocol with the `vga=` kernel parameter, which accepts decimal values derived from VESA mode numbers.

The conversion formula is:

    Linux_kernel_mode_number = VESA_mode_number + 0x200

Common VESA mode conversions:

| Resolution | 256 Color | 15-bit | 16-bit | 24-bit | 32-bit |
|------------|-----------|--------|--------|--------|--------|
| 640×480    | 0x101     | 0x110  | 0x111  | 0x112  | —      |
| 800×600    | 0x103     | 0x113  | 0x114  | 0x115  | 0x10E  |
| 1024×768   | 0x105     | 0x116  | 0x117  | 0x118  | 0x10A  |
| 1280×1024  | 0x107     | 0x119  | 0x11A  | 0x11B  | 0x10D  |

For example, to set 1024×768 at 16-bit color (VESA 0x117):

``` bash
# Add 0x200: 0x117 + 0x200 = 0x317
# Convert to decimal: 0x317 = 791
GRUB_CMDLINE_LINUX="vga=791"
```

Convert hexadecimal to decimal with Python:

``` bash
python3 -c "print(0x317)"  # Output: 791
```

## Querying Available Video Modes

### GRUB Command Line

At the GRUB boot menu, press `c` to enter the command line and type:

    vbeinfo

This displays all VESA modes your firmware supports:

    VBE info: version: 2.0
    total memory: 4096 KiB
    List of compatible video modes:
    0x101: 640 x 480 x 8 Packed
    0x110: 640 x 480 x 15 Direct
    0x111: 640 x 480 x 16 Direct
    0x112: 640 x 480 x 24 Direct
    0x103: 800 x 600 x 8 Packed
    0x113: 800 x 600 x 15 Direct
    ...
    Configured VBE mode = 0x101

### Using modetest

For modern systems, query connected displays and their capabilities:

``` bash
# AMD GPUs
modetest -M amdgpu

# Intel GPUs
modetest -M i915

# NVIDIA (when using nouveau driver)
modetest -M nouveau
```

This shows all detected displays and available resolutions with connector names.

## Kernel Mode Setting (KMS)

Modern systems with KMS enabled (amdgpu, i915, nouveau, radeon, etc.) handle mode-setting automatically. The kernel graphics driver typically handles everything without manual intervention unless you need to:

- Force a specific resolution before the display manager starts
- Work around driver detection or EDID bugs
- Debug display problems
- Configure framebuffer output on headless systems

Check if KMS is active:

``` bash
cat /proc/cmdline | grep -o 'video=[^ ]*'
```

Examine kernel logs for mode-setting activity:

``` bash
dmesg | grep -E 'drm|kms|framebuffer'
```

Look for messages like `[drm] Initialized amdgpu` or `i915 ... initialized`.

To disable KMS (rarely needed):

``` bash
GRUB_CMDLINE_LINUX="nomodeset"
```

This forces the kernel to use simple framebuffer drivers instead of hardware-specific drivers. Expect degraded performance and limited resolution.

## Troubleshooting Video Mode Issues

**Verify firmware support**: Use `vbeinfo` in GRUB to confirm the mode exists on your system.

**Check connector names**: Use `modetest` to list connected displays with their exact connector names:

``` bash
modetest | head -50
```

Use the exact connector name from output in your `video=` parameter.

**Force fallback modes**: Remove custom `video=` parameters and let the driver auto-detect:

``` bash
GRUB_CMDLINE_LINUX=""
```

**Review kernel logs**: Detailed information appears in dmesg:

``` bash
dmesg | grep -i 'video\|mode\|display'
```

Look for messages indicating failed mode-setting or unsupported resolutions.

**Update BIOS/firmware**: Video mode support varies by firmware revision. Firmware updates often improve compatibility and fix display bugs.

**Check EDID data**: The kernel reads display capabilities via EDID. On some displays, EDID is corrupted or missing. Force a known-good mode explicitly:

``` bash
GRUB_CMDLINE_LINUX="video=HDMI-1:1920x1080-32@60"
```

**Disable Secure Boot temporarily**: On EFI systems, some firmware has quirks with certain video modes under Secure Boot. Disabling Secure Boot can help isolate firmware-specific issues.

**Reduce resolution at boot**: If high-resolution modes fail, the kernel may lack sufficient firmware-allocated memory. Try a lower resolution:

``` bash
GRUB_CMDLINE_LINUX="video=1024x768-32@60"
```

**Enable verbose graphics logging**: Get detailed driver debugging output:

``` bash
GRUB_CMDLINE_LINUX="drm.debug=0xff"
```

This produces voluminous kernel log output but identifies low-level driver issues. Check `dmesg` after boot.
