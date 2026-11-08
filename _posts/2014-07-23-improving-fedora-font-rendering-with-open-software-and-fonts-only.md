---
title: "Font Configuration on Fedora: Using Open Source Fonts"
date: 2014-07-23 05:15:53 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /improving-fedora-font-rendering-with-open-software-and-fonts-only/
---

Fedora’s default font rendering works but benefits significantly from installing current font versions and tuning fontconfig. This guide covers practical font configuration using only free software and fonts available in standard repositories.

## Installing fonts

Fedora ships with Liberation fonts, but ensuring you have version 2.x (which renders substantially better than 1.x) is the first step.

### From repositories (recommended)

The simplest approach:

``` bash
sudo dnf install liberation-fonts dejavu-fonts noto-fonts noto-fonts-cjk
```

Verify the installed version:

``` bash
fc-match -v "Liberation Sans" | grep version
```

This should show 2.x. If your system has an older version, update:

``` bash
sudo dnf upgrade liberation-fonts
```

### Manual installation (specific versions)

If you need a version not in repositories, download from the <a href="https://github.com/liberationfonts/liberation-fonts/releases" rel="nofollow noopener" target="_blank">Liberation fonts repository</a>:

``` bash
# User-wide installation
mkdir -p ~/.local/share/fonts
tar -xzf liberation-fonts-ttf-*.tar.gz
cp liberation-fonts-ttf-*/LiberationSans-*.ttf ~/.local/share/fonts/

# Rebuild cache
fc-cache -fv
```

For system-wide installation:

``` bash
sudo mkdir -p /usr/share/fonts/truetype/liberation
sudo cp liberation-fonts-ttf-*/LiberationSans-*.ttf /usr/share/fonts/truetype/liberation/
sudo fc-cache -fv
```

## Configure fontconfig

Fontconfig controls how applications select and render fonts. Create `~/.config/fontconfig/fonts.conf` for user-specific settings or `/etc/fonts/local.conf` for system-wide changes (requires sudo):

``` xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Default font aliases -->
  <alias>
    <family>sans-serif</family>
    <prefer>
      <family>Liberation Sans</family>
      <family>DejaVu Sans</family>
      <family>Noto Sans</family>
    </prefer>
  </alias>

  <alias>
    <family>serif</family>
    <prefer>
      <family>Liberation Serif</family>
      <family>DejaVu Serif</family>
    </prefer>
  </alias>

  <alias>
    <family>monospace</family>
    <prefer>
      <family>Liberation Mono</family>
      <family>DejaVu Sans Mono</family>
    </prefer>
  </alias>

  <!-- Font rendering settings -->
  <match target="font">
    <edit name="antialias" mode="assign">
      <bool>true</bool>
    </edit>
    <edit name="hinting" mode="assign">
      <bool>true</bool>
    </edit>
    <edit name="hintstyle" mode="assign">
      <const>hintslight</const>
    </edit>
    <edit name="rgba" mode="assign">
      <const>rgb</const>
    </edit>
  </match>
</fontconfig>
```

The `hintslight` setting provides good balance for screen rendering—it applies enough hinting for clarity without distorting letterforms. `hintfull` can appear too bold on most displays.

Reload the cache to apply changes:

``` bash
fc-cache -fv
```

## GNOME font settings

If running GNOME, configure fonts through dconf. You can use the GUI editor or command line:

``` bash
gsettings set org.gnome.desktop.interface font-name "Liberation Sans 10"
gsettings set org.gnome.desktop.interface document-font-name "Liberation Serif 11"
gsettings set org.gnome.desktop.interface monospace-font-name "Liberation Mono 10"
```

To open the GUI editor:

``` bash
sudo dnf install dconf-editor
dconf-editor
```

Navigate to `org.gnome.desktop.interface` to adjust font names and sizes. Most GNOME and GTK applications respect fontconfig settings immediately, though some may require a restart.

## Recommended font packages

Beyond Liberation, these open source fonts improve rendering coverage:

``` bash
sudo dnf install ibm-plex-fonts google-roboto-fonts
```

- **DejaVu** — excellent serif and sans-serif with extensive Unicode support
- **Noto** — covers most writing systems; particularly useful for CJK characters
- **IBM Plex** — modern professional typeface family
- **Google Roboto** — clean sans-serif optimized for screen display

## Verify configuration

Test your settings:

``` bash
fc-list | grep -i liberation
fc-match -v sans | head -20
```

The second command shows which font is selected for sans-serif requests and its rendering properties. Open a terminal, web browser, and text editor to verify fonts render cleanly without pixelation or excessive boldness.

If a specific application ignores your fontconfig settings, check whether it uses a toolkit other than GTK (Qt applications, for example, may require separate configuration). Most terminal emulators respect fontconfig directly—configure your preferred monospace font there as well.

After applying fontconfig changes to `/etc/fonts/local.conf`, always run `sudo fc-cache -fv` to rebuild the system font cache.
