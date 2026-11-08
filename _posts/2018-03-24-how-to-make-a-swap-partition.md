---
title: "Creating a Swap Partition on Linux"
date: 2018-03-24 08:14:11 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-a-swap-partition/
---

Swap space is essential for system stability, allowing the kernel to move less-frequently-used memory pages to disk when physical RAM is exhausted. Here’s how to set up a dedicated swap partition.

### Step 1: Create the Partition

Use `fdisk`, `gdisk` (for GPT disks), or `parted` to create a new partition. For modern systems with GPT partition tables:

``` bash
sudo gdisk /dev/sdc
```

At the prompt:

- Press `n` to create a new partition
- Accept default partition number and first sector
- Specify the last sector (or size with `+XXGG` for size in GB)
- Set type to `8200` (Linux swap)
- Press `w` to write changes

For MBR/DOS partition tables, use `fdisk` and set the type to `82` (Linux swap).

After creating the partition, verify it exists:

``` bash
lsblk /dev/sdc
```

### Step 2: Format as Swap

Initialize the partition with the swap filesystem:

``` bash
sudo mkswap /dev/sdc1
```

The output will show the swap UUID and size. Keep note of this for later reference.

### Step 3: Enable Swap

Activate the swap partition immediately:

``` bash
sudo swapon /dev/sdc1
```

Verify it’s active:

``` bash
swapon -s
```

Or use the more modern approach with `free`:

``` bash
free -h
```

This shows all swap space currently in use.

### Step 4: Persist Across Reboots

Add the swap partition to `/etc/fstab` so it activates automatically on boot. Edit the file:

``` bash
sudo nano /etc/fstab
```

Add this line (using the UUID is more reliable than device names):

    UUID=your-swap-uuid    none    swap    sw    0 0

Find your swap UUID with:

``` bash
lsblk -o NAME,UUID /dev/sdc1
```

Or check the output from your earlier `mkswap` command.

### Disabling Swap

If you need to remove a swap partition:

``` bash
sudo swapoff /dev/sdc1
```

Remove the line from `/etc/fstab` to prevent it from reactivating on reboot.

### Important Considerations

**Swap size**: A common guideline is 1-2x your RAM on systems with 8GB or less, and 0.5x RAM on larger systems. On modern systems with sufficient RAM, minimal swap (1-2GB) is acceptable.

**Swap priority**: If you have multiple swap devices, assign priorities in `/etc/fstab` to control which is used first:

    UUID=swap-device-1    none    swap    sw,pri=10    0 0
    UUID=swap-device-2    none    swap    sw,pri=5     0 0

Higher priority numbers are used first.

**Swappiness**: Control how aggressively the kernel uses swap by adjusting the swappiness value (0-100, default 60):

``` bash
sudo sysctl vm.swappiness=10
```

Lower values preserve swap for emergencies; higher values use it more readily. Make permanent changes in `/etc/sysctl.conf`:

    vm.swappiness=10

**Zram alternative**: On systems with limited storage, consider `zram` instead—compressed in-memory swap that’s faster than disk-based swap. This is configured differently and doesn’t use a partition.

## 2026 Best Practices and Advanced Techniques

For Creating a Swap Partition on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
