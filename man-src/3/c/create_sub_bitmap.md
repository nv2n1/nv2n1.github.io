---
title: "create_sub_bitmap(3)"
name: "create_sub_bitmap"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_sub_bitmap/"
description: "create_sub_bitmap – Creates a memory sub bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_sub_bitmap &#8211; Creates a memory sub bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>BITMAP *create_sub_bitmap(BITMAP *parent, int x, y, width, height);</code></p>
<h2>DESCRIPTION</h2>
<p> Creates a sub-bitmap, ie. a bitmap sharing drawing memory with a pre-existing bitmap, but possibly with a different size and clipping settings. When creating a sub-bitmap of the mode-X screen, the x position must be a multiple of four. The sub-bitmap width and height can extend beyond the right and bottom edges of the parent (they will be clipped), but the origin point must lie within the parent region.</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to the created sub bitmap, or NULL if the sub bitmap could not be created. Remember to free the sub bitmap before freeing the parent bitmap to avoid memory leaks and potential crashes accessing memory which has been freed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-create_bitmap_ex/">create_bitmap_ex</a></code>(3), <code><a href="/docs/linux/man/3-destroy_bitmap/">destroy_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-is_sub_bitmap/">is_sub_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_bitmap/">clear_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-clear_to_color/">clear_to_color</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3), <code><a href="/docs/linux/man/3-exscroll/">exscroll</a></code>(3), <code><a href="/docs/linux/man/3-exswitch/">exswitch</a></code>(3) </p>
<h2>Index</h2>
