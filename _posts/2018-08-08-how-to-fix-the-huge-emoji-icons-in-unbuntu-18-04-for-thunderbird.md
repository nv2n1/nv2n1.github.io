---
title: "Fixing Oversized Emoji in Thunderbird: Font Configuration Guide"
date: 2018-08-08 04:09:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-fix-the-huge-emoji-icons-in-unbuntu-18-04-for-thunderbird/
---

Emoji rendering at incorrect sizes in Thunderbird usually comes down to font configuration. Unlike browsers that inherit system emoji rendering, Thunderbird manages its own font stack, which can drift out of sync with your system fonts or get corrupted in Thunderbird’s cache.

## Install a Color Emoji Font

Start by ensuring you have a proper color emoji font available system-wide:

``` bash
sudo apt install fonts-noto-color-emoji
```

For other distributions:

``` bash
# Fedora/RHEL
sudo dnf install google-noto-color-emoji-fonts

# Arch
sudo pacman -S noto-fonts-color-emoji

# Alpine
apk add noto-fonts-emoji
```

Noto Color Emoji is the most widely supported and reliable option across platforms.

## Rebuild the Font Cache

After installation, force a rebuild of the system font cache:

``` bash
fc-cache -fv
```

The `-f` flag forces a complete rebuild (useful when changes don’t immediately take effect), and `-v` gives you verbose output. Verify the emoji font is now indexed:

``` bash
fc-list | grep -i "noto color emoji"
```

You should see output confirming the font path and variants.

## Restart Thunderbird Completely

Don’t just close the window—fully terminate the process and clear font-related memory:

``` bash
killall thunderbird
thunderbird &
```

Or on systems where Thunderbird may have multiple processes:

``` bash
killall -9 thunderbird; sleep 2; thunderbird &
```

## Flatpak-Specific Steps

If you’re running Thunderbird as a Flatpak, it runs in a sandbox and can’t access system fonts by default. Grant read-only access to both user and system font directories:

``` bash
flatpak override --user --filesystem=~/.local/share/fonts:ro com.thunderbird.Thunderbird
flatpak override --user --filesystem=/usr/share/fonts:ro com.thunderbird.Thunderbird
```

The `:ro` flag ensures fonts are mounted read-only, which is sufficient and safer. Restart Thunderbird after applying these overrides.

## Check Your Display Server

Modern Ubuntu (22.04+) and Fedora default to Wayland instead of X11. Emoji rendering behavior differs between them:

- **X11**: System-level font rendering can sometimes conflict with application-level emoji display
- **Wayland**: Applications handle emoji rendering directly, so system font issues are less likely but require proper font availability within the app’s environment

Check which display server you’re using:

``` bash
echo $XDG_SESSION_TYPE
```

If you’re on Wayland and emoji size issues persist after the above steps, the problem likely lives in Thunderbird’s preferences rather than system fonts.

## Adjust Thunderbird Font Settings

If emoji still render oversized despite correct fonts installed:

1.  Open Thunderbird and go to **Settings** → **Fonts & Colors**
2.  Under the **Proportional** section, check that the font size is reasonable (12pt minimum for readability)
3.  Try unchecking **Allow messages to use other fonts** to enforce uniform emoji sizing across all messages

Alternatively, edit the Thunderbird profile directly. Find your profile folder:

``` bash
ls -d ~/.thunderbird/*.default-release/
```

Open `prefs.js` in that directory and verify or add these settings:

    user_pref("font.minimum-size.x-unicode", 12);
    user_pref("font.size.variable.x-unicode", 16);

Adjust point sizes to your preference. The `x-unicode` entries specifically control emoji and symbol rendering.

## Clear Thunderbird’s Cached Fonts

Thunderbird caches font metrics, and corruption can cause rendering issues. Close Thunderbird and remove the glyph cache:

``` bash
killall thunderbird
rm -rf ~/.thunderbird/*.default-release/startupCache/
rm -f ~/.thunderbird/*.default-release/glyph-metrics-cache.bin
thunderbird &
```

This forces Thunderbird to recalculate font metrics on the next launch. Wait 10–15 seconds after starting; the first startup will be slower.

## Verify You’re Running Recent Thunderbird

Older Thunderbird versions (before 115) had known emoji rendering issues. Check your current version:

``` bash
thunderbird --version
```

If you’re on an older version, update:

``` bash
sudo apt upgrade thunderbird
```

For Flatpak, updates are automatic, but you can force a check:

``` bash
flatpak update com.thunderbird.Thunderbird
```

## Troubleshooting Checklist

If emoji still render incorrectly:

1.  **List all installed emoji fonts** to check for conflicts:

    ``` bash
    fc-list | grep -i emoji
    ```

    You should see only one color emoji font listed. If multiple are present, remove duplicates.

2.  **Verify font is indexed correctly**:

    ``` bash
    fc-list "Noto Color Emoji"
    ```

3.  **Force font redetection** by clearing startupCache (shown above).

4.  **Check if message-level font overrides are causing issues**. Edit `prefs.js` and add:

        user_pref("mailnews.display.plaintext_globalplaintext", true);
        user_pref("mailnews.display.html_as", 1);

    This ensures all messages use your default font configuration, reducing emoji size inconsistencies between received emails.

5.  **Test in a fresh profile** to rule out profile corruption:

    ``` bash
    thunderbird -ProfileManager
    ```

    Create a new profile and check if emoji render correctly. If they do, your original profile is corrupted and needs the cache-clearing steps above.

Most emoji sizing issues resolve after installing Noto Color Emoji, rebuilding the font cache, and restarting Thunderbird. If problems persist, the issue is usually cached fonts within Thunderbird itself—the cache-clearing steps fix nearly all remaining cases.
