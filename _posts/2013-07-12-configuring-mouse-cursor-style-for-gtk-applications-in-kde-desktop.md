---
title: "Customizing GTK Cursor Themes in KDE"
date: 2013-07-12 16:32:12 +0000
layout: post
canonical: https://www.systutorials.com/configuring-mouse-cursor-style-for-gtk-applications-in-kde-desktop/
---

When using KDE Plasma with GTK applications, you’ll notice the mouse cursor switches to a default style when moving from the desktop to applications like Firefox or GIMP. This happens because GTK and Qt use separate cursor theme configurations by default.

## Quick Fix

The easiest solution is to explicitly configure GTK to use your chosen cursor theme. KDE Plasma reads cursor themes from `~/.icons/` and GTK can be configured to use the same theme.

### Step 1: Install GTK Configuration Tools

For KDE Plasma 5 and 6, install the GTK configuration module:

**Fedora/RHEL:**

``` bash
sudo dnf install kcm-gtk gtk3
```

**Ubuntu/Debian:**

``` bash
sudo apt install kde-config-gtk
```

**Arch:**

``` bash
sudo pacman -S kde-gtk-config
```

### Step 2: Find Your Cursor Theme

List available cursor themes in your system:

``` bash
ls /usr/share/icons/
```

Common cursor themes include `Breeze`, `Oxygen`, `Adwaita`, and others. You can also check `~/.local/share/icons/` for user-installed themes.

To verify which cursor theme KDE is currently using, check the Plasma settings or look at `~/.config/kcminputrc`:

``` bash
grep -A2 "\[Mouse\]" ~/.config/kcminputrc
```

### Step 3: Configure GTK Cursor Theme

Edit or create `~/.gtkrc-2.0` for GTK 2 applications:

``` bash
echo 'gtk-cursor-theme-name = "Breeze"' >> ~/.gtkrc-2.0
```

For GTK 3 and later, create/edit `~/.config/gtk-3.0/settings.ini`:

``` ini
[Settings]
gtk-cursor-theme-name=Breeze
gtk-cursor-theme-size=24
```

For GTK 4, use `~/.config/gtk-4.0/settings.ini`:

``` ini
[Settings]
gtk-cursor-theme-name=Breeze
gtk-cursor-theme-size=24
```

Replace `Breeze` with whichever cursor theme matches your KDE setup.

### Step 4: Apply Changes

Restart GTK applications or reload the desktop session:

``` bash
kquitapp6 plasmashell && kstart6 plasmashell
```

Or simply log out and back in.

## Using the GUI (Simpler Method)

In KDE Plasma 5 and 6, you can use the built-in GTK configuration tool:

1.  Open **System Settings** → **Appearance** → **GTK Appearance**
2.  Select the cursor theme that matches your chosen Qt cursor theme
3.  Changes apply immediately

This is the recommended approach for most users, as it handles all GTK versions consistently.

## Troubleshooting

**Cursor still doesn’t match:** Verify the theme name exists in `/usr/share/icons/` and check that no other configuration files are overriding your settings.

**GTK application crashes:** Ensure you’re using the correct settings file format for your GTK version. GTK 2 applications use `~/.gtkrc-2.0`, while GTK 3+ use the `settings.ini` approach.

**Only some applications affected:** Some GTK applications (particularly older ones) may ignore cursor theme settings and use hardcoded defaults. This is an application-level limitation.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
