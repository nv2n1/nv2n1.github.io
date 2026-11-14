---
title: "create_sub_zbuffer(3)"
name: "create_sub_zbuffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_sub_zbuffer/"
description: "create_sub_zbuffer – Creates a sub-z-buffer. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_sub_zbuffer &#8211; Creates a sub-z-buffer. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>ZBUFFER *create_sub_zbuffer(ZBUFFER *parent, int x, int y, int width, int height);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a sub-z-buffer, ie. a z-buffer sharing drawing memory with a pre-existing z-buffer, but possibly with a different size. The same rules as for sub-bitmaps apply: the sub-z-buffer width and height can extend beyond the right and bottom edges of the parent (they will be clipped), but the origin point must lie within the parent region. </p>
<p> When drawing z-buffered to a bitmap, the top left corner of the bitmap is always mapped to the top left corner of the current z-buffer. So this function is primarily useful if you want to draw to a sub-bitmap and use the corresponding sub-area of the z-buffer. In other cases, eg. if you just want to draw to a sub-bitmap of screen (and not to other parts of screen), then you would usually want to create a normal z-buffer (not sub-z-buffer) the size of the visible screen. You don&#8217;t need to first create a z-buffer the size of the virtual screen and then a sub-z-buffer of that.</p>
<h2>RETURN VALUE</h2>
<p> Returns the pointer to the sub ZBUFFER or NULL if there was an error. Remember to destroy the ZBUFFER once you are done with it, to avoid having memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_zbuffer/">create_zbuffer</a></code>(3), <code><a href="/docs/linux/man/3-create_sub_bitmap/">create_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-destroy_zbuffer/">destroy_zbuffer</a></code>(3) </p>
<h2>Index</h2>
