---
title: "How to Install and Configure HP Printers on CentOS 7"
date: 2018-03-24 11:51:14 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-set-up-hp-printer-and-scaner-on-centos-7/
---

HP printers and scanners on Rocky Linux, CentOS, or RHEL require the HPLIP (HP Linux Imaging and Printing) package. This guide covers the complete setup process.

### Install HPLIP packages

Start by installing the core HPLIP packages:

``` bash
sudo dnf install hplip hplip-gui hpijs
```

On older CentOS 7 systems, use `yum` instead of `dnf`. HPLIP may prompt you to install additional dependencies — allow these installations to proceed. Some printer models require proprietary plugins that won’t function without the complete package set.

### Install printer plugins

HP printers often need proprietary plugins for full functionality. Install them with:

``` bash
sudo hp-plugin
```

This tool downloads and installs device-specific plugins. You may need to accept licensing agreements. If the command fails, ensure you have internet connectivity and that your printer model is supported by the current HPLIP version.

### Configure your printer

Run the printer setup utility:

``` bash
sudo hp-setup
```

This interactive tool will:

- Detect connected printers (USB or network)
- Configure the printer for your system
- Set default print queues
- Test basic connectivity

Follow the on-screen prompts. For network printers, enter the IP address when prompted.

### Verify scanner functionality

Test scanner detection:

``` bash
scanimage -L
```

This lists all detected scanners. If your scanner appears, the configuration is complete.

For USB scanners, ensure your user account belongs to the `lpadmin` and `lp` groups to avoid permission issues:

``` bash
sudo usermod -aG lpadmin,lp $USER
```

Log out and back in for group changes to take effect.

### Troubleshooting

**Printer not detected:** Check USB connections or network connectivity. For network printers, verify the device is on the same subnet:

``` bash
sudo hp-probe -bnet
```

**Plugin installation fails:** Update HPLIP to the latest version. Older HPLIP versions may not support newer printer models:

``` bash
sudo dnf update hplip
```

**Scanner permissions denied:** Ensure you’ve added your user to the appropriate groups (see above).

**Check HPLIP status:** View detailed device and driver information:

``` bash
hp-info
```

### Accessing the GUI

If you installed `hplip-gui`, launch the control panel:

``` bash
sudo hp-toolbox
```

This provides a graphical interface for printer management, status monitoring, and basic diagnostics.

## Troubleshooting Common Issues

If you encounter problems during installation, check these common solutions:

- Ensure your system packages are up to date before installing new software
- Check for conflicting packages that might prevent installation
- Verify network connectivity if downloading packages from external repositories
- Review system logs in /var/log/ for detailed error messages

## Verification Steps

After installation, verify everything is working correctly by checking the installed version and running basic functionality tests. Most command-line tools respond to the –version or -v flag to display their version information.

## Keeping Your Installation Updated

Regularly update your system to receive security patches and bug fixes. On Fedora, use dnf update. On Ubuntu and Debian, use apt update followed by apt upgrade. For software installed via language-specific package managers like pip, npm, or gem, check their respective update commands.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
