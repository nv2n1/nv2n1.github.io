---
title: "Enable RPM Fusion Repository on RHEL 9 and Rocky Linux"
date: 2018-03-24 11:45:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-enable-rpm-fusion-for-centos-6-6/
---

RPM Fusion provides packages that Fedora and RHEL can’t ship by default due to patent, licensing, or trademark restrictions. This includes multimedia codecs, proprietary drivers, and other software. Here’s how to enable it on RHEL 9 and Rocky Linux.

## Enable RPM Fusion Free and Non-Free

```wp-block-code
# Enable EPEL first (required dependency)
sudo dnf install epel-release

# Enable RPM Fusion Free
sudo dnf install \
  https://download1.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm

# Enable RPM Fusion Non-Free
sudo dnf install \
  https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm
```

On Rocky Linux, EPEL is already available in the BaseOS repository, so `dnf install epel-release` should work directly.

## Verify Installation

```wp-block-code
dnf repolist | grep rpmfusion
```

You should see both `rpmfusion-free` and `rpmfusion-nonfree` repositories listed.

## Install Multimedia Codecs

One of the most common reasons to enable RPM Fusion is to install media playback codecs:

```wp-block-code
# Install multimedia playback
sudo dnf groupinstall multimedia

# Install sound and video codecs
sudo dnf groupinstall sound-and-video

# Install individual codecs
sudo dnf install gstreamer1-plugins-bad-free gstreamer1-plugins-bad-freeworld
sudo dnf install gstreamer1-plugins-ugly-free gstreamer1-plugins-ugly-freeworld
sudo dnf install ffmpeg
```

## Install Proprietary Drivers

RPM Fusion Non-Free provides proprietary GPU drivers:

```wp-block-code
# Nvidia proprietary driver
sudo dnf install akmod-nvidia
sudo akmods --force
sudo dracut --force
```

Reboot after installing Nvidia drivers. Verify with:

```wp-block-code
nvidia-smi
```

## Enable AppStream Data

For software centers (GNOME Software, KDE Discover) to show RPM Fusion packages:

```wp-block-code
# Install AppStream metadata
sudo dnf install rpmfusion-free-appstream-data rpmfusion-nonfree-appstream-data
```

## Configure Package Priorities

To prevent RPM Fusion packages from overriding base system packages, install `dnf-plugins-core` and set priorities:

```wp-block-code
sudo dnf install dnf-plugins-core

# Prefer base repos over RPM Fusion for overlapping packages
sudo dnf config-manager --setopt="rpmfusion-free.priority=10" --save
sudo dnf config-manager --setopt="rpmfusion-nonfree.priority=10" --save
```

## Troubleshooting

**Repository not found:**

```wp-block-code
# Clear DNF cache and retry
sudo dnf clean all
sudo dnf makecache
```

**GPG key import fails:**

```wp-block-code
# Manually import RPM Fusion keys
sudo rpm --import https://rpmfusion.org/keys/RPM-GPG-KEY-rpmfusion-free-el-9
sudo rpm --import https://rpmfusion.org/keys/RPM-GPG-KEY-rpmfusion-nonfree-el-9
```

**Packages not showing in GNOME Software:**

```wp-block-code
# Restart the software center after enabling repos
sudo dnf install rpmfusion-free-appstream-data
killall gnome-software
```

## What’s Available in RPM Fusion

**Free repository:** Open-source software that can’t be in Fedora due to patent concerns (multimedia codecs like x264, x265, AAC).

**Non-Free repository:** Proprietary software and drivers (Nvidia drivers, Steam, certain firmware).

Common packages people install from RPM Fusion:

- `ffmpeg` — Video/audio processing
- `VLC` — Media player
- `akmod-nvidia` — Nvidia proprietary driver
- `steam` — Gaming platform
- `chromium-ffmpeg` — Additional codecs for Chromium

## RPM Fusion on Rocky Linux vs RHEL

Rocky Linux is a downstream rebuild of RHEL, so RPM Fusion works identically on both. The key difference is that Rocky includes EPEL in its default repositories, while on RHEL you may need to enable it manually.

On RHEL 9 specifically, you may also need to enable the CRB (CodeReady Builder) repository:

```wp-block-code
# RHEL 9 only
sudo subscription-manager repos --enable codeready-builder-for-rhel-9-x86_64-rpms

# Rocky Linux 9
sudo dnf config-manager --enable crb
```

Some RPM Fusion packages have build dependencies in CRB, so enabling it prevents dependency resolution failures.

## Disabling RPM Fusion Temporarily

If you need to install a package from base repos without RPM Fusion interference:

```wp-block-code
# Disable RPM Fusion for a single transaction
sudo dnf install --disablerepo='*rpmfusion*' package-name

# Disable permanently (can re-enable later)
sudo dnf config-manager --set-disabled rpmfusion-free
sudo dnf config-manager --set-disabled rpmfusion-nonfree

# Re-enable
sudo dnf config-manager --set-enabled rpmfusion-free
sudo dnf config-manager --set-enabled rpmfusion-nonfree
```
