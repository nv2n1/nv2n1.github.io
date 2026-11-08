---
title: "Installing sbt on Fedora Linux"
date: 2018-03-24 08:19:38 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-sbt-for-scala-on-fedora-linux/
---

sbt (Scala Build Tool) isn’t available in the default Fedora repositories, though Scala itself is. Here’s how to install it properly.

## Using the Official Repository

The most reliable approach is to add sbt’s official repository to your system. This gives you automatic updates and avoids manual RPM downloads.

Create the repository configuration file:

``` bash
sudo tee /etc/yum.repos.d/sbt.repo > /dev/null << EOF
[scala-sbt-official]
name=Scala SBT Official Repository
baseurl=https://repo.scala-sbt.org/scalasbt/rpm
enabled=1
gpgcheck=1
gpgkey=https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x99E82A75642AC823
EOF
```

Then install sbt:

``` bash
sudo dnf install sbt
```

The `dnf` package manager (successor to yum on modern Fedora) handles repository setup automatically and provides better dependency resolution.

## Manual RPM Installation

If you prefer downloading directly, grab the latest RPM from the <a href="https://github.com/sbt/sbt/releases" rel="nofollow noopener" target="_blank">official releases page</a>:

``` bash
sudo dnf install https://github.com/sbt/sbt/releases/download/v1.10.1/sbt-1.10.1.rpm
```

Replace `1.10.1` with the current version. Use the direct GitHub download link instead of older mirrors — it’s more reliable and better maintained.

## First Run and Configuration

After installation, run sbt for the first time:

``` bash
sbt
```

The first startup takes time as sbt downloads its dependencies and the default Scala version. This is normal; subsequent runs are fast. You’ll see the sbt prompt when ready:

    sbt:root>

Exit with `exit` or Ctrl+D.

## Verify Installation

Check that sbt works correctly:

``` bash
sbt --version
```

You should see output like `sbt version 1.10.1`.

## Managing Multiple sbt Versions

For projects requiring different sbt versions, use <a href="https://github.com/paulp/sbt-extras" rel="nofollow noopener" target="_blank">sbt-extras</a>. It automatically selects the correct version based on `project/build.properties`:

``` bash
curl -s https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt > ~/bin/sbt
chmod +x ~/bin/sbt
```

Ensure `~/bin` is early in your `$PATH`. Create `project/build.properties` in your project:

```properties
sbt.version=1.9.9
```

The wrapper automatically downloads and uses that version.

## Common Issues

**Java not found:** sbt requires Java 8 or later. Install it with:

``` bash
sudo dnf install java-latest-openjdk-devel
```

**Slow first run on slow connections:** The initial bootstrap can take 5+ minutes. Let it complete without interruption.

**Disk space:** sbt’s cache directory (`~/.sbt` and `~/.ivy2`) grows over time. Clear old artifacts if needed:

``` bash
rm -rf ~/.sbt/*/cache
```

**Update to latest version:** If using the repository method:

``` bash
sudo dnf upgrade sbt
```

If using sbt-extras, just update the wrapper script from the GitHub repository.

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
