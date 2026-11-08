---
title: "Enabling Automatic Reboot on Kernel Panic in Linux"
date: 2018-03-24 11:45:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-linux-automatically-reboot-after-a-kernel-panic/
---

When a kernel panic occurs on a remote Linux server, manual intervention via SSH becomes impossible. The kernel can be configured to automatically reboot after a panic, allowing the system to recover without human intervention.

## Enable Kernel Panic Auto-Reboot

The `kernel.panic` parameter controls this behavior. A value of 0 disables auto-reboot; any positive integer specifies seconds to wait before rebooting.

### Temporary Configuration (Current Session)

``` bash
echo 20 > /proc/sys/kernel/panic
```

This takes effect immediately but is lost on reboot. Useful for testing before making permanent changes.

### Persistent Configuration

#### Option 1: Using sysctl.conf

Edit `/etc/sysctl.conf`:

``` bash
echo "kernel.panic = 20" | sudo tee -a /etc/sysctl.conf
```

Apply the change:

``` bash
sudo sysctl -p
```

This persists across reboots and is the recommended modern approach for most distributions.

#### Option 2: Kernel Boot Parameter (GRUB)

For GRUB2-based systems, edit `/etc/default/grub`:

``` bash
GRUB_CMDLINE_LINUX="panic=20"
```

Then regenerate the GRUB configuration:

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

On UEFI systems, use:

``` bash
sudo grub-mkconfig -o /boot/efi/EFI/debian/grub.cfg
```

This approach embeds the setting at the bootloader level, ensuring it applies even if `/proc/sys/kernel/panic` is modified at runtime.

## Verify Configuration

Check the current setting:

``` bash
cat /proc/sys/kernel/panic
```

Or via sysctl:

``` bash
sysctl kernel.panic
```

## Related Panic-Related Parameters

While `kernel.panic` handles the reboot timing, consider these related settings:

- `kernel.panic_on_oops` — Set to 1 to trigger a kernel panic on an Oops condition, forcing a reboot. Useful for unattended systems:

``` bash
echo "kernel.panic_on_oops = 1" | sudo tee -a /etc/sysctl.conf
```

- `kernel.panic_on_rcu_stall` — Forces panic on RCU stall detection (useful for detecting kernel deadlocks).

Apply these via `sysctl -p` after editing.

## Detect and Alert on Auto-Reboots

Automatic reboots leave no indication without monitoring. Track them using:

### Check Kernel Log for Panic

After an auto-reboot, examine the previous boot’s kernel messages:

``` bash
sudo journalctl -b -1 -p err
```

Or legacy systems without systemd:

``` bash
sudo dmesg | grep -i "kernel panic"
```

### Monitor Uptime Changes

Create a script that logs system startup and compares against expected reboots:

``` bash
#!/bin/bash
UPTIME=$(cat /proc/uptime | awk '{print int($1)}')
THRESHOLD=300  # 5 minutes

if [ "$UPTIME" -lt "$THRESHOLD" ]; then
    LAST_BOOT=$(date -d @$(date +%s -d "$(uptime -s)") "+%Y-%m-%d %H:%M:%S")
    echo "System rebooted at $LAST_BOOT" | mail -s "Unexpected Reboot Alert" admin@example.com
fi
```

Add to crontab to run at boot:

``` bash
@reboot /usr/local/bin/reboot-monitor.sh
```

### Use Systemd Service for Alerts

Create `/etc/systemd/system/panic-alert.service`:

``` ini
[Unit]
Description=Alert on Kernel Panic Recovery
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/panic-alert.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Then enable it:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable panic-alert.service
```

## Testing (Safely)

To verify the setting works without crashing production, you can trigger a controlled panic in a test VM:

``` bash
echo c | sudo tee /proc/sysrq-trigger
```

This causes an immediate kernel panic and tests the auto-reboot mechanism.

## Best Practices

- Set `kernel.panic` to a value between 10-30 seconds on production systems — enough time for disk I/O to flush but not so long that the system appears hung.
- Always test panic recovery in a staging environment before deploying to production.
- Combine auto-reboot with centralized logging (syslog, journald) to capture panic details before the reboot.
- Monitor consecutive reboots; multiple panics in quick succession indicate a deeper issue requiring investigation.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Enabling Automatic Reboot on Kernel Panic in Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Enabling Automatic Reboot on Kernel Panic in Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
