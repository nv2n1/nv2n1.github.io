---
title: "Accessing Preferences in gThumb on Linux"
date: 2018-03-24 11:48:07 +0000
modified: 2026-04-12 07:57:15 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-open-the-preferences-dialog-in-gthumb-3-4-on-linux/
---

\[md\]
gThumb’s preferences aren’t always obvious when you’re looking through the traditional menu bar. The location depends on your desktop environment and gThumb version.

\## GNOME Desktop

On GNOME 3 and later, preferences are accessed through the application menu rather than the window menu:

1\. Open gThumb
2\. Click the application name (“gThumb”) in the top bar
3\. Select \*\*Preferences\*\* from the dropdown

In GNOME’s Activities overview, you can also search for “Preferences” while gThumb has focus.

\## Older Desktop Environments

On GNOME 2, Xfce, MATE, or other traditional desktop environments, the preferences dialog is in the standard location:

1\. Open gThumb
2\. Click \*\*Edit\*\* → \*\*Preferences\*\*

\## KDE Plasma

On KDE, gThumb follows the GNOME convention since it’s a GTK application:

1\. Open gThumb
2\. Look for the hamburger menu (☰) or the application menu in the title bar
3\. Select \*\*Preferences\*\*

If you don’t see the menu, press \*\*F10\*\* to show it, or right-click the title bar.

\## What You Can Configure

The preferences dialog in gThumb 3.4+ provides several configuration sections:

\*\*General settings:\*\*
– Startup directory — choose whether to open the last visited folder or a specific location
– Thumbnail size — adjust preview quality vs. speed
– File properties — configure which metadata to display

\*\*Viewer settings:\*\*
– Image quality for zooming
– Transparency style (checkered pattern or solid color)
– Scroll behavior when zoomed in
– Fit-to-window vs. actual size default

\*\*Browser settings:\*\*
– Show hidden files
– Sort order for images
– Thumbnail caption format
– Whether to show file extensions

\## Keyboard Shortcuts for Quick Access

Instead of navigating menus, you can use keyboard shortcuts:

– \*\*Ctrl+P\*\* — Open preferences (in some gThumb versions)
– \*\*F10\*\* — Show/hide the application menu
– \*\*Shift+F10\*\* — Show context menu

\## gThumb Extensions

Beyond the preferences dialog, gThumb’s real power comes from its extensions. Access them via \*\*Edit\*\* → \*\*Extensions\*\* (or the equivalent menu path for your version):

\*\*Useful extensions to enable:\*\*
– \*\*Image Viewer\*\* — Enhanced zoom and pan controls
– \*\*Rename Files\*\* — Batch renaming with patterns
– \*\*Convert Format\*\* — Batch image conversion (JPEG, PNG, WebP)
– \*\*Resize Images\*\* — Batch resize with custom dimensions or percentages
– \*\*Contact Sheet\*\* — Generate thumbnail grids from selected images
– \*\*Photo Importer\*\* — Import from cameras and mobile devices
– \*\*Web Albums\*\* — Upload to online services

To install additional extensions on Fedora:

```wp-block-code
sudo dnf install gthumb-plugins
```

On Ubuntu/Debian:

```wp-block-code
sudo apt install gthumb-plugins
```

\## Troubleshooting Missing Preferences

If you can’t find the preferences dialog:

\*\*Menu bar is hidden:\*\* Press \*\*F10\*\* or look for a hamburger menu icon (☰) in the header bar. GNOME applications often hide the traditional menu bar by default.

\*\*Running under Wayland:\*\* Some menu integrations behave differently under Wayland compared to X11. If menus don’t appear correctly, try:

```wp-block-code
GDK_BACKEND=x11 gthumb
```

\*\*gThumb won’t start:\*\* Check for configuration file corruption:

```wp-block-code
# Backup and reset gThumb config
mv ~/.config/gthumb ~/.config/gthumb.bak
gthumb
```

This resets all preferences to defaults. Your image files are not affected — only gThumb’s settings.

\## Version Differences

gThumb has changed significantly over versions:

– \*\*gThumb 3.4\*\* — Uses traditional Edit menu on most desktops
– \*\*gThumb 3.10+\*\* — Uses GNOME-style application menu in the top bar
– \*\*gThumb 3.12+\*\* — Modern header bar with integrated preferences access

Check your version:

```wp-block-code
gthumb --version
```

If your distribution ships an older version and you want the latest features, consider installing via Flatpak:

```wp-block-code
flatpak install flathub org.gnome.gThumb
```
