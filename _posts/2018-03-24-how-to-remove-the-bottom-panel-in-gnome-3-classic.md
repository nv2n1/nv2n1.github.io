---
title: "Removing the Bottom Panel in GNOME 3 Classic"
date: 2018-03-24 11:51:24 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-remove-the-bottom-panel-in-gnome-3-classic/
---

The bottom panel in GNOME Classic displays the window list via the “Window List” extension. If you don’t use it, there are several ways to remove it depending on your approach.

## Method 1: Context menu removal (Recommended)

The simplest approach if your GNOME version supports it:

1.  Hover over a blank area of the bottom panel
2.  Press **Ctrl + Super + Right Click**
3.  Select “Remove This Panel” from the context menu

This works on modern GNOME Classic installations (GNOME 3.36+). The setting persists across sessions.

## Method 2: Disable the Window List extension

If the context menu method doesn’t work or you want to keep the panel structure but hide the window list:

1.  Open **Extensions** application
2.  Find “Window List” in the list
3.  Toggle it off

Note that on some distributions (like Rocky Linux, AlmaLinux), GNOME Classic has the Window List extension as a hard dependency. Disabling it via the GUI may not prevent it from loading on startup.

## Method 3: Remove the extension package

For a more permanent solution, particularly on systems where the Window List is a required dependency:

``` bash
sudo yum remove gnome-shell-extension-window-list
```

Or on Debian/Ubuntu systems:

``` bash
sudo apt remove gnome-shell-extension-window-list
```

Be aware that on some distributions, this may trigger removal of the entire `gnome-classic-session` package due to dependency constraints. Check what will be removed before confirming.

If you need to reinstall it later:

``` bash
sudo yum reinstall gnome-shell-extension-window-list
```

## Method 4: Direct file removal (Not recommended)

You can manually delete the extension directory, but this bypasses package management:

``` bash
sudo rm -rf /usr/share/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com
```

This method isn’t recommended because:

- Package managers won’t track the removal
- System updates may reinstall it
- Reinstalling the package won’t restore the extension files without additional steps

Use this only if you fully understand the implications.

## Troubleshooting

If the bottom panel persists after disabling the extension, try restarting GNOME Shell:

``` bash
killall -3 gnome-shell
```

On Wayland sessions (the default on modern distributions), you may need to log out and back in instead, as the shell restart method is less reliable.

If you want to completely hide the panel without removing it:

1.  Right-click the panel → Panel preferences
2.  Set the panel to “autohide” mode
3.  Adjust size to minimum if the option exists

This keeps the extension installed but hides it when unused.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
