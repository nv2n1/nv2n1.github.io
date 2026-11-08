---
title: "Forcefully Unmount a Busy Filesystem in Linux"
date: 2018-03-24 11:49:51 +0000
layout: post
canonical: https://www.systutorials.com/how-do-i-force-linux-to-unmount-a-filesystem/
---

When you try to unmount a filesystem, Linux sometimes refuses with a “device is busy” error. This safety mechanism prevents data loss when processes are actively using the filesystem. But there are legitimate cases where you need to force an unmount: a dead NFS server, a failed USB device, or a hung mount that won’t recover.

## Understanding the “device is busy” error

Before forcing anything, it’s worth knowing what’s holding the filesystem open. Use `lsof` to list open files on a specific mount:

``` bash
lsof /mnt/point
```

Or use `fuser` to find processes using a directory:

``` bash
fuser -m /mnt/point
```

This tells you which PIDs are keeping the filesystem busy. You might be able to simply kill those processes and unmount cleanly.

## Lazy unmount with -l flag

The safest forced unmount is a *lazy* unmount using the `-l` flag:

``` bash
umount -l /mnt/point
```

This detaches the filesystem from the namespace immediately, so the mount point becomes inaccessible. However, the actual cleanup happens later when all processes release their references. It’s especially useful for NFS mounts and removable media where you need immediate removal but aren’t concerned about lingering cleanup.

## Force unmount with -f flag

For filesystems that are completely unresponsive (like a dead NFS server), use the `-f` flag:

``` bash
umount -f /mnt/point
```

This tells the kernel to forcefully unmount the filesystem without waiting for processes to close files. The behavior depends on the filesystem type — some filesystems ignore this flag entirely.

## Combining flags

You can combine both flags for maximum force:

``` bash
umount -fl /mnt/point
```

This does a lazy unmount and also sends a force signal. It’s useful when a mount is completely hung.

## Unmounting from a different namespace

If the mount is in another container or namespace, you need to enter that namespace first. For a container:

``` bash
nsenter -t <pid> -m umount /mnt/point
```

Or for systemd containers:

``` bash
machinectl shell container-name /bin/bash
umount /mnt/point
```

## Killing processes holding the mount

If you identify specific processes preventing unmount, you can terminate them first:

``` bash
fuser -km /mnt/point
```

The `-k` flag kills all processes accessing that mount. The `-m` flag specifically targets the mount. Be careful — this will terminate whatever is using the filesystem.

## Dealing with rootfs and system mounts

If you’re trying to unmount the root filesystem or a critical system mount, you’re fighting the kernel itself. In these cases:

- Boot into a live USB or recovery mode
- Use `remount,ro` to make the filesystem read-only instead
- Consider using `mount --bind` to redirect the mount point

``` bash
mount -o remount,ro /
```

A read-only root filesystem is safer than a hung one and won’t prevent system shutdown.

## NFS-specific issues

For dead NFS mounts, lazy unmount is your best friend:

``` bash
umount -l /mnt/nfs
```

If that doesn’t work, you may need to restart the NFS client service:

``` bash
systemctl restart nfs-client.target
```

Then retry the unmount. If the NFS server is truly unreachable, a lazy unmount with `-l` is your only option.

## Preventing busy filesystems in the future

Set mount options that prevent this issue:

``` bash
mount -o soft,timeo=10,retrans=3 server:/export /mnt/point
```

The `soft` option tells NFS to fail quickly instead of hanging indefinitely. Lower timeout values (`timeo`) and retry counts (`retrans`) prevent the kernel from holding onto the mount too long.

Use `-t` flag with `umount` to specify filesystem type if the kernel has trouble detecting it, particularly with older or exotic filesystem types.
