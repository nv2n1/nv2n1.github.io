---
title: "How to Unmount a Busy Filesystem in Linux"
date: 2016-05-21 02:54:30 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /force-linux-unmount-filesystem-reporting-device-busy/
---

When you try to unmount a filesystem with `umount`, Linux may report “device is busy.” This is a safety mechanism — the kernel blocks unmounting when processes or kernel threads are actively accessing the partition or holding open files on it. Forcing an unmount without understanding what’s using the filesystem risks data corruption and data loss.

## Identify What’s Using the Filesystem

Start here. Before you kill anything or force anything, figure out exactly what’s holding onto the mount.

### Using lsof

`lsof +D` recursively lists all open files within a mount point:

``` bash
lsof +D /mnt/data
```

Output looks like:

    COMMAND    PID  USER  FD   TYPE     DEVICE SIZE/OFF    NODE NAME
    bash      17622  user1 cwd   DIR    253,2    4096       2 /mnt/data
    sshd      18901  root  txt   REG    253,2  123456       5 /mnt/data/app
    postgres  19045  postgres 3u REG    253,2 5242880   12345 /mnt/data/base/13909

Each line shows a process accessing the mount. Review the list carefully — killing the wrong thing is worse than leaving the mount alone.

### Using fuser

`fuser` is more direct and faster for large directories:

``` bash
fuser /mnt/data
```

Returns just the PIDs:

    /mnt/data: 17622 18901 19045

For more detail, add `-v`:

``` bash
fuser -v /mnt/data
```

This shows the process name and type of access (read, write, etc.), helping you decide what’s safe to kill.

### Using pgrep and ps

For a quick sanity check on specific processes:

``` bash
pgrep -f /mnt/data
ps aux | grep /mnt/data
```

This helps verify if a specific application is still running in that directory.

### Checking Open Files by Specific Process

If you know a process ID, see what it has open:

``` bash
lsof -p <PID>
```

This is useful for debugging why a particular service can’t be shut down cleanly.

## Remount Instead of Unmounting

If your goal is to refresh a mount with different options, avoid unmounting entirely:

``` bash
mount -o remount,ro /mnt/data
mount -o remount,noexec,nosuid /mnt/data
```

The `-o remount` flag changes mount options without detaching the filesystem. This preserves running processes and open files while letting you adjust behavior. For read-only remounts, this is often the safest first step and avoids the unmount problem entirely.

You can verify the new options took effect:

``` bash
mount | grep /mnt/data
```

## Kill Identified Processes Cleanly

Once you’ve confirmed which processes are safe to terminate, stop them gracefully first:

``` bash
systemctl stop myservice
```

For background processes or daemons without a service file:

``` bash
kill 17622 18901
sleep 2
umount /mnt/data
```

Give processes a moment to exit cleanly. Check if they’re gone:

``` bash
lsof +D /mnt/data
```

If processes still exist, use `fuser` to kill all at once:

``` bash
fuser -k /mnt/data
sleep 1
umount /mnt/data
```

For stubborn processes that ignore `SIGTERM`, use `-9` for forced termination:

``` bash
fuser -k -9 /mnt/data
umount /mnt/data
```

**Warning**: killing a database process mid-transaction can corrupt data. Always check what you’re killing with `lsof` first. For databases like PostgreSQL or MySQL, use their admin tools instead:

``` bash
pg_terminate_backend(<pid>);  -- in PostgreSQL
KILL CONNECTION <id>;          -- in MySQL
```

## Lazy Unmount

The `-l` flag detaches the filesystem from the namespace immediately, but the kernel keeps cleanup deferred until nothing holds open file handles:

``` bash
umount -l /mnt/data
```

The filesystem becomes inaccessible from that mount point instantly, but processes with open files continue working until they close naturally. This is the standard approach for:

- NFS mounts where the server is unreachable (processes won’t hang in D state)
- Temporary mounts during system shutdown
- USB drives that have stray file handles
- Mounted container images or loop devices with lingering references

After a lazy unmount, the mount point is gone from `mount` output immediately:

``` bash
mount | grep /mnt/data  # returns nothing
```

The actual cleanup happens silently in the background. You can remount the same point once the lazy unmount is complete.

## Force Unmount

The `-f` flag immediately detaches the filesystem regardless of state:

``` bash
umount -f /mnt/data
```

Use this only as a last resort. Force unmounting can:

- Corrupt files still open by processes
- Cause data loss
- Leave the filesystem in an inconsistent state
- Leave orphaned processes in D state (uninterruptible sleep)

It’s primarily meant for unreachable NFS systems where lazy unmount isn’t sufficient. On local filesystems, force unmount should almost never be necessary — lazy unmount handles nearly all real-world scenarios.

## NFS-Specific Handling

NFS mounts behave differently. Check mount status:

``` bash
cat /proc/mounts | grep nfs
df -t nfs
```

NFS mounts commonly hang when the server becomes unreachable. Lazy unmount is almost always the right choice:

``` bash
umount -l /mnt/nfs
```

For a mount that’s actively hanging, you can wrap the unmount with a timeout:

``` bash
timeout 5 umount /mnt/nfs || umount -l /mnt/nfs
```

This tries a normal unmount for 5 seconds, then falls back to lazy if it hangs. Avoid `-f` on NFS unless the lazy unmount has genuinely failed after several minutes.

For NFS mounts stuck in `hung` state, check if the server is actually responding:

``` bash
ping <nfs-server-ip>
showmount -e <nfs-server-ip>
```

If the server is down, lazy unmount is your only option short of rebooting.

## Check for Kernel Threads

Sometimes the filesystem is in use by the kernel itself, not user processes. Check kernel threads or memory mappings:

``` bash
cat /proc/locks | grep /mnt/data
lsof +D /mnt/data | grep kernel
```

For dynamically loaded kernel modules, check what’s loaded:

``` bash
lsmod | grep module_name
```

If a kernel module holds the mount and you can’t unload it, try:

``` bash
rmmod module_name
```

If removal fails because something depends on it, find what’s using it:

``` bash
modinfo module_name
lsmod | grep module_name
```

If you can’t unload the module, lazy unmount is your only option short of rebooting.

## Reboot as Last Resort

If all else fails in production:

``` bash
systemctl reboot
reboot
```

If the system is unresponsive and you have SysRq enabled:

``` bash
echo b > /proc/sysrq-trigger
```

This forces an immediate reboot. Only use this when the system is truly hung and unresponsive to normal commands. Be aware that this skips filesystem sync and can cause data loss.

To check if SysRq is enabled:

``` bash
cat /proc/sys/kernel/sysrq
```

A value of `1` means it’s fully enabled. A value of `0` means it’s disabled for security.

## Practical Workflow

1.  **Identify what’s using the filesystem**: `lsof +D /mnt/data` or `fuser -v /mnt/data`
2.  **Stop services cleanly**: `systemctl stop myservice` or gracefully kill processes with `kill <PID>`
3.  **Try remounting if you just need to change options**: `mount -o remount /mnt/data`
4.  **Verify processes are gone**: `lsof +D /mnt/data` should return nothing
5.  **Attempt normal unmount**: `umount /mnt/data`
6.  **Use lazy unmount for unresponsive or NFS mounts**: `umount -l /mnt/data`
7.  **Force unmount only as absolute last resort**: `umount -f /mnt/data`
8.  **Document why lazy or force unmounting was required** — it usually indicates a configuration or service shutdown issue worth fixing

The majority of “device is busy” problems can be solved with `lsof`, cleanly stopping services, and a lazy unmount if needed. Jumping to force unmount is almost always wrong and indicates you need to investigate your service shutdown procedures.
