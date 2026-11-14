---
title: "draw_sprite(3)"
name: "draw_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_sprite/"
description: "draw_sprite – Draws a copy of the sprite onto the destination bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_sprite &#8211; Draws a copy of the sprite onto the destination bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Draws a copy of the sprite bitmap onto the destination bitmap at the specified position. This is almost the same as blit(sprite, bmp, 0, 0, x, y, sprite-&gt;w, sprite-&gt;h), but it uses a masked drawing mode where transparent pixels are skipped, so the background image will show through the masked parts of the sprite. Transparent pixels are marked by a zero in 256-color modes or bright pink for truecolor data (maximum red and blue, zero green). Example: </p>
<pre><code>
BITMAP *spaceship;
... draw_sprite(screen, spaceship, x, y);
</code></pre>
<p> If the GFX_HW_VRAM_BLIT_MASKED bit in the gfx_capabilities flag is set, the current driver supports hardware accelerated sprite drawing when the source image is a video memory bitmap or a sub-bitmap of the screen. This is extremely fast, so when this flag is set it may be worth storing some of your more frequently used sprites in an offscreen portion of the video memory. </p>
<p> Warning: if the hardware acceleration flag is not set, draw_sprite() will not work correctly when used with a sprite image in system or video memory so the latter must be a memory bitmap. </p>
<p> Although generally not supporting graphics of mixed color depths, as a special case this function can be used to draw 256-color source images onto truecolor destination bitmaps, so you can use palette effects on specific sprites within a truecolor program. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite_v_flip/">draw_sprite_v_flip</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-stretch_sprite/">stretch_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rotate_sprite/">rotate_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_character_ex/">draw_character_ex</a></code>(3), <code><a href="/docs/linux/man/3-draw_rle_sprite/">draw_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_compiled_sprite/">draw_compiled_sprite</a></code>(3), <code><a href="/docs/linux/man/3-masked_blit/">masked_blit</a></code>(3), <code><a href="/docs/linux/man/3-blit/">blit</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
<h2>Index</h2>
