---
title: "GNOME 3 Keyboard Shortcuts for Screenshots"
date: 2021-06-13 12:26:31 +0000
author: "David Yang"
layout: post
categories: [linux-systems-administration]
canonical: /gnone-3-screenshot-keyboard-shortcuts/
---

GNOME 3 and later versions include built-in screenshot functionality accessible via keyboard shortcuts. These work without opening any application, making them faster than the dedicated Screenshot utility. The shortcuts split into two categories: saving directly to the Pictures folder, and copying to the clipboard for immediate pasting.

## Save screenshots as files

These shortcuts save to `~/Pictures/` by default.

- **Print** — Full screen
- **Shift+Print** — Selected area (interactive selection box appears)
- **Alt+Print** — Active window only

## Copy screenshots to clipboard

Add Ctrl to the above shortcuts to copy instead of save:

- **Ctrl+Print** — Full screen to clipboard
- **Ctrl+Shift+Print** — Selected area to clipboard
- **Ctrl+Alt+Print** — Active window to clipboard

After copying, paste directly into image editors, chat applications, or documents using Ctrl+V.

## Accessing screenshots

Screenshots saved to disk appear in the Pictures folder. You can also access them from the file manager or by checking recent files. The filename format is typically `Screenshot from [date] [time].png`.

If you’ve changed your default Pictures location, saved screenshots go there instead. To verify your Pictures directory:

``` bash
xdg-user-dir PICTURES
```

## Modifying screenshot settings

While GNOME’s default shortcuts are fixed, you can customize behavior through dconf. For example, to include a timestamp in the filename:

``` bash
gsettings set org.gnome.gnome-screenshot auto-save-filename 'screenshot-%d-%m-%Y_%H:%M:%S'
```

To add a delay before capturing (useful for menu screenshots):

``` bash
gsettings set org.gnome.gnome-screenshot delay 3
```

Check current settings:

``` bash
gsettings list-recursively org.gnome.gnome-screenshot
```

## Screenshot tools and alternatives

For more advanced needs, consider these tools:

- **Flameshot** — Powerful screenshot tool with annotation and editing
- **Spectacle** — KDE’s screenshot utility (works on GNOME too)
- **scrot** — Lightweight CLI tool: `scrot ~/screenshot.png`
- **maim** — Similar to scrot with better compositing support

## Troubleshooting missing screenshots

If screenshots aren’t saving, verify:

- The Pictures folder exists: `mkdir -p ~/Pictures`
- You have write permissions: `ls -ld ~/Pictures`
- GNOME Shell is running: `echo $XDG_CURRENT_DESKTOP`

For Wayland sessions, screenshot support depends on your compositor. If shortcuts fail silently on Wayland, fall back to the Screenshot application or Flameshot.

## Using the command line

The `gnome-screenshot` command provides additional options:

``` bash
gnome-screenshot -w          # Capture active window
gnome-screenshot -a          # Capture selected area
gnome-screenshot -d 5        # 5-second delay
gnome-screenshot -o ~/shot.png  # Save to specific path
```

Chain with other tools for automation:

``` bash
gnome-screenshot -a -c && xclip -selection clipboard -t image/png -o | convert - -negate output.png
```

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
