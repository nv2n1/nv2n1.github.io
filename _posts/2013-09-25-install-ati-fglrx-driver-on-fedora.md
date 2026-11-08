---
title: "Installing AMD GPU Drivers on Fedora: A Setup Guide"
date: 2013-09-25 10:32:06 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/install-ati-fglrx-driver-on-fedora/
---

The proprietary fglrx driver reached end-of-life in 2015 and is incompatible with current Fedora releases. For modern AMD GPUs, use AMDGPU—AMD’s actively maintained open-source driver that supports Wayland, current kernel versions, and both desktop and compute workloads.

## GPU Compatibility

**RDNA and newer** (RX 5000 series and later): AMDGPU is required and fully supported.

**GCN-era Radeons** (R9 290X, Fury, RX 400/500): AMDGPU is recommended, but the open-source `radeon` driver is included by default and provides basic 3D acceleration.

**Older Radeons** (pre-GCN): Use the `radeon` driver; AMDGPU may have limited support.

## Installing AMDGPU

### Enable RPM Fusion Repositories

AMDGPU packages are available in RPM Fusion’s free and nonfree repositories:

``` bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf makecache
```

### Install the Driver Stack

``` bash
sudo dnf install amdgpu-dkms libdrm-amdgpu vulkan-amdgpu
```

The `amdgpu-dkms` package automatically compiles the kernel module for your running kernel. When you install kernel updates, DKMS rebuilds the module automatically.

For gaming and 3D graphics:

``` bash
sudo dnf install vulkan-amdgpu-libs
```

For GPU compute workloads (HIP/ROCm):

``` bash
sudo dnf install rocm-hip rocm-smi rocm-core
```

Then reboot:

``` bash
sudo reboot
```

## Verify Installation

Confirm hardware detection:

``` bash
lspci | grep -i amd
```

Check that the kernel module loaded:

``` bash
lsmod | grep amdgpu
```

Inspect GPU details:

``` bash
rocm-smi
```

Verify Vulkan support:

``` bash
vulkaninfo --summary
```

Check GPU memory and temperature:

``` bash
rocm-smi --showmeminfo
rocm-smi --showtemp
```

## GPU Monitoring and Power Management

Monitor real-time GPU status:

``` bash
rocm-smi
watch -n 1 rocm-smi
```

Check temperature, clock speeds, and power draw:

``` bash
rocm-smi --showtemp
rocm-smi --sclk
rocm-smi --mclk
rocm-smi --showpower
```

Check GPU utilization:

``` bash
rocm-smi --showuse
```

Set performance level to control frequency scaling:

``` bash
rocm-smi --setperflevel high    # Maximum clocks
rocm-smi --setperflevel auto    # Dynamic scaling (default)
rocm-smi --setperflevel low     # Minimum clocks
```

Monitor kernel messages for thermal or driver events:

``` bash
dmesg | grep -i amdgpu | tail -20
journalctl -u amdgpu | tail -20
journalctl -b -p err..warn | grep -i amdgpu
```

## Troubleshooting

### GPU Not Detected or No 3D Acceleration

Verify the kernel module loaded:

``` bash
lsmod | grep amdgpu
```

If the module is missing, check Xorg logs:

``` bash
grep -i error /var/log/Xorg.0.log
grep -i amdgpu /var/log/Xorg.0.log
```

Check the systemd journal for driver errors:

``` bash
journalctl -xe | grep -i amdgpu
journalctl -b -p err
```

If Xorg isn’t installed or you’re on Wayland, check the Wayland compositor logs (GNOME and KDE log to journalctl).

### DKMS Kernel Module Build Failure

Install kernel headers matching your running kernel:

``` bash
sudo dnf install kernel-devel-$(uname -r)
```

Rebuild the DKMS module manually:

``` bash
sudo dkms autoinstall
```

Check DKMS logs:

``` bash
sudo cat /var/lib/dkms/amdgpu/*/build/make.log
```

Or trigger a rebuild explicitly:

``` bash
sudo dkms remove -m amdgpu -v $(dnf list installed amdgpu-dkms | tail -1 | awk '{print $2}') --all
sudo dkms install -m amdgpu -v $(dnf list installed amdgpu-dkms | tail -1 | awk '{print $2}')
```

### Wayland Display Server Issues

AMDGPU fully supports Wayland on GNOME and KDE. Verify your session type:

``` bash
echo $XDG_SESSION_TYPE
```

Should return `wayland`. If it returns `x11`, switch to Wayland at the login screen (usually a dropdown menu in the bottom-left).

### Screen Tearing on Wayland

GNOME compositing is enabled by default. For KDE Plasma, ensure compositing is enabled:

1.  Open System Settings
2.  Go to Workspace Behavior → Screen Locking
3.  Ensure “Block compositing when windows are maximized” is disabled

### Vulkan Not Detected

Verify Vulkan libraries are installed:

``` bash
vulkaninfo --summary
vulkan-config
```

If Vulkan layers are missing, reinstall the drivers:

``` bash
sudo dnf reinstall vulkan-amdgpu-libs amdgpu-dkms
sudo reboot
```

### GPU Overheating or Thermal Throttling

Monitor GPU temperature:

``` bash
watch -n 1 'rocm-smi --showtemp'
```

The GPU automatically throttles when approaching ~85°C. Ensure:

- Case has adequate ventilation
- Dust filters are clean
- GPU fans spin freely
- Thermal paste on the GPU heatsink isn’t degraded

If temperatures exceed 95°C consistently, check for dust buildup or insufficient airflow.

### HIP/ROCm Compute Not Working

Verify the ROCm installation:

``` bash
rocm-smi --showproductname
hipcc --version
```

Check that the user is in the `render` and `video` groups (required for GPU access without sudo):

``` bash
groups
sudo usermod -a -G render,video $USER
# Log out and back in for group changes to take effect
```

Test GPU compute access:

``` bash
rocm-smi --showmeminfo system
```

## Legacy Radeon Driver (GCN 1-3 Era)

Older GCN-era GPUs can use the open-source `radeon` driver, which is installed by default:

``` bash
lspci | grep -i radeon
lsmod | grep radeon
```

No additional installation is needed. The module loads automatically at boot. Basic 3D acceleration works out-of-the-box, though performance and feature support are limited. For better performance and modern features, install AMDGPU instead—it’s backward compatible with GCN-era cards.

## Why Not fglrx?

The proprietary fglrx (Catalyst) driver is unsupported on modern Fedora:

- No compatibility with Xorg 1.20+ or Xwayland
- No Wayland support
- Incompatible with kernel 5.10 and later
- No GNOME/KDE support past 2015
- No security updates since end-of-life in 2015

AMDGPU is the only supported path for AMD GPUs on modern Fedora systems.
