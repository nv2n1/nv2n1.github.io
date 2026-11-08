---
title: "How to Force fsck on Next Linux Reboot"
date: 2018-03-24 11:54:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-force-a-fsck-during-next-rebooting-of-linux/
---

Filesystem corruption occasionally happens. When it does, you need fsck to run before the system fully mounts its filesystems. Here’s how to force a filesystem check during the next boot.

### Using touch to Mark Filesystems

The traditional method is to create `/forcefsck`:

``` bash
sudo touch /forcefsck
sudo reboot
```

On the next boot, the system will check all filesystems marked for checking before they’re mounted read-write. The file is automatically removed after the check completes.

This works on most systemd-based distributions. Some older systems that still use SysVinit may require `/fastboot` to be absent for this to work reliably.

### Using systemctl (Systemd)

For modern distributions, you can use systemctl to schedule a filesystem check:

``` bash
sudo systemctl start systemd-fsck-root.service
```

However, this is typically for the root filesystem and requires the system to be in a specific state. A more reliable approach for scheduling a check on next boot is still the `/forcefsck` method.

### Forcing fsck on Specific Filesystems

To force a check on non-root filesystems, you can modify `/etc/fstab`. The last column (sixth field) is the `pass` number. Set it to a non-zero value:

    /dev/sda2  /home  ext4  defaults  0  2

Here, `2` means the filesystem will be checked after the root filesystem. Use `1` for the root filesystem, `2` for others, and `0` to skip checks entirely.

After modifying `/etc/fstab`, reboot:

``` bash
sudo reboot
```

### Manual fsck Without Reboot

If you need to check a filesystem immediately and it’s not currently mounted, you can run fsck directly:

``` bash
sudo fsck /dev/sda2
```

For ext4 filesystems specifically:

``` bash
sudo e2fsck -f /dev/sda2
```

The `-f` flag forces a check even if the filesystem appears clean. **Do not run fsck on mounted filesystems** — this will cause corruption. Unmount first:

``` bash
sudo umount /dev/sda2
sudo e2fsck -f /dev/sda2
```

### Checking Root Filesystem in Read-Only Mode

If you suspect corruption on the root filesystem but can’t unmount it, you can boot into single-user mode and run fsck with the filesystem mounted read-only:

1.  Reboot and interrupt the bootloader (usually by holding Shift or Esc during startup)
2.  Add `single` or `rd.break` to your kernel parameters
3.  Once in single-user mode, the root filesystem is typically mounted read-only
4.  Run `fsck /` to check it
5.  Reboot normally

### Verifying Filesystem Health

Before forcing a full fsck, check the filesystem’s status:

``` bash
sudo tune2fs -l /dev/sda2 | grep "Filesystem state"
```

You can also view the current mount count and max mount count:

``` bash
sudo dumpe2fs /dev/sda2 | grep -i "mount count"
```

To set fsck to run automatically after N mounts:

``` bash
sudo tune2fs -c 50 /dev/sda2
```

This forces a check every 50 mounts. Set to `-1` to disable mount-based checks:

``` bash
sudo tune2fs -c -1 /dev/sda2
```

### Modern Considerations

Btrfs and XFS have different approaches. Btrfs includes built-in repair capabilities and self-healing via RAID profiles, while XFS typically requires `xfs_repair` run offline. Always check your specific filesystem’s documentation.

For systems using LVM or LUKS encryption, ensure the underlying block devices are checked, not the logical volumes directly. Run fsck after decryption but before mounting.

Journaling filesystems like ext4, XFS, and Btrfs can usually recover from crashes automatically on mount. However, persistent I/O errors or genuine corruption may still require a manual check. Always have backups before forcing filesystem repairs, especially in production environments.
