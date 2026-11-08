---
title: "Building musl libc on Fedora: From Source or Packages"
date: 2018-03-24 11:45:16 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-musl-libc-on-fedora-21-linux/
---

Fedora’s default repositories don’t include musl libc, but you have two practical options: install it from a community repository if available, or build from source. Building from source gives you full control and is the most reliable approach across Fedora versions.

## Option 1: Build from Source (Recommended)

Start by installing the build dependencies:

``` bash
sudo dnf install gcc make
```

Download the latest musl libc source from the official site. Check <a href="https://musl-libc.org/download.html" rel="nofollow noopener" target="_blank">musl-libc.org</a> for the current stable version:

``` bash
cd /tmp
wget https://musl.libc.org/releases/musl-1.2.5.tar.gz
tar xzf musl-1.2.5.tar.gz
cd musl-1.2.5
```

Configure and build:

``` bash
./configure --prefix=/usr/local/musl
make
```

The `--prefix` option ensures musl installs to `/usr/local/musl` rather than system paths, keeping it isolated from glibc. Install it:

``` bash
sudo make install
```

Add musl’s bin directory to your PATH permanently by editing `~/.bashrc`:

``` bash
export PATH="/usr/local/musl/bin:$PATH"
```

Then reload your shell:

``` bash
source ~/.bashrc
```

Verify the installation:

``` bash
musl-gcc --version
```

## Using musl-gcc for Compilation

Once installed, you can compile C programs with musl instead of glibc:

``` bash
musl-gcc -static -o myapp myapp.c
```

The `-static` flag bundles musl into the binary, creating a fully portable executable that doesn’t depend on the system libc.

For projects using autoconf, configure with:

``` bash
CC=musl-gcc ./configure --prefix=/usr/local/musl-build
make
make install
```

## Option 2: Check COPR Repositories

Some community maintainers provide musl packages via Fedora COPR. Search for available repositories:

``` bash
dnf copr search musl
```

If a relevant repository exists, enable it:

``` bash
sudo dnf copr enable <username>/musl
sudo dnf install musl musl-tools
```

This approach avoids compilation but depends on the repository being maintained for your Fedora version.

## Common Issues

**`musl-gcc: command not found`** — Make sure `/usr/local/musl/bin` is in your PATH. Check with `echo $PATH`.

**Compilation fails with missing headers** — Ensure `gcc` and `make` are installed: `sudo dnf install gcc make`.

**Static binaries still link glibc** — Verify you’re using `musl-gcc`, not `gcc`. Run `which musl-gcc` to confirm the correct binary is in use.

## Updating musl

To upgrade musl libc later, download a newer version, follow the same build steps, and reinstall. Your old version remains in `/usr/local/musl` until explicitly removed.

``` bash
sudo rm -rf /usr/local/musl
```

Building musl from source gives you the flexibility to maintain multiple versions or customize the installation for specific projects.

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
