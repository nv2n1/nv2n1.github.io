---
title: "bitmap_color_depth(3)"
name: "bitmap_color_depth"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bitmap_color_depth/"
description: "bitmap_color_depth – Returns the color depth of the specified bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> bitmap_color_depth &#8211; Returns the color depth of the specified bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int bitmap_color_depth(BITMAP *bmp);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the color depth of the specified bitmap (8, 15, 16, 24, or 32). Example: </p>
<pre><code>
switch (bitmap_color_depth(screen)) {
case 8:
    /* Access screen using optimized 8-bit code. */
    break;
default:
    /* Use generic slow functions. */
    break;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3), <code><a href="/docs/linux/man/3-exzbuf/">exzbuf</a></code>(3) </p>
<h2>Index</h2>
