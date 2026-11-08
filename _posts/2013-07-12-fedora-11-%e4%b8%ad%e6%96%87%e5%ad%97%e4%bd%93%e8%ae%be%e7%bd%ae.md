---
title: "Chinese Character Support on Fedora 11"
date: 2013-07-12 16:31:37 +0000
author: "Eric Ma"
layout: post
permalink: /fedora-11-%e4%b8%ad%e6%96%87%e5%ad%97%e4%bd%93%e8%ae%be%e7%bd%ae/
canonical: https://www.systutorials.com/fedora-11-%e4%b8%ad%e6%96%87%e5%ad%97%e4%bd%93%e8%ae%be%e7%bd%ae/
---

Configuring proper Chinese character rendering in Fedora requires attention to font selection and system settings. This guide covers configuration for contemporary Fedora/RHEL systems where you run an English locale but need reliable Chinese character display.

## Font Selection

You have several solid open-source options for Chinese fonts. Each has different characteristics suited to different use cases.

### Using UMing and UKai Fonts

The AR PL UMing and UKai fonts provide good rendering across most applications. Install them via:

``` bash
sudo dnf install cjkuni-ukai-fonts cjkuni-uming-fonts
```

Configure font preferences in `~/.config/fontconfig/fonts.conf` (modern Fontconfig uses this path instead of `~/.fonts.conf`):

``` xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Set preferred Chinese fonts for sans-serif -->
  <match target="pattern">
    <test qual="any" name="family">
      <string>sans-serif</string>
    </test>
    <edit name="family" mode="prepend" binding="strong">
      <string>AR PL UMing CN</string>
    </edit>
  </match>

  <!-- Set preferred Chinese fonts for serif -->
  <match target="pattern">
    <test qual="any" name="family">
      <string>serif</string>
    </test>
    <edit name="family" mode="prepend" binding="strong">
      <string>AR PL UMing CN</string>
    </edit>
  </match>

  <!-- Set preferred Chinese fonts for monospace -->
  <match target="pattern">
    <test qual="any" name="family">
      <string>monospace</string>
    </test>
    <edit name="family" mode="prepend" binding="strong">
      <string>AR PL UMing Mono CN</string>
    </edit>
  </match>

  <!-- Enable font smoothing -->
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
  </match>
</fontconfig>
```

After modifying the config, reload Fontconfig:

``` bash
fc-cache -fv
```

### Using WenQuanYi Fonts

WenQuanYi is a comprehensive open-source font project with excellent coverage. Installation is straightforward:

``` bash
sudo dnf install wqy-microhei wqy-microhei-light wqy-bitmapfont
```

Then add to your Fontconfig similarly:

``` xml
<match target="pattern">
  <test qual="any" name="family">
    <string>sans-serif</string>
  </test>
  <edit name="family" mode="prepend" binding="strong">
    <string>WenQuanYi Micro Hei</string>
  </edit>
</match>
```

### Other Available Options

Modern Fedora repositories include:

- `noto-fonts-cjk` — Google’s Noto Sans CJK, comprehensive and well-maintained
- `source-han-sans-fonts` / `source-han-serif-fonts` — Adobe’s Source Han fonts
- `lato-fonts` — Good Latin coverage with reasonable Chinese support

Stick with open-source fonts. Avoid proprietary Microsoft fonts; they violate licensing terms and open-source alternatives are now comparable in quality.

## Desktop Environment Integration

### GNOME/GNOME Wayland

Font settings in GNOME 45+ are managed through `gnome-control-center`:

``` bash
gnome-control-center fonts
```

Enable hinting and antialiasing through the interface, or configure via dconf:

``` bash
gsettings set org.gnome.desktop.interface font-name 'Cantarell 11'
gsettings set org.gnome.desktop.interface monospace-font-name 'Monospace 10'
gsettings set org.gnome.desktop.interface document-font-name 'Cantarell 10'
```

### KDE Plasma

In KDE Settings → Appearance → Fonts, set your preferred Chinese font as a fallback.

## Terminal and Monospace Applications

For terminal emulators and text editors, ensure your terminal font supports CJK. Recommended monospace fonts:

- `noto-fonts-monospace-cjk`
- `sarasa-gothic-fonts` (Sarasa Gothic has excellent monospace CJK rendering)

Configure in your terminal emulator settings (GNOME Terminal, Konsole, etc.) directly.

## Emacs Configuration

Emacs often benefits from explicit locale configuration. Create a wrapper script at `~/bin/emacs-cjk`:

``` bash
#!/bin/bash
export LANG=zh_CN.UTF-8
exec /usr/bin/emacs "$@"
```

Make it executable:

``` bash
chmod +x ~/bin/emacs-cjk
```

Then add to your Emacs configuration (`~/.config/emacs/init.el` or `~/.emacs.d/init.el`):

```elisp
;; Set preferred fonts for CJK
(set-face-attribute 'default nil :font "Monospace 10")
(dolist (charset '(kana han symbol cjk-misc bopomofo))
  (set-fontset-font (frame-parameter nil 'fontset)
                    charset
                    (font-spec :family "Noto Sans Mono CJK SC" :size 10)))
```

Or use the simpler approach of aliasing your terminal’s emacs command to the wrapper script in your shell configuration.

## Verification

Test font rendering by checking available fonts:

``` bash
fc-list :lang=zh
```

This lists all fonts with Chinese language support. Verify a specific font is installed:

``` bash
fc-list | grep "WenQuanYi\|UMing\|Noto Sans CJK"
```

Restart your applications after modifying Fontconfig to load the new settings. Some applications cache font information and won’t reflect changes until restarted.

## Troubleshooting

If Chinese characters still display as boxes or broken glyphs:

1.  Verify the font package actually installed: `rpm -q cjkuni-uming-fonts`
2.  Check Fontconfig syntax: `xmllint ~/.config/fontconfig/fonts.conf`
3.  Clear the Fontconfig cache: `fc-cache -fv`
4.  Inspect which font is actually being used in your application (many have font debugging options)
5.  Some older X11 applications may need core fonts; install `xorg-x11-fonts-misc` for fallback support

Modern distributions have largely moved to Fontconfig and Xft rendering, making Chinese character support substantially more reliable than in older Fedora releases.
