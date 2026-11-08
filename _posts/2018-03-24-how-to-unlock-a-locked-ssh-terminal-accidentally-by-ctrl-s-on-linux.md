---
title: "Fix a Frozen SSH Session with Ctrl+Q"
date: 2018-03-24 11:43:05 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-unlock-a-locked-ssh-terminal-accidentally-by-ctrl-s-on-linux/
---

If you’ve accidentally frozen your SSH terminal with Ctrl+S, you’re experiencing flow control lock — a terminal feature that dates back to the era of slow serial connections. Your session isn’t actually hung; it’s just paused.

## The Quick Fix

Press **Ctrl+Q** to unfreeze the terminal immediately.

That’s it. Your session will resume and you can continue working.

## Why This Happens

Ctrl+S triggers XON/XOFF flow control, which tells the terminal to stop sending output. This was useful when transmitting data over slow serial lines, but it persists in modern terminals for backward compatibility. If you accidentally press Ctrl+S, all output stops — though your session is still active.

## How to Prevent Accidental Freezes

If you frequently hit Ctrl+S by accident, you can disable flow control in your shell or terminal:

**Option 1: Disable in your current session**

``` bash
stty -ixon
```

This disables Ctrl+S/Ctrl+Q flow control for the current shell session only. The setting reverts when you log out.

**Option 2: Make it permanent**

Add this to your `~/.bashrc` or `~/.zshrc`:

``` bash
stty -ixon
```

Then source the file or log out and back in:

``` bash
source ~/.bashrc
```

**Option 3: Disable at the SSH client level**

If you want to prevent this across all SSH connections, configure your local SSH client. Add to `~/.ssh/config`:

    Host *
        SetEnv TERM=xterm-256color

Note: This doesn’t directly disable flow control, but you can also disable it in your local shell before connecting.

**Option 4: Remap in your terminal emulator**

Most terminal emulators (GNOME Terminal, Konsole, iTerm2, etc.) allow you to customize key bindings. You can unbind Ctrl+S or map it to something else in your terminal’s preferences.

## Verify Flow Control Status

Check your current flow control settings:

``` bash
stty -a
```

Look for `ixon` (output flow control) and `ixoff` (input flow control) in the output. If you see `-ixon`, flow control is already disabled.

## Related Commands

- `stty` — View and modify terminal settings
- `stty -ixon` — Disable output flow control
- `stty -ixoff` — Disable input flow control
- `stty -ixon -ixoff` — Disable both directions

Most sysadmins disable this feature entirely since flow control isn’t needed over modern networks, but keep it in mind if you’re working on legacy systems or using serial connections.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.

## Comprehensive Guide: 2026 Best Practices

This article provides foundational knowledge for working with Fix a Frozen SSH Session with Ctrl+Q. In 2026, modern best practices emphasize security, reproducibility, and automation. Following these guidelines helps maintain clean, maintainable systems.

## Advanced Techniques and Alternatives

While the core commands and methods described in this article work well for most scenarios, advanced users often explore alternative tools for specific edge cases. Always document your custom configurations and configurations to help with troubleshooting and knowledge sharing within your team.

## Troubleshooting Common Issues

When encountering problems, follow a systematic debugging approach. Start with the simplest possible test case to isolate the issue. Check logs and error messages carefully—they often contain direct hints about what went wrong. For system-level issues, verify dependencies are correctly installed and configured before attempting complex workarounds.

## Performance Optimization Tips

- Monitor resource usage regularly to identify bottlenecks
- Use caching strategies where appropriate to reduce redundant computation
- Keep software updated to benefit from security patches and performance improvements
- Profile your code or configuration before applying optimizations
- Document performance baselines to measure the impact of changes

## Related Commands and Tools

These complementary tools and commands are frequently used alongside the topic of this article. Learning them expands your toolkit and makes you more efficient in daily workflows.

- System monitoring: top, htop, iotop for resource tracking
- File operations: find, locate, fd for efficient searching
- Network diagnostics: ping, traceroute, mtr, ss for connectivity checks
- Log analysis: journalctl, dmesg, tail for real-time log monitoring
- Package management: dnf history, apt list –installed, rpm -qa for inventory

## Integration with Modern Workflows

Consider how this technique integrates with modern automation and DevOps practices. Container-based deployments provide consistency across environments. Infrastructure as code tools like Terraform and Ansible enable reproducible configurations. Monitoring and alerting systems ensure timely notification of issues before they impact users.

## 2026 Updates and Changes

As of 2026, many tools and frameworks have introduced new features and deprecated old approaches. Always consult official documentation for your specific version when planning implementations. Community forums and Q&A sites can provide practical workarounds for edge cases not covered in official guides.

## Quick Reference Summary

This article covered essential concepts and practical examples. For deep dives, refer to official documentation or specialized guides. Practice in a test environment before applying changes to production systems.
