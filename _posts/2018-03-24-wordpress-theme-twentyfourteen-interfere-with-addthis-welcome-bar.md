---
title: "AddThis Welcome Bar Conflict with WordPress Twenty Fourteen Theme"
date: 2018-03-24 08:20:38 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/wordpress-theme-twentyfourteen-interfere-with-addthis-welcome-bar/
---

If you’re using the AddThis Welcome Bar with WordPress, you may see an unwanted gap appearing at the top of your page. This happens because AddThis injects a placeholder div that reserves vertical space:

``` html
<div class="addthis_bar_placeholder" style="height: 46px;"></div>
```

The 46px height creates a visible gap that disrupts your layout, especially on themes with fixed headers or specific spacing requirements.

## Quick fix with CSS

The simplest solution is to override the placeholder’s positioning to prevent it from consuming page space. Add this CSS to your theme:

``` css
.addthis_bar_placeholder {
  position: absolute;
  height: 0;
}
```

### Where to add this CSS

You have several options:

- **Child theme stylesheet** — Add the rule to your child theme’s `style.css` (recommended for maintainability)
- **Theme customizer** — Go to **Appearance → Customize → Additional CSS** and paste the rule there
- **Custom CSS plugins** — Use <a href="https://wordpress.org/plugins/custom-css-js/" rel="nofollow noopener" target="_blank">Simple Custom CSS and JS</a> or similar
- **functions.php** — Enqueue a custom stylesheet in your theme’s `functions.php`:

``` php
function fix_addthis_placeholder() {
  wp_enqueue_style(
    'addthis-fix',
    get_stylesheet_directory_uri() . '/addthis-fix.css'
  );
}
add_action( 'wp_enqueue_scripts', 'fix_addthis_placeholder' );
```

## Why this works

Setting `position: absolute` removes the element from the document flow, so it no longer reserves horizontal space. The `height: 0` ensures the placeholder doesn’t take any vertical space either. The AddThis bar itself still displays normally since it’s a separate element.

## Alternative approaches

If the above doesn’t fully resolve your issue:

- **Adjust the bar’s offset** — Some AddThis configurations let you set a negative margin on the bar itself to overlap the gap
- **Move the bar placement** — Consider placing the Welcome Bar lower on the page rather than at the very top, which can sidestep layout conflicts entirely
- **Disable and use inline sharing** — If the Welcome Bar causes persistent problems, disable it and use inline AddThis buttons instead

## Note on modern alternatives

If you’re building new WordPress sites, consider whether AddThis is still the best choice for your sharing needs. Modern themes often handle social sharing natively, and many site owners now rely on WordPress Jetpack or built-in sharing options for better performance and privacy control.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Web Server Best Practices

Keep your web server configuration clean and well-documented. Use version control for configuration files so changes can be tracked and rolled back. Always test configuration changes in a staging environment before applying to production.

Enable gzip compression and browser caching for better performance. Configure proper security headers including Content-Security-Policy, X-Frame-Options, and Strict-Transport-Security for HTTPS sites. Regularly update all server software to patch security vulnerabilities.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
