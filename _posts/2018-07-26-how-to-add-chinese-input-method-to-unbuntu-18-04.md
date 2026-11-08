---
title: "Ubuntu Chinese Input: IBus vs Fcitx5 Setup"
date: 2018-07-26 04:53:40 +0000
modified: 2026-04-11 15:43:26 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-add-chinese-input-method-to-unbuntu-18-04/
---

Linux input method frameworks have matured significantly over the past few years. Ubuntu offers two solid options: IBus (integrated into GNOME by default) and Fcitx5 (more feature-rich and actively maintained). This guide covers both approaches and helps you choose the right one for your setup.

## IBus: Quick Setup for Basic Use

IBus comes pre-installed on most Ubuntu systems and requires minimal configuration.

1.  Open **Settings** → **Keyboard** → **Input Sources**
2.  Click the **+** button and search for “Chinese (Intelligent Pinyin)”
3.  Add it to your input sources
4.  Switch between input methods using **Super + Space** (or configure a custom shortcut in Input Sources)

IBus works adequately for basic typing but lacks predictive features and customization options. If you need more power, skip to Fcitx5.

## Fcitx5: The Recommended Approach

Fcitx5 offers better predictive text, cloud pinyin support, superior Wayland compatibility, and active development. Most users who work regularly with Chinese text prefer it.

### Installation

First, update your package manager and install the core components:

``` bash
sudo apt update
sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-frontend-gtk3 fcitx5-frontend-qt5
```

For GNOME desktop, also install the input method panel extension:

``` bash
sudo apt install gnome-shell-extension-kimpanel
```

### Configuration

Set Fcitx5 as your default input method:

1.  Open **Settings** → **Language Support** (if not present, run `sudo apt install language-support-zh`)
2.  Set “Keyboard input method system” to **Fcitx 5**
3.  **Log out completely and log back in** — a GNOME Shell restart is insufficient

After logging back in, switch input methods using **Ctrl + Space**. Access configuration via:

``` bash
fcitx5-configtool
```

## Customizing Fcitx5

### Appearance Settings

Edit the configuration file directly:

``` bash
nano ~/.config/fcitx5/conf/classicui.conf
```

Common customizations include font size, theme selection, and candidate window position. After making changes, reload Fcitx5:

``` bash
fcitx5-remote -r
```

### Enabling Cloud Pinyin

Cloud pinyin provides real-time word suggestions for improved accuracy with modern terminology and proper nouns:

1.  Open **Fcitx5 Configuration Tool** (`fcitx5-configtool`)
2.  Navigate to the **Add-ons** tab
3.  Enable **Cloud Pinyin**
4.  Choose your provider (Baidu or Sogou are common options)

Note that cloud pinyin requires an active internet connection and depends on your chosen provider’s availability in your region.

## Alternative Input Methods

For Cantonese (Jyutping), Wubi, Five-stroke, or other schemes:

``` bash
sudo apt install fcitx5-table fcitx5-table-other
```

Then add them via the configuration tool:

1.  Open `fcitx5-configtool`
2.  Click **Add Input Method**
3.  Select your desired scheme (Cantonese Jyutping, Wubi, Five-stroke, etc.)
4.  Click **Add**

## Wayland Compatibility

Modern Ubuntu versions default to Wayland. Both IBus and Fcitx5 support it, but with different characteristics:

- **IBus**: Works reliably in GNOME but may have issues with X11 applications running under XWayland
- **Fcitx5**: More consistent Wayland support, including better integration with Flatpak applications

Check your current session:

``` bash
echo $XDG_SESSION_TYPE
```

For Flatpak applications, install the official Fcitx5 Flatpak runtime for seamless integration:

``` bash
flatpak install flathub org.fcitx.Fcitx5
```

For individual Flatpak apps, grant filesystem access:

``` bash
flatpak override --user --filesystem=xdg-config/fcitx5 com.example.app
```

## Troubleshooting

### Input method not appearing after installation

Ensure you’ve logged out completely (not just locked the screen). A full system reboot is the safest approach:

``` bash
sudo reboot
```

### Fcitx5 not responding in specific applications

Check if the application is running under XWayland:

``` bash
ps aux | grep -E "Xwayland|application-name"
```

For Flatpak apps, verify Fcitx5 integration or use the Fcitx5 Flatpak as described above.

### Cloud pinyin not working

Verify internet connectivity and check Fcitx5 logs:

``` bash
journalctl --user -u fcitx5 -f
```

Confirm that your chosen cloud provider (Baidu, Sogou) is accessible from your network and not blocked by local firewall rules.

### IBus and Fcitx5 conflicts

If you’ve already installed IBus and want to switch to Fcitx5, remove IBus to avoid conflicts:

``` bash
sudo apt remove ibus ibus-libpinyin ibus-libzhuyin
sudo apt autoremove
```

Then reconfigure language settings as described above.

### Input method stops working after system updates

Fcitx5 occasionally requires reinitialization after kernel or desktop environment updates. Try reloading it:

``` bash
fcitx5-remote -r
```

Or log out and back in. If problems persist, reset Fcitx5 to defaults:

``` bash
rm -rf ~/.config/fcitx5
sudo apt reinstall fcitx5 fcitx5-chinese-addons
```

This preserves configuration templates while clearing any corrupted state.
