---
title: "Batch Resize Images on Linux with ImageMagick"
date: 2018-03-24 11:44:04 +0000
modified: 2026-04-12 16:57:04 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-resize-a-batch-of-images-on-linux/
---

Resizing a single image is straightforward, but processing dozens or hundreds requires automation. ImageMagick’s `convert` command (or the modern `magick` command) paired with a bash loop is the standard approach for batch image resizing on Linux.

## Using ImageMagick

ImageMagick remains the most reliable tool for this task. Here’s a practical script to resize all images in a directory:

``` bash
mkdir -p resize
for i in *.{jpg,jpeg,png,gif}; do
    [ -f "$i" ] || continue
    echo "Processing $i"
    magick "$i" -resize 600 "resize/$i"
done
```

Key points:

- `mkdir -p resize` creates the output directory (the `-p` flag prevents errors if it already exists)
- The glob pattern `*.{jpg,jpeg,png,gif}` targets common image formats
- `[ -f "$i" ] || continue` skips non-matching patterns safely
- `magick` is the modern ImageMagick command (replaces deprecated `convert`)
- `-resize 600` scales the image to 600px width, maintaining aspect ratio

To resize to a specific width and height without maintaining aspect ratio, use:

``` bash
magick "$i" -resize 600x400\! "resize/$i"
```

The backslash-escaped `!` forces exact dimensions.

## Handling Filenames with Spaces

The script above already handles spaces correctly because we’re using proper quoting. The old `IFS` trick is unnecessary with modern bash:

``` bash
mkdir -p resize
for i in *; do
    [ -f "$i" ] || continue
    magick "$i" -resize 600 "resize/$i"
done
```

The quotes around `"$i"` protect filenames with spaces, newlines, and special characters.

## Using Parallel Processing for Speed

For large batches, process multiple images simultaneously:

``` bash
mkdir -p resize
find . -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.png" \) | \
    parallel magick {} -resize 600 "resize/{/}"
```

Install `parallel` if needed (`sudo apt install parallel` on Debian/Ubuntu). This dramatically speeds up processing on multi-core systems.

## Using FFmpeg for Additional Control

FFmpeg can handle batch image resizing with more advanced options:

``` bash
mkdir -p resize
for i in *.{jpg,png}; do
    [ -f "$i" ] || continue
    ffmpeg -i "$i" -vf "scale=600:-1" "resize/$i" -y
done
```

The `-vf "scale=600:-1"` filter scales to 600px width with proportional height. Use `scale=600:400` for fixed dimensions.

## Converting Between Formats

Resize and convert formats in one step:

``` bash
mkdir -p resize
for i in *.png; do
    [ -f "$i" ] || continue
    magick "$i" -resize 600 -quality 85 "resize/${i%.png}.jpg"
done
```

The `${i%.png}` removes the `.png` extension before adding `.jpg`.

## Checking Results

Before processing hundreds of images, test on a single file:

``` bash
magick original.jpg -resize 600 test.jpg
identify test.jpg  # Check dimensions and file size
```

Use `identify` to verify the output dimensions and confirm quality settings produce acceptable file sizes.

## Common Gotchas

- **Progressive JPEG**: Use `magick -interlace Plane` for web-optimized JPEGs
- **Transparency**: PNG resizing preserves alpha channels by default; JPEGs don’t support them
- **Disk space**: Keep the original directory and verify the resize folder has enough space before running large batches
- **ImageMagick policies**: Some systems restrict ImageMagick’s functionality via `/etc/ImageMagick-6/policy.xml`; adjust if needed

ImageMagick remains the standard because it handles edge cases well, produces consistent output, and integrates seamlessly with shell scripts.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Batch Resize Images on Linux with ImageMagick with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Batch Resize Images on Linux with ImageMagick. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
