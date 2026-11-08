---
title: "Creating ISO Images from DVDs on Linux"
date: 2013-07-12 16:31:42 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /create-iso-image-on-linux/
---

ISO images are sector-by-sector copies of optical media stored as binary files. They’re useful for archiving DVDs or creating portable copies without keeping physical disks around. On Linux, several tools can accomplish this—`dd` is the simplest, but modern alternatives offer better features.

## Using dd to Create an ISO Image

The most straightforward approach uses `dd`:

``` bash
sudo dd if=/dev/sr0 of=/path/to/store/image.iso bs=8192 status=progress
```

Or with the symlinked device:

``` bash
sudo dd if=/dev/cdrom of=/path/to/store/image.iso bs=8192 status=progress
```

The `status=progress` flag displays transfer speed and remaining time—helpful for large DVDs. On most modern distributions, `/dev/cdrom` symlinks to `/dev/sr0`, but verify with `ls -l /dev/cdrom`.

**Block size note:** The `bs=8192` setting reads data in 8KB chunks, balancing speed and buffer usage. You can increase to `bs=32768` on systems with ample RAM for faster transfers on modern hardware.

The process reads the entire disc sequentially, so expect 5-15 minutes for a full 4.7GB DVD depending on drive speed and system load.

## Using ddrescue for Better Error Handling

For DVDs with read errors or degraded media, `ddrescue` is superior to `dd`:

``` bash
sudo ddrescue -D --force /dev/sr0 image.iso image.log
```

`ddrescue` maps bad sectors, attempts recovery multiple times, and logs the process. The `--force` flag skips permission checks. The `.log` file tracks which sectors failed, useful for verification.

Install it on Debian/Ubuntu with `sudo apt install gddrescue` or on Fedora/RHEL with `sudo dnf install ddrescue`.

## Using ffmpeg for Video DVDs

If you’re working with video DVDs and need to extract VOB files or convert on-the-fly, `ffmpeg` is more flexible than raw ISO creation:

``` bash
ffmpeg -i dvd:///dev/sr0 -c copy output.mpg
```

This bypasses ISO creation entirely and outputs MPEG directly. Useful if you don’t need the ISO format.

## Mounting and Accessing ISO Images

Once created, mount the ISO to browse or extract files:

``` bash
sudo mount -o loop,ro /path/to/store/image.iso /mnt/dvd
```

The `-o ro` flag mounts read-only, preventing accidental modifications. List contents:

``` bash
ls -la /mnt/dvd
```

For tools like VLC or archive managers, you can often double-click the ISO in your file manager to auto-mount it.

Unmount when finished:

``` bash
sudo umount /mnt/dvd
```

If the umount fails with “target is busy,” check what’s accessing it:

``` bash
lsof /mnt/dvd
```

Kill blocking processes or change to a different directory before retrying.

## Verifying ISO Integrity

After creation, verify the ISO matches the physical disc. Calculate checksums:

``` bash
sudo md5sum /dev/sr0 > dvd.md5
md5sum image.iso >> dvd.md5
diff dvd.md5
```

For faster verification without checksumming, compare file sizes:

``` bash
blockdev --getsize64 /dev/sr0
ls -lh image.iso
```

Both should match in bytes.

## Practical Tips

- **Disable automount:** Some desktops auto-mount inserted discs. Disable this in your file manager settings before `dd` to avoid read conflicts.
- **Device name variations:** On some systems, DVD drives appear as `/dev/sr0`, `/dev/scd0`, or `/dev/hdc` (older IDE drives). Use `lsblk` to identify your drive.
- **Permissions:** Always use `sudo` for device reads to avoid permission errors.
- **Large ISOs:** For dual-layer DVDs (8.5GB), ensure your filesystem supports files larger than 4GB (ext4, NTFS, exFAT do; older FAT32 doesn’t).
- **Storage planning:** A full DVD requires 4.7GB; dual-layer requires 8.5GB. Account for this before starting.

## When to Use Each Tool

| Tool             | Best For                                      |
|------------------|-----------------------------------------------|
| `dd`             | Fast, simple ISO creation from clean discs    |
| `ddrescue`       | Damaged media or sectors with read errors     |
| `ffmpeg`         | Video DVD extraction without ISO intermediate |
| File Manager GUI | One-off mounting without terminal use         |

Choose `dd` for routine archiving. Use `ddrescue` if the disc is visibly damaged or shows read errors during the first attempt. Both create proper ISO files compatible with any Linux distribution or other operating systems.
