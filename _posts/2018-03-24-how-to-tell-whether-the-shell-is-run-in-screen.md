---
title: "Detecting if Your Shell is Running in GNU Screen"
date: 2018-03-24 08:18:57 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-tell-whether-the-shell-is-run-in-screen/
---

You sometimes need to know whether your shell is running inside screen or tmux. The most straightforward approach is checking the `TERM` environment variable.

### Using TERM

When screen starts a shell, it sets `TERM=screen` by default:

``` bash
[user@host ~]$ echo $TERM
screen
```

Compare this to a normal terminal session:

``` bash
[user@host ~]$ echo $TERM
xterm-256color
```

The `TERM` value will vary depending on your terminal emulator (xterm, xterm-256color, rxvt, gnome-terminal, etc.), but inside screen it’s specifically `screen`.

### Checking in a Script

For conditional logic in a script or bashrc, use a simple test:

``` bash
if [ "$TERM" = "screen" ]; then
    echo "Running in screen"
fi
```

Or with pattern matching to catch both screen and tmux:

``` bash
if [[ "$TERM" =~ ^(screen|tmux) ]]; then
    echo "Running in screen or tmux"
fi
```

### More Reliable Detection

While `TERM` works, a more robust approach is checking the `STY` variable, which screen sets to identify the session name and process ID:

``` bash
if [ -n "$STY" ]; then
    echo "Running in screen: $STY"
fi
```

This is cleaner than relying on `TERM` because:

- `STY` is explicitly set by screen and won’t be affected by terminal emulator configuration
- `TERM` can be manually overridden with `TERM=screen` in a regular terminal
- `STY` uniquely identifies the screen session (format: `pid.tty.host`)

For tmux, use `TMUX` instead:

``` bash
if [ -n "$TMUX" ]; then
    echo "Running in tmux: $TMUX"
fi
```

### Practical Example

Here’s a bashrc snippet that adjusts behavior based on the multiplexer:

``` bash
if [ -n "$STY" ]; then
    # screen-specific settings
    PS1="\u@\h [screen] \w$ "
elif [ -n "$TMUX" ]; then
    # tmux-specific settings
    PS1="\u@\h [tmux] \w$ "
else
    # regular terminal
    PS1="\u@\h \w$ "
fi
```

### Why This Matters

Detecting multiplexer sessions is useful when:

- Configuring shell colors or prompts differently
- Conditionally loading terminal multiplexer plugins or functions
- Scripts that need to behave differently inside vs. outside multiplexed environments
- Debugging terminal issues and confirming your execution context

The `STY` or `TMUX` variable approach is preferred in modern practice because it’s more reliable and explicit than checking `TERM`.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
