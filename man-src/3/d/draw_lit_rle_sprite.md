---
title: "draw_lit_rle_sprite(3)"
name: "draw_lit_rle_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_lit_rle_sprite/"
description: "draw_lit_rle_sprite – Draws a tinted RLE sprite. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_lit_rle_sprite &#8211; Draws a tinted RLE sprite. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_lit_rle_sprite(BITMAP *bmp, const RLE_SPRITE *sprite,</code> <code>int x, y, color);</code></p>
<h2>DESCRIPTION</h2>
<p> Tinted version of draw_rle_sprite(). See the description of draw_lit_sprite(). This must only be used after you have set up the color mapping table (for 256-color modes) or blender functions (for truecolor modes). Example: </p>
<pre><code>
/* Some one time initialisation code. */
COLOR_MAP global_light_table;
create_light_table(&amp;global_trans_table, my_palette,
                   10, 10, 60, NULL);
... if (get_color_depth() == 8)
    color_map = &amp;global_light_table;
else set_trans_blender(40, 40, 255, 255);

/* Lit the cape with a blueish light. */
draw_lit_rle_sprite(buffer, rle_colored_cape, x, y, 64);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_rle_sprite/">draw_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_rle_sprite/">draw_trans_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3) </p>
<h2>Index</h2>
