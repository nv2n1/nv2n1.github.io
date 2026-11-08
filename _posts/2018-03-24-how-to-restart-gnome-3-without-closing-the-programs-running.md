---
title: "Restarting GNOME 3 Without Closing Running Programs"
date: 2018-03-24 08:15:33 +0000
author: "Q A"
layout: post
categories: [web-development]
canonical: /how-to-restart-gnome-3-without-closing-the-programs-running/
---

If you need to restart GNOME while keeping your applications open, you have several options depending on your GNOME version and setup.

### Quick restart with Alt+F2

The fastest method is to use GNOME’s run dialog:

1.  Press `Alt + F2`
2.  Type `r` and press Enter

This restarts the GNOME shell while preserving your running applications and their state. Your windows remain open, and you’ll return to your desktop with everything intact.

### Why you might need this

GNOME shell sometimes becomes unresponsive, freezes, or displays rendering issues. A full restart of the desktop environment fixes these problems without the overhead of logging out and back in. Applications continue running in the background, and you don’t lose unsaved work (though you should save first to be safe).

### Alternative: Restart via systemctl (Wayland/systemd systems)

On modern systems using systemd and Wayland, you can restart GNOME more explicitly:

``` bash
systemctl --user restart gnome-shell
```

This is functionally equivalent to the `Alt + F2 → r` method but useful if you’re scripting or the run dialog isn’t available.

### Fallback: Manual X11/Wayland session restart

If neither method works, you can kill the shell process directly:

``` bash
killall -9 gnome-shell
```

GNOME will respawn automatically on both X11 and Wayland. Your applications stay running, though you may lose window positions or unsaved state in GNOME itself.

### What gets restarted vs. what doesn’t

When you restart GNOME shell:

- **Restarted**: The desktop environment, panel, activities overview, window manager
- **Preserved**: All running applications, terminal sessions, browser tabs, text editors
- **Reset**: Window positions may shift slightly, wallpaper/theme settings reload from disk, open dialogs in GNOME system tools close

### Troubleshooting

If `Alt + F2` doesn’t work:

- You may have disabled the run dialog in GNOME settings
- Re-enable it in Settings → Keyboard → View and Customize Shortcuts → search for “run”
- Alternatively, use the systemctl command above

If the shell doesn’t restart properly:

- Check `journalctl --user -xe` for errors
- Ensure no background processes are holding GNOME resources
- On Wayland systems, session restart is more reliable than X11

### When to do a full logout instead

If GNOME won’t restart cleanly or you’re experiencing display server issues, a full logout/login cycle is more reliable:

``` bash
gnome-session-quit --logout
```

This closes everything and returns you to the login screen, useful when troubleshooting session-level problems.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
