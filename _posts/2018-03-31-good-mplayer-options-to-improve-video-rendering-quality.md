---
title: "Improving Video Rendering Quality in MPlayer"
date: 2018-03-31 17:28:30 +0000
layout: post
canonical: https://www.systutorials.com/good-mplayer-options-to-improve-video-rendering-quality/
---

MPlayer reached end-of-life in 2010 and hasn’t received updates since. If you’re still using it, you’re missing years of improvements in video decoding, filtering, and performance. For new projects, use **mpv** instead—it’s the maintained fork that incorporates MPlayer’s codebase with significant enhancements.

That said, if you’re stuck maintaining legacy MPlayer setups, here’s how to optimize rendering quality.

## MPlayer Configuration Profiles

MPlayer supports profiles in `~/.mplayer/config` for different quality/performance trade-offs:

``` ini
[fast]
vf=eq2
vc=ffmpeg12vdpau

[default]
vf=hqdn3d=2:1:2
vo=gl:yuv=4:lscale=lanczos2:cscale=lanczos2
ao=pulse
font=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
```

The **fast** profile uses the `eq2` filter (simple brightness/contrast equalization) with hardware acceleration via VDPAU if available. This minimizes CPU overhead.

The **default** profile applies `hqdn3d` denoising, which reduces noise at the cost of slight softening. The GL video output with `yuv=4` (4:2:0 chroma subsampling) and Lanczos scaling provides better interpolation than the older `yuv=3` setting.

Invoke profiles explicitly:

``` bash
mplayer -profile fast video.mp4
mplayer -profile default video.mp4
```

## Better Alternative: Use mpv

**mpv** is actively maintained and handles modern codecs and hardware acceleration properly:

``` bash
# Install mpv
sudo apt install mpv  # Debian/Ubuntu
sudo dnf install mpv  # Fedora
brew install mpv      # macOS

# Basic high-quality playback
mpv --profile=high-quality video.mp4

# Custom configuration in ~/.config/mpv/mpv.conf
vo=gpu
hwdec=auto
scale=lanczos
cscale=lanczos
dscale=linear
video-sync=display-resample
```

mpv’s `--profile=high-quality` preset includes appropriate scaling filters, dithering, and output options without manual tuning.

## Hardware Acceleration

Modern systems should use GPU decoding to offload work from the CPU:

**For mpv:**

``` bash
mpv --hwdec=auto video.mp4  # Auto-detect best available
mpv --hwdec=vdpau video.mp4  # NVIDIA with VDPAU
mpv --hwdec=vaapi video.mp4  # Intel/AMD with VA-API
```

**For MPlayer (legacy):**

``` bash
mplayer -vc ffmpeg12vdpau,ffh264vdpau, video.mp4
mplayer -vc ffmpeg12vaapi,ffh264vaapi, video.mp4
```

Requires `libvdpau` or `libva` and appropriate drivers.

## Video Filtering in mpv

Instead of MPlayer’s dated filters, use mpv’s modern filter chain:

``` bash
# Denoise with nlmeans (slower, better quality)
mpv --vf=nlmeans video.mp4

# Denoise with hqdn3d (faster, like MPlayer)
mpv --vf=hqdn3d=2:1:2 video.mp4

# Deinterlace
mpv --vf=bwdif video.mp4

# Sharpen (use cautiously)
mpv --vf=unsharp=5:5:1.0 video.mp4

# Combine filters
mpv --vf=hqdn3d=2:1:2,unsharp=5:5:0.5 video.mp4
```

Store in `~/.config/mpv/mpv.conf`:

``` ini
[fast]
profile=fast-preset
hwdec=auto

[quality]
profile=high-quality
vf=hqdn3d=2:1:2
hwdec=auto
```

Then invoke with:

``` bash
mpv --profile=fast video.mp4
mpv --profile=quality video.mp4
```

## Performance Tuning

If you need lower CPU usage without sacrificing too much quality:

- Enable hardware decoding (`hwdec=auto`)
- Use simpler scaling: `scale=bilinear` instead of `lanczos`
- Reduce filter complexity: prefer `eq2` over `hqdn3d`
- Lower output resolution if the display doesn’t require 4K

For high-performance requirements on modern hardware, mpv with GPU rendering (`vo=gpu`) and hardware decoding will always outperform MPlayer significantly.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
