---
title: "Customizing Fonts in GNOME: GUI and CLI Methods"
date: 2014-03-30 08:01:01 +0000
layout: post
canonical: https://www.systutorials.com/customizing-fonts-in-gnome-3/
---

GNOME’s default Settings app doesn’t expose comprehensive font options, but GNOME Tweaks and command-line tools give you full control over typefaces across the desktop, shell, and window decorations.

## Installing GNOME Tweaks

GNOME Tweaks is the easiest way to customize fonts. Install it on your system:

**Fedora:**

``` bash
sudo dnf install gnome-tweaks
```

**Debian/Ubuntu:**

``` bash
sudo apt install gnome-tweaks
```

**Arch:**

``` bash
sudo pacman -S gnome-tweaks
```

## Configuring Fonts in GNOME Tweaks

Open GNOME Tweaks and navigate to the **Appearance** tab (in newer versions) or **Fonts** section. You can customize:

- **Interface Font** — controls UI elements (buttons, menus, labels)
- **Document Font** — used in text editors and document viewers
- **Monospace Font** — applied to terminals and code editors
- **Legacy Window Titles** — titlebar font (if available in your GNOME version)

Changes apply immediately in most cases. If they don’t, restart GNOME Shell:

``` bash
killall -HUP gnome-shell
```

Or use the older method (Alt+F2, type `r`, press Enter).

## Configuring Window Title Fonts with gsettings

GNOME Tweaks may not expose all titlebar font options. Use `gsettings` directly for finer control:

``` bash
gsettings set org.gnome.desktop.wm.preferences titlebar-font 'Sans Bold 11'
gsettings set org.gnome.desktop.wm.preferences titlebar-uses-system-font false
```

Check your current settings:

``` bash
gsettings get org.gnome.desktop.wm.preferences titlebar-font
```

Reset to defaults:

``` bash
gsettings reset org.gnome.desktop.wm.preferences titlebar-font
```

Font format is `'FontName Style Size'`. Common examples:

- `'Sans 10'`
- `'Monospace Bold 12'`
- `'Noto Serif 11'`
- `'Ubuntu Mono 13'`

Size is in points, not pixels.

## Customizing GNOME Shell Theme Fonts

GNOME Shell (the top bar, notifications, Activities overview) uses CSS-based styling. To modify shell fonts:

First, check which theme you’re using:

``` bash
gsettings get org.gnome.shell.extensions.user-theme name
```

System themes are typically in `/usr/share/gnome-shell/themes/[theme-name]/gnome-shell.css`. User themes are in `~/.local/share/gnome-shell/themes/[theme-name]/gnome-shell.css`.

Before editing, create a backup:

``` bash
cp gnome-shell.css gnome-shell.css.bak
```

Edit the CSS file and modify font declarations:

``` css
stage {
  font-family: 'Noto Sans', sans-serif;
  font-size: 11pt;
}

#panel {
  font-size: 11pt;
  font-weight: 500;
}

.clock-display {
  font-family: 'Monospace';
  font-size: 12pt;
}
```

After saving, restart GNOME Shell:

``` bash
killall -HUP gnome-shell
```

If changes don’t apply, log out and back in.

## System-Wide Font Configuration

To set GTK font defaults that apply across most applications, edit `~/.config/gtk-3.0/settings.ini`:

``` ini
[Settings]
gtk-font-name = Noto Sans 10
gtk-monospace-font-name = Noto Mono 10
```

For GTK 4 applications (increasingly common), also create or edit `~/.config/gtk-4.0/settings.ini`:

``` ini
[Settings]
gtk-font-name = Noto Sans 10
gtk-monospace-font-name = Noto Mono 10
```

Then reload settings:

``` bash
dconf update
```

## Advanced Configuration with dconf-editor

For lower-level control and discovery of undocumented settings, install `dconf-editor`:

``` bash
sudo dnf install dconf-editor
```

Navigate to `org.gnome.desktop.interface` to view all font-related keys. This is useful for discovering hidden options but be cautious—changing wrong values can break your desktop. Always note the original value before changing anything.

## Listing Available Fonts

To see what fonts are installed on your system:

``` bash
fc-list : family | sort | uniq
```

For monospace fonts only:

``` bash
fc-list : family spacing | grep scalable | grep spacing=100 | awk '{print $1}' | sort | uniq
```

## Verifying Font Changes

Check what fonts are currently configured:

``` bash
gsettings list-keys org.gnome.desktop.interface | grep font
gsettings get org.gnome.desktop.interface font-name
```

For GTK settings:

``` bash
grep gtk-font-name ~/.config/gtk-3.0/settings.ini
```

## Persistence and Troubleshooting

Font changes made through GNOME Tweaks or `gsettings` persist across sessions automatically. CSS modifications to theme files require manual reapplication if the theme updates.

If fonts revert unexpectedly, check if a theme update overwrote your CSS changes:

``` bash
diff gnome-shell.css gnome-shell.css.bak
```

For applications that ignore system fonts, check if they have their own font configuration files (many browsers and development tools do).

If GNOME Shell becomes unresponsive after CSS modifications, revert your changes and restart:

``` bash
cp gnome-shell.css.bak gnome-shell.css
killall -9 gnome-shell
```
