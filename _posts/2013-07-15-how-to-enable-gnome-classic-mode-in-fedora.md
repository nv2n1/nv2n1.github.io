---
title: "Enable GNOME Classic Desktop on Fedora, CentOS, and RHEL"
date: 2013-07-15 03:16:26 +0000
layout: post
canonical: https://www.systutorials.com/how-to-enable-gnome-classic-mode-in-fedora/
---

GNOME Classic is a session mode that provides a traditional desktop experience with an application menu, places menu, and window switcher. It’s useful if you prefer a layout closer to GNOME 2 or want a traditional taskbar-based interface instead of GNOME Shell’s Activities overview.

## Installation

The `gnome-classic-session` package isn’t installed by default. Install it with DNF:

``` bash
sudo dnf install gnome-classic-session
```

This is a lightweight package that won’t significantly impact your system. After installation, the Classic session option becomes available at the login screen.

## Switching to Classic Mode

At the GDM login screen:

1.  Click your username
2.  Look for a gear icon or “Session” button (typically in the bottom-right corner)
3.  Select “GNOME Classic” from the available sessions
4.  Enter your password and log in

GNOME remembers your session choice and will default to Classic mode on future logins unless you change it.

To test Classic mode without logging out, open the system menu (top-right), select your user account, click “Log Out”, and choose GNOME Classic at the login screen.

## What You Get

GNOME Classic includes:

- Application menu at the top-left for quick program access
- Places menu for file system navigation
- Window switcher along the bottom taskbar
- Traditional panel layout with visible application indicators
- System tray with network, volume, and status indicators visible by default
- Full extension support via <a href="https://extensions.gnome.org" rel="nofollow noopener" target="_blank">GNOME Extensions</a>

The interface is more discoverable than GNOME Shell’s Activities overview, making it suitable for users transitioning from older desktop environments.

## Verifying Your Session

Confirm you’re running Classic mode from the command line:

``` bash
echo $XDG_CURRENT_DESKTOP
```

This should output:

    GNOME-Classic:GNOME

You can also check the active session with:

``` bash
loginctl show-session --property=Type
```

## Troubleshooting

**Session option doesn’t appear at login:**

Verify the package installed correctly:

``` bash
rpm -q gnome-classic-session
```

If missing, reinstall it:

``` bash
sudo dnf reinstall gnome-classic-session
```

Ensure GNOME Shell is also installed:

``` bash
sudo dnf install gnome-shell
```

**Session crashes or won’t start:**

Check for GNOME-related errors in the journal:

``` bash
journalctl -xe | grep -i gnome
journalctl --user -xe
```

If you’re on Wayland and experiencing issues, switch to X11 before logging in. Some extensions may not work properly on Wayland. You can check your current session type with:

``` bash
echo $XDG_SESSION_TYPE
```

**Extensions cause performance issues or crashes:**

Temporarily disable all extensions:

``` bash
gsettings set org.gnome.shell enabled-extensions "[]"
```

Then re-enable them one at a time through the GNOME Extensions app to identify the problematic extension.

**Reverting to standard GNOME:**

Simply select “GNOME” (not “GNOME Classic”) from the session menu at login.

## Customization

Once in Classic mode, you can further customize the desktop:

- Right-click the top or bottom panels to add/remove buttons, applets, or indicators
- Access panel preferences by right-clicking and selecting “Properties”
- Adjust keyboard shortcuts: Settings → Keyboard → Shortcuts
- Configure application favorites by dragging them to the taskbar
- Customize keyboard layouts: Settings → Keyboard → Input Sources

### Recommended Extensions

Popular extensions for Classic mode include:

- **Dash to Panel** — adds a modern taskbar with application previews
- **Applications Menu** — provides a traditional application menu
- **Caffeine** — prevents the screensaver from activating
- **System Monitor** — displays CPU, memory, and network in the panel

Enable extensions in small batches and verify compatibility with your GNOME version before enabling multiple at once.

## Supported Systems

GNOME Classic is supported on:

- Fedora 38+
- CentOS Stream 9+
- RHEL 8+

RHEL 7 (legacy) is not recommended and relies on older GNOME 3.28 components. Upgrade to RHEL 8+ for current security updates and broader extension support.
