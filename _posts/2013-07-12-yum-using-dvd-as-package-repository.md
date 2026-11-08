---
title: "Using DVDs as Local Package Repositories in DNF"
date: 2013-07-12 16:33:26 +0000
modified: 2026-04-11 16:41:35 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /yum-using-dvd-as-package-repository/
---

Insert the installation media and create a mount point:

``` bash
sudo mkdir -p /media/dvd
sudo mount /dev/sr0 /media/dvd
```

For a DVD image file instead of physical media:

``` bash
sudo mount -o loop /path/to/image.iso /media/dvd
```

Verify the mount and check that packages exist:

``` bash
ls /media/dvd/Packages/ | head
```

On systems with automatic mounting (systemd-based), the DVD may already be mounted at `/run/media/$USER/` — adjust your paths accordingly.

## Configuring the DNF Repository

Create a repository configuration file for the DVD:

``` bash
sudo tee /etc/yum.repos.d/dvd-local.repo > /dev/null << 'EOF'
[dvd-local]
name=Local DVD Repository
baseurl=file:///media/dvd
enabled=1
gpgcheck=1
gpgkey=file:///media/dvd/RPM-GPG-KEY-redhat-release
EOF
```

The GPG key filename varies by distribution. Check what’s available on the DVD:

``` bash
ls /media/dvd/ | grep -i gpg
```

For RHEL, CentOS Stream, or Fedora, the key might be named `RPM-GPG-KEY-redhat-release`, `RPM-GPG-KEY-centos-official`, or `RPM-GPG-KEY-fedora`. Adjust the `gpgkey` line accordingly.

If the key is missing and you need to proceed, you can temporarily disable signature checking with `gpgcheck=0`, but this is not recommended for production systems. Always identify and use the correct key when possible.

## Importing Repository Keys

Import the GPG key manually to avoid prompts during package operations:

``` bash
sudo rpm --import /media/dvd/RPM-GPG-KEY-redhat-release
```

Verify the key was imported:

``` bash
rpm -qa gpg-pubkey*
```

## Disabling Network Repositories

If you want the DVD to be your only source, disable the default network repos. First, identify enabled repositories:

``` bash
sudo dnf repolist enabled
```

Then disable them selectively:

``` bash
sudo dnf config-manager --set-disabled appstream baseos extras powertools
```

Or disable all repos at once, then re-enable only the DVD:

``` bash
sudo sed -i 's/^enabled=1/enabled=0/' /etc/yum.repos.d/*.repo
sudo sed -i '/\[dvd-local\]/a enabled=1' /etc/yum.repos.d/dvd-local.repo
```

## Testing the Repository

Clear the DNF cache and verify configuration:

``` bash
sudo dnf clean all
sudo dnf repolist
```

The `dvd-local` repository should appear in the output. Test by installing a package from the DVD:

``` bash
sudo dnf install kernel-devel
sudo dnf search vim
```

If you get “no packages to install,” the package may not be on the DVD media. Check what’s actually available:

``` bash
ls /media/dvd/Packages/ | grep kernel-devel
```

## Persistent Mounting with systemd

For systems that use the DVD frequently, create a systemd mount unit instead of relying on `/etc/fstab`. This approach is more reliable on modern systems:

``` bash
sudo tee /etc/systemd/system/media-dvd.mount > /dev/null << 'EOF'
[Unit]
Description=DVD Repository Mount
After=local-fs.target

[Mount]
What=/dev/sr0
Where=/media/dvd
Type=iso9660
Options=ro
TimeoutSec=0

[Install]
WantedBy=multi-user.target
EOF
```

Enable and start the mount:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable media-dvd.mount
sudo systemctl start media-dvd.mount
```

Alternatively, use `/etc/fstab` with the `noauto` flag to avoid boot failures when the DVD is missing:

``` bash
echo '/dev/sr0 /media/dvd iso9660 ro,noauto 0 0' | sudo tee -a /etc/fstab
```

Mount manually when needed:

``` bash
sudo mount /media/dvd
```

## Troubleshooting

**Repository not found:** Verify the baseurl and mount point:

``` bash
test -d /media/dvd/Packages && echo "OK" || echo "Mount problem"
cat /etc/yum.repos.d/dvd-local.repo | grep baseurl
```

**GPG errors:** Ensure the key file exists and is readable:

``` bash
ls -l /media/dvd/RPM-GPG-KEY-*
file /media/dvd/RPM-GPG-KEY-*
```

If the key is missing, set `gpgcheck=0` temporarily, then investigate what the actual key filename is.

**Limited packages:** DVD media contains far fewer packages than online repositories. You can enable multiple repositories simultaneously — keep the DVD enabled and re-enable a network repo for packages not on the disc:

``` bash
sudo dnf config-manager --set-enabled baseos
```

**Permission issues:** Ensure the mount point is readable:

``` bash
ls -ld /media/dvd
sudo chmod 755 /media/dvd
```

**Unmounting:** When finished, safely unmount the DVD:

``` bash
sudo umount /media/dvd
sudo eject /dev/sr0
```

If `umount` fails because files are still in use, identify what’s holding the mount open:

``` bash
sudo lsof | grep /media/dvd
```

Use `fuser` to force-kill processes if necessary:

``` bash
sudo fuser -km /media/dvd
```

Then try unmounting again.
