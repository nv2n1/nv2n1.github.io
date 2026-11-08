---
title: "Building with musl libc on Debian and Ubuntu"
date: 2018-03-24 11:44:46 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-musl-libc-on-linux-mint-17/
---

musl libc is a lightweight C library implementation that’s useful for creating statically-linked binaries, containerized applications, and embedded systems. It’s the standard C library in Alpine Linux and increasingly common in production environments.

## Installation from distribution repositories

The simplest approach is installing musl from your distribution’s repositories:

``` bash
sudo apt update
sudo apt install musl musl-dev musl-tools
```

This installs three packages:

- **musl**: the runtime library itself
- **musl-dev**: headers and static libraries for compilation
- **musl-tools**: includes the musl-gcc wrapper and other tooling

After installation, verify the setup:

``` bash
musl-gcc --version
which musl-gcc
```

## Compiling with musl

Once installed, compile C programs against musl instead of glibc using the `musl-gcc` wrapper:

``` bash
musl-gcc -static -o myapp myapp.c
```

The `-static` flag creates a fully self-contained binary with no libc dependencies—useful for containers, serverless environments, or distribution across systems.

For more complex projects using autoconf:

``` bash
./configure CC=musl-gcc --prefix=/usr/local/musl
make
sudo make install
```

## Installing a newer version

Distribution repositories often lag behind the latest musl releases. You have several options:

**Option 1: Build from source**

Download the latest from <a href="https://musl.libc.org" rel="nofollow noopener" target="_blank">musl.libc.org</a>:

``` bash
curl -O https://musl.libc.org/releases/musl-latest.tar.gz
tar xzf musl-latest.tar.gz
cd musl-*
./configure --prefix=/opt/musl
make
sudo make install
```

Then reference it explicitly in your builds:

``` bash
/opt/musl/bin/musl-gcc -static -o myapp myapp.c
```

**Option 2: Third-party PPAs (if available)**

Some community maintainers publish updated musl packages, though availability varies. Check your distribution’s package search before relying on external sources.

## Common use cases

**Static linking for containers:**

``` bash
musl-gcc -static -fPIC -o app app.c
docker build -t myapp .  # Copy the static binary
```

Static binaries work across any Linux distribution and Alpine-based containers without glibc present.

**Cross-compilation:**

musl-tools includes cross-compiler variants. For ARM:

``` bash
apt install musl-tools:armhf
arm-linux-musleabihf-gcc -static -o app-arm app.c
```

**Testing glibc vs musl compatibility:**

Compile the same program with both and compare behavior:

``` bash
gcc -o app-glibc app.c
musl-gcc -static -o app-musl app.c
./app-glibc
./app-musl
```

## Troubleshooting

If musl-gcc isn’t found after installation, ensure `/usr/bin` is in your PATH or use the full path to the binary. On systems with multiple libc implementations, explicitly pass the musl-gcc wrapper rather than relying on symlinks.

For compilation errors mentioning missing headers, verify musl-dev is installed:

``` bash
dpkg -l | grep musl
```

Some GNU extensions (like qsort_r) aren’t available in musl. Check the <a href="https://musl.libc.org/compatibility.html" rel="nofollow noopener" target="_blank">musl compatibility documentation</a> if code fails to compile.

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
