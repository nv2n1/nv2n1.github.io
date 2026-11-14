---
title: "stretch_blit(3)"
name: "stretch_blit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stretch_blit/"
description: "stretch_blit – Scales a rectangular area from one bitmap to another. Allegro game programming library."
---

<p>stretch_blit &#8211; Scales a rectangular area from one bitmap to another. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void stretch_blit(BITMAP *source, BITMAP *dest,

                  int source_x, source_y, source_width, source_height,

                  int dest_x, dest_y, dest_width, dest_height);</code></pre>
<h2>Description</h2>
<p>Like blit(), except it can scale images (so the source and destination rectangles don&#8217;t need to be the same size) and requires the source and destination bitmaps to be of the same color depth. This routine doesn&#8217;t do as much safety checking as the regular blit(): in particular you must take care not to copy from areas outside the source bitmap, and you cannot blit between overlapping regions, ie. you must use different bitmaps for the source and the destination. Moreover, the source must be a memory bitmap. Example: </p>
<pre> BITMAP *bmp;
 ...
 /* Stretch bmp to fill the screen. */
 stretch_blit(bmp, screen, 0, 0, bmp-&gt;w, bmp-&gt;h,
 0, 0, SCREEN_W, SCREEN_H);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-masked_stretch_blit/">masked_stretch_blit</a></code>(3), <code><a href="/docs/linux/man/3-stretch_sprite/">stretch_sprite</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3), <code><a href="/docs/linux/man/3-exscale/">exscale</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
