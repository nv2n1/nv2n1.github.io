---
title: "Fix Chinese Character Display in LXTerminal"
date: 2018-03-24 11:45:01 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-display-chinese-character-in-lxterminal/
---

LXTerminal may fail to display Chinese characters correctly if fonts aren’t properly configured. This is typically a font availability or configuration issue rather than a terminal limitation.

## Check Your Font Setup

First, verify that Chinese fonts are installed on your system. Install them if needed:

**Fedora/RHEL:**

``` bash
sudo dnf install fonts-noto-cjk
```

**Debian/Ubuntu:**

``` bash
sudo apt install fonts-noto-cjk
```

**Arch:**

``` bash
sudo pacman -S noto-fonts-cjk
```

List installed fonts to confirm:

``` bash
fc-list | grep -i cjk
```

## Configure LXTerminal for Chinese Fonts

Edit your LXTerminal configuration file at `~/.config/lxterminal/lxterminal.conf`:

``` ini
[general]
fontname=Noto Sans Mono CJK JP 12
```

You can use any of these common CJK fonts:

- `Noto Sans Mono CJK JP`
- `Noto Sans Mono CJK SC` (Simplified Chinese)
- `Noto Sans Mono CJK TC` (Traditional Chinese)
- `Noto Sans Mono CJK KR`
- `DejaVu Sans Mono` (basic CJK support)

## Configure X Resources (Alternative Method)

If editing the config file doesn’t work, configure fonts via X resources. Edit or create `~/.Xresources`:

```xresources
LXTerminal.fontName: Noto Sans Mono CJK JP
LXTerminal.fontSize: 12
```

Then reload the settings:

``` bash
xrdb -merge ~/.Xresources
```

## Test CJK Display

Restart LXTerminal and test with Chinese text:

``` bash
echo "你好世界"
```

Or display a file with CJK content:

``` bash
cat /path/to/chinese-file.txt
```

## Check Locale Settings

Ensure your locale supports UTF-8:

``` bash
locale
```

If not configured, set it:

``` bash
export LANG=en_US.UTF-8
```

Add this to your shell profile (`.bashrc`, `.zshrc`, etc.) to make it permanent.

## Verify with Other Terminals

If Chinese characters still don’t display, test with GNOME Terminal or xterm to isolate whether the issue is LXTerminal-specific:

``` bash
gnome-terminal
```

or

``` bash
xterm
```

If these terminals display Chinese correctly, the issue is LXTerminal configuration. If they also fail, the problem is likely missing fonts or locale misconfiguration.

## Common Issues

**Characters show as boxes:** Font lacks CJK glyphs. Install `fonts-noto-cjk` and ensure LXTerminal is configured to use it.

**Characters don’t appear at all:** Check that your locale is set to UTF-8 and that the LANG environment variable is exported.

**Configuration changes don’t apply:** LXTerminal may need to be restarted. Close all instances and reopen.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
