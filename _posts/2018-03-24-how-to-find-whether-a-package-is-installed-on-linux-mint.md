---
title: "How to Check if a Package is Installed on Linux Mint"
date: 2018-03-24 11:42:25 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-whether-a-package-is-installed-on-linux-mint/
---

Linux Mint uses the APT package management system (derived from Debian). There are several straightforward methods to verify whether a specific package is installed.

## Using dpkg

The `dpkg` command directly queries the package database on your system.

``` bash
dpkg -l | grep ghostscript
```

This lists all installed packages and filters for `ghostscript`. If the package is installed, the output will show a line starting with `ii` (indicating “installed”). If nothing returns, the package isn’t installed.

For a cleaner check, use the `-l` flag with a pattern:

``` bash
dpkg -l ghostscript
```

Or check the exit code programmatically:

``` bash
dpkg -l | grep -q "^ii  ghostscript" && echo "Installed" || echo "Not installed"
```

## Using dpkg -s (Most Direct)

The clearest method for checking a single package:

``` bash
dpkg -s ghostscript
```

This returns detailed package information if it’s installed. If the package isn’t installed, you’ll get an error: `dpkg-query: package 'ghostscript' is not installed`. This is the preferred approach when you only need to check one package.

## Using apt

Modern APT also provides a direct way:

``` bash
apt show ghostscript
```

This displays package details whether or not it’s installed. Look for the `Status:` field to confirm installation status.

## Checking Multiple Packages

To verify several packages at once:

``` bash
for pkg in ghostscript imagemagick curl; do
  if dpkg -l | grep -q "^ii  $pkg"; then
    echo "$pkg: installed"
  else
    echo "$pkg: not installed"
  fi
done
```

Or use a more efficient approach:

``` bash
dpkg -l ghostscript imagemagick curl | grep "^ii"
```

## Listing All Installed Packages

If you need a complete inventory of installed packages:

``` bash
dpkg -l | grep "^ii" | awk '{print $2}'
```

Or with apt:

``` bash
apt list --installed
```

The `apt list --installed` command is more modern and readable, showing package names and versions in a clean format.

## Exit Codes for Scripting

When writing scripts, checking exit codes is cleaner than parsing output:

``` bash
if dpkg -l ghostscript 2>/dev/null | grep -q "^ii"; then
  echo "Package is installed"
  exit 0
else
  echo "Package is not installed"
  exit 1
fi
```

## Summary

- **Single package check**: `dpkg -s ghostscript`
- **List all installed**: `apt list --installed`
- **Script-friendly check**: `dpkg -l ghostscript 2>/dev/null | grep -q "^ii"`

The `dpkg -s` method is the simplest for quick verification, while `apt list --installed` works better when you need readable output of all packages on your system.

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
