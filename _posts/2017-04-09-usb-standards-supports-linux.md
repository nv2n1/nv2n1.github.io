---
title: "USB Standards in Linux: Speeds and Driver Troubleshooting"
date: 2017-04-09 06:36:31 +0000
layout: post
canonical: https://www.systutorials.com/usb-standards-supports-linux/
---

USB technology continues evolving with each generation delivering significant speed improvements. Linux provides comprehensive kernel support across all modern standards through dedicated drivers.

### USB 2.0

**Speed:** 480 Mbps (theoretical ~60 MB/s)

**Status:** Legacy but still common. Nearly all systems retain USB 2.0 ports for backward compatibility.

**Linux support:** Built-in via the `ehci-hcd` driver in all modern kernels.

### USB 3.0 (SuperSpeed)

**Speed:** 5 Gbps (theoretical ~625 MB/s; real-world 200–400 MB/s depending on device quality and controller implementation)

**Status:** Widely deployed since ~2012.

**Linux support:** Integrated since kernel 2.6.31 via the `xhci-hcd` driver. Fully stable across all current distributions.

### USB 3.1 (SuperSpeed+)

**Speed:** 10 Gbps (Gen 2)

**Status:** Common on newer server motherboards and consumer hardware since 2015.

**Linux support:** Supported since kernel 4.6. All maintained distributions include full support.

### USB 3.2 (SuperSpeed+)

**Speed:** 20 Gbps (Gen 2×2 over Type-C)

**Status:** Increasingly common on recent workstations, servers, and high-end laptops.

**Linux support:** Supported in kernel 5.9+.

### USB4 and Thunderbolt

**Speed:** 40 Gbps (USB4), up to 120 Gbps (Thunderbolt 4)

**Status:** Available on high-end workstations and premium laptops.

**Linux support:** Supported since kernel 5.6 via the `tb_xhci` driver. Some distributions may require firmware updates for optimal hardware support.

## Identifying USB Versions

USB version can often be identified visually by connector color, though this isn’t always reliable:

| Standard | Connector Color | Notes |
|----|----|----|
| USB 2.0 | Black interior | Legacy |
| USB 3.0/3.1 Gen 1 | Blue interior | Type-A only |
| USB 3.1 Gen 2 | Red interior | Type-A only, often labeled “SuperSpeed+” |
| USB 3.2 | Teal interior | Type-A, rare in practice |
| USB-C | Flat, reversible | Can carry any USB 3.x or USB4 standard |

**Always verify against device specifications and labeling rather than relying solely on connector color.**

## Checking Your System’s USB Capabilities

### List USB Controllers and Devices

List all connected USB devices:

``` bash
lsusb
```

Get detailed host controller information:

``` bash
lspci | grep -i usb
```

Example output from a modern system:

    00:14.0 USB controller: Intel Corporation Meteor Lake xHCI Host Controller
    02:00.0 USB controller: Realtek Semiconductor Co., Ltd. RTL8153 Gigabit Ethernet Adapter

### Check Kernel Boot Messages

View USB driver initialization:

``` bash
dmesg | grep -E "xhci|ehci|usb"
```

Example output:

    [    0.491877] xhci_hcd 0000:00:14.0: xHCI Host Controller
    [    0.491899] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 1
    [    0.501360] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver

### List Connected Devices with Speeds

Get verbose information on all devices:

``` bash
lsusb -v
```

View devices organized by bus hierarchy with speed info:

``` bash
lsusb -tv
```

Example tree view:

    /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/16p, 20000M
        |__ Port 1: Dev 2, If 0, Class=Mass Storage, Driver=usb-storage, 5000M
        |__ Port 5: Dev 3, If 0, Class=Wireless, Driver=bluetooth, 480M

Check a specific device’s negotiated speed:

``` bash
lsusb -v -d 0951:1666 | grep -A 2 "bcdUSB"
```

Substitute the vendor and product IDs for your device (found via `lsusb`).

### Verify Driver Status

Confirm the xHCI driver is loaded:

``` bash
lsmod | grep xhci
```

Expected output:

    xhci_pci               20480  0
    xhci_hcd              249856  1 xhci_pci
    usbcore               286720  5 xhci_hcd,xhci_pci,usbfs,usbhid

Check active quirk parameters applied to specific problematic devices:

``` bash
cat /sys/module/xhci_hcd/parameters/
```

### Check Your Kernel Version

``` bash
uname -r
```

Modern distributions ship with kernels that support all current USB standards:

- **RHEL/Rocky 9.x:** Kernel 5.14+
- **Ubuntu 24.04 LTS:** Kernel 6.8+
- **Fedora 41+:** Kernel 6.10+
- **Debian 12+:** Kernel 6.1+

All support USB 3.0, 3.1, and 3.2. USB4 and Thunderbolt support is present in all maintained releases.

## Monitoring USB Activity

### Real-Time USB Traffic

Load the USB monitor module if not already loaded:

``` bash
sudo modprobe usbmon
```

Capture USB traffic on a specific bus (e.g., bus 1):

``` bash
sudo cat /sys/kernel/debug/usb/usbmon/1u
```

The output shows URB (USB Request Block) events in real-time. Format:

    ffff880048f04980 1234567890 S Ii:1:001:1 -115 4 = 01020304

Fields represent timestamp, event type, direction, endpoint, status, and data.

### Packet-Level Analysis with Wireshark

For detailed protocol analysis:

``` bash
sudo wireshark
```

Select `usbmon0` (or similar) as the capture interface. This reveals USB protocol details for debugging device behavior or analyzing communication issues.

## Troubleshooting USB Issues

### Device Not Recognized or Operating at Wrong Speed

Check kernel messages for errors:

``` bash
dmesg | tail -100 | grep -i usb
```

Look for messages indicating speed negotiation problems:

    usb 2-1: new high-speed USB device number 5 ports 1
    usb 2-1: device descriptor read/64, error -110
    usb 2-1: reset high-speed USB device using xhci_hcd and address 5

These indicate the device negotiated at an incorrect speed or encountered communication errors.

### Verify the Correct Driver Handles the Device

Check what driver is actually handling the device:

``` bash
lsusb -v -d <vendor>:<product> | grep -i "maxpacket\|speed"
```

For more human-readable output:

``` bash
usb-devices | grep -A 20 "Vendor=xxxx ProdID=yyyy"
```

Replace the vendor and product IDs with values from your `lsusb` output.

### Check for Known Kernel Quirks

Modern kernels include USB chipset-specific workarounds. If a device has issues, search the kernel source for your chipset:

``` bash
grep -r "USB_QUIRK" /usr/src/linux*/drivers/usb/ | grep -i "<device_name>"
```

Common quirks and their effects:

- `USB_QUIRK_DELAY_INIT`: Device requires initialization delay before use
- `USB_QUIRK_STRING_DELAY`: Device needs delay before reading string descriptors
- `USB_QUIRK_NO_LPM`: Disable Link Power Management (problematic on some devices)
- `USB_QUIRK_NO_AUTOSUSPEND`: Prevent automatic device suspension (causes issues on unreliable devices)

### Update Firmware

Older server BIOS versions may have incomplete or buggy xHCI implementations. Firmware updates often resolve speed negotiation issues:

1.  Check your motherboard manufacturer’s support page for BIOS/firmware updates
2.  Download the firmware file
3.  Flash via BIOS menu (typically F2, Del, or F12 at boot—check your system’s prompt)
4.  Reboot and verify with `dmesg | grep xhci` that initialization messages have changed

### Test with Different Port

Some ports connect to different controllers or have different electrical properties. Try moving the device to another USB port:

``` bash
lspci -v | grep -A 10 "USB controller"
```

This shows which physical ports attach to each host controller. If the device works on one port but not another, the issue likely stems from a specific controller.

### Disable Power Management

USB devices can be suspended to save power, causing recognition issues. Disable autosuspend for a specific device:

``` bash
echo -1 > /sys/bus/usb/devices/<device>/power/autosuspend_delay_ms
```

Replace `<device>` with the device name (e.g., `1-1` for port 1 on bus 1).

To make this permanent across reboots:

``` bash
echo "options usbcore autosuspend=-1" | sudo tee /etc/modprobe.d/usb-autosuspend.conf
```

Then regenerate initramfs and reboot:

``` bash
sudo update-initramfs -u
sudo reboot
```

On Red Hat systems, use `dracut -f` instead of `update-initramfs`.

## Performance Optimization

### Real-World Speed Expectations

Actual USB speeds are typically 60–80% of theoretical maximum due to protocol overhead and device limitations:

- **USB 3.0:** Expect 300–500 MB/s sustained with quality external SSDs
- **USB 3.1 Gen 2:** Expect 600–1000+ MB/s with proper devices
- **USB 3.2:** Expect 1500+ MB/s (varies heavily with device firmware)

### Enable UAS for Storage Devices

UAS (USB Attached SCSI) provides better performance and lower CPU overhead than bulk-only transfers for storage devices. Check if your device supports UAS:

``` bash
lsusb -v -d <vendor>:<product> | grep -i "class.*storage\|bInterfaceClass"
```

If available but not enabled by default, force UAS:

``` bash
echo "options usb-storage quirks=<vendorid>:<productid>:u" | sudo tee /etc/modprobe.d/usb-storage-uas.conf
```

Substitute actual vendor and product IDs (use colon as separator, e.g., `0951:1666`).

Reload the module:

``` bash
sudo modprobe -r usb-storage && sudo modprobe usb-storage
```

### Monitor Actual Throughput

Check real-time read/write bandwidth while transferring files:

``` bash
iostat -x 1 | grep -E "sdb|avg"
```

This shows device I/O statistics updated every second. Look at `r_await` and `w_await` (latency) to identify bottlenecks.

For more detailed per-device stats:

``` bash
iotop -o
```

This shows which processes are responsible for I/O, useful for identifying when devices are actually at fault versus application issues.
