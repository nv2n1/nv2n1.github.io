---
title: "Safely Allow Code Blocks in WordPress Comments"
date: 2018-03-24 11:40:17 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /how-to-allow-pre-tag-in-wordpress-comments/
---

WordPress sanitizes HTML in comments by default for security. The `<pre>` tag is stripped unless you explicitly whitelist it. Here’s how to enable it without compromising security.

## Using wp_allowed_post_html Filter

The proper approach is to whitelist `<pre>` and related tags via the `wp_allowed_post_html` filter:

``` php
function allow_pre_in_comments( $allowed ) {
    $allowed['pre'] = array();
    $allowed['code'] = array(
        'class' => true,
    );
    return $allowed;
}

add_filter( 'wp_allowed_post_html', 'allow_pre_in_comments' );
```

This adds `<pre>` and `<code>` to the whitelist. The `class` attribute on `<code>` is useful for syntax highlighter libraries like Highlight.js or Prism.js.

If you need attributes on `<pre>` itself (less common but sometimes needed):

``` php
function allow_pre_in_comments( $allowed ) {
    $allowed['pre'] = array(
        'class' => true,
        'data-line' => true,  // For line highlighting
    );
    $allowed['code'] = array(
        'class' => true,
    );
    return $allowed;
}

add_filter( 'wp_allowed_post_html', 'allow_pre_in_comments' );
```

Add this to your theme’s `functions.php` or create a mu-plugin at `/wp-content/mu-plugins/allow-code-comments.php`.

## Understanding wp_kses_post()

WordPress uses `wp_kses_post()` internally to sanitize comments. This function compares submitted HTML against the whitelist and strips anything not explicitly allowed. When you modify `wp_allowed_post_html`, you’re expanding that whitelist.

Avoid whitelisting dangerous attributes like `onclick`, `onerror`, or `style` that could introduce XSS vulnerabilities.

## Why pre_comment_approved Doesn’t Work for This

You might find references to the `pre_comment_approved` filter. This hook only controls comment approval status (approved, pending, spam), not HTML sanitization:

``` php
// This does NOT strip or allow tags
function filter_comment_approval( $approved, $commentdata ) {
    // $approved is 1 (approved), 0 (pending), or 'spam'
    return $approved;
}

add_filter( 'pre_comment_approved', 'filter_comment_approval', 10, 2 );
```

For HTML tag filtering, always use `wp_allowed_post_html`.

## Adding Syntax Highlighting

Once `<pre>` and `<code>` are allowed, pair them with a client-side highlighter. Add this to your theme or plugin:

``` php
function enqueue_highlightjs() {
    wp_enqueue_script( 'highlight', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js' );
    wp_enqueue_style( 'highlight-style', 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css' );

    wp_add_inline_script( 'highlight', 'hljs.highlightAll();' );
}

add_action( 'wp_enqueue_scripts', 'enqueue_highlightjs' );
```

Commenters can then use:

``` html
<pre><code class="language-php">echo "Hello, World!";</code></pre>
```

## Testing the Configuration

Submit a test comment with code:

``` html
<pre><code class="language-bash">curl -X GET https://api.example.com/users</code></pre>
```

If the `<pre>` and `<code>` tags appear in the published comment, your filter is active. If they vanish, verify:

1.  The filter function is in a file that loads on every WordPress request
2.  You’re using the correct hook name (`wp_allowed_post_html`)
3.  The function returns the `$allowed` array

## When to Use a Plugin Instead

For technical blogs or sites with heavy code discussion, consider dedicated plugins:

- **Syntax Highlighter Code Fence** — Block-based code formatting with language detection
- **Code Snippets** — Manages code snippets with built-in security handling
- **Prism.js** — Lightweight syntax highlighting (add manually via theme)

These handle escaping and styling automatically, reducing the maintenance burden on custom code.

## Security Best Practices

- Never whitelist tags blindly; only enable what you need
- Don’t allow attributes like `style`, `onclick`, or `onerror`
- Escape code output with `esc_html()` if displaying elsewhere
- Consider requiring comment moderation for sites with public code snippets
- Keep WordPress and plugins updated for security patches

If you’re allowing user-submitted code in comments, assume malicious intent and sanitize accordingly.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Safely Allow Code Blocks in WordPress Comments with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Safely Allow Code Blocks in WordPress Comments. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
