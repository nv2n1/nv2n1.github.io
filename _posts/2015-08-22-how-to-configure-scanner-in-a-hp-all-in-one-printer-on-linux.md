---
title: "Setting Up an HP Scanner on Linux with HPLIP and SANE"
date: 2015-08-22 13:27:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-scanner-in-a-hp-all-in-one-printer-on-linux/
---

Configuring an HP all-in-one printer’s scanner on Linux requires HPLIP (HP Linux Imaging and Printing) for device support and SANE (Scanner Access Now Easy) for scanning functionality. The main gotcha is that a working printer doesn’t guarantee a working scanner — they use different subsystems and need separate configuration.

## Installing Required Packages

Start by installing HPLIP, SANE backends, and a scanning frontend:

``` bash
# Debian/Ubuntu
apt-get install hplip sane sane-backends simple-scan

# Fedora/RHEL/CentOS
dnf install hplip sane sane-backends simple-scan

# Arch Linux
pacman -S hplip sane
```

`sane-backends` provides the scanner drivers, while `simple-scan` is a lightweight GUI alternative to the older `xsane`. You may also need `libusb` and `cups` (usually pre-installed) for USB device communication.

## Running the HP Setup Utility

Execute the HPLIP setup tool to detect and configure your device:

``` bash
sudo hp-setup
```

This interactive utility will:

- Prompt for your password
- Scan for connected USB and networked HP devices
- Display detected models
- Configure CUPS (printing) and SANE (scanning) automatically

For USB devices, select `USB` when prompted. For networked printers, select `JetDirect (port 9100)` or `SNMPv3` depending on your setup.

## Verifying Scanner Detection

After setup, confirm SANE recognizes your scanner:

``` bash
scanimage -l
```

You should see output like:

    Device: hp:libusb:001:005
      Canon LiDE 110 flatbed scanner

If nothing appears, your scanner isn’t detected. Check user permissions:

``` bash
sudo usermod -aG scanner,lp $USER
```

Log out completely and back in — group membership changes require a fresh login session. Simply opening a new terminal won’t work.

## Checking for Proprietary Plugins

Some HP scanner models require proprietary firmware. Install plugins if needed:

``` bash
sudo hp-plugin -i
```

This downloads and installs closed-source components for models that require them. After installation, restart SANE:

``` bash
sudo systemctl restart saned
```

## Troubleshooting Device Detection

If your scanner still isn’t detected, verify the device is connected:

``` bash
lsusb | grep -i hp
```

If it appears in `lsusb` but not in `scanimage -l`, reload SANE:

``` bash
sudo systemctl restart saned
```

Check SANE configuration for blacklisting:

``` bash
grep -r "blacklist" /etc/sane.d/
```

Remove any blacklist entries that match your device model.

For network scanners, ensure connectivity:

``` bash
ping <scanner-ip>
scanimage -h <scanner-ip>
```

## Scanning via GUI

Launch the default SANE frontend:

``` bash
simple-scan
```

Or use the older but more feature-rich `xsane`:

``` bash
xsane
```

## Command-Line Scanning

For scripting and automation, use `scanimage` directly:

``` bash
# List scanner-specific options
scanimage -A

# Scan at 300 DPI to PPM (uncompressed)
scanimage --resolution 300 > scan.ppm

# Scan to JPEG
scanimage --resolution 300 --format=jpeg > document.jpg

# Scan with ADF (automatic document feeder) if available
scanimage --source "Automatic Document Feeder" > multi.ppm

# Preview mode (faster, lower quality)
scanimage --preview > preview.ppm
```

Convert PPM to more practical formats:

``` bash
# PPM to PDF
convert scan.ppm scan.pdf

# PPM to PNG
convert scan.ppm scan.png

# Batch convert multiple PPMs
for file in *.ppm; do convert "$file" "${file%.ppm}.pdf"; done
```

## Full Test Workflow

Verify your complete setup:

``` bash
# Check scanner access
scanimage -A | head -20

# Perform a test scan
scanimage --resolution 150 > test.ppm

# Verify the file was created and has content
ls -lh test.ppm
file test.ppm

# Convert to practical format
convert test.ppm test.pdf
```

## Common Issues and Solutions

**Permission denied when scanning:**

``` bash
# Verify your user is in required groups
groups $USER

# Should show: username : username scanner lp ...
# If not, add yourself and reload:
sudo usermod -aG scanner,lp $USER
newgrp scanner
```

**CUPS connection fails:**

``` bash
sudo systemctl status cups
sudo systemctl restart cups
```

**Scanner works as root but not as regular user:**

This is always a permissions issue. Verify group membership with `groups $USER` and use `newgrp scanner` to activate the group in your current shell without logging out.

**Networked scanner times out:**

Ensure the scanner is on the same network and reachable. Check if your router’s firewall is blocking port 9100 or the SANE discovery port (6566 UDP).

Once `scanimage -l` shows your device and test scans complete successfully, your HP scanner is ready for regular use.
