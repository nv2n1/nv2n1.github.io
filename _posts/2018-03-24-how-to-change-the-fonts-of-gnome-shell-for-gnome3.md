---
title: "Customizing GNOME Shell Fonts in GNOME 3"
date: 2018-03-24 08:20:24 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-change-the-fonts-of-gnome-shell-for-gnome3/
---

GNOME Shell in GNOME 3 uses a specific font for the top bar, activities overview, and system notifications. You can customize these fonts using GNOME Tweaks or dconf to match your preferences.

## Using GNOME Tweaks (Recommended)

```wp-block-code
# Install GNOME Tweaks
sudo dnf install gnome-tweaks    # Fedora
sudo apt install gnome-tweaks    # Ubuntu
```

Open GNOME Tweaks and navigate to:

1.  **Appearance** section
2.  Under “Fonts”, you’ll find options for:
    - **Interface Text** — Font used in GNOME Shell UI elements
    - **Document Text** — Default font for documents
    - **Monospace Text** — Fixed-width font for terminal and code
    - **Legacy Window Title Text** — Title bar font (for non-headerbar apps)

Change the Interface Text font to affect GNOME Shell’s top bar, calendar, notifications, and system dialogs.

## Using dconf for Direct Configuration

If you prefer the command line or need to script font changes:

```wp-block-code
# View current font settings
dconf read /org/gnome/desktop/interface/font-name
dconf read /org/gnome/desktop/interface/document-font-name
dconf read /org/gnome/desktop/interface/monospace-font-name

# Set interface font
dconf write /org/gnome/desktop/interface/font-name "'Noto Sans 11'"

# Set document font
dconf write /org/gnome/desktop/interface/document-font-name "'Noto Sans 11'"

# Set monospace font
dconf write /org/gnome/desktop/interface/monospace-font-name "'Noto Sans Mono 11'"

# Set text scaling factor (for HiDPI or accessibility)
dconf write /org/gnome/desktop/interface/text-scaling-factor 1.25
```

## Install Additional Fonts

Popular font packages on Fedora:

```wp-block-code
# Google Noto fonts (comprehensive Unicode coverage)
sudo dnf install google-noto-sans-fonts google-noto-serif-fonts

# Inter (modern UI font)
sudo dnf install inter-fonts

# IBM Plex (professional sans-serif)
sudo dnf install ibm-plex-sans-fonts ibm-plex-mono-fonts

# Hack (monospace for developers)
sudo dnf install hack-fonts

# JetBrains Mono (popular developer font)
sudo dnf install jetbrains-mono-fonts
```

Install fonts manually by copying `.ttf` or `.otf` files to `~/.local/share/fonts/` and running `fc-cache -fv`.

## Font Rendering Tuning

Improve font appearance with rendering settings:

```wp-block-code
# Enable antialiasing
dconf write /org/gnome/settings-daemon/plugins/xsettings/antialiasing "'rgba'"

# Set hinting
dconf write /org/gnome/settings-daemon/plugins/xsettings/hinting "'slight'"

# Or use fontconfig for more control
mkdir -p ~/.config/fontconfig
cat > ~/.config/fontconfig/fonts.conf << 'EOF'


  
    true
    true
    hintslight
    rgb
    lcddefault
  

EOF
```

## GNOME Shell Theme Fonts

Some GNOME Shell themes override the system font. To use your custom font with a theme:

```wp-block-code
# Check which theme is active
dconf read /org/gnome/shell/extensions/user-theme/name

# Edit the theme's CSS if needed
# Theme files are in ~/.themes/themename/gnome-shell/gnome-shell.css
# Look for "font-family" declarations and modify them
```

## Quick Reference

- `gnome-tweaks` — GUI font configuration
- `dconf write .../font-name "'Font Name 11'"` — Set font via CLI
- `~/.local/share/fonts/` — User font directory
- `fc-cache -fv` — Rebuild font cache
- `fc-list | grep FontName` — Verify font is installed

## Per-Application Font Override

Override fonts for specific applications without changing system-wide settings. For GTK applications, you can set environment variables before launching. For terminal emulators, set the font in the terminal own preferences independently of the GNOME system font.

## Fixing Blurry Fonts on Wayland

If fonts appear blurry on Wayland, especially with fractional scaling:

```wp-block-code
# Enable XWayland scaling fix
dconf write /org/gnome/mutter/xwayland-allow-scale-monitor-configuration true

# Or switch to X11 session at login
# Click gear icon and select "GNOME on Xorg"
```

Fractional scaling (125%, 150%) can cause font rendering issues on Wayland. Using integer scaling (100%, 200%) or the X11 session avoids this problem entirely.

## Debugging Font Issues

```wp-block-code
# List all installed fonts
fc-list | sort

# Check which font matches a pattern
fc-match "sans-serif"
fc-match "serif"
fc-match "monospace"

# Rebuild font cache
fc-cache -fv
```
