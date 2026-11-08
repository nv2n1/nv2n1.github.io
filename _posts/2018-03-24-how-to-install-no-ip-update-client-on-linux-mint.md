---
title: "Installing No-IP DUC on Linux"
date: 2018-03-24 11:42:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-no-ip-update-client-on-linux-mint/
---

The No-IP Dynamic Update Client (DUC) keeps your dynamic DNS hostname pointing to your current IP address. Here’s how to install and configure the noip2 client on modern Linux distributions.

## Prerequisites

Before you start, install the required build tools and development libraries:

``` bash
sudo apt-get update
sudo apt-get install build-essential gcc libc6-dev
```

If you’re on a system without apt (RHEL/CentOS/Fedora), use:

``` bash
sudo yum groupinstall "Development Tools"
sudo yum install glibc-devel
```

## Download and Compile

Navigate to a temporary build directory and download the No-IP source:

``` bash
cd /tmp
wget https://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
tar xzf noip-duc-linux.tar.gz
cd no-ip-*
```

Compile and install:

``` bash
make
sudo make install
```

The binary will be installed to `/usr/local/bin/noip2`.

## Configure the Client

Run the configuration wizard to set up your No-IP credentials and preferred update interval:

``` bash
sudo /usr/local/bin/noip2 -C
```

You’ll be prompted to enter your No-IP username, password, and select which hostnames to update. The client will save configuration to `/usr/local/etc/no-ip2.conf`.

## Start the Daemon

Launch the noip2 daemon immediately:

``` bash
sudo /usr/local/bin/noip2
```

Verify it’s running:

``` bash
ps aux | grep noip2
```

## Enable at Boot

For systemd-based systems (modern Linux distributions), create a service file:

``` bash
sudo nano /etc/systemd/system/noip2.service
```

Add the following:

``` ini
[Unit]
Description=No-IP Dynamic DNS Update Client
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/noip2
ExecStop=/usr/local/bin/noip2 -K
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable noip2
sudo systemctl start noip2
```

If you’re on an older system using cron instead, add this line to your root crontab:

``` bash
sudo crontab -e
```

    @reboot /usr/local/bin/noip2

## Troubleshooting Missing Headers

If you encounter a compilation error like `fatal error: stdio.h: No such file or directory`, you’re missing development headers. Install them:

**Debian/Ubuntu:**

``` bash
sudo apt-get install libc6-dev
```

**RHEL/CentOS/Fedora:**

``` bash
sudo yum install glibc-devel
```

**Alpine Linux:**

``` bash
apk add libc-dev
```

## Common Commands

Check daemon status:

``` bash
/usr/local/bin/noip2 -S
```

Kill the running daemon:

``` bash
sudo /usr/local/bin/noip2 -K
```

View configuration:

``` bash
cat /usr/local/etc/no-ip2.conf
```

## Alternative: Package Installation

Some distributions now package noip2 in their repositories. Check first before compiling:

``` bash
apt-cache search noip2
yum search noip2
```

If available, a simple `sudo apt-get install noip2` or `sudo yum install noip2` may work and is easier to maintain.

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
