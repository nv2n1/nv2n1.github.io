---
title: "set_clip_rect(3)"
name: "set_clip_rect"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_clip_rect/"
description: "set_clip_rect – Sets the clipping rectangle of a bitmap. Allegro game programming library."
---

<p>set_clip_rect &#8211; Sets the clipping rectangle of a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_clip_rect(BITMAP *bitmap, int x1, int y1, int x2, int y2);</code></pre>
<h2>Description</h2>
<p>Each bitmap has an associated clipping rectangle, which is the area of the image that it is OK to draw onto. Nothing will be drawn to positions outside this space. This function sets the clipping rectangle for the specified bitmap. Pass the coordinates of the top-left and bottom-right corners of the clipping rectangle in this order; these are both inclusive, i.e. set_clip_rect(bitmap, 16, 16, 32, 32) will allow drawing to (16, 16) and (32, 32), but not to (15, 15) and (33, 33). Drawing operations will be performed (at least partially) on the bitmap as long as the first coordinates of its clipping rectangle are not greater than the second coordinates and its intersection with the actual image is non-empty. If either condition is not fulfilled, drawing will be turned off for the bitmap, e.g. </p>
<pre> set_clip_rect(bmp, 0, 0, -1, -1); /* disable drawing on bmp */</pre>
<p>Note that passing &quot;out-of-bitmap&quot; coordinates is allowed, but they are likely to be altered (and so the coordinates returned by get_clip_rect() will be different). However, such modifications are guaranteed to preserve the external effect of the clipping rectangle, that is not to modify the actual area of the image that it is OK to draw onto. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_clip_rect/">get_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-add_clip_rect/">add_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-set_clip_state/">set_clip_state</a></code>(3), <code><a href="/docs/linux/man/3-get_clip_state/">get_clip_state</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3) </p>
