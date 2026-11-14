---
title: "is_inside_bitmap(3)"
name: "is_inside_bitmap"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_inside_bitmap/"
description: "is_inside_bitmap – Tells if a point is inside a bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> is_inside_bitmap &#8211; Tells if a point is inside a bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int is_inside_bitmap(BITMAP *bmp, int x, int y, int clip);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns non-zero if point (x, y) lies inside the bitmap. If `clip&#8217; is non-zero, the function compares the coordinates with the clipping rectangle, that is it returns non-zero if the point lies inside the clipping rectangle or if clipping is disabled for the bitmap. If `clip&#8217; is zero, the function compares the coordinates with the actual dimensions of the bitmap. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_clip_rect/">set_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-set_clip_state/">set_clip_state</a></code>(3), <code><a href="/docs/linux/man/3-getpixel/">getpixel</a></code>(3) </p>
<h2>Index</h2>
