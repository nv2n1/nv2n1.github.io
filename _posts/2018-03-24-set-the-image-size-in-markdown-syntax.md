---
title: "How to Set Image Size in Markdown"
date: 2018-03-24 08:14:16 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /set-the-image-size-in-markdown-syntax/
---

Standard Markdown syntax doesn’t include built-in parameters for image dimensions. The basic syntax `![alt text](image.url)` produces images at their original size or constrained by container width, with no way to specify explicit dimensions.

If you need to control image size, you have several options depending on your use case and platform.

## HTML `<img>` Tag

The most direct approach is using HTML directly within your Markdown document:

``` html
<img src="http://example.com/img.png" alt="img text" width="400" height="300" />
```

This works universally across Markdown processors and gives you full control. Specify dimensions in pixels, or use percentage values for responsive layouts:

``` html
<img src="http://example.com/img.png" alt="img text" width="80%" />
```

## Markdown Extensions

Many Markdown flavors support extended syntax for sizing. Check what your platform uses:

**Kramdown** (Jekyll, GitHub Pages):

``` markdown
![alt text](image.png){:width="400px" height="300px"}
```

**Pandoc**:

``` markdown
![alt text](image.png){width=400 height=300}
```

**MultiMarkdown**:

``` markdown
![alt text][image]

[image]: http://example.com/img.png "title" {width=400px height=300px}
```

## HTML with CSS Classes

For styling consistency across multiple images, use HTML with class attributes:

``` html
<img src="http://example.com/img.png" alt="img text" class="thumbnail" />
```

Then define in your CSS:

``` css
img.thumbnail {
    width: 200px;
    height: auto;
}
```

## Picture Element for Responsive Images

If you’re building modern web content, use the HTML `<picture>` element for responsive images:

``` html
<picture>
    <source media="(min-width: 768px)" srcset="large-image.png">
    <source media="(min-width: 480px)" srcset="medium-image.png">
    <img src="small-image.png" alt="descriptive text" style="width: 100%; height: auto;">
</picture>
```

This approach loads different image sizes based on device width, improving performance and user experience.

## Practical Considerations

- **Aspect ratio**: Use `width` and `height` attributes together, or set one dimension and use `height: auto` in CSS to maintain aspect ratio
- **Responsive design**: Avoid fixed pixel dimensions on fluid layouts; prefer percentage-based widths or CSS media queries
- **Accessibility**: Always include meaningful `alt` text regardless of which method you use
- **Platform limitations**: Check your Markdown processor’s documentation—not all support extensions equally

For static site generators like Jekyll or Hugo, check what Markdown library they use (kramdown, goldmark, etc.) to know which syntax extensions are available. For simple cases where you need one-off sizing, raw HTML remains the most portable solution.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
