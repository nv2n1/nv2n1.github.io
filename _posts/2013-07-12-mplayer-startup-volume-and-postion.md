---
title: "MPlayer: Setting Startup Volume and Position"
date: 2013-07-12 16:31:53 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/mplayer-startup-volume-and-postion/
---

mpv inherits much of MPlayer’s command structure, but with modern improvements for hardware acceleration, Wayland support, and codec handling. Here’s how to configure default startup volume and playback position.

## Configuration File

Edit `~/.config/mpv/mpv.conf` and add your defaults:

``` ini
volume=80
start=10
```

The `volume` parameter sets initial volume as a percentage (0–100). The `start` parameter specifies playback start position in seconds.

## Common Configuration Options

Beyond volume and position, several other startup parameters are useful:

``` ini
volume=80
volume-max=200
start=10
fullscreen=yes
hwdec=auto
audio-channels=stereo
```

- `volume-max`: Sets the maximum achievable volume (useful for quiet source material; values above 100 amplify)
- `fullscreen`: Launch in fullscreen mode
- `hwdec=auto`: Enable hardware acceleration automatically (VA-API on Linux, best for 4K/HDR)
- `audio-channels`: Force stereo or other channel layout

## Per-File Configuration

For file-specific settings, create `~/.config/mpv/script-opts/` or use profile-based configs. Add a profile section:

``` ini
[hd-content]
hwdec=auto
start=0
volume=75

[anime]
deinterlace=yes
volume=85
```

Launch with a profile:

``` bash
mpv --profile=hd-content video.mkv
mpv --profile=anime episode.mp4
```

## Command-Line Overrides

Command-line arguments override config file settings:

``` bash
mpv --volume=60 --start=5 video.mp4
mpv --fullscreen --hwdec=vaapi video.mkv
```

## Hardware Acceleration

On modern systems (2026+), ensure optimal codec support:

``` ini
hwdec=auto-safe
gpu-context=wayland
vo=gpu-next
```

- `hwdec=auto-safe`: Use hardware decoding when available, fallback to software safely
- `gpu-context=wayland`: Specify Wayland backend for better compatibility
- `vo=gpu-next`: Use the modern GPU video output (preferred over legacy `opengl`)

Check available hardware decoders:

``` bash
mpv --hwdec=help
```

## Scripting and Advanced Control

mpv supports Lua scripts for runtime control. Create `~/.config/mpv/scripts/volume-startup.lua` to set dynamic volume based on file type:

``` lua
mp.register_event("file-loaded", function()
    local filename = mp.get_property("filename")
    if filename:match("%.mkv$") then
        mp.set_property("volume", 75)
    elseif filename:match("%.mp4$") then
        mp.set_property("volume", 80)
    end
end)
```

Scripts in the `scripts/` directory load automatically on startup.

## Resuming Playback Position

mpv can remember where you stopped in videos:

``` ini
save-position-on-quit=yes
watch-later-dir=~/.config/mpv/watch_later
```

This creates resumable state files. Resume with:

``` bash
mpv --watch-later-directory=~/.config/mpv/watch_later video.mkv
```

Or manually resume by keybinding (default: Shift+Q to quit and save, ‘q’ to quit without saving).

## Troubleshooting Config Issues

Verify your config syntax:

``` bash
mpv --show-profile=default
```

Check which config file mpv actually loads:

``` bash
mpv -v 2>&1 | grep "config"
```

If settings don’t apply, ensure the config file is readable:

``` bash
ls -la ~/.config/mpv/mpv.conf
```

mpv reads only the first matching option in the config, so organize settings clearly and avoid duplicate keys.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.

## Comprehensive Guide: 2026 Best Practices

This article provides foundational knowledge for working with MPlayer: Setting Startup Volume and Position. In 2026, modern best practices emphasize security, reproducibility, and automation. Following these guidelines helps maintain clean, maintainable systems.

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
