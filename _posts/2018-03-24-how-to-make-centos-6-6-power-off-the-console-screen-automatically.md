---
title: "DPMS Screen Blanking and Power-Off on Rocky Linux 9"
date: 2018-03-24 11:45:26 +0000
modified: 2026-04-12 16:38:23 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-centos-6-6-power-off-the-console-screen-automatically/
---

Rocky Linux 9 can blank the console screen after a period of inactivity, but by default it may not actually power off the display. This is often caused by kernel mode settings or DPMS (Display Power Management Signaling) configuration.

## Check Current DPMS Status

First, verify whether DPMS is enabled on your console:

``` bash
cat /sys/module/kernel/parameters/consoleblank
```

If this returns nothing or an error, DPMS may not be active. Check your kernel parameters:

``` bash
cat /proc/cmdline
```

Look for `nomodeset` or `vesa` parameters, which can disable kernel mode setting and prevent proper power management.

## Remove nomodeset to Enable KMS

If `nomodeset` is present in your boot parameters, removing it often resolves the issue. Edit your GRUB configuration:

``` bash
sudo nano /etc/default/grub
```

Find the line starting with `GRUB_CMDLINE_LINUX` and remove `nomodeset`. For example, change:

``` bash
GRUB_CMDLINE_LINUX="rhgb quiet nomodeset"
```

To:

``` bash
GRUB_CMDLINE_LINUX="rhgb quiet"
```

Regenerate your GRUB configuration:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

On UEFI systems, use:

``` bash
sudo grub2-mkconfig -o /boot/efi/EFI/rocky/grub.cfg
```

## Why nomodeset Matters

`nomodeset` disables **Kernel Mode Setting (KMS)**, which moved graphics initialization from the X server to the kernel. When KMS is disabled, the kernel can’t properly manage display power states, so DPMS commands don’t reach the hardware.

Removing this parameter allows the kernel to take direct control of video mode switching and power management, which is the standard on modern systems.

## Configure Console Blank Timeout

Set the blanking timeout (in seconds) directly. This requires root or sudo:

``` bash
echo 300 | sudo tee /sys/module/kernel/parameters/consoleblank
```

This blanks the console after 300 seconds. Make it permanent by adding to `/etc/default/grub`:

``` bash
GRUB_CMDLINE_LINUX="rhgb quiet consoleblank=300"
```

Then regenerate GRUB as above.

## Enable DPMS on the Console

For full power-off capability, you may need to explicitly enable DPMS. Add this to `/etc/default/grub`:

``` bash
GRUB_CMDLINE_LINUX="rhgb quiet consoleblank=300 vga=normal"
```

The `vga=normal` parameter ensures standard VESA video mode is used, which supports DPMS better than some UEFI framebuffer modes.

## Verify Changes

After rebooting, test whether the console blanks:

``` bash
sudo bash -c 'echo 10 > /sys/module/kernel/parameters/consoleblank'
```

Wait 10 seconds. The screen should go black. Move the mouse or press a key to wake it.

Check which video driver the kernel is using:

``` bash
dmesg | grep -i "drm\|video\|framebuffer" | head -20
```

This helps confirm whether KMS is active.

## Troubleshooting

If power-off still doesn’t work after removing `nomodeset`:

- Check BIOS settings for display power management options
- Verify your GPU driver is loaded: `lsmod | grep -E "nouveau|amdgpu|i915"`
- Try adding `pcie_port_pm=off` to GRUB if using PCIe devices
- Some VM environments don’t support DPMS—check if you’re in a virtual machine

## References

- <a href="https://fedoraproject.org/wiki/Features/KernelModesetting" rel="nofollow noopener" target="_blank">Fedora KernelModesetting documentation</a>
- <a href="https://www.kernel.org/doc/html/latest/power/pm.html" rel="nofollow noopener" target="_blank">ACPI Power Management on Linux</a>

## 2026 Best Practices and Advanced Techniques

For DPMS Screen Blanking and Power-Off on Rocky Linux 9, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
