---
title: "Installing HP Printer Drivers on Linux Mint and Ubuntu"
date: 2018-03-24 11:42:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-up-hp-printer-drivers-on-linux-mint/
---

HP printers work reasonably well on Linux, though the setup process varies depending on whether you have a network printer or a USB-connected device. Here’s what you need to know.

## Install HPLIP

HPLIP (HP Linux Imaging and Printing) is the main driver package for HP printers. Install it along with the GUI configuration tool:

``` bash
sudo apt update
sudo apt install hplip hplip-gui
```

Note: `aptitude` still works but `apt` is the standard in modern Mint and Ubuntu. Aptitude also isn’t installed by default anymore.

## Configure Your Printer

### Using the GUI

For most users, the graphical setup is easiest:

``` bash
sudo hp-setup
```

This launches a wizard that detects connected printers and walks you through configuration. The tool will auto-detect USB printers immediately and network printers on your local subnet.

### Using the Command Line

If you prefer the terminal or need to script printer setup:

``` bash
sudo hp-setup -i
```

This runs the setup in interactive mode without the GUI. You can also auto-detect and install without interaction:

``` bash
sudo hp-setup -a
```

## Verify the Installation

Check if your printer was detected and added to CUPS (the printing system):

``` bash
lpstat -p -d
```

This shows all configured printers and which one is default. Test printing:

``` bash
echo "Test print" | lp -d PrinterName
```

Replace `PrinterName` with your actual printer’s name from `lpstat` output.

## Network Printer Setup

For network printers, ensure your printer is on the same subnet and has a stable IP address (set a static IP in your printer’s web interface if possible). The HP setup tool will find it automatically, but you can also add it manually through the CUPS web interface:

``` bash
sudo cupsctl --remote-admin --share-printers
```

Then navigate to `http://localhost:631` in your browser and add the printer via the “Administration” tab.

## Troubleshooting

**Printer not detected:**

- Check that USB cable is securely connected (for USB printers) or that the device is on the network
- Run `sudo hp-probe -buslist` to manually detect connected devices
- Try unplugging and replugging the USB cable

**Plugin installation needed:**\
Some newer HP printers require proprietary plugins. The setup wizard will prompt you to download these if needed. If it fails, try:

``` bash
sudo hp-plugin -i
```

**Permission denied errors:**\
Ensure your user is in the `lp` and `lpadmin` groups:

``` bash
sudo usermod -aG lp,lpadmin $USER
```

You’ll need to log out and back in for group changes to take effect.

**Printer queue stuck:**\
Clear the print queue if jobs won’t process:

``` bash
sudo cancel -a
sudo systemctl restart cups
```

## Check Printer Status

View real-time printer information and test cartridge levels (on supported models):

``` bash
hp-info -d PrinterName
```

Or use the diagnostic tool:

``` bash
hp-doctor
```

This runs a comprehensive health check on your HPLIP installation and connected devices.

## Remove or Switch Printers

To delete a printer from CUPS:

``` bash
sudo lpadmin -x PrinterName
```

To view all configured printers and remove via GUI:

``` bash
sudo system-config-printer
```

Most HP printers—including multifunction devices—work reliably on Linux once HPLIP is properly installed. If you encounter driver issues on a specific model, check the <a href="https://hplipopensource.com/hplip-web/supported_devices/printers" rel="nofollow noopener" target="_blank">HPLIP Supported Printers database</a> to confirm your model is supported and note any quirks for that device.
