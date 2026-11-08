---
title: "Setting the Default Boot Entry in GRUB2"
date: 2013-07-12 16:32:31 +0000
modified: 2026-04-12 16:34:33 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-default-entry-in-grub2-and-grub/
---

Modern Linux systems use GRUB2 as the bootloader. You’ll set the default boot entry either through the configuration file or via command-line tools.

### View Available Boot Entries

First, list all available GRUB2 menu entries:

``` bash
grep ^menuentry /etc/grub2.cfg | cut -d "'" -f2
```

On UEFI systems, use `/etc/grub2-efi.cfg` instead. If you’re unsure which mode your system uses:

``` bash
[ -d /sys/firmware/efi ] && echo "UEFI" || echo "BIOS"
```

### Method 1: Using grub2-set-default (Temporary)

Set the default entry by name:

``` bash
sudo grub2-set-default 'Ubuntu'
```

Verify it was set:

``` bash
grub2-editenv list
```

This stores the selection in `/boot/grub2/grubenv`. The setting persists across reboots but can fail on some systems if `GRUB_DEFAULT` in `/etc/default/grub` is set to a numeric value. Check your `/etc/default/grub` to see which approach will work.

### Method 2: Editing /etc/default/grub (Permanent)

Edit the configuration file:

``` bash
sudo nano /etc/default/grub
```

Locate the `GRUB_DEFAULT` line and set it to the entry name:

    GRUB_DEFAULT="Ubuntu"

You can also use the numeric index (starting from 0):

    GRUB_DEFAULT=0

Using the entry name is more reliable — numeric indices can shift if you add or remove boot entries.

After editing, regenerate the GRUB2 configuration:

``` bash
sudo grub2-mkconfig -o /etc/grub2.cfg
```

On UEFI systems:

``` bash
sudo grub2-mkconfig -o /etc/grub2-efi.cfg
```

Verify the change took effect:

``` bash
grep ^GRUB_DEFAULT /etc/default/grub
```

### Finding Entry Names with Submenus

On some systems, entries exist in submenus. Use this to list them with hierarchy:

``` bash
grep -E "^menuentry|^submenu" /etc/grub2.cfg | sed 's/[{}]//g'
```

For submenu entries, use the format:

``` bash
GRUB_DEFAULT="Submenu Name>Entry Name"
```

For example, if you have a submenu called “Advanced options for Ubuntu” with an entry “Ubuntu, with Linux 5.15.0-56-generic”:

    GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 5.15.0-56-generic"

### Setting a Default with a Timeout

If you want the system to wait before booting the default entry, also set:

    GRUB_TIMEOUT=5

This gives users 5 seconds to interrupt the boot and choose a different entry.

### Troubleshooting

**Issue: Changes don’t persist after reboot**

Check if `/boot/grub2/grubenv` is corrupted:

``` bash
sudo grub2-editenv create
```

Then try setting the default again.

**Issue: Entry name contains special characters**

If an entry name has quotes or pipes, escape them:

``` bash
sudo grub2-set-default 'Windows Boot Manager (on /dev/sda1)'
```

**Issue: GRUB2 not detecting all entries**

Regenerate the configuration if you’ve added new kernels or OS installations:

``` bash
sudo grub2-mkconfig -o /etc/grub2.cfg
```

### Legacy GRUB (Grub 0.99)

Older systems using legacy GRUB (rarely encountered now) store settings in `/boot/grub/grub.conf`:

    default=0
    timeout=5

    title Ubuntu
        root (hd0,0)
        kernel /vmlinuz

The `default=0` means boot the first entry. Edit this file directly and don’t regenerate — legacy GRUB doesn’t use mkconfig.

## 2026 Best Practices and Advanced Techniques

For Setting the Default Boot Entry in GRUB2, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
