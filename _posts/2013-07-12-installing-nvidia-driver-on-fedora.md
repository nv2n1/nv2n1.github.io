---
title: "Installing NVIDIA Drivers with Akmod on Fedora"
date: 2013-07-12 16:32:01 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /installing-nvidia-driver-on-fedora/
---

Installing the NVIDIA driver on Fedora via `akmod` (automatic kernel module) is the cleanest approach when using RPM Fusion. The driver rebuilds automatically whenever the kernel updates, saving you manual reinstalls.

### Prerequisites

First, verify your GPU is supported. Check the <a href="https://www.nvidia.com/Download/driverDetails.aspx" rel="nofollow noopener" target="_blank">NVIDIA driver support matrix</a> for your hardware. Most consumer and professional cards from the past decade are supported, but older Kepler-era GPUs may have reached EOL.

### Enable RPM Fusion Repositories

RPM Fusion provides the `akmod-nvidia` packages for Fedora:

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Update your package cache:

``` bash
sudo dnf makecache
```

### Install akmod-nvidia and Dependencies

Install the driver and 32-bit libraries for Steam and other applications:

``` bash
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-libs.i686
```

The `akmod` package will build the kernel module at boot. This typically takes 2-5 minutes on first boot. Monitor progress with:

``` bash
sudo journalctl -f | grep -i nvidia
```

### Disable Nouveau Driver

The open-source Nouveau driver conflicts with NVIDIA’s proprietary driver. Blacklist it during boot:

``` bash
echo "blacklist nouveau" | sudo tee /etc/modprobe.d/blacklist-nouveau.conf
```

Regenerate the initial ramdisk to apply the blacklist:

``` bash
sudo dracut --force
```

This command automatically detects your current kernel and rebuilds `initramfs` without manual path manipulation.

### Handle SELinux if Necessary

Modern Fedora with `akmod-nvidia` typically doesn’t require SELinux policy changes. However, if you encounter driver loading errors, check:

``` bash
sudo ausearch -m avc | grep -i nvidia
```

If SELinux is blocking the driver, set:

``` bash
sudo setsebool -P allow_execstack on
```

This is rarely needed on current Fedora releases, as policies have been updated for modern drivers.

### Reboot and Verify

``` bash
sudo reboot
```

After reboot, confirm the driver loaded:

``` bash
nvidia-smi
```

You should see output showing your GPU, driver version, and memory information. If it fails, check the kernel module status:

``` bash
lsmod | grep nvidia
```

### Troubleshooting

**akmod still building after reboot:** This is normal on first install or after kernel updates. Wait for the build to complete before rebooting again.

``` bash
sudo akmods --kernels $(uname -r)
```

**Nouveau still loading:** Verify the blacklist file was created and dracut completed:

``` bash
cat /etc/modprobe.d/blacklist-nouveau.conf
sudo lsinitrd /boot/initramfs-$(uname -r).img | grep nouveau
```

**Graphics glitches or tearing:** Enable triple buffering and composite extensions in X11 or Wayland settings, or use NVIDIA’s control panel if using GNOME:

``` bash
nvidia-settings
```

**Wayland compatibility:** On Wayland, ensure you’re using Fedora 39+. The driver now supports Wayland natively, so you can run:

``` bash
echo "options nvidia-drm modeset=1" | sudo tee /etc/modprobe.d/nvidia-drm.conf
sudo dracut --force
```

Then reboot. This enables proper Wayland support without X11 fallback.

### Keeping the Driver Updated

`akmod-nvidia` automatically rebuilds when you update the kernel:

``` bash
sudo dnf upgrade
```

Monitor the rebuild after kernel updates:

``` bash
sudo tail -f /var/log/akmods.log
```

For CUDA or cuDNN workloads, also install `cuda-repo` from NVIDIA’s package repository to stay aligned with driver versions.

## 2026 Best Practices and Advanced Techniques

For Installing NVIDIA Drivers with Akmod on Fedora, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
