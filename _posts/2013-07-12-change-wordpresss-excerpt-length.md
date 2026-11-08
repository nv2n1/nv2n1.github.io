---
title: "Customize WordPress Excerpt Length via Functions.php"
date: 2013-07-12 16:46:10 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/change-wordpresss-excerpt-length/
---

WordPress generates excerpts by default using the first 55 words of post content. You can override this globally or per-post type by adding filters to your theme or a must-use plugin.

## Basic excerpt length filter

Add this to `wp-content/themes/your-theme/functions.php`:

``` php
function custom_excerpt_length( $length ) {
    return 35;
}
add_filter( 'excerpt_length', 'custom_excerpt_length' );
```

Replace `35` with your desired word count. This filter affects all auto-generated excerpts produced by `the_excerpt()` calls.

**Important:** This only applies to excerpts WordPress generates from post content. If you’ve manually set an excerpt in the post editor’s “Excerpt” field, WordPress uses that instead and ignores this filter.

## Different excerpt lengths by post type or page

Use conditional logic to apply different lengths in different contexts:

``` php
function custom_excerpt_length( $length ) {
    if ( is_admin() ) {
        return $length;
    }

    if ( is_home() || is_archive() ) {
        return 30;
    }

    if ( is_singular( 'post' ) ) {
        return 50;
    }

    if ( is_singular( 'page' ) ) {
        return 75;
    }

    return $length;
}
add_filter( 'excerpt_length', 'custom_excerpt_length' );
```

This returns 30 words on home and archive pages, 50 on single posts, and 75 on pages. Adjust the conditionals based on your site structure.

## Customize the excerpt ending

WordPress appends `[...]` by default when an excerpt is truncated. Change this with the `excerpt_more` filter:

``` php
function custom_excerpt_more( $more ) {
    return ' <a href="' . get_permalink() . '">Read more →</a>';
}
add_filter( 'excerpt_more', 'custom_excerpt_more' );
```

This replaces the ellipsis with a “Read more” link that points to the full post.

## Using a child theme

If you’re using a third-party theme, create a child theme to protect your customizations during theme updates:

1.  Create the directory: `wp-content/themes/your-theme-child/`
2.  Create `style.css` with a header identifying the parent:

``` css
/*
 Theme Name: Your Theme Child
 Template: your-theme
 */
```

3.  Create `functions.php`:

``` php
<?php
add_action( 'wp_enqueue_scripts', 'enqueue_child_theme_styles' );
function enqueue_child_theme_styles() {
    wp_enqueue_style( 'parent-theme', get_template_directory_uri() . '/style.css' );
    wp_enqueue_style( 'child-theme', get_stylesheet_uri() );
}

function custom_excerpt_length( $length ) {
    return 35;
}
add_filter( 'excerpt_length', 'custom_excerpt_length' );
```

## Must-use plugins for persistent customizations

For critical customizations that should survive theme changes, use a must-use (MU) plugin instead. MU plugins load before regular plugins and themes:

1.  Create `wp-content/mu-plugins/excerpt-length.php`
2.  Add your filter code:

``` php
<?php
function custom_excerpt_length( $length ) {
    return 35;
}
add_filter( 'excerpt_length', 'custom_excerpt_length' );
```

MU plugins are ideal for site-critical functionality that shouldn’t depend on theme or plugin activation state.

## Generate excerpts programmatically

For complex scenarios where filters aren’t enough, generate excerpts in your templates directly:

``` php
<?php
$excerpt = wp_trim_words( get_the_content(), 30, '... <a href="' . get_permalink() . '">Continue reading</a>' );
echo wp_kses_post( $excerpt );
```

`wp_trim_words()` returns exactly 30 words (adjustable) and lets you specify custom text at the end. Use `wp_kses_post()` to sanitize the HTML output safely.

## Testing your changes

After implementing your filter:

- Check your homepage and archive pages to verify `the_excerpt()` displays correctly
- Confirm manually-set excerpts still work (they should bypass your filter)
- If using post-type conditionals, test each post type
- Clear any caching plugin’s cache
- Check the browser’s page source to ensure your custom “Read more” link appears

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Customize WordPress Excerpt Length via Functions.php with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Customize WordPress Excerpt Length via Functions.php. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
