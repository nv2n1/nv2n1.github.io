---
title: "How to Subscribe to RSS Feeds in Chrome Using Feedly"
date: 2018-03-24 08:16:12 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/set-chrome-rss-subscription-extension-to-subscribe-to-rss-feed-using-feedly/
---

If you use both the Chrome RSS Subscription Extension and Feedly, you can integrate them so that clicking the RSS icon in your browser automatically opens your feed in Feedly instead of the browser’s default handler.

## Understanding the Integration

When you subscribe to an RSS feed through the Chrome extension, it needs a target URL where the subscription gets processed. Feedly has a subscription URL structure that accepts the feed URL as a parameter. By adding Feedly as a custom service in the extension, you create a seamless workflow.

## Finding Your Feed URL

First, locate the RSS feed URL you want to subscribe to. For example:

    https://www.systutorials.com/b/feed/

Feedly’s subscription link for this feed would be:

    http://www.feedly.com/home#subscription/feed/https://www.systutorials.com/b/feed/

## Configuring the Extension

The Chrome RSS Subscription Extension accepts custom subscription services. To add Feedly:

1.  Open the extension’s options/settings page (right-click the extension icon → Options, or find it in Chrome’s extension settings)

2.  Look for the “Add Service” or “Manage Services” section

3.  Add a new service with these details:
    - **Service Name**: Feedly
    - **Service URL**: `http://www.feedly.com/home#subscription/feed/%s`

The `%s` acts as a placeholder for the actual feed URL. When you click the RSS icon on any page, the extension replaces `%s` with the detected feed URL and opens Feedly’s subscription dialog.

## Testing Your Setup

After adding Feedly as a service:

1.  Visit a website with an RSS feed (like a blog)
2.  Click the RSS subscription extension icon in your toolbar
3.  Select “Feedly” from the service dropdown
4.  You should be taken directly to Feedly’s subscription confirmation page

## Alternative: Using Feedly Collections

When you subscribe through Feedly via this method, you can select which collection to add the feed to during the subscription confirmation. This is more flexible than the browser’s default subscription method.

## Note on HTTPS

Modern Feedly uses HTTPS, so you may want to update the URL to:

    https://feedly.com/home#subscription/feed/%s

This ensures better compatibility with newer versions of the service and avoids potential redirect issues.

## Troubleshooting

If the integration doesn’t work:

- Verify you’re using the latest version of both Chrome and the RSS Subscription Extension
- Clear your browser cache and reload the extension
- Check that Feedly’s URL structure hasn’t changed by manually visiting `https://feedly.com/home` and testing a subscription
- Ensure the feed URL is valid by pasting it directly in your browser

This integration eliminates the need to manually copy feed URLs to Feedly and keeps your subscription workflow entirely within the browser.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
