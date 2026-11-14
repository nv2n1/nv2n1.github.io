---
title: "masked_blit(3)"
name: "masked_blit"
section: "3"
letter: "m"
url: "/docs/linux/man/3-masked_blit/"
description: "masked_blit – Copies a rectangle skipping pixels with the mask color. Allegro game programming library."
---

<h2>NAME</h2>
<p> masked_blit &#8211; Copies a rectangle skipping pixels with the mask color. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void masked_blit(BITMAP *source, BITMAP *dest, int source_x, int source_y,</code> <code>int dest_x, int dest_y, int width, int height);</code></p>
<h2>DESCRIPTION</h2>
<p> Like blit(), but skips transparent pixels, which are marked by a zero in 256-color modes or bright pink for truecolor data (maximum red and blue, zero green), and requires the source and destination bitmaps to be of the same color depth. The source and destination regions must not overlap. Example: </p>
<pre><code>
BITMAP *hud_overlay;
...
    /* Paint hud overlay on the screen. */
    masked_blit(hud_overlay, screen, 0, 0, 0, 0,
                hud_overlay-&gt;w, hud_overlay-&gt;h);
</code></pre>
<p> If the GFX_HW_VRAM_BLIT_MASKED bit in the gfx_capabilities flag is set, the current driver supports hardware accelerated masked blits from one part of the screen onto another. This is extremely fast, so when this flag is set it may be worth storing some of your more frequently used sprites in an offscreen portion of the video memory. </p>
<p> Warning: if the hardware acceleration flag is not set, masked_blit() will not work correctly when used with a source image in system or video memory so the latter must be a memory bitmap. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-masked_stretch_blit/">masked_stretch_blit</a></code>(3), <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-expat/">expat</a></code>(3) </p>
<h2>Index</h2>
