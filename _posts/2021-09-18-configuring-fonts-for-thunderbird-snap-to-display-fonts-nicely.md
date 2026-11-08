---
title: "Configuring Custom Fonts in Thunderbird Snap"
date: 2021-09-18 14:41:17 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/configuring-fonts-for-thunderbird-snap-to-display-fonts-nicely/
---

Snaps bundle applications with their dependencies to work across distributions, but this isolation creates compatibility gaps. One common problem with Thunderbird snap is missing or incorrectly rendered fonts—a direct result of how fontconfig is handled inside the snap sandbox.

## Why Thunderbird snap doesn’t use system fonts

Thunderbird snap includes its own `fonts.conf` located at `~/.var/app/com.thunderbird.Thunderbird/config/fontconfig/fonts.conf` (note: snap paths changed in recent versions; some systems still use `~/snap/thunderbird/current/.config/fontconfig/fonts.conf`).

The default configuration looks like this:

``` xml
<fontconfig>
  <dir>~/.local/share/fonts</dir>
  <dir>~/.fonts</dir>
  <dir>/snap/thunderbird/current/gnome-platform/usr/share/fonts</dir>
  <dir>/usr/local/share/fonts</dir>
  <dir>/usr/share/fonts</dir>
  <cachedir prefix="xdg">fontconfig</cachedir>
  <cachedir>/var/snap/thunderbird/common/fontconfig</cachedir>
</fontconfig>
```

The problem: system-wide fontconfig paths (`/etc/fonts/conf.d` and `/etc/fonts/fonts.conf`) are excluded from the snap’s fontconfig scope. This means custom fonts installed system-wide and font rendering rules you’ve configured globally won’t apply to Thunderbird.

## Fix: Include system fontconfig paths

Edit your Thunderbird snap’s `fonts.conf` file to include system paths. First, locate the file:

``` bash
# For newer snaps
cat ~/.var/app/com.thunderbird.Thunderbird/config/fontconfig/fonts.conf

# For older snaps
cat ~/.snap/thunderbird/current/.config/fontconfig/fonts.conf
```

Add these lines at the top of the `<fontconfig>` block:

``` xml
<include ignore_missing="yes">/etc/fonts/conf.d</include>
<include ignore_missing="yes">/etc/fonts/fonts.conf</include>
```

Your modified file should look like:

``` xml
<fontconfig>
  <include ignore_missing="yes">/etc/fonts/conf.d</include>
  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>
  <dir>~/.local/share/fonts</dir>
  <dir>~/.fonts</dir>
  <dir>/snap/thunderbird/current/gnome-platform/usr/share/fonts</dir>
  <dir>/usr/local/share/fonts</dir>
  <dir>/usr/share/fonts</dir>
  <cachedir prefix="xdg">fontconfig</cachedir>
  <cachedir>/var/snap/thunderbird/common/fontconfig</cachedir>
</fontconfig>
```

The `ignore_missing="yes"` attribute ensures fontconfig won’t fail if paths don’t exist—useful for portability across systems with different font configurations.

After saving, close Thunderbird completely and reopen it. The system font configuration should now apply.

## Verification and troubleshooting

To verify fonts are being loaded correctly, check fontconfig’s effective configuration:

``` bash
fc-list : family
```

This lists all fonts available to your user. If you installed fonts recently, run:

``` bash
fc-cache -fv
```

to rebuild the font cache. Then restart Thunderbird.

If specific fonts still render incorrectly, check your system’s font substitution rules:

``` bash
fc-match "Your Font Name"
```

This shows which actual font file fontconfig selects when you request a particular font. Mismatches here indicate configuration issues in `/etc/fonts/conf.d/`.

## Persistence across updates

Snap updates can regenerate `fonts.conf`, overwriting your changes. Monitor this after updates and reapply the fix if needed. For a more permanent solution, create a custom fontconfig drop-in file:

``` bash
mkdir -p ~/.var/app/com.thunderbird.Thunderbird/config/fontconfig/conf.d
```

Add your system paths to a new file:

``` bash
cat > ~/.var/app/com.thunderbird.Thunderbird/config/fontconfig/conf.d/99-system-paths.conf << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <include ignore_missing="yes">/etc/fonts/conf.d</include>
  <include ignore_missing="yes">/etc/fonts/fonts.conf</include>
</fontconfig>
EOF
```

This approach survives snap updates since it’s in a separate file rather than the main `fonts.conf`.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
