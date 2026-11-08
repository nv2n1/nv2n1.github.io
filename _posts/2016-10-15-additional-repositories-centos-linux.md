---
title: "Managing Third-Party Repositories on CentOS, Rocky Linux, and AlmaLinux"
date: 2016-10-15 09:38:31 +0000
layout: post
canonical: https://www.systutorials.com/additional-repositories-centos-linux/
---

Modern RHEL-based systems (EL9+) ship with dnf as the package manager. Most additional software you’ll need comes from well-maintained third-party repositories rather than compiling from source. This guide covers the essential ones and how to use them safely.

## EPEL (Extra Packages for Enterprise Linux)

EPEL is the go-to third-party repository for RHEL-based systems. It provides development tools, databases, monitoring software, and utility packages not in the base repositories. It’s stable and widely deployed in production.

Install on EL9+ (Rocky Linux 9, AlmaLinux 9, CentOS Stream 9):

``` bash
sudo dnf install epel-release
```

On EL8 (if still in your environment):

``` bash
sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

Verify it’s active:

``` bash
dnf repolist
```

You should see `epel` and `epel-modular` in the output.

To disable EPEL temporarily (testing, troubleshooting):

``` bash
sudo dnf config-manager --set-disabled epel
```

Reference: <a href="https://docs.fedoraproject.org/en-US/epel/" rel="nofollow noopener" target="_blank">EPEL Documentation</a>

## CRB (CodeReady Builder)

CRB provides development libraries, debugging symbols, and build tools required for compiling software from source on EL9+. It replaces the older PowerTools repository. Enable it if you’re building packages, need development headers (gcc, make, library headers), or installing software that requires source compilation.

On EL9+:

``` bash
sudo dnf config-manager --set-enabled crb
```

On EL8 (legacy equivalent):

``` bash
sudo dnf config-manager --set-enabled powertools
```

CRB should remain enabled for development systems—there’s minimal risk to a running server.

## Remi Repository (PHP and Web Stack)

Remi maintains current PHP versions (8.2, 8.3, 8.4+) and related web stack software like MariaDB, PostgreSQL, and Redis. Use it when you need newer PHP than what EPEL provides.

Install on EL9:

``` bash
sudo dnf install https://rpms.remirepo.net/enterprise/remi-release-9.rpm
```

List available PHP module streams:

``` bash
dnf module list php
```

Enable and install PHP 8.4:

``` bash
sudo dnf module enable php:remi-8.4
sudo dnf install php php-cli php-fpm php-mysql php-xml php-pdo
```

To switch PHP versions on an existing system:

``` bash
sudo dnf module disable php:remi-8.3
sudo dnf module enable php:remi-8.4
sudo dnf upgrade 'php*'
sudo systemctl restart php-fpm
```

Always disable the old module stream before enabling a new one—this prevents dependency conflicts.

Reference: <a href="https://rpms.remirepo.net/" rel="nofollow noopener" target="_blank">Remi Repository</a>

## RPM Fusion (Multimedia and Codecs)

RPM Fusion provides FFmpeg, VLC, Handbrake, and properly maintained codec support. It’s the modern replacement for deprecated repositories like Nux Dextop. Install both free and nonfree repos:

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-9.noarch.rpm \
  https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-9.noarch.rpm
```

Install common media tools:

``` bash
sudo dnf install ffmpeg vlc handbrake libdvdcss
```

Reference: <a href="https://rpmfusion.org/" rel="nofollow noopener" target="_blank">RPM Fusion</a>

## Google Chrome Repository

Google maintains an official RPM repository for Chrome on x86_64 and ARM64.

Add the repository:

``` bash
sudo tee /etc/yum.repos.d/google-chrome.repo > /dev/null <<'EOF'
[google-chrome]
name=Google Chrome
baseurl=https://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
EOF
```

Install:

``` bash
sudo dnf install google-chrome-stable
```

For ARM64 systems, replace `x86_64` with `aarch64` in the baseurl. For beta or unstable channels, use `https://dl.google.com/linux/chrome/rpm/unstable/x86_64` instead.

## Best Practices for Third-Party Repositories

**Verify GPG keys before enabling**: A compromised repository affects your entire system. Check GPG key fingerprints against official sources:

``` bash
dnf repoinfo repository-name
```

**Disable unused repositories**: Reduce attack surface and improve DNF performance:

``` bash
sudo dnf config-manager --set-disabled repository-name
```

**Avoid version conflicts**: Don’t enable multiple conflicting PHP or database repositories simultaneously. Use DNF modules instead—they provide isolated version streams within a single repository and prevent dependency hell.

**Set repository priority if needed**: When packages exist in multiple repos, edit `/etc/yum.repos.d/` files and add `priority=10` to trusted repos. Lower numbers = higher priority.

``` ini
[epel]
name=Extra Packages for Enterprise Linux
baseurl=https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch
priority=10
```

**Clean metadata regularly**: Stale cache causes installation failures:

``` bash
sudo dnf clean all
sudo dnf check-update
```

**Use dnf exclusively**: On EL9+, `dnf` is the standard. `yum` is a deprecated wrapper. All modern documentation and tools assume dnf.

**Test in non-production first**: Enable new repositories on staging for 1-2 weeks before production. Watch for unexpected dependency changes or broken updates.

**Monitor for official package migration**: Some third-party packages eventually move to official RHEL repos. Periodically check if software you installed from external sources is now available in EPEL or base repositories.

## Repository Selection Strategy

Start with EPEL for most additional packages—it has the highest quality control and widest adoption across RHEL-based systems. Add Remi only for current PHP versions. Use RPM Fusion for multimedia. These three cover 95% of typical server and desktop needs. Always enable CRB on development systems for compilation work.
