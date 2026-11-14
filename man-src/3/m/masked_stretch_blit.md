---
title: "masked_stretch_blit(3)"
name: "masked_stretch_blit"
section: "3"
letter: "m"
url: "/docs/linux/man/3-masked_stretch_blit/"
description: "masked_stretch_blit – Scales a rectangular area skipping pixels with the mask color. Allegro game programming library."
---

<h2>NAME</h2>
<p> masked_stretch_blit &#8211; Scales a rectangular area skipping pixels with the mask color. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void masked_stretch_blit(BITMAP *source, BITMAP *dest,</code> <code>int source_x, source_y, source_w, source_h,</code> <code>int dest_x, dest_y, dest_w, dest_h);</code></p>
<h2>DESCRIPTION</h2>
<p> Like masked_blit(), except it can scale images (so the source and destination rectangles don&#8217;t need to be the same size). This routine doesn&#8217;t do as much safety checking as the regular masked_blit(): in particular you must take care not to copy from areas outside the source bitmap. Moreover, the source must be a memory bitmap. Example: </p>
<pre><code>
BITMAP *hud_overlay;
...
    /* Stretch hud overlay over the screen. */
    masked_stretch_blit(hud_overlay, screen, 0, 0,
                        hud_overlay-&gt;w, hud_overlay-&gt;h,
                        0, 0, SCREEN_W, SCREEN_H);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-masked_blit/">masked_blit</a></code>(3), <code><a href="/docs/linux/man/3-stretch_blit/">stretch_blit</a></code>(3), <code><a href="/docs/linux/man/3-stretch_sprite/">stretch_sprite</a></code>(3) </p>
<h2>Index</h2>
