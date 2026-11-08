---
title: "How to Set Up and Manage File-Based Swap on Linux"
date: 2018-04-03 15:01:38 +0000
modified: 2026-04-11 15:44:04 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-add-a-file-based-swap-for-linux/
---

When you need additional swap space but all partitions are allocated, creating a swap file lets you add capacity without repartitioning. This is especially useful on systems with fixed disk layouts or cloud instances where you can’t modify the underlying disk structure.

## Creating the Swap File

Start by allocating space. `fallocate` is the fastest option on most modern filesystems:

``` bash
fallocate -l 2G /swapfile
```

If you’re on btrfs, NFS, or another filesystem where `fallocate` fails, use `dd` instead:

``` bash
dd if=/dev/zero of=/swapfile bs=1M count=2048
```

The `bs=1M` block size is significantly faster than smaller sizes for large files. Verify creation:

``` bash
ls -lh /swapfile
```

## Set Proper Permissions

Swap files can contain sensitive data in memory dumps, so restrict access:

``` bash
chmod 600 /swapfile
chown root:root /swapfile
```

The `600` permission (read/write for root only) is the standard. Don’t use `700`—it’s unnecessarily permissive.

## Initialize the Swap Space

Format the file as swap:

``` bash
mkswap /swapfile
```

You’ll see output like:

    Setting up swapspace version 1, size = 2 GiB (2147479552 bytes)
    no label, UUID=f30730f3-eb1d-4d30-a088-a0274f3c2f3e

Ignore warnings about bootbits—these are harmless.

## Enable the Swap File

Activate it immediately:

``` bash
swapon /swapfile
```

Verify it’s active:

``` bash
swapon --show
```

Output shows:

    NAME      TYPE SIZE USED PRIO
    /swapfile file 2.0G   0B  -2

Check overall memory and swap status:

``` bash
free -h
```

## Make Swap Persistent Across Reboots

Add an entry to `/etc/fstab`:

    /swapfile none swap sw 0 0

Use `none` as the mount point, not `swap`—this is the modern convention. Test the configuration without rebooting:

``` bash
swapon --all --verbose
```

This validates that fstab parses correctly.

## Managing Multiple Swap Files

To add additional swap alongside existing swap:

``` bash
fallocate -l 4G /swapfile2
chmod 600 /swapfile2
mkswap /swapfile2
swapon /swapfile2
```

Then append to `/etc/fstab`:

``` bash
echo "/swapfile2 none swap sw 0 0" >> /etc/fstab
```

Each swap file can have different priorities. Lower priority numbers are used first. To set a priority when enabling swap:

``` bash
swapon -p 10 /swapfile2
```

Then update `/etc/fstab` with the priority option:

    /swapfile2 none swap sw,pri=10 0 0

## Removing Swap

To disable a swap file:

``` bash
swapoff /swapfile
```

Remove its line from `/etc/fstab`, then delete the file:

``` bash
rm /swapfile
```

## Monitoring Swap Usage

Check overall swap consumption:

``` bash
grep Swap /proc/meminfo
```

For per-process swap usage, use:

``` bash
for pid in $(pgrep -P 1); do 
  label=$(cat /proc/$pid/comm 2>/dev/null)
  swap=$(grep VmSwap /proc/$pid/status 2>/dev/null | awk '{print $2}')
  [ -n "$swap" ] && [ "$swap" != "0" ] && echo "$label (PID $pid): ${swap}kB"
done
```

Or use `smem` if installed:

``` bash
smem -s swap -r
```

Watch swap activity in real-time with `iostat` (from sysstat package):

``` bash
iostat -x 1 | grep -E "Device|sda"
```

## Performance Considerations

**Filesystem choice matters.** File-based swap performs nearly identically to partition-based swap on ext4 and XFS. Modern NVMe disks make swap files practical even for performance-critical systems.

**Btrfs requires care.** Copy-on-Write (CoW) conflicts with swap. Disable CoW on the swap file:

``` bash
chattr +C /swapfile
```

Do this *before* running `mkswap`.

**Avoid network filesystems.** NFS and other network-mounted filesystems are too slow for swap. Always place swap on local storage.

**Tune swappiness.** The `vm.swappiness` setting (0–100) controls how aggressively the kernel uses swap. Check the current value:

``` bash
cat /proc/sys/vm/swappiness
```

Set it temporarily:

``` bash
sysctl vm.swappiness=30
```

For servers, `30` is a reasonable default. For desktops, higher values (50–60) may feel more responsive. Make it permanent in `/etc/sysctl.conf`:

    vm.swappiness=30

**Size recommendations.** For modern systems with adequate RAM, swap equal to 25% of physical RAM is usually sufficient. For servers with 64GB+ RAM, even 4–8GB of swap handles edge cases. Virtual machines and containers benefit from slightly more swap due to unpredictable load spikes.
