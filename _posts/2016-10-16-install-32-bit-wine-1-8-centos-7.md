---
title: "Building 32-bit Wine on CentOS 7, Rocky Linux, and AlmaLinux"
date: 2016-10-16 08:46:38 +0000
modified: 2026-04-11 16:21:26 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /install-32-bit-wine-1-8-centos-7/
---

RHEL-based distributions only provide 64-bit Wine packages in their standard repositories. Many Windows applications—especially legacy software—require 32-bit Wine. Building Wine from source is the most reliable approach to get a working 32-bit installation alongside 64-bit support.

## Prerequisites and Resource Requirements

Building Wine requires significant resources:

- ~2GB temporary disk space, ~500MB installed
- Compilation takes 20-40 minutes depending on CPU speed
- Both 32-bit (i686) and 64-bit (x86_64) development libraries
- The 64-bit build must complete before the 32-bit build (they’re interdependent)

Ensure you have at least 4GB of free disk space in `/usr/src` and adequate RAM. If your system has less than 2GB RAM, you’ll need to limit parallel jobs during compilation.

## Remove Existing Wine Installation

If Wine is already installed from packages, remove it to prevent conflicts:

``` bash
sudo yum erase wine wine-\*
```

## Install Build Dependencies

Start with development tools:

``` bash
sudo yum groupinstall 'Development Tools' -y
sudo yum install samba-winbind-clients -y
```

Install architecture-specific development libraries. You need both i686 (32-bit) and x86_64 (64-bit) versions for each package:

``` bash
sudo yum install \
  glibc-devel.{i686,x86_64} \
  libgcc.{i686,x86_64} \
  libX11-devel.{i686,x86_64} \
  freetype-devel.{i686,x86_64} \
  gnutls-devel.{i686,x86_64} \
  libxml2-devel.{i686,x86_64} \
  libjpeg-turbo-devel.{i686,x86_64} \
  libpng-devel.{i686,x86_64} \
  libXrender-devel.{i686,x86_64} \
  libXext-devel.{i686,x86_64} \
  alsa-lib-devel.{i686,x86_64} \
  libXfixes-devel.{i686,x86_64} \
  -y
```

Optionally install these for broader compatibility:

``` bash
sudo yum install \
  openssl-devel.{i686,x86_64} \
  libcap-devel.{i686,x86_64} \
  vulkan-loader-devel.{i686,x86_64} \
  -y
```

## Download Wine Source

Set your desired Wine version and download. Wine 9.x is currently stable (2026):

``` bash
VER=9.0
VERMAJOR=$(echo ${VER} | cut -d'.' -f1)
VERURLSTR=$(echo ${VER} | cut -d'.' -f1,2)

cd /usr/src
sudo wget https://dl.winehq.org/wine/source/${VERURLSTR}/wine-${VER}.tar.xz
sudo tar xf wine-${VER}.tar.xz
cd wine-${VER}
```

Check <a href="https://wiki.winehq.org/Download" rel="nofollow noopener" target="_blank">WineHQ’s download page</a> for available versions. Modern Wine versions use xz compression exclusively.

## Prepare Build Directories

Create separate build directories to keep 32-bit and 64-bit builds isolated:

``` bash
mkdir -p wine32 wine64
```

## Build 64-bit Wine First

The 32-bit build depends on 64-bit libraries, so compile 64-bit first:

``` bash
cd wine64
../configure --enable-win64
make -j$(nproc)
```

The `-j$(nproc)` flag uses all available CPU cores. If compilation fails with memory errors (“gcc: fatal error: Killed signal terminated program cc1plus”), reduce parallel jobs:

``` bash
make -j2
```

On systems with very limited RAM, use `-j1` (single-threaded compilation).

## Build 32-bit Wine

Link the 32-bit build against the 64-bit libraries you just compiled:

``` bash
cd ../wine32
PKG_CONFIG_PATH=/usr/lib/pkgconfig ../configure --with-wine64=../wine64
make -j$(nproc)
```

## Install Both Versions

Install 32-bit first, then 64-bit (order matters):

``` bash
cd ../wine32
sudo make install

cd ../wine64
sudo make install
```

Both binaries install to `/usr/local/bin` by default. To install to a custom prefix, add `--prefix=/opt/wine-9.0` to both configure commands.

## Verify Installation

Confirm both versions installed correctly:

``` bash
file $(which wine)
file $(which wine64)
```

Expected output:

    /usr/local/bin/wine: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), ...
    /usr/local/bin/wine64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), ...

The “ELF 32-bit” and “ELF 64-bit” strings confirm correct installation. If you see “ELF 64-bit” for both, the 32-bit build failed—check the make output for errors and ensure all i686 development libraries installed.

## Running Windows Applications

Run 32-bit Windows executables with Wine’s automatic detection:

``` bash
wine program.exe
```

Wine automatically selects 32-bit or 64-bit based on the executable format. For legacy 32-bit applications, you can explicitly set the architecture:

``` bash
WINEARCH=win32 wine program.exe
```

Check the installed Wine version:

``` bash
wine --version
```

## Troubleshooting Build Errors

**Missing dependencies during configure**

Check the configure output carefully. Install the `-devel` package for the missing library in both i686 and x86_64 variants, then run configure again in the `wine32` directory.

**“cannot find -lXfixes” or similar linker errors**

The multiarch libraries didn’t install correctly. Reinstall the problematic package:

``` bash
sudo yum install libXfixes-devel.{i686,x86_64}
```

Restart the configure step in `wine32`:

``` bash
cd wine32
../configure --with-wine64=../wine64
make -j$(nproc)
```

**“32-bit libraries not found” after configure**

You likely missed installing some `{i686,x86_64}` packages. Re-run the dependencies section and verify all packages installed:

``` bash
rpm -qa | grep -E 'i686|x86_64' | grep devel | wc -l
```

This should return at least 15-20 packages. If significantly lower, reinstall the full dependency list.

**Compilation out of memory (OOM kill)**

Your system ran out of memory. Reduce parallel jobs:

``` bash
make -j1
```

Alternatively, close background applications and increase swap space temporarily.

**“libtoolize: error: file named ‘ltmain.sh’ not found”**

Run autoreconf before configure:

``` bash
cd wine64
autoreconf -fiv
../configure --enable-win64
```

## Upgrading Wine

To upgrade to a newer Wine version:

1.  Download and extract the new version to `/usr/src`
2.  Repeat the build process with the new version
3.  The new build installs alongside the old one (both in `/usr/local/bin`)

To switch back to an older version, simply run:

``` bash
ln -sf /usr/local/bin/wine-9.0 /usr/local/bin/wine
```

## Removing Wine Completely

To uninstall Wine entirely:

``` bash
sudo rm -rf /usr/local/bin/wine* /usr/local/lib/wine /usr/local/include/wine
```

If you used a custom `--prefix` during configure, remove that directory instead:

``` bash
sudo rm -rf /opt/wine-9.0
```
