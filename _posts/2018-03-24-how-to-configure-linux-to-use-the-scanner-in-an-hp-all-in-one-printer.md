---
title: "Setting Up HP Scanner on Linux with SANE"
date: 2018-03-24 11:48:01 +0000
modified: 2026-04-11 15:53:53 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-linux-to-use-the-scanner-in-an-hp-all-in-one-printer/
---

Once your HP printer is working on a Linux system, enabling the scanner requires installing SANE (Scanner Access Now Easy) and HP-specific backends. If wireless connectivity is already established for printing, the scanner should be discoverable on the same network.

## Install Required Packages

On Fedora:

``` bash
sudo dnf install sane-backends sane-backends-devel hplip hplip-common
```

On Ubuntu/Debian:

``` bash
sudo apt install sane-backends sane-utils hplip
```

The `hplip` package includes HP device drivers and utilities for both printing and scanning. `sane-backends` provides the core scanning framework.

## Verify Scanner Detection

Check if your device is recognized:

``` bash
sudo scanimage -L
```

This lists all detected scanners. If your HP device appears with a valid URI (like `hp:/net/...`), move to the next step. If nothing appears, your device may not be on the network or SANE doesn’t have permissions yet.

## Configure SANE Permissions

SANE requires proper permissions to access USB and network devices. Add your user to the `scanner` group:

``` bash
sudo usermod -aG scanner $USER
```

You’ll need to log out and back in for group membership to take effect, or use:

``` bash
newgrp scanner
```

For network scanners, also check `/etc/sane.d/net.conf` and ensure the HP device’s IP isn’t blocked. For wireless HP printers, this is usually not an issue, but verify:

``` bash
sudo nano /etc/sane.d/net.conf
```

Make sure the file doesn’t have a blanket `deny` rule that would block your subnet.

## Test the Scanner

After permissions are set, test scanning:

``` bash
scanimage -T
```

This performs a test scan. For actual scanning:

``` bash
scanimage -x 210 -y 297 --format=png > scan.png
```

This scans an A4 page as PNG. Adjust dimensions as needed (in millimeters).

## Use a GUI Application

For everyday use, install a scanning front-end:

``` bash
sudo dnf install simple-scan
```

or on Ubuntu:

``` bash
sudo apt install simple-scan
```

Open Simple Scan, and your HP device should appear in the device menu. If it doesn’t, restart the application after confirming `scanimage -L` shows your device.

## Troubleshooting Wireless HP Devices

If `scanimage -L` doesn’t detect your wireless scanner:

**Check HP device discovery:**

``` bash
hp-probe -i
```

This scans your network for HP devices. If found, note the IP address.

**Manually add the device to SANE:**

Edit `/etc/sane.d/hp.conf`:

``` bash
sudo nano /etc/sane.d/hp.conf
```

Add the line (replace with your printer’s actual IP):

    #/dev/usb/lp0
    #192.168.1.100

Then test again with `scanimage -L`.

**Verify network connectivity:**

Ping your printer to ensure it’s reachable:

``` bash
ping 192.168.1.100
```

If it times out, check your WiFi connection and router settings.

## Restart SANE Services

If you’ve made configuration changes, restart the SANE daemon:

``` bash
sudo systemctl restart saned.socket
```

or for systems using the older approach:

``` bash
sudo systemctl restart saned
```

Then retest with `scanimage -L`.

## Additional Notes

- **PDF scanning:** Pipe `scanimage` output to convert to PDF:

  ``` bash
  scanimage -x 210 -y 297 --format=pnm | convert - scan.pdf
  ```

  This requires ImageMagick (`sudo dnf install imagemagick`).

- **Batch scanning:** Use Simple Scan’s batch feature for multi-page documents, or script `scanimage` calls with pauses between pages.

- **AirPrint/Bonjour:** Modern HP printers use mDNS discovery. If your printer doesn’t appear, check that Avahi is running:

  ``` bash
  sudo systemctl status avahi-daemon
  ```

If the scanner still isn’t detected after these steps, verify the printer model is SANE-compatible at the <a href="http://www.sane-project.org/lists/sane-backends-cvs.html" rel="nofollow noopener" target="_blank">SANE device list</a>, and check logs with `journalctl -u saned -n 50` for error details.
