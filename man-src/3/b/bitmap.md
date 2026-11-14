---
title: "bitmap(3)"
name: "bitmap"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bitmap/"
description: "BITMAP – Stores the contents of a bitmap. Allegro game programming library."
---

<p>BITMAP &#8211; Stores the contents of a bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>typedef struct BITMAP</code></p>
<h2>Description</h2>
<pre> int w, h; - size of the bitmap in pixels
 int clip; - non-zero if clipping is turned on
 int cl, cr, ct, cb; - clip rectangle left, right, top,
 and bottom
 unsigned char *line[]; - pointers to the start of each line</pre>
<p>There is some other stuff in the structure as well, but it is liable to change and you shouldn&#8217;t use anything except the above. The `w&#8217; and `h&#8217; fields can be used to obtain the size of an existing bitmap: </p>
<pre> bmp = load_bitmap(&quot;file.bmp&quot;, pal);
 allegro_message(&quot;Bitmap size: (%dx%d)
&quot;, bmp-&gt;w, bmp-&gt;h);</pre>
<p>The clipping rectangle is inclusive on the left and top (0 allows drawing to position 0) but exclusive on the right and bottom (10 allows drawing to position 9, but not to 10). Note this is not the same format as that of the clipping API, which takes inclusive coordinates for all four corners. All the values of this structure should be regarded as read-only, with the exception of the line field, whose access is described in depth in the &quot;Direct access to video memory&quot; section of the manual. If you want to modify the clipping region, please refrain from changing this structure. Use set_clip_rect() instead. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-create_bitmap/">create_bitmap</a></code>(3), <code><a href="/docs/linux/man/3-set_clip_rect/">set_clip_rect</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_color_depth/">bitmap_color_depth</a></code>(3), <code><a href="/docs/linux/man/3-rle_sprite/">RLE_SPRITE</a></code>(3), <code><a href="/docs/linux/man/3-compiled_sprite/">COMPILED_SPRITE</a></code>(3)</p>
