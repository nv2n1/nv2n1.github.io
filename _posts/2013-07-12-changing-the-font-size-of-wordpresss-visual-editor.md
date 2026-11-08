---
title: "Adjusting Font Size in the WordPress Block Editor"
date: 2013-07-12 16:46:13 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /changing-the-font-size-of-wordpresss-visual-editor/
---

The default 13px font size in WordPress’s block editor can strain your eyes, especially on high-resolution displays or during extended editing sessions. Several approaches let you adjust editor typography without touching core files.

## Using the Site Editor (Easiest)

For block themes and WordPress 5.9+, the visual Site Editor is the simplest route:

1.  Navigate to **Appearance → Editor** (or **Customize** for older versions)
2.  Click **Typography** in the sidebar
3.  Adjust base font size, line height, and letter spacing
4.  Changes save directly to your theme’s `style.json`

This requires no coding and gives real-time preview. It’s the recommended approach for non-developers.

## Modifying style.json (Block Themes)

If you need more control, edit your theme’s `style.json` directly. Add custom font sizes to the settings block:

``` json
{
  "version": 3,
  "settings": {
    "typography": {
      "fontSizes": [
        {
          "name": "Small",
          "slug": "small",
          "size": "14px"
        },
        {
          "name": "Normal",
          "slug": "normal",
          "size": "16px"
        },
        {
          "name": "Large",
          "slug": "large",
          "size": "18px"
        }
      ]
    }
  }
}
```

Users can then select these preset sizes when editing blocks. This is maintainable and persists across WordPress updates.

## Creating Editor Styles (Classic Themes)

For traditional PHP-based themes, create an `editor-style.css` file in your theme root:

``` css
.block-editor-rich-text__editable,
.wp-block {
    font-size: 16px;
    line-height: 1.6;
}

.wp-block-paragraph,
.wp-block-heading {
    font-size: 16px;
}

.wp-block-code {
    font-size: 14px;
}
```

Register it in `functions.php`:

``` php
add_theme_support( 'editor-styles' );
add_editor_style( 'editor-style.css' );
```

This approach applies your typography rules globally without modifying core files.

## Using Block Styles for Flexibility

Define reusable typography variants that users can apply to individual blocks:

``` php
add_theme_support( 'editor-styles' );
add_theme_support( 'appearance-tools' );

register_block_style(
    'core/paragraph',
    array(
        'name'  => 'large-text',
        'label' => 'Large Text',
    )
);
```

Then style it in `editor-style.css`:

``` css
.is-style-large-text {
    font-size: 18px;
    line-height: 1.75;
}
```

Users see “Large Text” as an option in the block toolbar, making it easy to apply consistent sizing without modifying individual block settings.

## PHP Filter for Quick Adjustments

For temporary changes without modifying theme files, use a mu-plugin or add this to `functions.php`:

``` php
add_filter( 'block_editor_settings_all', function( $settings, $post ) {
    $settings['__experimentalFeatures']['typography']['fontSize']['default'] = '16px';
    return $settings;
}, 10, 2 );
```

This is useful for testing but less maintainable than theme-based approaches. Filters using experimental features may change in future WordPress versions.

## Browser DevTools for Testing

To temporarily test font size changes without affecting your site:

1.  Press **F12** (Windows/Linux) or **Cmd+Option+I** (macOS)
2.  Go to the **Console** tab
3.  Paste this code:

``` javascript
const style = document.createElement('style');
style.textContent = `
    .block-editor-rich-text__editable,
    .wp-block {
        font-size: 16px !important;
        line-height: 1.6 !important;
    }
`;
document.head.appendChild(style);
```

This persists for your browser session only. It’s excellent for finding the right size before implementing it permanently.

## Typography Best Practices

Regardless of your method:

- **Base font size**: Use 16px minimum for body text; 14px is acceptable for secondary content only
- **Line height**: Set 1.5–1.8 for screen reading (looser than print typography)
- **Code blocks**: Keep slightly smaller (14px) to prevent horizontal overflow
- **Headings**: Scale proportionally using modular scale; don’t match body size
- **Cross-device testing**: Verify readability on laptop, external monitors, and tablets

Use browser DevTools Inspector to measure actual rendered sizes in the editor. The editor should mirror your frontend typography as closely as possible so your content looks correct before publishing.

## What to Avoid

Never directly edit `wp-includes/css/dist/editor/editor.css` or other core WordPress files. WordPress overwrites these during updates, and you’ll lose changes with every upgrade. Theme-based customization, filters, and the Site Editor are always preferable because they survive updates.
