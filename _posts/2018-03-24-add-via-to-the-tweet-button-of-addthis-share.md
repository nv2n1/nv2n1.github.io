---
title: "Add a Via Parameter to AddThis Tweet Button"
date: 2018-03-24 08:20:32 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /add-via-to-the-tweet-button-of-addthis-share/
---

AddThis provides social sharing buttons for websites. If you’re using the AddThis Tweet button and want to add a `via` parameter (to attribute tweets to a specific Twitter account), here’s how to configure it.

## AddThis Tweet Button with via Parameter

Modify the AddThis button configuration to include the `tw:via` attribute:

```wp-block-code
<!-- AddThis Tweet button with via parameter -->
<a class="addthis_button_tweet"
   tw:via="YourTwitterHandle"
   tw:related="SuggestedFollow"></a>

<!-- Full AddThis toolbox example -->
<div class="addthis_toolbox addthis_default_style">
    <a class="addthis_button_facebook_like" fb:like:layout="button_count"></a>
    <a class="addthis_button_tweet" tw:via="YourHandle" tw:related="OtherHandle"></a>
    <a class="addthis_button_google_plusone" g:plusone:size="medium"></a>
</div>
```

The `tw:via` attribute adds “via @YourTwitterHandle” to the pre-filled tweet text. The `tw:related` attribute suggests an additional account to follow after tweeting.

## Additional Tweet Button Attributes

AddThis supports several Twitter-specific attributes:

- `tw:via="handle"` — Attribution account (without @)
- `tw:related="handle1,handle2"` — Suggested follow accounts
- `tw:text="Custom text"` — Override the default tweet text
- `tw:url="https://example.com"` — Override the shared URL
- `tw:count="horizontal|vertical|none"` — Count box position
- `tw:lang="en"` — Language for the tweet button interface

## Using Twitter’s Native Share Button

If you don’t need AddThis’s analytics or other sharing platforms, Twitter provides a native share button with simpler configuration:

```wp-block-code
<a href="https://twitter.com/intent/tweet?via=YourHandle&text=Check+this+out&url=https://example.com"
   class="twitter-share-button"
   data-via="YourHandle"
   data-related="OtherHandle">Tweet</a>

<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
```

## Web Intent URL Format

You can also create a simple share link without any JavaScript:

```wp-block-code
<a href="https://twitter.com/intent/tweet?via=YourHandle&text=Hello+World&url=https%3A%2F%2Fexample.com"
   target="_blank"
   rel="noopener noreferrer">Share on Twitter</a>
```

Parameters for the intent URL:

- `text` — Pre-filled tweet text (URL-encoded)
- `url` — URL to share (URL-encoded)
- `via` — Attribution handle (without @)
- `related` — Comma-separated suggested follow handles
- `hashtags` — Comma-separated hashtags (without \#)
- `in_reply_to` — Tweet ID to reply to

## AddThis Alternatives (2026)

AddThis was shut down by Oracle in May 2023. If you’re still using AddThis code, it no longer works. Here are modern alternatives:

- **ShareThis** — Similar sharing widget, free tier available
- **AddToAny** — Lightweight sharing buttons with wide platform support
- **Native share buttons** — Use each platform’s official button (best performance)
- **Web Share API** — Browser-native sharing dialog for mobile: `navigator.share({title, text, url})`

For most sites in 2026, using native platform buttons or the Web Share API provides better performance and privacy than third-party sharing widgets.

## Implementing Web Share API

The modern approach to sharing on the web uses the browser’s native sharing dialog:

```wp-block-code
// Check if Web Share API is supported
if (navigator.share) {
  navigator.share({
    title: 'My Page Title',
    text: 'Check out this article!',
    url: window.location.href
  })
  .then(() => console.log('Shared successfully'))
  .catch((error) => console.log('Sharing failed:', error));
} else {
  // Fallback: copy to clipboard or show custom share menu
  navigator.clipboard.writeText(window.location.href)
    .then(() => alert('Link copied to clipboard!'));
}
```

Browser support is excellent in 2026 — all major mobile browsers and most desktop browsers support it. For browsers that don’t, provide a clipboard fallback.

## Migrating from AddThis

If your site still has AddThis code, remove it and replace with lightweight alternatives:

```wp-block-code
<!-- Remove this AddThis code -->
<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-xxxxx"></script>

<!-- Replace with simple share links -->
<div class="share-buttons">
  <a href="https://twitter.com/intent/tweet?via=YourHandle&url=ENCODED_URL&text=TITLE" target="_blank" rel="noopener">Twitter</a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=ENCODED_URL" target="_blank" rel="noopener">Facebook</a>
  <a href="https://www.linkedin.com/shareArticle?mini=true&url=ENCODED_URL" target="_blank" rel="noopener">LinkedIn</a>
</div>
```

This approach is faster (no external JavaScript), privacy-friendly (no tracking), and works without any third-party service dependencies.

## Adding Open Graph Meta Tags

For better social sharing across all platforms, add Open Graph meta tags to your pages:

```wp-block-code
<meta property="og:title" content="Your Page Title">
<meta property="og:description" content="A brief description of the page">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@YourHandle">
```

These tags control how your page appears when shared on Twitter, Facebook, LinkedIn, and other platforms — regardless of which sharing button implementation you use.
