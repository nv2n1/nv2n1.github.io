---
title: "Changing Fonts in GNOME 3"
date: 2018-03-24 08:20:24 +0000
modified: 2026-04-12 16:21:05 +0000
author: "Eric Ma"
layout: post
categories: [linux-system-configuration]
canonical: /how-to-change-the-fonts-used-in-gnome-3/
---

The default GNOME Settings application doesn’t expose font configuration options. You’ll need additional tools to customize system fonts, but you have several approaches depending on your GNOME version and preferences.

## Using GNOME Tweaks

GNOME Tweaks (formerly gnome-tweak-tool) is the recommended graphical approach for font customization.

### Installation

On Fedora/RHEL:

``` bash
sudo dnf install gnome-tweaks
```

On Ubuntu/Debian:

``` bash
sudo apt install gnome-tweaks
```

On Arch:

``` bash
sudo pacman -S gnome-tweaks
```

### Configuring Fonts via GNOME Tweaks

Launch GNOME Tweaks from your application menu or run:

``` bash
gnome-tweaks
```

Navigate to **Fonts** in the left sidebar. You’ll find options to configure:

- **Interface Font** — used in window titles and menus
- **Document Font** — default font for text editors and documents
- **Monospace Font** — terminal and code editors
- **Legacy Window Titles** — older application title bars

Adjust font sizes with the scaling slider or select different font families from the dropdown menus. Changes apply immediately to most applications.

## Using dconf Editor

For more granular control, use `dconf-editor` (graphical) or `gsettings`/`dconf` (command-line):

``` bash
sudo apt install dconf-editor  # Debian/Ubuntu
sudo dnf install dconf-editor  # Fedora
```

Launch it and navigate to `/org/gnome/desktop/interface/` to modify:

``` bash
dconf write /org/gnome/desktop/interface/font-name "'DejaVu Sans 11'"
dconf write /org/gnome/desktop/interface/document-font-name "'DejaVu Sans 12'"
dconf write /org/gnome/desktop/interface/monospace-font-name "'DejaVu Sans Mono 11'"
```

Check current settings:

``` bash
gsettings get org.gnome.desktop.interface font-name
```

## Installing Additional Fonts

Before changing fonts, ensure they’re installed on your system.

Check available fonts:

``` bash
fc-list | grep -i "font-name"
```

Install fonts system-wide:

``` bash
# Debian/Ubuntu
sudo apt install fonts-dejavu fonts-liberation fonts-noto

# Fedora
sudo dnf install dejavu-fonts liberation-fonts google-noto-fonts

# Arch
sudo pacman -S noto-fonts liberation-fonts
```

For single-user font installation, place `.ttf` or `.otf` files in `~/.local/share/fonts/` and run:

``` bash
fc-cache -fv
```

## Font Size Scaling

For HiDPI displays or accessibility needs, adjust the scaling factor:

``` bash
dconf write /org/gnome/desktop/interface/text-scaling-factor 1.25
```

Values range from 0.75 to 2.0. This scales all fonts proportionally system-wide.

## Troubleshooting

**Changes not applying to specific applications**: Some older GTK2 applications may require restart or additional configuration in `~/.gtkrc-2.0`.

**Missing fonts after installation**: Run `fc-cache -fv` and restart GNOME (log out and back in, or restart the display server).

**Terminal fonts unchanged**: Terminal emulator settings override system fonts. Configure them in your terminal’s preferences (GNOME Terminal Settings → Appearance).

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.

## Comprehensive Guide: 2026 Best Practices

This article provides foundational knowledge for working with Changing Fonts in GNOME 3. In 2026, modern best practices emphasize security, reproducibility, and automation. Following these guidelines helps maintain clean, maintainable systems.

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
