---
title: "Alt-Tab Between Windows Only in GNOME"
date: 2018-03-24 08:22:04 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-make-alt-tab-switch-among-windows-instead-of-applications-in-gnome-3/
---

GNOME’s default Alt-Tab behavior switches between applications, grouping all windows from the same app together. If you work with multiple windows in a single application—multiple browser tabs, text editors, or terminals—this becomes frustrating. Here’s how to change it to window-based switching.

## Using the Alternate Tab Extension

The simplest approach is enabling GNOME’s built-in Alternate Tab extension, which replaces application-based switching with window-focused switching.

**GUI method:**

1.  Open the Extensions application
2.  Search for “Alternate Tab”
3.  Toggle the switch to enable it

After activation, Alt-Tab cycles through individual windows instead of jumping between applications.

**Command-line installation:**

``` bash
# Fedora/RHEL/CentOS
sudo dnf install gnome-shell-extension-alternate-tab

# Ubuntu/Debian
sudo apt install gnome-shell-extension-alternate-tab

# Arch
sudo pacman -S gnome-shell-extension-alternate-tab
```

After installation, reload GNOME Shell or log out and back in. You can reload without logging out by pressing Alt+F2, typing `r`, and pressing Enter.

## Direct dconf Configuration

If you prefer not to use extensions, modify GNOME’s switcher behavior directly:

``` bash
dconf write /org/gnome/shell/window-switcher/current-workspace-only true
```

This limits Alt-Tab to windows in your current workspace, making switching feel more window-centric. You can also adjust the switcher appearance:

``` bash
# Use list view instead of grid (shows window titles more clearly)
dconf write /org/gnome/shell/window-switcher/app-icon-mode 1
```

## Hybrid Approach: Super Key for Windows, Alt-Tab for Apps

If you want both behaviors available, configure separate keybindings:

``` bash
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications "['<Alt>Tab']"
```

Now Super+Tab switches windows while Alt-Tab switches applications. This works well if you occasionally need application-level switching.

To reverse direction (Shift modifier), use:

``` bash
gsettings set org.gnome.desktop.wm.keybindings switch-windows-backward "['<Super><Shift>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "['<Alt><Shift>Tab']"
```

## Troubleshooting

**Alt-Tab still groups by application:**

- Ensure GNOME Shell has reloaded. Run `killall -HUP gnome-shell` or log out and back in
- Check version compatibility: `gnome-shell --version`
- Disable conflicting extensions (check Extensions app for other switcher-related extensions)

**Extension won’t install:**

- Verify your GNOME version matches extension requirements at extensions.gnome.org
- For GNOME 45+, most extensions require manual compilation if not packaged for your distribution

**Need to see what each window contains:**

- Enable window previews by setting `dconf write /org/gnome/shell/window-switcher/show-thumbnails true`
- This shows small previews of each window’s content, useful when multiple windows share the same application

## Resetting to Default

To restore GNOME’s default behavior:

``` bash
gsettings reset org.gnome.desktop.wm.keybindings switch-windows
gsettings reset org.gnome.desktop.wm.keybindings switch-applications
dconf reset /org/gnome/shell/window-switcher/current-workspace-only
```

Then disable the Alternate Tab extension if you enabled it.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
