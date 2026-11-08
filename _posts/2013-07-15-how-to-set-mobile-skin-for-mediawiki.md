---
title: "Device-Specific Skins in MediaWiki: Setup & Configuration"
date: 2013-07-15 12:57:49 +0000
modified: 2026-04-11 17:16:18 +0000
author: "Eric Ma"
layout: post
categories: [testing-devops]
canonical: /how-to-set-mobile-skin-for-mediawiki/
---

Modern MediaWiki installations should prioritize responsive design, but you may still need explicit device-based skin switching for specific use cases. This guide covers both approaches and how to implement them correctly.

## Responsive Skins: The Recommended Approach

The default solution is using a responsive skin that adapts automatically to screen size without separate configuration. **Vector 2022** (default in MediaWiki 1.35+) and **MinervaNeue** (the official mobile skin) both handle this well.

To enable MinervaNeue:

``` php
wfLoadSkin( 'MinervaNeue' );
```

MinervaNeue auto-detects mobile browsers and adjusts the interface accordingly. This approach is superior to user-agent detection because it provides better UX and requires less maintenance.

## Device-Based Skin Switching

If you need to assign different skins based on device type, use proper user-agent detection instead of fragile regex patterns. Add this function to `LocalSettings.php`:

``` php
function isMobileDevice() {
    $userAgent = $_SERVER['HTTP_USER_AGENT'] ?? '';
    $mobilePatterns = [
        '/iphone|ipod|ipad/i',
        '/android/i',
        '/windows phone/i',
        '/webos/i',
        '/opera mini/i',
        '/mobile/i'
    ];

    foreach ($mobilePatterns as $pattern) {
        if ( preg_match( $pattern, $userAgent ) ) {
            return true;
        }
    }
    return false;
}

// Set skin based on device type
if ( isMobileDevice() ) {
    $wgDefaultSkin = 'MinervaNeue';
} else {
    $wgDefaultSkin = 'vector';
}
```

This is more maintainable than inline regex and easier to update as device identifiers change. Note that user-agent detection has inherent limitations—modern JavaScript detection or server-side analytics can be more accurate, but user-agent detection remains lightweight for most deployments.

## Let Users Override Device Detection

Allow users to force a specific skin via query parameter:

``` php
$forceDesktop = isset( $_GET['mobilemode'] ) && $_GET['mobilemode'] === 'desktop';
$forceMobile = isset( $_GET['mobilemode'] ) && $_GET['mobilemode'] === 'mobile';

if ( $forceMobile ) {
    $wgDefaultSkin = 'MinervaNeue';
} elseif ( $forceDesktop ) {
    $wgDefaultSkin = 'vector';
} elseif ( isMobileDevice() ) {
    $wgDefaultSkin = 'MinervaNeue';
} else {
    $wgDefaultSkin = 'vector';
}
```

Users can append `?mobilemode=desktop` or `?mobilemode=mobile` to force a specific experience.

## Configure Logos and Branding

Set your site logo with DPI variants in `LocalSettings.php`:

``` php
$wgLogos = [
    '1x' => "$wgUploadDirectory/logo.png",
    '1.5x' => "$wgUploadDirectory/logo-1.5x.png",
    '2x' => "$wgUploadDirectory/logo-2x.png",
    'icon' => "$wgUploadDirectory/favicon.ico",
];

// For MinervaNeue mobile login
$wgMFLogInEndpoint = "/Special:UserLogin";
$wgMFStubEnabledDevices = [ 'base', 'mobile' ];
```

Use structured logo configuration with DPI variants (1x, 1.5x, 2x) instead of relying on root-level files. This ensures logos display correctly across different device densities.

## Cache Management with Device Detection

File caching with device detection requires careful handling—mobile and desktop versions must be cached separately to avoid serving the wrong markup to users.

The best approach is separate cache directories:

``` php
if ( isMobileDevice() ) {
    $wgFileCacheDirectory = "{$IP}/cache/mobile";
} else {
    $wgFileCacheDirectory = "{$IP}/cache/desktop";
}

$wgUseFileCache = true;
$wgCachePages = true;
```

Alternatively, disable caching for mobile if your server has sufficient resources:

``` php
if ( isMobileDevice() ) {
    $wgUseFileCache = false;
} else {
    $wgUseFileCache = true;
    $wgFileCacheDirectory = "{$IP}/cache";
}
```

The separate directory approach is preferable for performance—it preserves caching benefits for all users.

Create the cache directories with proper permissions:

``` bash
mkdir -p $MEDIAWIKI_ROOT/cache/mobile
mkdir -p $MEDIAWIKI_ROOT/cache/desktop
chown www-data:www-data $MEDIAWIKI_ROOT/cache/mobile
chown www-data:www-data $MEDIAWIKI_ROOT/cache/desktop
chmod 755 $MEDIAWIKI_ROOT/cache/mobile
chmod 755 $MEDIAWIKI_ROOT/cache/desktop
```

Replace `www-data` with your web server’s user (apache, nginx, \_www, or other depending on your distribution).

## Test Your Configuration

Test skin selection using curl with different user agents:

``` bash
# iPhone user agent
curl -H "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15" http://yourwiki.local/

# Android user agent
curl -H "User-Agent: Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36" http://yourwiki.local/

# Desktop user agent
curl -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" http://yourwiki.local/
```

Verify the response includes the correct skin files and markup for each device type.

Use browser developer tools (press F12) to test responsive design without physical devices. Check the Network tab to confirm correct skin files are loading, and use device emulation mode to test at different viewport sizes.

For debugging, temporarily add logging to `LocalSettings.php`:

``` php
error_log( "Mobile: " . ( isMobileDevice() ? 'yes' : 'no' ) . " | Skin: $wgDefaultSkin" );
```

Monitor `debug.log` to verify skin selection logic is executing correctly, then remove the logging line for production.

## Performance Considerations

For wikis with high traffic, consider using a reverse proxy (nginx, Varnish, or Cloudflare) to cache responses based on device detection headers. This offloads device detection from PHP and improves cache hit rates. Set appropriate cache keys that include device type in the cache key calculation.

If you’re using Redis or Memcached, store device detection results briefly to reduce repeated user-agent parsing overhead.
