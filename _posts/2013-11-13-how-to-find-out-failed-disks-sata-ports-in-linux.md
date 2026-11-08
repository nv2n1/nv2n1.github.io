---
title: "Map Failed Disks to Physical SATA Ports in Linux"
date: 2013-11-13 12:28:17 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-out-failed-disks-sata-ports-in-linux/
---

Linux device names like `/dev/sda` and `/dev/sdb` are unreliable identifiers for physical hardware. They shift when you add, remove, or reseat drives, and there’s no guaranteed mapping between a SATA port and its device name. When a disk fails, you need to know exactly which physical slot to replace—guessing wrong takes down the wrong system.

## Get the Serial Number

Every disk has a unique serial number stored in firmware and printed on the label. This is your anchor point for reliable identification.

Query it with `hdparm`:

``` bash
sudo hdparm -i /dev/sdb | grep SerialNo
SerialNo=5VP5DYYY
```

If `hdparm` isn’t installed:

``` bash
# Debian/Ubuntu
sudo apt install hdparm

# RHEL/CentOS/Fedora
sudo dnf install hdparm
```

Alternative tools to get serial numbers:

``` bash
# Using smartctl (from smartmontools)
sudo smartctl -i /dev/sdb | grep Serial

# Using lsblk to list all devices with serials
lsblk -o NAME,SERIAL,SIZE

# Direct sysfs query
cat /sys/block/sdb/device/serial
```

## Find the SATA Port

Once you’ve identified the device name, map it to a physical port using sysfs and ATA information:

``` bash
# Check ATA port assignment
readlink /sys/block/sda/device
# Output example: ../../devices/pci0000:00/0000:00:1f.2/ata1/host0/target0:0:0/0:0:0:0

# This shows the drive is on ata1 (SATA port 1)
```

For a clearer picture of the hardware hierarchy:

``` bash
# Get transport type and detailed mapping
lsblk -o NAME,SERIAL,SIZE,TRAN
```

Use `lshw` for complete slot information:

``` bash
sudo lshw -C disk -businfo
# Output shows Bus info, Device, and logical name mappings
```

On servers with port multipliers or expanders, you may need to check:

``` bash
# List all ATA channels and attached devices
cat /proc/scsi/scsi
ls -la /sys/class/scsi_device/
```

## Verify with SMART Before Replacement

Before assuming a disk has failed, confirm it with S.M.A.R.T. status:

``` bash
# Install smartmontools
sudo apt install smartmontools  # Debian/Ubuntu
sudo dnf install smartmontools  # RHEL/CentOS/Fedora

# Check overall health status
sudo smartctl -H /dev/sdb

# Get full report including error log
sudo smartctl -a /dev/sdb

# Check specific attributes for wear/errors
sudo smartctl -A /dev/sdb | grep -E "Reallocated_Sector_Ct|Current_Pending_Sector"
```

A failing disk typically shows increased reallocated sectors, pending sectors, or offline uncorrectable errors. If SMART reports healthy but you see kernel errors, the drive may be failing in ways SMART doesn’t detect—replace it anyway.

## Enable Proactive Monitoring

Don’t wait for complete failure. Configure `smartd` to monitor all drives:

``` bash
sudo systemctl enable smartd
sudo systemctl start smartd
```

Edit `/etc/smartd.conf` to enable email alerts:

``` bash
/dev/sda -a -m root -M exec /usr/libexec/smartmontools/smartdnotify
/dev/sdb -a -m root -M exec /usr/libexec/smartmontools/smartdnotify
/dev/sdc -a -m root -M exec /usr/libexec/smartmontools/smartdnotify
```

This catches degrading disks before they fail completely.

## Use UUIDs, Not Device Names

Stop relying on device names in `/etc/fstab` and bootloader configs. They’re too fragile.

Get UUIDs for all filesystems:

``` bash
blkid
lsblk -o NAME,UUID,FSTYPE
```

Update `/etc/fstab` to use UUIDs:

``` bash
# Before (unreliable)
/dev/sdb1  /data  ext4  defaults  0  2

# After (reliable)
UUID=c4eccd0b-8fa7-4efc-b8a7-3e5b0e3e4f2a  /data  ext4  defaults,nofail  0  2
```

The `nofail` option prevents boot hangs if a drive is missing or failed. Update GRUB to use UUIDs:

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

## Complete Workflow for Failed Disk Replacement

1.  **Check kernel logs for errors:**

    ``` bash
    dmesg | grep -i "ata.*error\|disk.*error\|i/o error"
    journalctl -u kernel -p err
    ```

2.  **Identify the failed device and get its serial number:**

    ``` bash
    sudo smartctl -a /dev/sdX
    sudo hdparm -i /dev/sdX | grep SerialNo
    ```

3.  **Confirm failure with SMART:**

    ``` bash
    sudo smartctl -H /dev/sdX
    ```

4.  **Find its physical SATA port:**

    ``` bash
    readlink /sys/block/sdX/device
    lsblk -o NAME,SERIAL,SIZE,TRAN | grep sdX
    ```

5.  **Physically locate and replace the drive** using the serial number and SATA port information.

6.  **After installing the replacement, verify it’s healthy:**

    ``` bash
    # Rescan to detect the new drive
    echo "- - -" | sudo tee /sys/class/scsi_host/host*/scan
    sudo smartctl -H /dev/sdX
    sudo smartctl -a /dev/sdX
    ```

7.  **If RAID/LVM: rebuild the array:**

    ``` bash
    # For mdraid
    sudo mdadm --manage /dev/md0 --add /dev/sdX1

    # For LVM
    sudo pvresize /dev/sdX1
    ```

Using serial numbers and sysfs-based port detection works reliably regardless of controller type, drive count, or system configuration.
