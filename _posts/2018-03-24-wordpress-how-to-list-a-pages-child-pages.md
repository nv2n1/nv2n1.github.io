---
title: "How to Display Child Pages in WordPress"
date: 2018-03-24 08:14:16 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/wordpress-how-to-list-a-pages-child-pages/
---

The `wp_list_pages()` function is the standard way to display child pages of a page in WordPress. This is useful for building navigation menus, sidebars, or displaying page hierarchies.

## Basic Implementation

Here’s a working example that displays all child pages of the current page:

``` php
<h3>Pages under <?php the_title(); ?></h3>
<div class="entry">
  <ul>
    <?php 
      wp_list_pages(array(
        'title_li'    => '',
        'child_of'    => get_the_ID(),
        'sort_column' => 'menu_order',
      ));
    ?>
  </ul>
</div>
```

Note the shift from global `$id` to `get_the_ID()`. The global `$id` variable isn’t reliable in all contexts (like custom queries or Gutenberg blocks), so `get_the_ID()` is the safer modern approach.

## Common Parameters

`wp_list_pages()` accepts an array of arguments. Here are the most useful ones:

- **title_li**: Sets the list item wrapper (empty string `''` removes it)
- **child_of**: Parent page ID — use `get_the_ID()` for the current page
- **sort_column**: Order by `menu_order`, `post_title`, `post_date`, etc.
- **exclude**: Comma-separated page IDs to exclude
- **echo**: Set to `false` to return the HTML instead of echoing it
- **depth**: How many levels deep to display (`-1` for unlimited)
- **link_before** / **link_after**: Wrap page titles with custom HTML

## Advanced Example with Modified Dates

To display child pages with their last modified date:

``` php
<?php 
  wp_list_pages(array(
    'title_li'     => '',
    'child_of'     => get_the_ID(),
    'sort_column'  => 'menu_order',
    'show_date'    => 'modified',
    'date_format'  => get_option('date_format'),
  ));
?>
```

Using `get_option('date_format')` respects the site’s date settings rather than hardcoding a format.

## Excluding Pages

To skip specific pages from the list:

``` php
<?php 
  wp_list_pages(array(
    'title_li' => '',
    'child_of' => get_the_ID(),
    'exclude'  => '42, 99, 156',
  ));
?>
```

## Capturing Output Instead of Echoing

If you need to manipulate the output before displaying it:

``` php
<?php 
  $pages = wp_list_pages(array(
    'title_li' => '',
    'child_of' => get_the_ID(),
    'echo'     => false,
  ));

  if (!empty($pages)) {
    echo '<nav class="child-pages">';
    echo $pages;
    echo '</nav>';
  }
?>
```

## Template Tag Considerations

For block-based themes using Gutenberg, avoid using `wp_list_pages()` directly in templates. Use the built-in Page List block instead, or register a custom block that wraps the function. If you need `wp_list_pages()` in a block, use `do_blocks()` or create a dynamic block with a render callback.

## Alternatives

For more control over output HTML, use `get_pages()` with a custom loop:

``` php
<?php 
  $child_pages = get_pages(array(
    'parent' => get_the_ID(),
    'sort_column' => 'menu_order',
  ));

  if (!empty($child_pages)) {
    echo '<ul>';
    foreach ($child_pages as $page) {
      echo '<li>';
      echo '<a href="' . get_permalink($page->ID) . '">';
      echo esc_html($page->post_title);
      echo '</a>';
      echo '</li>';
    }
    echo '</ul>';
  }
?>
```

This approach gives you complete control over HTML structure and lets you access additional page properties like `post_excerpt` or custom fields.

## 2026 Best Practices and Advanced Techniques

For How to Display Child Pages in WordPress, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
