---
title: "Prevent Packages from Being Updated with yum and dnf"
date: 2018-03-24 11:40:51 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-force-yum-not-to-update-certain-packages/
---

If you’ve compiled a kernel module for a specific kernel version or need to pin a package to prevent automatic updates, you’ll want to exclude it from yum or dnf. There are several approaches depending on whether you need a permanent exclusion, per-repository exclusion, or temporary lockdown.

## Global Exclusions in Configuration

The simplest approach is to add an `exclude` directive to your package manager configuration.

Edit `/etc/yum.conf` (yum) or `/etc/dnf/dnf.conf` (dnf) and add an exclude line under the `[main]` section:

``` ini
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1
gpgcheck=1
plugins=1
installonly_limit=3
exclude=kernel sbt
```

Multiple packages should be space-separated. Glob patterns work here too:

``` ini
exclude=kernel-5.10.* sbt-1.3.* postgresql-*
```

This prevents updates to any kernel 5.10.x, sbt 1.3.x, or all postgresql versions.

## Per-Repository Exclusions

To exclude packages only from specific repositories, add the `exclude` directive to individual repo configurations in `/etc/yum.repos.d/`:

``` ini
[fedora]
name=Fedora $releasever - $basearch
baseurl=https://mirrors.fedoraproject.org/metalink?repo=fedora-$releasever&arch=$basearch
exclude=kernel sbt
```

This approach is useful when you trust updates from one repository but want to control updates from another.

## One-Off Exclusions During Updates

For temporary exclusions without modifying config files:

``` bash
yum update --exclude=kernel
dnf update --exclude=kernel,sbt
```

You can exclude multiple packages by separating them with commas in dnf, or spaces in yum.

## Using Version Locking (Recommended for Production)

Version locking is more reliable than exclude directives because it explicitly pins versions rather than blocking updates. This prevents accidental downgrades or side effects from exclude patterns.

Install the versionlock plugin:

``` bash
dnf install python3-dnf-plugins-extras-versionlock
```

Lock a package to its current version:

``` bash
dnf versionlock add kernel
dnf versionlock add postgresql postgresql-libs postgresql-server
```

List all locked packages:

``` bash
dnf versionlock list
```

Clear specific locks:

``` bash
dnf versionlock delete kernel
```

Clear all locks:

``` bash
dnf versionlock clear
```

## Handling Kernel Module Compatibility

If you’re excluding the kernel because of a custom-compiled module, understand that you’re also blocking security patches. Consider these alternatives:

**Option 1: Use DKMS for automatic recompilation**

Install DKMS (Dynamic Kernel Module Support) if your module supports it:

``` bash
dnf install dkms
dkms autoinstall
```

After a kernel update, DKMS automatically rebuilds your module against the new kernel without manual intervention.

**Option 2: Rebuild modules manually after updates**

After a kernel update, rebuild your module:

``` bash
cd /path/to/module/source
make clean
make
sudo make install
```

**Option 3: Use installonly packages**

For packages like the kernel, which support multiple concurrent versions, increase the `installonly_limit` in `/etc/dnf/dnf.conf`:

``` ini
installonly_limit=5
```

This allows 5 kernel versions to coexist, so you can test a new kernel before removing the old one.

## Important Considerations

**Security Risk**: Excluding the kernel or other packages with frequent security updates leaves your system vulnerable. Only exclude packages temporarily while resolving compatibility issues.

**dnf vs yum**: On RHEL 8+, CentOS 8+, and Fedora 22+, dnf is the default package manager. The syntax is largely compatible, but use dnf commands on those systems. yum on newer systems is typically a wrapper around dnf anyway.

**Configuration Reload**: Changes to `/etc/dnf/dnf.conf` or `/etc/yum.conf` take effect immediately on the next update command—no service restart needed.

**Testing First**: Always test kernel updates and dependency changes in a non-production environment before deploying to production systems, especially if you’re excluding packages from updates.
