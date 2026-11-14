---
title: "bitmap_mask_color(3)"
name: "bitmap_mask_color"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bitmap_mask_color/"
description: "bitmap_mask_color – Returns the mask color of the specified bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> bitmap_mask_color &#8211; Returns the mask color of the specified bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int bitmap_mask_color(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the mask color for the specified bitmap (the value which is skipped when drawing sprites). For 256-color bitmaps this is zero, and for truecolor bitmaps it is bright pink (maximum red and blue, zero green). A frequent use of this function is to clear a bitmap with the mask color so you can later use this bitmap with masked_blit() or draw_sprite() after drawing other stuff on it. Example: </p>
<pre><code>
/* Replace mask color with another color. */
for (y = 0; y h; y++)
    for (x = 0; x w; x++)
        if (getpixel(bmp, x, y) == bitmap_mask_color(bmp))
            putpixel(bmp, x, y, another_color);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mask_color_8/">MASK_COLOR_8</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_color_depth/">bitmap_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exmouse/">exmouse</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3) </p>
<h2>Index</h2>
