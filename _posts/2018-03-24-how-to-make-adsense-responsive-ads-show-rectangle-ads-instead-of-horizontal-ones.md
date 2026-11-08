---
title: "Force Rectangle Ads in AdSense Responsive Formats"
date: 2018-03-24 11:47:03 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-adsense-responsive-ads-show-rectangle-ads-instead-of-horizontal-ones/
---

If you’re running AdSense responsive ads on a content area narrower than full viewport width, you’ve probably noticed the ads default to horizontal (leaderboard) formats instead of the vertical rectangle ads that typically perform better. You can control which ad sizes appear by modifying the ad format parameter.

## The Problem with Auto Format

When you use `data-ad-format="auto"`, Google’s algorithm chooses ad dimensions based on available space and performance data. On narrower layouts—typically under 728px—it often selects horizontal ads that don’t fit well with content flow and may have lower CTR than rectangle ads.

## Forcing Rectangle Ad Format

Locate your AdSense ad code block, which typically looks like this:

``` html
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
     data-ad-slot="1234567890"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

Change the `data-ad-format` attribute from `"auto"` to `"rectangle"`:

``` html
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-xxxxxxxxxxxxxxxx"
     data-ad-slot="1234567890"
     data-ad-format="rectangle"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

This restricts ads to rectangle dimensions: primarily 336×280 (large rectangle) or 300×250 (medium rectangle).

## Other Useful Format Options

- `data-ad-format="horizontal"` — Forces leaderboard (728×90) or similar horizontal formats
- `data-ad-format="vertical"` — Restricts to vertical skyscraper (120×600, 160×600, 300×600)
- `data-ad-format="auto"` — Default behavior; Google optimizes based on performance

## Why Rectangle Ads Perform Better

Rectangle ads typically have higher engagement rates because:

- They integrate more naturally with content flow
- They occupy less horizontal space on narrow viewports
- Users are more accustomed to this ad format
- They work well both on desktop and mobile

## Important Notes

You don’t need any special AdSense account tier to use specific ad formats—this is a standard feature available in the AdSense settings interface under “Advanced Options.” You can also manage ad format preferences per placement in your AdSense dashboard.

Keep in mind that forcing a specific format may reduce the number of available ads in Google’s inventory for your site, potentially lowering overall earnings. Monitor your performance metrics after making changes. If revenue drops significantly, consider using `"auto"` or testing different formats to find the optimal balance.

## Mobile Responsiveness with Rectangle Ads

If you’re using `data-full-width-responsive="true"` alongside `data-ad-format="rectangle"`, the ad will scale responsively while maintaining rectangle proportions. On very narrow mobile screens (under 300px), ensure your content area width accommodates at least a 300×250 rectangle, or the ad may not display.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
