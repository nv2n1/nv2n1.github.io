---
title: "Building 32-bit Wine on CentOS/RHEL 8+"
date: 2020-03-27 16:28:26 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-wine-32-bit-on-centos-8/
---

RHEL and CentOS 8+ ship 64-bit only by default. Some Windows applications require 32-bit Wine or run better under it. Since the distribution repositories don’t provide prebuilt 32-bit Wine, you’ll need to compile from source. The process requires building 64-bit Wine first, then 32-bit, then rebuilding 64-bit to establish proper cross-architecture linking.

## Install Build Dependencies

Start with the core build toolchain:

``` bash
sudo dnf install -y gcc gcc-c++ make flex bison fontconfig-devel \
  freetype-devel libxcursor-devel libxi-devel libxrandr-devel \
  libxinerama-devel mesa-libGL-devel perl perl-Locale-gettext \
  xorg-x11-server-devel openssl-devel gnutls-devel libsane-devel \
  ncurses-devel samba-devel cups-devel gphoto2-devel libxml2-devel \
  libxslt-devel alsa-lib-devel pulseaudio-libs-devel gstreamer1-plugins-base-devel
```

Install 32-bit development libraries:

``` bash
sudo dnf install -y glibc-devel.i686 libgcc.i686 libstdc++-devel.i686 \
  ncurses-devel.i686 fontconfig-devel.i686 freetype-devel.i686 \
  libxcursor-devel.i686 libxi-devel.i686 libxrandr-devel.i686 \
  libxinerama-devel.i686 mesa-libGL-devel.i686 openssl-devel.i686 \
  gnutls-devel.i686 libsane-devel.i686 cups-devel.i686 alsa-lib-devel.i686 \
  pulseaudio-libs-devel.i686 gstreamer1-plugins-base-devel.i686
```

Verify i686 packages are installed:

``` bash
dnf list installed | grep "\.i686" | head -10
```

## Download Wine Source

Grab a stable release from WineHQ:

``` bash
cd /tmp
wget https://dl.winehq.org/wine/source/9.0/wine-9.0.tar.xz
tar xf wine-9.0.tar.xz
cd wine-9.0
```

Check available versions at <a href="https://wiki.winehq.org/Download" rel="nofollow noopener" target="_blank">https://wiki.winehq.org/Download</a> — use stable branches (9.x, 8.x) rather than development versions for production systems. Version 10.0 and later may have different build requirements, so verify compatibility with your system first.

## Build 64-bit Wine

Create a separate build directory to avoid polluting the source tree:

``` bash
mkdir build64
cd build64
../configure --prefix=/usr/local --with-x --enable-win64
make -j$(nproc)
cd ..
```

Build time typically ranges from 20-45 minutes on modern systems. The `-j$(nproc)` flag parallelizes compilation across all available CPU cores. Monitor the build for errors—compilation failures often indicate missing dependencies.

If compilation fails, check the `config.log` file in the build64 directory for specific missing libraries:

``` bash
grep -i "checking for" build64/config.log | tail -20
```

Then install the missing development packages and reconfigure.

## Build 32-bit Wine

The 32-bit build must reference the completed 64-bit build directory:

``` bash
mkdir build32
cd build32
../configure --prefix=/usr/local --with-x --enable-win32 \
  --with-wine64=../build64
make -j$(nproc)
cd ..
```

The `--with-wine64=../build64` flag tells the 32-bit build where to find the 64-bit libraries for proper cross-architecture linking. This step typically takes 15-30 minutes. If the build fails with linker errors about missing 32-bit libraries, verify all i686 packages installed correctly and re-run the dnf install command above.

## Rebuild 64-bit Wine with 32-bit Support

After 32-bit completes successfully, rebuild 64-bit with awareness of the 32-bit build:

``` bash
cd build64
../configure --prefix=/usr/local --with-x --enable-win64 \
  --with-wine32=../build32
make -j$(nproc)
cd ..
```

This second 64-bit build establishes cross-architecture dependencies correctly. This is essential for proper wine/wine64 interoperability.

## Install Both Architectures

Install 64-bit first, then 32-bit:

``` bash
cd build64
sudo make install
cd ../build32
sudo make install
cd ..
```

This installs both the `wine` (32-bit wrapper) and `wine64` binaries to `/usr/local/bin`. By default, the wrapper script intelligently routes calls to the appropriate architecture based on the executable type.

## Verify Installation

Check which architectures are available:

``` bash
wine --version
wine64 --version
```

Confirm file types:

``` bash
file /usr/local/bin/wine
file /usr/local/bin/wine64
```

Expected output:

    /usr/local/bin/wine: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked
    /usr/local/bin/wine64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked

If you only see 64-bit binaries or the file command shows neither as executable, the 32-bit build didn’t complete successfully. Check the `build32/config.log` for errors and verify all i686 dependencies installed.

## Running Windows Applications

For any executable:

``` bash
wine ~/path/to/application.exe
```

The wine wrapper auto-detects the executable architecture and routes to the correct binary. However, if you need explicit control:

``` bash
wine ~/path/to/32bit-app.exe      # Force 32-bit
wine64 ~/path/to/64bit-app.exe    # Force 64-bit
```

## Using Wine Prefixes

Keep separate Wine configurations using the WINEPREFIX environment variable:

``` bash
WINEPREFIX=~/.wine32 wine program.exe
WINEPREFIX=~/.wine64 wine64 program.exe
```

Each prefix maintains isolated registry hives, system library configurations, and application data. This prevents conflicts when running applications with incompatible dependencies.

Initialize a new prefix explicitly:

``` bash
WINEPREFIX=~/.wine-app1 wine wineboot --init
```

For persistent use, set WINEPREFIX in your shell profile:

``` bash
echo 'export WINEPREFIX=~/.wine-gaming' >> ~/.bashrc
```

## Troubleshooting Build Failures

**Missing 32-bit linker errors**: The 32-bit build depends on a complete 64-bit build. Verify the 64-bit build finished without errors before starting 32-bit. Check for lines ending in `error:` in `build64/config.log`.

**Configure script fails**: Ensure the full Development Tools group is installed:

``` bash
sudo dnf groupinstall -y "Development Tools"
```

Then re-run the configure step.

**32-bit build complains about wine64 location**: The path in `--with-wine64=` must point to the actual build64 directory, not installed binaries. Use the relative path as shown above. Verify the directory exists:

``` bash
ls build64/dlls/
```

**Linker fails to find 32-bit libraries**: Force reinstall i686 packages:

``` bash
sudo dnf install --allowerasing -y glibc-devel.i686 libgcc.i686
```

**Runtime errors or application crashes**: Wine alone may not run modern DirectX applications. Consider installing DXVK for DirectX support:

``` bash
git clone https://github.com/doitsujin/dxvk.git
cd dxvk
./setup_dxvk.sh install
```

Alternatively, use Proton (Valve’s Wine fork) for gaming workloads, which includes DXVK and other enhancements by default.

## Maintaining Your Build

Keep the source and build directories for potential rebuilds. When Wine updates are released, repeat the build process:

``` bash
cd /tmp
rm -rf wine-9.0*
wget https://dl.winehq.org/wine/source/9.0/wine-9.x.tar.xz
tar xf wine-9.x.tar.xz
cd wine-9.x
mkdir build64 build32
# Repeat build steps above
```

Before installing a new version, uninstall the old one:

``` bash
cd old-wine-build/build64 && sudo make uninstall
cd ../build32 && sudo make uninstall
```

Or use `sudo dnf remove wine` if you want a clean state. Keep the source trees in `/opt` or `/usr/local/src` for long-term maintenance rather than `/tmp`, which may be cleaned by the system.
