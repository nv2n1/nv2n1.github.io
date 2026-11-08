---
title: "Detecting USB Devices on Remote Linux Servers via SSH"
date: 2018-03-24 11:45:47 +0000
modified: 2026-04-11 15:56:25 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-check-whether-a-usb-disk-is-connected-to-a-linux-server/
---

When you’re managing a Linux server remotely over SSH, determining whether a USB drive has been connected requires checking kernel messages and device listings since you can’t visually inspect the hardware.

## Check dmesg for USB Detection Events

The most reliable method is examining kernel logs with `dmesg`. When a USB device is detected, the kernel logs detailed information about the connection:

``` bash
dmesg | tail -50
```

Look for messages containing USB device information. A typical USB storage device will produce output like:

    [ 3131.583934] usb 2-2: new high-speed USB device number 2 using ehci-hcd
    [ 3131.698846] usb 2-2: New USB device found, idVendor=152d, idProduct=0539
    [ 3131.698850] usb 2-2: New USB device strings: Mfr=10, Product=11, SerialNumber=5
    [ 3131.698854] usb 2-2: Product: USB to ATA/ATAPI Bridge
    [ 3131.698856] usb 2-2: Manufacturer: JMicron
    [ 3132.756095] scsi 4:0:0:0: Direct-Access ORICO H/W RAID0 0X06 PQ: 0 ANSI: 6
    [ 3132.758101] sd 4:0:0:0: [sde] Very big device. Trying to use READ CAPACITY(16).
    [ 3132.758433] sd 4:0:0:0: [sde] 11720785920 512-byte logical blocks: (6.00 TB/5.45 TiB)
    [ 3132.859257] sde: sde1
    [ 3132.862826] sd 4:0:0:0: Attached SCSI disk

The key indicators are:

- `new high-speed USB device` — device detected
- `[sdX]` — the block device assigned (sde, sdf, etc.)
- Partition information like `sde1` — partitions found on the device
- Capacity information — useful for identifying the correct device

Filter for recent USB events specifically:

``` bash
dmesg | grep -i "usb\|scsi.*disk" | tail -20
```

## List Block Devices

Check what block devices are currently attached using `lsblk`, which provides a clean tree view:

``` bash
lsblk
```

Output shows something like:

    NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
    sda      8:0    0  238G  0 disk
    ├─sda1   8:1    0  512M  0 part /boot
    └─sda2   8:2    0 237.5G  0 part /
    sdb      8:16   0  500G  0 disk
    sde      8:64   1  6.0T  0 disk  ← newly connected USB
    └─sde1   8:65   1  6.0T  0 part

The `RM` column shows whether a device is removable (1 = removable, 0 = fixed). This is the clearest way to identify USB drives.

Alternatively, use the lower-level `ls` command:

``` bash
ls -l /dev/sd*
```

Compare the output to your previous baseline to identify new devices.

## Combine Both Methods for Reliability

For the most complete picture, run both checks together:

``` bash
echo "=== Recent USB/SCSI Events ===" && dmesg | grep -i "usb\|scsi.*disk" | tail -10
echo "" && echo "=== Current Block Devices ===" && lsblk -o NAME,SIZE,TYPE,RM,MOUNTPOINT
```

This shows both the detection timeline and current device state. The combination reveals whether a device was detected recently and if it’s properly initialized.

## Identify Specific USB Device Details

For more granular information about USB devices, use `lsusb`:

``` bash
lsusb
```

This lists all USB devices on the bus but doesn’t directly show which device file they’re mapped to. However, combine it with device properties:

``` bash
udevadm info -q path -n /dev/sde
```

This shows the physical USB path and additional device metadata, useful for identifying a specific drive if multiple USB devices are connected.

## Monitor for Real-Time USB Connection

If you need to watch for USB devices being connected in real-time:

``` bash
while true; do lsblk -o NAME,SIZE,RM; sleep 5; done
```

Or use `inotifywait` on `/dev`:

``` bash
inotifywait -m /dev -e create 2>/dev/null | grep -E "sd[a-z]"
```

This blocks until a new device appears, making it useful for automation scripts.

## Practical Tips

- Always run `lsblk` before and after USB insertion to clearly identify the new device
- On multi-USB systems with many devices, use `dmesg` to correlate device insertion time with the block device assignment
- The `RM` flag in `lsblk` is definitive for identifying removable media — don’t rely on device naming alone
- Never assume a device based on naming; always verify size and other properties match your expectations
- If the USB device doesn’t appear after 10-15 seconds, check `dmesg` for errors like “device not responding” or “reset failed”
