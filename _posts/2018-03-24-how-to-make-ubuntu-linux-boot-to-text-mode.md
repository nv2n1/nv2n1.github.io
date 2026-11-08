---
title: "How to Boot Ubuntu to Text Mode (Runlevel 3)"
date: 2018-03-24 11:50:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-ubuntu-linux-boot-to-text-mode/
---

Ubuntu boots to the graphical desktop by default, but you can change it to boot directly to a text-mode login prompt. This is useful for headless servers, troubleshooting, or resource-constrained systems.

The method depends on your init system. Modern Ubuntu uses systemd, but the GRUB approach still works if you need it.

## Using systemd (recommended)

Ubuntu 16.04 and newer use systemd to manage boot targets. Switch to text mode with:

``` bash
sudo systemctl set-default multi-user.target
```

This sets the default boot target to `multi-user.target`, which provides a text login prompt without the graphical display manager.

To verify the change:

``` bash
systemctl get-default
```

You should see `multi-user.target` returned.

To temporarily boot to text mode without making a permanent change:

``` bash
sudo systemctl isolate multi-user.target
```

## Switching back to graphical mode

When you want to return to the GUI, use:

``` bash
sudo systemctl set-default graphical.target
```

Then reboot. You can also switch back temporarily without rebooting:

``` bash
sudo systemctl isolate graphical.target
```

## GRUB method (alternative)

If you prefer to boot text mode via GRUB parameters instead of changing the systemd target, you can edit the bootloader configuration:

Backup the GRUB config first:

``` bash
sudo cp /etc/default/grub /etc/default/grub.bak
```

Edit the GRUB configuration:

``` bash
sudo nano /etc/default/grub
```

Find the line `GRUB_CMDLINE_LINUX=` and add the `text` parameter:

    GRUB_CMDLINE_LINUX="text"

Save and update GRUB:

``` bash
sudo update-grub
```

Reboot to apply the change.

## Removing the text parameter

To revert the GRUB change, remove `text` from `GRUB_CMDLINE_LINUX`, then run `sudo update-grub` again.

## Checking your display manager

If you’re using the GRUB method but still boot to the GUI, your display manager may be starting anyway. Check which one is active:

``` bash
systemctl status display-manager
```

Common display managers include `gdm3` (GNOME), `lightdm` (XFCE/Cinnamon), and `sddm` (KDE Plasma). You can disable it with:

``` bash
sudo systemctl disable gdm3
```

Or whichever manager you have installed.

## SSH access without display manager

If you’re managing a remote Ubuntu system, you don’t need to change the boot target. Keep the GUI running and just use SSH:

``` bash
ssh user@hostname
```

This gives you text mode access without affecting the server’s graphical environment, which may still be useful for local console work or troubleshooting.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers How to Boot Ubuntu to Text Mode (Runlevel 3) with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for How to Boot Ubuntu to Text Mode (Runlevel 3). For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
