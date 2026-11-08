---
title: "Creating, Mounting, and Burning ISO Images on Linux"
date: 2013-07-12 16:31:29 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/mount-create-burn-iso-linux/
---

Mounting an ISO on Linux requires a loop device. Modern systems support this directly with `mount`:

``` bash
sudo mount -o loop /path/to/image.iso /mnt/mount-point
```

Or use the `-t iso9660` option for explicit filesystem specification:

``` bash
sudo mount -t iso9660 -o loop /path/to/image.iso /mnt/mount-point
```

To unmount:

``` bash
sudo umount /mnt/mount-point
```

For temporary mounts that don’t require persistence across reboots, consider using `udisksctl` instead:

``` bash
udisksctl loop-setup -f /path/to/image.iso
udisksctl mount -b /dev/loop0
```

This manages loop devices automatically and cleans up when done.

## Create an ISO image

`xorriso` is the modern replacement for `genisoimage` and `mkisofs`. It’s better maintained and handles edge cases more reliably:

``` bash
xorriso -as mkisofs -R -J -joliet-long -iso-level 4 -o image.iso /path/to/directory/
```

For directories with files larger than 4GB, UDF support is usually preferable to the deprecated `-allow-limited-size`:

``` bash
xorriso -as mkisofs -R -J -udf -iso-level 4 -o image.iso /path/to/directory/
```

Key options:

- `-R`: Rock Ridge extensions for long filenames and Unix attributes
- `-J`: Joliet extensions for Windows compatibility
- `-joliet-long`: Allow longer Joliet names (up to 103 characters)
- `-udf`: Universal Disk Format for large file support
- `-iso-level 4`: ISO 9660 level 4 (supports files up to 4GB per file, unlimited total)

To create a hybrid ISO that boots from both CD and USB:

``` bash
xorriso -as mkisofs -R -J -isohybrid-mbr /usr/lib/ISOLINUX/isohdpfx.bin \
  -c boot.cat -b isolinux.bin -no-emul-boot -boot-load-size 4 \
  -boot-info-table -o image.iso /path/to/directory/
```

## Burn ISO to optical media

`wodim` (the maintained fork of `cdrecord`) still works but is rarely necessary on modern systems. For USB media, `dd` or `ddrescue` is the standard:

``` bash
sudo dd if=image.iso of=/dev/sdX bs=4M status=progress
sudo sync
```

**Warning**: Verify the target device with `lsblk` before using `dd`. Wrong device selection causes data loss.

For more reliable writes with automatic retry and error handling:

``` bash
sudo ddrescue -D --force image.iso /dev/sdX
```

For CD/DVD burning, if you still have optical drives, use `wodim`:

``` bash
# List available devices
wodim --devices

# Burn with verbose output
sudo wodim -v dev='/dev/sr0' image.iso
```

Common options:

- `-v`: Verbose output
- `-driveropts=burnfree`: Enable buffer underrun protection
- `-speed=4`: Set burn speed (adjust based on media and drive capability)

## Verify images

After creating or burning, verify image integrity:

``` bash
# Check ISO against original source files
sha256sum image.iso > image.iso.sha256
sha256sum -c image.iso.sha256

# Verify burned USB/optical media
sudo dd if=/dev/sdX bs=4M status=progress | sha256sum
```

Compare the hash with the original image file to ensure the write completed successfully.

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
