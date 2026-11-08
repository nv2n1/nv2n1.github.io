---
title: "Formatting DVD+RW and DVD-RW Disks on Linux"
date: 2013-07-12 16:32:30 +0000
layout: post
canonical: https://www.systutorials.com/linux-format-erase-dvdrw-disks/
---

Start by identifying your optical drive device. List your CD/DVD drives:

``` bash
ls -l /dev/cdrom
```

This typically shows a symlink to your actual device:

    lrwxrwxrwx. 1 root root 3 Aug  1 17:00 /dev/cdrom -> sr0

You can also check active optical drives with `lsblk`:

``` bash
lsblk | grep -i rom
```

Modern systems may use `/dev/sr0`, `/dev/sr1`, etc. If you have multiple drives, insert your media and use `dmesg` to see which device it’s mounted to:

``` bash
dmesg | tail -20
```

## Formatting DVD+RW Media

Install the dvd+rw-tools package. On Debian/Ubuntu systems:

``` bash
sudo apt install dvd+rw-tools
```

On RHEL/CentOS/Fedora:

``` bash
sudo dnf install dvd+rw-tools
```

Insert your DVD+RW disk and format it:

``` bash
sudo dvd+rw-format -force /dev/sr0
```

The `-force` flag bypasses the confirmation prompt. Without it, you’ll be asked to confirm before erasing:

``` bash
sudo dvd+rw-format /dev/sr0
```

You can also use growisofs, which is part of the same package, for a quicker blank without full formatting:

``` bash
sudo growisofs -Z /dev/sr0=/dev/zero
```

This zero-fills the disk, which is faster for quick rewrites.

## Formatting DVD-RW Media

DVD-RW disks (write-once variant) format differently than DVD+RW. Use dvd+rw-format with the `-blank` option:

``` bash
sudo dvd+rw-format -blank /dev/sr0
```

For a faster blank that only clears the first few sectors:

``` bash
sudo dvd+rw-format -blank=fast /dev/sr0
```

## Erasing CD+RW Media

For CD+RW disks, use `wodim` (the successor to cdrecord):

``` bash
sudo apt install wodim
sudo wodim dev=/dev/sr0 blank=fast
```

For a complete erase of CD+RW:

``` bash
sudo wodim dev=/dev/sr0 blank=all
```

The `blank=fast` option only clears the table of contents and is much quicker than a full erase.

## Checking Disk Status

Before formatting, check your disk status with `dvd+rw-format` in read mode:

``` bash
sudo dvd+rw-format -info /dev/sr0
```

This shows the disk type, current capacity, and whether it’s blank or has data.

## Common Issues

**Permission Denied**: Use `sudo` or add your user to the `cdrom` group:

``` bash
sudo usermod -aG cdrom $USER
```

You’ll need to log out and back in for group membership to take effect.

**Device Busy**: Unmount the disk first if the system auto-mounted it:

``` bash
sudo umount /dev/sr0
```

**No Disk Detected**: Ensure the disk is fully inserted and the drive is powered. Try ejecting and reinserting:

``` bash
sudo eject /dev/sr0
```

**Stale Device Symlink**: If `/dev/cdrom` points to the wrong device, check `/dev/sr*` directly or reload the kernel module:

``` bash
sudo modprobe -r sr_mod
sudo modprobe sr_mod
```

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
