---
title: "GNOME Shell Extensions to Enhance GNOME 45"
date: 2016-10-22 10:22:39 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /essential-gnome-shell-extensions-gnome-3-users/
---

GNOME Shell’s clean, minimal design works well for many users, but the extension ecosystem lets you adapt it to your actual workflow. Here are extensions worth considering for modern GNOME (45+).

## AlternateTab

Changes Alt-Tab behavior from application-grouped switching to per-window switching — more like traditional window managers. If GNOME’s default grouping feels disruptive, this restores predictable window cycling.

Installation via package manager:

``` bash
sudo apt install gnome-shell-extension-alternatetab  # Debian/Ubuntu
sudo dnf install gnome-shell-extension-alternatetab  # Fedora
```

Alternatively, grab it from <a href="https://extensions.gnome.org" rel="nofollow noopener" target="_blank">extensions.gnome.org</a> and enable it through Settings \> Extensions or the GNOME Extensions app.

## Dash to Dock

Converts the Activities overview dash into a persistent side dock — useful if you frequently launch applications and want faster access than clicking Activities repeatedly. Works especially well on ultrawide displays where you have horizontal space to spare.

The dock auto-hides by default but supports various positioning options (left, right, bottom, top). Configure visibility behavior, icon sizing, and app preview behavior through the extension preferences. You can also set it to show only when the Activities overview is visible, or always show when you’re on a specific workspace.

Install via your package manager or directly from extensions.gnome.org for the latest version compatible with your GNOME release.

## Vitals

Adds CPU, memory, temperature, network, and disk I/O indicators to the top panel. This modern alternative to the older System Monitor extension gives you glanceable system metrics without opening a separate window. Expand individual sections to drill down into details.

``` bash
sudo apt install gnome-shell-extension-vitals  # Debian/Ubuntu
sudo dnf install gnome-shell-extension-vitals  # Fedora
```

Be aware that continuous monitoring adds modest overhead. On resource-constrained systems, consider `top`, `htop`, or `btop` in a terminal instead. Vitals lets you customize which metrics display and their update frequency.

## User Themes

Enables loading custom shell themes from your home directory. GNOME restricts theme loading by default, so this extension removes that security restriction. Install themes to `~/.local/share/gnome-shell/themes/` and select them in Settings \> Appearance.

Pairs well with matching GTK themes (like Adwaita variants or community themes) to maintain visual consistency across your desktop. After installing a new theme, you may need to restart GNOME Shell:

``` bash
Alt+F2, then type 'r' and press Enter
```

## Clipboard Indicator

GNOME removed clipboard history years ago, so extensions fill the gap. Clipboard Indicator maintains a searchable clipboard history accessible from the top panel. Configure retention limits (number of entries and time-based expiration) through preferences.

Useful if you’re frequently copying multiple items in sequence — search history instead of cycling through repeated pastes. This is particularly handy during code reviews or documentation work where you’re juggling multiple snippets.

## Caffeine

Temporarily disable screensaver and screen locking with a single toggle in the top panel. Useful during presentations, long-running processes, or when you need the system to stay active without touching the keyboard. Simpler than repeatedly adjusting power settings.

``` bash
sudo apt install gnome-shell-extension-caffeine  # Debian/Ubuntu
sudo dnf install gnome-shell-extension-caffeine  # Fedora
```

## Extension Management

Most extensions are installable via your distribution’s package manager or directly from extensions.gnome.org. Manage extensions graphically through Settings \> Extensions or via command line:

``` bash
# List enabled extensions
gnome-extensions list --enabled

# List all installed extensions
gnome-extensions list

# Enable an extension
gnome-extensions enable extension-name@example.com

# Disable an extension
gnome-extensions disable extension-name@example.com

# Check extension details
gnome-extensions info extension-name@example.com
```

For batch operations, you can script extension management:

``` bash
# Disable all extensions
gsettings set org.gnome.shell enabled-extensions "[]"

# Query current enabled extensions
gsettings get org.gnome.shell enabled-extensions
```

## Compatibility and Performance

Always verify GNOME version compatibility before installing — not all extensions support every release. Check the extension page on extensions.gnome.org for version requirements. Extensions that worked in GNOME 44 may break in GNOME 45 or later due to API changes.

Review what permissions each extension requests. Disable unused extensions to minimize performance impact and reduce system noise. Extensions run in the same process as GNOME Shell, so a misbehaving extension can degrade the entire desktop environment.

Test extensions one at a time if you’re troubleshooting stability issues. If GNOME Shell becomes unresponsive or crashes, disable all extensions:

``` bash
gsettings set org.gnome.shell enabled-extensions "[]"
```

Then selectively re-enable them to identify the culprit. After identifying a problematic extension, report the issue on its GitHub repository or the GNOME Extensions website — maintainers often fix compatibility problems quickly.

Monitor extension maintenance status on extensions.gnome.org. Active extensions with recent updates are more likely to remain compatible with future GNOME releases. Abandoned extensions are liabilities; they may break unexpectedly and leave you with an unstable desktop.
