---
title: "Installing Specific Package Versions with Yum"
date: 2013-07-12 16:32:14 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /installing-specific-old-versions-of-packages-in-yum/
---

To find all available versions of a package in your repository, use the `--showduplicates` flag:

``` bash
dnf list --showduplicates kernel
```

Or for other packages:

``` bash
dnf list --showduplicates <package-name>
```

The output shows both installed and available versions with their release tags. For example:

    Installed Packages
    kernel.x86_64                 6.8.1-1.fc39              @updates
    Available Packages
    kernel.x86_64                 6.7.12-200.fc39           updates
    kernel.x86_64                 6.6.25-1.fc39             updates
    kernel.x86_64                 6.5.13-300.fc39           fedora

## Installing a Specific Version

Once you’ve identified the version you need, install it by specifying the full package name with the version:

``` bash
dnf install kernel-6.7.12-200.fc39
```

If the package is already installed, DNF will handle keeping both versions (particularly useful for kernels, where you want a fallback option in the bootloader).

For non-kernel packages that conflict with the current version, you may need to explicitly allow downgrading:

``` bash
dnf downgrade package-name-X.Y.Z
```

Or to replace the current version entirely:

``` bash
dnf install --allowerasing package-name-X.Y.Z
```

## Working with Historical Versions

If a version isn’t showing in the default repositories, check if it’s archived:

``` bash
dnf search --all kernel
```

For very old versions, you might need to enable archived or EOL repositories. On RHEL/CentOS, this could mean adjusting `/etc/yum.repos.d/` configs. On Fedora, old releases are typically archived and require manually pointing to the archive repository.

## Checking What’s Installed

View all versions of a package currently on your system:

``` bash
dnf list installed | grep <package-name>
```

To see detailed information about a specific package version:

``` bash
dnf info package-name-X.Y.Z
```

## Preventing Automatic Updates

If you install an older package, DNF may try to update it on the next system upgrade. To pin a package to a specific version, add it to the exclude list in `/etc/dnf/dnf.conf`:

``` ini
[main]
excludepkgs=kernel-6.5.13-300.fc39
```

Or use DNF’s `mark` command to lock it:

``` bash
dnf mark hold package-name-X.Y.Z
dnf mark remove  # to unlock
```

## Note on DNF vs Yum

On RHEL 8+ and Fedora 22+, `dnf` is the standard package manager. The `yum` command is aliased to DNF on these systems, but DNF offers improved dependency resolution and cleaner command syntax. The examples here use `dnf`; the commands work identically if you substitute `yum`.

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

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.
