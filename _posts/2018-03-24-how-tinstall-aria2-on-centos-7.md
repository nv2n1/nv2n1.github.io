---
title: "How to Install aria2 on CentOS 7"
date: 2018-03-24 11:51:07 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-tinstall-aria2-on-centos-7/
---

aria2 is a lightweight, multi-protocol download manager that supports HTTP(S), FTP, BitTorrent, and Metalink protocols. It’s particularly useful for resumable downloads, parallel connections, and command-line automation.

### Prerequisites

You’ll need root or sudo access. This guide covers CentOS 7, CentOS Stream, and Rocky Linux 8+. For older systems still on CentOS 7, package availability may be limited, so building from source is an alternative.

### Installation from EPEL

The simplest approach is installing aria2 from the EPEL (Extra Packages for Enterprise Linux) repository.

First, enable EPEL:

``` bash
sudo dnf install epel-release
```

On CentOS 7, use:

``` bash
sudo yum install epel-release
```

Then install aria2:

``` bash
sudo dnf install aria2
```

Or on CentOS 7:

``` bash
sudo yum install aria2
```

Verify the installation:

``` bash
aria2c --version
```

### Building from Source

If EPEL packages aren’t available or you need a newer version, build aria2 from source:

``` bash
sudo dnf groupinstall "Development Tools"
sudo dnf install openssl-devel libxml2-devel zlib-devel sqlite-devel
```

Download the latest release from the <a href="https://github.com/aria2/aria2/releases" rel="nofollow noopener" target="_blank">aria2 GitHub releases page</a>:

``` bash
cd /tmp
wget https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0.tar.gz
tar xzf aria2-1.36.0.tar.gz
cd aria2-1.36.0
./configure --prefix=/usr/local
make
sudo make install
```

Verify the installation:

``` bash
/usr/local/bin/aria2c --version
```

### Basic Usage

Download a single file:

``` bash
aria2c https://example.com/largefile.iso
```

Download with multiple connections (faster):

``` bash
aria2c -x 5 https://example.com/largefile.iso
```

Download multiple URLs from a file:

``` bash
aria2c -i download_list.txt
```

Resume a partial download:

``` bash
aria2c -c https://example.com/largefile.iso
```

Set output directory and filename:

``` bash
aria2c -d /home/user/downloads -o myfile.iso https://example.com/largefile.iso
```

### Using aria2 as a Daemon (RPC Server)

aria2 can run as a daemon with RPC control for automation:

``` bash
mkdir -p ~/.config/aria2
cat > ~/.config/aria2/aria2.conf << EOF
# Listen on localhost:6800
rpc-listen-all=false
rpc-listen-addr=127.0.0.1
rpc-listen-port=6800
EOF
```

Start the daemon:

``` bash
aria2c --conf-path=~/.config/aria2/aria2.conf -D
```

Use an RPC client like <a href="https://github.com/ziahamza/webui-aria2" rel="nofollow noopener" target="_blank">webui-aria2</a> to control downloads through a web interface.

### Configuration File

Create a persistent configuration at `~/.config/aria2/aria2.conf`:

``` bash
# Number of parallel connections
max-concurrent-downloads=5
max-connection-per-server=4

# Timeout
connect-timeout=120

# Output directory
dir=/home/user/downloads

# Log file
log-level=notice
log=/home/user/.aria2/aria2.log
```

Run aria2 with your config:

``` bash
aria2c --conf-path=~/.config/aria2/aria2.conf [URLs]
```

### Troubleshooting

If downloads fail, check connectivity and verify the URL. Enable debug logging:

``` bash
aria2c --log-level=debug --log=/tmp/aria2-debug.log https://example.com/file
```

For permission errors when writing to directories, ensure the user running aria2 has write access to the download directory.

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
