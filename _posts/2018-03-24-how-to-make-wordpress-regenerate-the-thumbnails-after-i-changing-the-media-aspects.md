---
title: "Regenerate WordPress Thumbnails After Changing Image Sizes"
date: 2018-03-24 11:46:40 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-wordpress-regenerate-the-thumbnails-after-i-changing-the-media-aspects/
---

When you change thumbnail dimensions in WordPress, existing images won’t automatically resize to match. You need to regenerate them — either through a plugin or command line.

## Using a Plugin

The easiest approach is the **Regenerate Thumbnails** plugin. Install it from WordPress.org, then activate it.

Once activated:

1.  Navigate to **Tools → Regenerate Thumbnails**
2.  Click the regenerate button
3.  Wait for the process to complete (this can take several minutes on sites with many images)

This works well for small to medium image libraries. For sites with thousands of images, the web interface may timeout.

## Using WP-CLI (Recommended for Large Sites)

For better control and reliability, use WP-CLI:

``` bash
wp media regenerate --yes
```

This regenerates all attachment thumbnails in the background without browser timeout issues.

To regenerate specific attachments:

``` bash
wp media regenerate --post_ids=123,456,789
```

To see progress and skip failures gracefully:

``` bash
wp media regenerate --yes --skip-delete
```

The `--skip-delete` flag keeps original files if regeneration fails, useful for debugging.

## Manual Regeneration via Code

If you need custom logic, add this to your theme’s `functions.php` or a custom plugin:

``` php
// Regenerate all thumbnails
$args = array(
    'post_type'      => 'attachment',
    'post_status'    => 'inherit',
    'posts_per_page' => -1,
);

$attachments = get_posts( $args );

foreach ( $attachments as $attachment ) {
    wp_generate_attachment_metadata( $attachment->ID, get_attached_file( $attachment->ID ) );
}
```

Run this via WP-CLI:

``` bash
wp eval 'include(get_theme_file_path("functions.php")); wp_generate_attachment_metadata(...);'
```

Or create a custom WP-CLI command in a must-use plugin for greater flexibility.

## Before You Regenerate

Backup your uploads directory:

``` bash
cp -r wp-content/uploads wp-content/uploads.backup
```

Check your thumbnail sizes are properly defined in `functions.php`:

``` php
add_image_size( 'featured', 800, 450, true );
add_image_size( 'thumbnail-small', 300, 200, true );
```

The third parameter `true` enables hard cropping to exact dimensions.

## Performance Considerations

- **Large media libraries** (10,000+ images): Use WP-CLI with batch processing
- **Shared hosting**: Run regeneration during off-peak hours to avoid resource limits
- **Custom image sizes**: Make sure you’ve defined them before regenerating, or they’ll generate with default dimensions

## Troubleshooting

If regeneration stalls or produces blank images:

1.  Check file permissions on `wp-content/uploads/`

2.  Verify PHP memory limit is at least 256MB:

    ``` bash
    wp config get WP_MEMORY_LIMIT
    ```

3.  Increase if needed:

    ``` bash
    wp config set WP_MEMORY_LIMIT 512M
    ```

4.  Check for corrupted source images causing the process to fail on specific attachments

5.  Use the `--skip-delete` flag in WP-CLI to identify problem files

For ongoing automation, consider a cron job that regenerates thumbnails after uploading new media, avoiding bulk regeneration later.

## Web Server Best Practices

Keep your web server configuration clean and well-documented. Use version control for configuration files so changes can be tracked and rolled back. Always test configuration changes in a staging environment before applying to production.

Enable gzip compression and browser caching for better performance. Configure proper security headers including Content-Security-Policy, X-Frame-Options, and Strict-Transport-Security for HTTPS sites. Regularly update all server software to patch security vulnerabilities.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
