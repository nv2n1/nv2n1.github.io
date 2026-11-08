---
title: "Installing Alien on CentOS 7: Convert .deb to .rpm"
date: 2018-03-24 11:54:26 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-alien-on-centos-7-to-convert-deb-to-rpm/
---

`alien` is a straightforward package converter available in EPEL that handles conversion between .deb, .rpm, Slackware, and other package formats. This is useful when you need to install Debian packages on RPM-based systems.

## Prerequisites

You need EPEL (Extra Packages for Enterprise Linux) enabled. On CentOS 7, 8, or Rocky Linux 8+:

``` bash
sudo dnf install epel-release
```

Or if you’re on an older CentOS/RHEL system without `dnf`:

``` bash
sudo yum install epel-release
```

## Installation

Install `alien` from EPEL:

``` bash
sudo dnf install alien
```

Verify the installation:

``` bash
alien --version
```

You should see output like:

    alien version 8.95 or newer

## Basic Usage

### Converting a .deb to .rpm

Convert a Debian package to RPM format:

``` bash
sudo alien -r package.deb
```

The `-r` flag tells `alien` to output an RPM file. This generates a `.rpm` file in your current directory that you can then install with `dnf` or `rpm -i`.

### Converting with version adjustments

By default, `alien` may adjust the package version to be RPM-compliant. To maintain the original version number:

``` bash
sudo alien -r --keep-version package.deb
```

### Installing after conversion

After conversion, install the resulting RPM:

``` bash
sudo dnf install ./package.rpm
```

### Converting to other formats

Convert .deb to Slackware `.tgz`:

``` bash
alien -t package.deb
```

Convert .rpm to .deb (less common but supported):

``` bash
alien -d package.rpm
```

## Important Considerations

**Dependencies**: `alien` converts the package structure but doesn’t resolve all dependencies. If the converted package depends on libraries not available in your RPM repositories, you’ll need to install those separately.

**Testing**: Always test converted packages in a non-production environment first. The conversion process can sometimes introduce issues, particularly with:

- Systemd service files
- Configuration file locations
- Library paths

**Architecture mismatch**: Ensure the .deb package matches your system architecture (x86_64, aarch64, etc.). Convert only packages meant for your platform.

**Better alternatives**: Before converting, check if the software is available directly in RPM format from the vendor or from community repositories like COPR. Native RPM packages are always preferable to converted packages.

## Example: Converting a specific package

If you have `example-1.0.deb` and need it as an RPM:

``` bash
sudo alien -r example-1.0.deb
# Creates: example-1.0-2.x86_64.rpm

sudo dnf install example-1.0-2.x86_64.rpm
```

## Troubleshooting

If `alien` is not found after installation, verify EPEL is properly enabled:

``` bash
dnf repolist | grep epel
```

If EPEL doesn’t appear in the list, re-run the EPEL installation and clear your package cache:

``` bash
sudo dnf clean all
sudo dnf install epel-release
```

For detailed help with conversion options:

``` bash
alien --help
```

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
