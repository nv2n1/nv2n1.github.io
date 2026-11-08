---
title: "Disable WordPress Block Editor and Classic Editor"
date: 2013-07-12 16:46:16 +0000
author: "Eric Ma"
layout: post
categories: [object-oriented-programming]
canonical: /wordpress-disabling-visual-editor/
---

The WordPress block editor (Gutenberg) and legacy visual editor can mangle custom HTML, delete formatting, and cause frustration for users who work directly with code. If you prefer writing HTML directly or need to preserve complex markup, you can disable the visual editing experience entirely.

## Disable for Your Own Account

The simplest approach is to disable the editor for your user account:

1.  Log in to WordPress admin
2.  Go to **Users → Your Profile**
3.  Scroll to the **Editing** section
4.  Check **Disable the visual editor when writing**
5.  Click **Update Profile**

After this, you’ll see the code editor by default when creating or editing posts. You can still toggle between code and visual modes if needed, but the code editor becomes your starting point.

## Disable Site-Wide via wp-config.php

To enforce this across your entire WordPress installation, add these constants to your `wp-config.php` file:

``` php
define( 'GUTENBERG_PHASE', 0 );
```

This disables the block editor globally. The `GUTENBERG_PHASE` constant set to `0` prevents Gutenberg from loading entirely, which is cleaner than trying to disable individual editor components.

If you want to keep the block editor but only disable the legacy visual editor in classic posts, omit that line and use the user-level settings or programmatic approaches instead.

Note: `DISALLOW_FILE_EDIT` is sometimes confused with editor disabling, but it actually prevents editing themes and plugins through the admin interface—a separate security concern.

## Disable for Specific Users

WordPress administrators can disable the editor for individual users:

1.  Go to **Users → All Users**
2.  Click **Edit** on the user you want to modify
3.  Check **Disable the visual editor when writing**
4.  Click **Update User**

This is useful when managing multiple editors or enforcing consistency across a team without affecting the entire site.

## Programmatic Approach

For custom WordPress installations or conditional logic, you can filter the editor in your theme’s `functions.php` or a must-use plugin:

``` php
add_filter( 'user_can_richedit', '__return_false' );
```

This disables the visual editor globally for all users. For conditional disabling (e.g., only for certain post types), use:

``` php
add_filter( 'user_can_richedit', function( $status ) {
    $screen = get_current_screen();

    // Disable visual editor for pages only
    if ( isset( $screen->post_type ) && $screen->post_type === 'page' ) {
        return false;
    }

    return $status;
} );
```

You can also disable Gutenberg for specific post types while keeping the legacy editor:

``` php
add_filter( 'use_block_editor_for_post_type', function( $use_block_editor, $post_type ) {
    if ( in_array( $post_type, array( 'page', 'custom_post_type' ), true ) ) {
        return false;
    }
    return $use_block_editor;
}, 10, 2 );
```

## Block Editor-Specific Disabling

Modern WordPress (6.x and later) uses Gutenberg by default. To disable just the block editor while keeping other admin interfaces intact, add this to `functions.php`:

``` php
add_filter( 'use_block_editor_for_post_type', '__return_false' );
```

This works better than disabling Gutenberg globally via `wp-config.php` if you want selective control.

## Important Considerations

**Classic Editor Plugin**: If you’re working with legacy sites or need the classic editor UI, install the <a href="https://wordpress.org/plugins/classic-editor/" rel="nofollow noopener" target="_blank">Classic Editor plugin</a>. This provides the pre-Gutenberg interface and can coexist with these settings.

**HTML and Content Filtering**: Even in code editor mode, WordPress still applies formatting filters through `wp_kses_post()` and `wp_filter_post_kses()`. If you need to preserve raw HTML (iframes, scripts, custom markup), you’ll need to either:

- Whitelist allowed tags using `wp_kses_allowed_html()`
- Use a plugin specifically designed for raw HTML preservation
- Create a custom post type with different sanitization rules

**Staging Environment Testing**: Before making site-wide changes, test on a staging environment. Some plugins or custom post types may behave unexpectedly without the block editor, especially if they inject content that relies on block rendering.

**Performance**: Disabling Gutenberg globally via `wp-config.php` saves some overhead on every page load. The programmatic approach is more flexible but adds a small filter on every post edit screen.
