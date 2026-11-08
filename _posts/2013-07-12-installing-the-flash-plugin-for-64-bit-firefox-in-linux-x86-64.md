---
title: "Installing Flash Plugin on 64-bit Firefox for Linux"
date: 2013-07-12 16:32:23 +0000
layout: post
canonical: https://www.systutorials.com/installing-the-flash-plugin-for-64-bit-firefox-in-linux-x86-64/
---

Flash Player reached end-of-life on December 31, 2020, and modern browsers no longer support it. However, if you’re working with legacy systems, archived content, or old web applications that still require Flash, here’s what you need to know about the historical setup and modern alternatives.

## The Original Setup (Historical Reference)

On 64-bit Linux with Firefox, Flash support originally required installing the Adobe Flash plugin:

```wp-block-code
# Ubuntu/Debian (historical)
sudo apt install flashplugin-installer

# Or the Adobe repository method (historical)
sudo apt install adobe-flashplugin
```

For 64-bit Firefox specifically, there was a period where only a 32-bit plugin was available, requiring `nspluginwrapper` to bridge the architecture gap. Later, Adobe released a native 64-bit version that worked directly.

## Why Flash Is No Longer Available

Adobe officially discontinued Flash Player on December 31, 2020:

- All major browsers removed NPAPI plugin support (Chrome, Firefox, Edge, Safari)
- Adobe blocks Flash content from running after January 12, 2021
- The Flash Player download page no longer distributes the plugin
- Modern Linux distributions have removed Flash packages from repositories

## Modern Alternatives for Flash Content

### Ruffle — Flash Emulator

<a href="https://ruffle.rs" rel="nofollow noopener" target="_blank">Ruffle</a> is an open-source Flash Player emulator written in Rust that runs Flash content without the original plugin:

```wp-block-code
# Browser extension (Chrome/Firefox)
# Install from https://ruffle.rs/extensions

# Desktop version for local SWF files
# Download from https://github.com/ruffle-rs/ruffle/releases
./ruffle path/to/file.swf
```

Ruffle supports a growing subset of ActionScript 1/2/3 and works with many legacy Flash games and animations. It’s actively maintained and receives regular compatibility updates.

### Lightspark — Open Source Flash Player

Lightspark is another open-source Flash player that focuses on ActionScript 3 compatibility:

```wp-block-code
sudo dnf install lightspark       # Fedora
sudo apt install lightspark       # Ubuntu/Debian
```

Lightspark integrates with Firefox as an NPAPI plugin replacement and supports many AS3-based applications.

### Flashpoint — Archival Project

<a href="https://flashpointarchive.org" rel="nofollow noopener" target="_blank">BlueMaxima’s Flashpoint</a> is a web game preservation project that has archived thousands of Flash games and animations. It includes a curated launcher with built-in Flash support for playing preserved content offline.

```wp-block-code
# Download Flashpoint Infinity (lightweight) or Flashpoint Ultimate (complete archive)
# From https://flashpointarchive.org/downloads.html
```

## Converting Flash Content to Modern Formats

If you own Flash content that needs to be preserved:

- **Adobe Animate** can export legacy FLA files to HTML5 Canvas or WebGL
- **CreateJS** converts Flash animations to JavaScript/HTML5
- **Swf2js** converts SWF files to JavaScript for browser playback
- **JPEXS Free Flash Decompiler (FFDec)** can extract assets, convert to HTML5, and edit SWF files

```wp-block-code
# Install FFDec for SWF decompilation
# Download from https://github.com/jindrapetrik/jpexs-decompiler
java -jar ffdec.jar file.swf -export script,output_dir
```

## Working with Legacy Enterprise Flash Applications

Some enterprise environments still have Flash-dependent applications:

- Contact the vendor for HTML5 migration paths
- Use Ruffle as a temporary compatibility layer
- Consider browser virtualization (running an old browser in a VM) for critical legacy tools
- Internet Explorer mode in Microsoft Edge can still run some ActiveX/Flash content in enterprise environments

The long-term solution is always migration away from Flash. By 2026, no supported browser should have any Flash dependency.

## Identifying Flash Dependencies in Your Site

To check if your website still has Flash references:

```wp-block-code
# Search HTML for Flash embeds
find /var/www -name '*.html' -exec grep -l 'application/x-shockwave-flash\|
```

Common patterns to look for:

- `<object>` or `<embed>` tags with Flash MIME types
- `swfobject.js` JavaScript includes
- SWF file references in CSS or JavaScript
- ActionScript files (\`.as\`, \`.fla\`) in source repositories

## Browser Console Warnings

Modern browsers show warnings when encountering Flash content. Open the developer console (F12) and look for messages about blocked plugins or unsupported content types. These warnings help identify which pages still reference Flash during a migration audit.
