---
title: "Building and Installing a Linux Kernel from Source"
date: 2017-03-18 11:32:13 +0000
modified: 2026-04-11 16:21:15 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /compile-install-linux-kernel-source-code-existing-linux-os/
---

Grab a release from <a href="https://www.kernel.org" rel="nofollow noopener" target="_blank">kernel.org</a>. Recent stable versions (6.x and later) are recommended for production systems:

``` bash
wget https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.tar.gz
tar xf linux-6.12.tar.gz
cd linux-6.12/
```

If `wget` isn’t available, use `curl`:

``` bash
curl -O https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.tar.gz
```

### Verify the tarball

Always verify the kernel’s integrity using checksums and signatures published on kernel.org. This is essential for production systems:

``` bash
wget https://www.kernel.org/pub/linux/kernel/v6.x/linux-6.12.tar.gz.asc
gpg --verify linux-6.12.tar.gz.asc linux-6.12.tar.gz
```

You should see output like `gpg: Good signature from "Linux Kernel Release Signing Key"`. If GPG isn’t configured with kernel.org’s public key, import it first:

``` bash
gpg --keyserver keyserver.ubuntu.com --recv-keys 647F28654894E3BD457199BE38DBBDC86092693E
```

## Install build dependencies

Required packages vary by distribution. On RHEL/CentOS/Rocky/Fedora:

``` bash
sudo dnf install gcc make ncurses-devel openssl-devel elfutils-devel \
  flex bison pahole
```

On Debian/Ubuntu:

``` bash
sudo apt-get install build-essential ncurses-dev libssl-dev libelf-dev \
  flex bison dwarves
```

The `elfutils-devel`/`libelf-dev` packages handle BTF (BPF Type Format) support, now standard in modern kernels. The `pahole`/`dwarves` packages are required for BTF generation during the build. `flex` and `bison` are needed for kernel configuration parsing.

Verify your GCC version matches what your distribution uses for its kernel:

``` bash
gcc --version
```

For development work or building external kernel modules, also install:

``` bash
# RHEL/CentOS/Rocky
sudo dnf install kernel-devel

# Debian/Ubuntu
sudo apt-get install linux-headers-$(uname -r)
```

## Prepare a kernel configuration

Compiling a kernel from scratch requires extensive knowledge of hardware and subsystems. Instead, reuse your existing kernel’s configuration as a starting point:

``` bash
ls /boot/config-*
cp /boot/config-$(uname -r) .config
```

Update the configuration for your target kernel version:

``` bash
make oldconfig
```

This processes your old config against new kernel options, prompting you only for settings that didn’t exist in your previous version. For non-interactive use (accepts defaults for new options):

``` bash
make olddefconfig
```

### Interactive configuration

If you need to customize options, use a configuration tool. The modern ncurses interface is recommended:

``` bash
make nconfig
```

This provides search functionality (press `/`), which is much faster than navigating through `menuconfig` on large configurations. You can toggle options with Space (Y for built-in, M for module, N to disable).

Alternative interfaces:

``` bash
make menuconfig    # classic ncurses interface
make xconfig       # Qt-based GUI (requires X11)
```

Both will validate settings and warn about incompatibilities:

    .config:444:warning: symbol value 'm' invalid for MICROCODE
    .config:618:warning: symbol value 'm' invalid for CPU_FREQ_STAT

These warnings are usually harmless—the build process will automatically disable invalid options.

To review your current configuration without editing:

``` bash
grep "^CONFIG" .config | head -30
```

## Build and install

Compile using all available CPU cores to significantly reduce build time:

``` bash
make -j $(nproc)
```

This spawns one job per CPU core. On a 16-core system, this is dramatically faster than single-threaded compilation.

Install the modules and kernel:

``` bash
sudo make modules_install
sudo make install
```

To combine these steps with error handling:

``` bash
make -j $(nproc) && sudo make modules_install && sudo make install
```

This runs sequentially and fails fast if any step breaks. Successful completion shows:

    INSTALL /lib/firmware/...
    DEPMOD  6.12.0
    sh ./arch/x86/boot/install.sh 6.12.0 arch/x86/boot/bzImage
            System.map "/boot"

The `make install` step updates your bootloader automatically on most distributions.

### Verify the bootloader entry

**For GRUB 2 (RHEL/CentOS/Rocky):**

``` bash
grep -A3 "6.12.0" /boot/grub2/grub.cfg
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

**For GRUB 2 (Debian/Ubuntu):**

``` bash
grep -A3 "6.12.0" /boot/grub/grub.cfg
sudo update-grub
```

**For systemd-boot** (common on newer installations):

``` bash
ls /boot/loader/entries/
cat /boot/loader/loader.conf
```

Check if an entry exists for your new kernel version in `/boot/loader/entries/`.

## Boot the new kernel

Reboot your system:

``` bash
sudo reboot
```

During startup, select the new kernel from the GRUB menu, or set it as default:

**RHEL/CentOS/Rocky:**

``` bash
sudo grub2-set-default "Rocky Linux (6.12.0) 9"
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

**Debian/Ubuntu:**

``` bash
sudo update-grub
```

**systemd-boot:**

``` bash
sudo bootctl set-default linux-6.12.0
```

After rebooting, verify the running kernel:

``` bash
uname -r
uname -a
```

Check that modules loaded correctly:

``` bash
sudo dmesg | grep -i "modules"
lsmod | head -10
```

## Troubleshooting

### Build fails with missing headers

Ensure build tools are installed. RHEL systems may need `kernel-devel` for in-tree module builds. If you skipped distro-provided kernel headers, some drivers won’t compile. Reinstall dependencies if needed.

### Compilation fails partway through

Common causes include missing dependencies or insufficient disk space. A full kernel build can consume 15–20GB in `/usr/src`. Check available space:

``` bash
du -sh linux-6.12/
df -h /
```

If disk space is low, clean previous builds:

``` bash
make distclean
```

Then restart the build.

### Module signature issues

Newer kernels enforce module signing by default. If external module builds fail with signature errors, either disable signing in `.config`:

``` bash
sed -i 's/CONFIG_MODULE_SIG=y/CONFIG_MODULE_SIG=n/' .config
make clean
make -j $(nproc)
```

Then rebuild. For custom kernels, module signing often causes friction—disabling it is usually the practical choice unless you have specific security requirements (like Secure Boot).

### GRUB doesn’t find the new kernel

Manually regenerate the bootloader configuration:

``` bash
# RHEL/CentOS
sudo grub2-mkconfig -o /boot/grub2/grub.cfg

# Debian/Ubuntu
sudo update-grub
```

### Compilation takes too long

Use `make -j $(nproc)` to parallelize across all cores. A typical kernel takes 10–30 minutes on modern hardware depending on configuration. To speed things up further, disable unnecessary drivers in `nconfig`:

- Disable unused hardware support (SCSI, storage controllers you don’t use)
- Remove unneeded filesystems
- Disable network protocols not in use

Each of these can shave several minutes off the build.

### Reverting to the old kernel

If the new kernel doesn’t work, reboot and select your previous kernel from GRUB. Once you’ve confirmed the old kernel works, remove the broken one:

``` bash
sudo rm /boot/vmlinuz-6.12.0 /boot/initramfs-6.12.0.img /boot/System.map-6.12.0
sudo update-grub  # or grub2-mkconfig on RHEL/CentOS
```

The kernel modules remain in `/lib/modules/6.12.0/` until you manually delete them:

``` bash
sudo rm -rf /lib/modules/6.12.0/
```
