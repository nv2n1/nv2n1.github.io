---
title: "Boot Windows from GRUB2 Command Line"
date: 2018-03-24 08:21:51 +0000
layout: post
canonical: https://www.systutorials.com/how-to-manually-set-the-boot-entry-for-windows-in-grub2/
---

If you need to boot Windows from the GRUB2 command line—whether during troubleshooting, recovery, or when your boot configuration is broken—you can do it with a few commands. This guide covers both BIOS and UEFI systems.

## Quick boot for BIOS systems

Assuming Windows is installed on the first partition of the first disk in NTFS format:

    insmod ntfs
    set root=(hd0,1)
    chainloader +1
    boot

Press Enter after each line. The `boot` command starts the system; you don’t need to press F10 or any other key.

## Finding your Windows partition

If you’re not sure which partition holds Windows, start by listing available disks at the GRUB command line:

    ls

This shows available disks and partitions. Then inspect partitions individually:

    ls (hd0,1)
    ls (hd0,2)
    ls (hd1,1)

Look for a directory listing with Windows system folders (`Windows`, `Program Files`, `Users`, `ProgramData`). Once you identify the correct partition, note the partition number for use in your boot commands.

## Understanding GRUB2 disk notation

GRUB2 uses `(hdX,Y)` notation where:

- **X** is the disk number (starting at 0)
- **Y** is the partition number (starting at 1)

Examples:

- `(hd0,1)` — first disk, first partition
- `(hd0,2)` — first disk, second partition
- `(hd1,3)` — second disk, third partition

## UEFI systems

On UEFI systems, Windows uses the EFI System Partition (ESP). Locate the ESP (typically FAT32 formatted) and use:

    insmod fat
    set root=(hd0,1)
    chainloader /EFI/Microsoft/Boot/bootmgfw.efi
    boot

If the ESP is on a different partition, adjust `(hd0,1)` accordingly. You can identify the ESP with:

    ls (hd0,1)/EFI/Microsoft/Boot/

If this directory exists, you’ve found the right partition.

## Making the boot entry permanent

If you regularly need this functionality, add it to your GRUB configuration. Edit or create `/etc/grub.d/40_custom`:

``` bash
#!/bin/sh -e
echo "Adding Windows boot entry" >&2

cat << EOF
menuentry 'Windows (BIOS)' {
    insmod ntfs
    set root=(hd0,1)
    chainloader +1
}
EOF
```

For UEFI:

``` bash
#!/bin/sh -e
echo "Adding Windows boot entry" >&2

cat << EOF
menuentry 'Windows (UEFI)' {
    insmod fat
    set root=(hd0,1)
    chainloader /EFI/Microsoft/Boot/bootmgfw.efi
}
EOF
```

Make the file executable:

    sudo chmod +x /etc/grub.d/40_custom

Rebuild the GRUB configuration:

    sudo grub-mkconfig -o /boot/grub/grub.cfg

The new entry should appear in your GRUB menu on the next boot.

## Troubleshooting

**Chainloading fails or Windows doesn’t boot:**

- Verify the partition contains Windows: `ls (hd0,1)/Windows`
- Check NTFS support loads correctly: `insmod ntfs` should complete silently with no error
- On UEFI, ensure you’re using the correct EFI bootloader path: `ls (hd0,1)/EFI/Microsoft/Boot/`
- Test BIOS-mode Windows boot: `echo (hd0,1)/bootmgr`
- Disable Secure Boot in firmware if using UEFI and experiencing boot failures
- If Windows uses exFAT (modern installations), use `insmod exfat` instead of `insmod ntfs`

**Partition numbering seems wrong:**

GRUB and Linux sometimes use different partition numbering. Use `parted -l` from a Linux environment to see the exact partition layout before rebooting:

    sudo parted -l

This shows which partition contains Windows and maps it to GRUB’s notation.

**Module loading errors:**

If `insmod ntfs` or `insmod fat` fails, the modules may not be compiled into your GRUB build. Check your distribution’s GRUB configuration or consider rebuilding GRUB with additional modules.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Boot Windows from GRUB2 Command Line with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Boot Windows from GRUB2 Command Line. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
