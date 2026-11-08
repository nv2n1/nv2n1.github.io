---
title: "Hide AdSense Ads on Mobile and WebView in WordPress"
date: 2018-03-24 11:47:35 +0000
layout: post
canonical: https://www.systutorials.com/block-ads-in-wordpress-while-mobile-view/
---

When you wrap your WordPress site in a native Android app using WebView, Google’s AdSense policy prohibits serving those ads through the app wrapper. You need to hide AdSense on mobile views while keeping them on desktop, and ideally detect when your site is loaded inside a WebView to block ads there too.

## Detecting Mobile and WebView Context

The `wp_is_mobile()` function works for basic mobile detection, but it won’t distinguish between a browser and a WebView wrapper. For better control, you need to detect the WebView User-Agent specifically.

Add this to your theme’s `functions.php`:

``` php
function is_webview_app() {
    $user_agent = $_SERVER['HTTP_USER_AGENT'] ?? '';
    // Android WebView detection
    if ( strpos( $user_agent, 'wv' ) !== false || strpos( $user_agent, 'Version' ) === false ) {
        return true;
    }
    // iOS WebView detection
    if ( strpos( $user_agent, 'Mobile' ) !== false && strpos( $user_agent, 'Safari' ) === false ) {
        return true;
    }
    return false;
}

function should_show_adsense() {
    return ! ( wp_is_mobile() || is_webview_app() );
}
```

## Method 1: Direct Theme Code

If you’ve added AdSense code directly in your theme files (like `sidebar.php`, `single.php`, etc.), wrap the ads:

``` php
<?php if ( should_show_adsense() ) : ?>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
         data-ad-slot="xxxxxxxxxx"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
<?php endif; ?>
```

## Method 2: Using Ad Plugins

For plugins like Advanced Ads, Mediavine, or AdThrive, check their settings first. Most modern ad plugins have built-in options to disable ads on mobile or specific conditions.

If using a simpler plugin that doesn’t have mobile options, you can filter its output:

``` php
add_filter( 'the_content', function( $content ) {
    if ( ! should_show_adsense() ) {
        // Remove ad shortcodes from content
        $content = preg_replace( '/\[adsbygoogle.*?\]/i', '', $content );
    }
    return $content;
} );
```

## Method 3: Widget Logic

For sidebar widgets, install and activate **Widget Context** (successor to the older Widget Logic plugin). It lets you conditionally display widgets based on PHP code or predefined conditions without coding.

Alternatively, add this to `functions.php` to control widgets programmatically:

``` php
add_filter( 'sidebars_widgets', function( $sidebars_widgets ) {
    if ( should_show_adsense() ) {
        return $sidebars_widgets;
    }

    // Remove widgets by ID (adjust 'custom_html-2' to your widget ID)
    if ( isset( $sidebars_widgets['sidebar-1'] ) ) {
        $sidebars_widgets['sidebar-1'] = array_filter(
            $sidebars_widgets['sidebar-1'],
            function( $widget_id ) {
                return strpos( $widget_id, 'custom_html' ) === false;
            }
        );
    }

    return $sidebars_widgets;
} );
```

## Caching Configuration

If you use caching plugins, you **must** separate caches for mobile and desktop, or ads will still appear incorrectly on mobile.

**WP Super Cache:**

- Go to Settings → WP Super Cache
- Check “Cache mobile requests separately” under Advanced
- This ensures mobile views get cached without ads

**LiteSpeed Cache:**

``` php
// In .htaccess or via plugin UI, set:
Header set Cache-Control "private"
```

**WP Rocket:**

- Settings → Mobile → Check “Enable mobile cache”
- This automatically handles mobile-specific caching

**Cloudflare:**

- Create a cache rule for mobile User-Agents
- Add a page rule: `https://yoursite.com/* → Cache Level: Bypass` for mobile

## Client-Side Detection (Fallback)

If server-side detection fails, add this to your header template:

``` javascript
<script>
function isWebView() {
    var ua = navigator.userAgent;
    return /wv|Version\/[\d.]+.*Safari\/[\d.]+/.test(ua);
}

if (isWebView() || /Android|webOS|iPhone|iPad/.test(ua)) {
    document.body.classList.add('no-ads');
}
</script>
```

Then hide ads with CSS:

``` css
body.no-ads .adsbygoogle {
    display: none !important;
}
```

## Testing

Test your WebView detection:

- Use Chrome DevTools to spoof User-Agents
- Test with actual Android WebView by loading your site in Android Studio’s WebView component
- Check browser console for any JavaScript errors loading ad code

Combine server-side detection with caching optimization to ensure ads never serve through your app wrapper while maintaining monetization on web browsers.
