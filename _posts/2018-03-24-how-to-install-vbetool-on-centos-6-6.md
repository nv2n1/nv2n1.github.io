---
title: "Building vbetool from Source on Rocky Linux 9"
date: 2018-03-24 11:45:21 +0000
modified: 2026-04-12 05:48:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-vbetool-on-centos-6-6/
---

\[md\]
vbetool is a utility for executing real-mode x86 BIOS calls, commonly used for power management and display mode switching on legacy systems. Rocky Linux 9 doesn’t include it in standard repositories, so you’ll need to build it from source.

\## What vbetool Does

vbetool communicates with the video BIOS through the Video BIOS Extensions (VBE) interface. It can:

– \*\*Change display modes\*\* — Switch resolutions on legacy VGA outputs
– \*\*Power management\*\* — Control monitor power states (DPMS standby, suspend, off)
– \*\*Save/restore video state\*\* — Preserve and restore the VGA register state across operations
– \*\*Post video cards\*\* — Re-initialize a video BIOS after certain hardware changes

This makes it particularly useful for headless servers that need occasional display management, or legacy systems where the kernel video drivers don’t fully support power management.

\## Prerequisites

Install the required development tools and dependencies:

```wp-block-code
sudo dnf groupinstall "Development Tools"
sudo dnf install pciutils-devel libx86-devel zlib-devel
```

On some systems, you may also need:

```wp-block-code
sudo dnf install kernel-devel
```

If you’re on Rocky Linux 8 or CentOS Stream, the same packages apply — just replace `dnf` with `yum` if needed.

\## Download and Prepare the Source

Fetch the latest vbetool source:

```wp-block-code
cd /tmp
wget http://www.codon.org.uk/~mjg59/vbetool/vbetool-1.2.3.tar.gz
tar xzf vbetool-1.2.3.tar.gz
cd vbetool-1.2.3
```

Check the Codon website for the current version number, as the above may be outdated. As of 2026, 1.2.3 remains the latest release, but it’s worth verifying.

\## Fix Library Path Issues

vbetool often has trouble locating `libpci.a`. Create a symbolic link to ensure the build process finds it:

```wp-block-code
sudo ln -s /usr/lib64/libpci.a /usr/local/lib64/libpci.a
```

On 32-bit systems (rare in 2026), use `/usr/lib/` instead:

```wp-block-code
sudo ln -s /usr/lib/libpci.a /usr/local/lib/libpci.a
```

If the static library doesn’t exist, you may need to install the static package:

```wp-block-code
sudo dnf install pciutils-static
```

\## Build and Install

Configure, compile, and install:

```wp-block-code
./configure
make
sudo make install
```

This installs vbetool to `/usr/local/bin/vbetool` by default.

Verify the installation:

```wp-block-code
vbetool --version
```

\## Common Usage Examples

Once installed, here are the most common operations:

\*\*Check current video mode:\*\*

```wp-block-code
sudo vbetool vbemode get
```

\*\*Set a specific video mode (e.g., mode 0x118 = 1024x768x16):\*\*

```wp-block-code
sudo vbetool vbemode set 0x118
```

\*\*Turn off the display (DPMS off):\*\*

```wp-block-code
sudo vbetool dpms off
```

\*\*Turn the display back on:\*\*

```wp-block-code
sudo vbetool dpms on
```

\*\*Save and restore video state (useful for scripting):\*\*

```wp-block-code
sudo vbetool vbestate save > /tmp/vbe.state
# ... do something that changes the display ...
sudo vbetool vbestate restore < /tmp/vbe.state
```

\*\*Post (re-initialize) the video card:\*\*

```wp-block-code
sudo vbetool post
```

The `post` command is particularly useful after resuming from suspend-to-RAM on systems where the video BIOS doesn't reinitialize properly.

\## Troubleshooting

\*\*Build errors with missing headers:\*\*

Check for multilib development packages:

```wp-block-code
sudo dnf install glibc-devel.i686 libx86-devel.i686
```

\*\*configure fails to find libpci:\*\*

Manually specify its location:

```wp-block-code
./configure LDFLAGS="-L/usr/lib64" CFLAGS="-I/usr/include/pci"
```

\*\*"vbetool: cannot open /dev/mem" error:\*\*

vbetool requires root access to access physical memory through `/dev/mem`. Always run it with `sudo`.

\*\*Kernel lockdown prevents access:\*\*

On systems with UEFI Secure Boot enabled, the kernel may block access to `/dev/mem`. You can check with:

```wp-block-code
cat /sys/kernel/security/lockdown
```

If it shows `integrity` or `confidentiality`, vbetool won't work unless you disable Secure Boot or adjust the lockdown mode.

\## Modern Systems Considerations

vbetool is primarily designed for legacy BIOS systems with classic VGA hardware. Here's what to consider on modern hardware:

\- \*\*UEFI systems\*\* typically don't need vbetool — the GOP (Graphics Output Protocol) handles display initialization
\- \*\*Kernel mode setting (KMS)\*\* manages display power states on most modern drivers (i915, amdgpu, nouveau)
\- \*\*systemd-logind\*\* handles lid-switch-based display power management automatically
\- For display brightness control on modern systems, use `xrandr` or write to `/sys/class/backlight/` instead

vbetool remains relevant for:
\- Legacy BIOS-only hardware still in production
\- Headless servers with old GPU passthrough configurations
\- Embedded systems with custom video BIOS implementations
\- Debugging VBE mode support on older hardware

\## Uninstalling

If you need to remove vbetool:

```wp-block-code
cd /tmp/vbetool-1.2.3
sudo make uninstall
```

Or manually remove the binary:

```wp-block-code
sudo rm /usr/local/bin/vbetool
```
