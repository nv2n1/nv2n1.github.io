---
title: "draw_trans_sprite(3)"
name: "draw_trans_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_trans_sprite/"
description: "draw_trans_sprite – Draws a sprite blending it with the destination. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_trans_sprite &#8211; Draws a sprite blending it with the destination. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_trans_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Uses the global color_map table or truecolor blender functions to overlay the sprite on top of the existing image. This must only be used after you have set up the color mapping table (for 256-color modes) or blender functions (for truecolor modes). Because it involves reading as well as writing the bitmap memory, translucent drawing is very slow if you draw directly to video RAM, so wherever possible you should use a memory bitmap instead. Example: </p>
<pre><code>
/* Some one time initialisation code. */
COLOR_MAP global_trans_table;
create_trans_table(&amp;global_trans_table, my_palette,
                   128, 128, 128, NULL);
... if (get_color_depth() == 8)
    color_map = &amp;global_trans_table;
else set_trans_blender(128, 128, 128, 128);

draw_trans_sprite(buffer, ghost_sprite, x, y);
</code></pre>
<p> The bitmap and sprite must normally be in the same color depth, but as a special case you can draw 32 bit RGBA format sprites onto any hicolor or truecolor bitmap, as long as you call set_alpha_blender() first, and you can draw 8-bit alpha images onto a 32-bit RGBA destination, as long as you call set_write_alpha_blender() first. As draw_sprite() this function skips transparent pixels, except if the source sprite is an 8-bit image; if this is the case, you should pay attention to properly set up your color map table for index 0. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_rle_sprite/">draw_trans_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_write_alpha_blender/">set_write_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-exalpha/">exalpha</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3), <code><a href="/docs/linux/man/3-exxfade/">exxfade</a></code>(3) </p>
<h2>Index</h2>
