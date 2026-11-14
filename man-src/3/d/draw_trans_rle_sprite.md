---
title: "draw_trans_rle_sprite(3)"
name: "draw_trans_rle_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_trans_rle_sprite/"
description: "draw_trans_rle_sprite – Draws a translucent RLE sprite. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_trans_rle_sprite &#8211; Draws a translucent RLE sprite. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_trans_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite,</code> <code>int x, int y);</code></p>
<h2>DESCRIPTION</h2>
<p> Translucent version of draw_rle_sprite(). See the description of draw_trans_sprite(). This must only be used after you have set up the color mapping table (for 256-color modes) or blender functions (for truecolor modes). The bitmap and sprite must normally be in the same color depth, but as a special case you can draw 32-bit RGBA format sprites onto any hicolor or truecolor bitmap, as long as you call set_alpha_blender() first. Example: </p>
<pre><code>
/* Some one time initialisation code. */
COLOR_MAP global_trans_table;
create_trans_table(&amp;global_trans_table, my_palette,
                   128, 128, 128, NULL);
... if (get_color_depth() == 8)
    color_map = &amp;global_trans_table;
else set_trans_blender(128, 128, 128, 128);

draw_trans_rle_sprite(buffer, rle_ghost_sprite, x, y);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_rle_sprite/">draw_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_rle_sprite/">draw_lit_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
<h2>Index</h2>
