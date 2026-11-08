---
title: "Linux Kernel: Disable GuC/HuC Auto Mode on Pre-Gen11"
date: 2020-10-01 14:25:35 +0000
author: "Tony"
layout: post
categories: [linux-systems-administration]
canonical: /linux-kernel-drm-i915-guc-dont-enable-guc-huc-in-auto-mode-on-pre-gen11/
---

This kernel change (commit 87d855e) prevents the Graphics Micro-Controller (GuC) and HEVC Video Codec (HuC) from being enabled by default on Intel GPU generations before Gen11, even when using automatic detection mode.

## Background: GuC and HuC in i915

The i915 driver supports hardware-based GPU command submission and video codec acceleration through GuC and HuC firmware. These components improve performance and power efficiency on newer hardware, but their stability and reliability vary significantly across GPU generations.

The `enable_guc` module parameter controls GuC/HuC behavior:

- `0` – Disabled (explicit)
- `-1` – Auto mode (hardware decides based on detection logic)
- `2` – Enabled (explicit)

## Why Pre-Gen11 Needs Special Handling

Before Gen11 (Skylake, Kaby Lake, Coffee Lake, Whiskey Lake, Comet Lake), GuC and HuC support was either incomplete or problematic. The kernel team planned to change the default from explicit disable (`0`) to auto mode (`-1`), which would automatically enable these features on capable hardware. However, this would inadvertently activate GuC/HuC on older generations where they weren’t production-ready.

This patch ensures that even in auto mode, pre-Gen11 platforms skip GuC/HuC initialization entirely. Users on older hardware can still explicitly force enablement with `enable_guc=2` if they’re willing to accept the risks, but they won’t get these features accidentally.

## Code Changes

The change modifies `__get_platform_enable_guc()` in `drivers/gpu/drm/i915/intel_uc.c`:

``` c
static int __get_platform_enable_guc(struct drm_i915_private *i915)
{
    struct intel_uc_fw *guc_fw = &i915->guc.fw;
    struct intel_uc_fw *huc_fw = &i915->huc.fw;
    int enable_guc = 0;

    if (!HAS_GUC(i915))
        return 0;

    /* We don't want to enable GuC/HuC on pre-Gen11 by default */
    if (INTEL_GEN(i915) < 11)
        return 0;

    if (intel_uc_fw_is_selected(guc_fw) && intel_uc_fw_is_selected(huc_fw))
        enable_guc |= ENABLE_GUC_LOAD_HUC;

    return enable_guc;
}
```

The key additions are:

- Early return if the platform lacks GuC support at all
- Early return if the GPU is pre-Gen11, preventing auto-enablement
- Removes outdated comment about platform-specific tuning

## Practical Impact for Sysadmins

If you’re managing systems with older Intel integrated graphics (Intel HD Graphics 630 and earlier), this patch doesn’t change anything if you already have `enable_guc=0` in your kernel parameters. However, if you plan to upgrade kernels where the default switches to auto mode, pre-Gen11 systems will maintain stable behavior.

For newer platforms (Gen11+, which includes Ice Lake, Tiger Lake, Alder Lake mobile and newer), auto mode will work as intended, providing GuC and HuC benefits without explicit configuration.

## Checking Your GPU Generation

To verify your Intel GPU generation:

``` bash
lspci | grep VGA
```

Look up your device ID on the <a href="https://01.org/linuxgraphics/documentation/hardware-specification" rel="nofollow noopener" target="_blank">Intel GPU specs wiki</a> or check the kernel logs:

``` bash
dmesg | grep -i "gen\|gpu"
```

You can also inspect the i915 module’s current configuration:

``` bash
cat /sys/module/i915/parameters/enable_guc
```

## Explicit GuC/HuC Control

To override this behavior on pre-Gen11 hardware (not recommended unless you understand the implications):

``` bash
echo "options i915 enable_guc=2" | sudo tee /etc/modprobe.d/i915-guc.conf
```

Then rebuild your initramfs and reboot. Monitor kernel logs for warnings or stability issues:

``` bash
sudo journalctl -b -k | grep -i "guc\|huc"
```

This patch exemplifies how kernel maintainers handle hardware capability detection—providing sensible defaults that don’t break older systems while allowing power users to opt into experimental features when needed.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Linux Kernel: Disable GuC/HuC Auto Mode on Pre-Gen11 with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Linux Kernel: Disable GuC/HuC Auto Mode on Pre-Gen11. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
