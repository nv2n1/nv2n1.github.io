---
title: "Installing NVIDIA Drivers on Fedora"
date: 2013-07-12 16:31:42 +0000
modified: 2026-04-12 16:43:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /install-nvidia-driver-on-fedora/
---

Installing NVIDIA drivers on Fedora is straightforward when using RPM Fusion repositories. This guide covers modern Fedora releases (39+) using DNF package management.

### Prerequisites

Before starting, determine which driver your GPU requires. Check the <a href="https://www.nvidia.com/Download/driverDetails.aspx" rel="nofollow noopener" target="_blank">NVIDIA driver download page</a> or use this command to identify your GPU:

``` bash
lspci | grep -i nvidia
```

For newer GPUs (Maxwell and later), use the standard driver. Older GPUs may require legacy drivers available through RPM Fusion.

### Enable RPM Fusion Repositories

RPM Fusion provides optimized NVIDIA driver packages with proper nouveau blacklisting already configured.

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Update your package cache:

``` bash
sudo dnf makecache
```

### Install the Driver

For most modern NVIDIA GPUs:

``` bash
sudo dnf install gcc kernel-devel kernel-headers akmod-nvidia xorg-x11-drv-nvidia
```

The `akmod-nvidia` package automatically compiles the kernel module using DKMS when you install updates, eliminating manual rebuilds.

Wait for the kernel module to build. You can check the build status with:

``` bash
sudo akmods --force
```

Watch for build completion in `/var/cache/akmods/nvidia/`.

### Reboot and Verify

Reboot your system for the driver to take effect:

``` bash
sudo reboot
```

After rebooting, verify the driver loaded correctly:

``` bash
nvidia-smi
```

You should see GPU information displayed. Check kernel logs if the driver didn’t load:

``` bash
sudo journalctl -u akmods -n 50
dmesg | grep -i nvidia
```

### Nouveau Blacklisting

RPM Fusion automatically adds nouveau blacklist rules during installation. Verify they’re in place:

``` bash
cat /etc/modprobe.d/blacklist-nouveau.conf
```

You should see entries blacklisting the nouveau driver. This prevents conflicts with NVIDIA’s kernel module.

If nouveau is still loaded despite blacklisting, regenerate your initramfs:

``` bash
sudo dracut --force
```

### Wayland Considerations

If you’re using Wayland, NVIDIA driver support varies by release. For optimal stability, GNOME on X11 remains more mature. You can select the session type at login or check your current session:

``` bash
echo $XDG_SESSION_TYPE
```

### Troubleshooting

**Driver module fails to build:**
Ensure kernel headers match your running kernel version:

``` bash
uname -r
rpm -qa | grep kernel-headers
```

Reinstall if mismatched:

``` bash
sudo dnf reinstall kernel-devel-$(uname -r) kernel-headers-$(uname -r)
sudo akmods --force
```

**NVIDIA settings crashes or X session unstable:**
Check for driver/X compatibility issues:

``` bash
sudo Xvfb :99 -screen 0 1024x768x24 &
DISPLAY=:99 glxgears
```

If rendering fails, verify the driver actually loaded via `nvidia-smi` first.

**System boots to black screen:**
Boot into emergency mode with `Ctrl+Alt+F2` and check:

``` bash
sudo systemctl status gdm
sudo journalctl -xe
```

If the driver is the culprit, temporarily remove it:

``` bash
sudo dnf remove akmod-nvidia xorg-x11-drv-nvidia
sudo dracut --force
sudo reboot
```

### CUDA and cuDNN

If developing with CUDA, install the toolkit from RPM Fusion or NVIDIA directly:

``` bash
sudo dnf install cuda-toolkit
```

Add to your shell profile:

``` bash
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

Verify installation:

``` bash
nvcc --version
```

## 2026 Best Practices and Advanced Techniques

For Installing NVIDIA Drivers on Fedora, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
