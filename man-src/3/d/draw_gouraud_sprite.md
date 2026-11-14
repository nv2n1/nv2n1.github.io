---
title: "draw_gouraud_sprite(3)"
name: "draw_gouraud_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_gouraud_sprite/"
description: "draw_gouraud_sprite – Draws a sprite with gouraud shading. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_gouraud_sprite &#8211; Draws a sprite with gouraud shading. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_gouraud_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y,</code> <code>int c1, int c2, int c3, int c4);</code></p>
<h2>DESCRIPTION</h2>
<p> More sophisticated version of draw_lit_sprite(): the &#8216;color&#8217; parameter is not constant across the sprite image anymore but interpolated between the four specified corner colors. The corner values passed to this function indicate the strength of the color applied on them, ranging from 0 (no strength) to 255 (full strength). Example: </p>
<pre><code>
/* Some one time initialisation code. */
COLOR_MAP global_light_table;
create_light_table(&amp;global_trans_table, my_palette,
                   0, 0, 0, NULL);
... if (get_color_depth() == 8)
    color_map = &amp;global_light_table;
else set_trans_blender(0, 0, 0, 128);

/* Enemies are in shadow unless lit by torch. */
draw_gouraud_sprite(buffer, menacing_spy, x, y,
                    light_strength_on_corner_1,
                    light_strength_on_corner_2,
                    light_strength_on_corner_3,
                    light_strength_on_corner_4);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3) </p>
<h2>Index</h2>
