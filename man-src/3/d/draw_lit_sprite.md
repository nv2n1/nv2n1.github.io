---
title: "draw_lit_sprite(3)"
name: "draw_lit_sprite"
section: "3"
letter: "d"
url: "/docs/linux/man/3-draw_lit_sprite/"
description: "draw_lit_sprite – Draws a sprite tinted with a specific color. Allegro game programming library."
---

<h2>NAME</h2>
<p> draw_lit_sprite &#8211; Draws a sprite tinted with a specific color. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void draw_lit_sprite(BITMAP *bmp, BITMAP *sprite, int x, int y, int color);</code></p>
<h2>DESCRIPTION</h2>
<p> In 256-color modes, uses the global color_map table to tint the sprite image to the specified color or to light it to the level specified by (create_trans_table or create_light_table), and draws the resulting image to the destination bitmap. In truecolor modes, uses the blender functions to light the sprite image using the alpha level specified by &#8216;color&#8217; (the alpha level which was passed to the blender functions is ignored) and draws the resulting image to the destination bitmap. The &#8216;color&#8217; parameter must be in the range [0-255] whatever its actual meaning is. This must only be used after you have set up the color mapping table (for 256-color modes) or blender functions (for truecolor modes). Example: </p>
<pre><code>
/* Some one time initialisation code. */
COLOR_MAP global_light_table;
create_light_table(&amp;global_trans_table, my_palette,
                   10, 10, 60, NULL);
... if (get_color_depth() == 8)
    color_map = &amp;global_light_table;
else set_trans_blender(40, 40, 255, 255);

/* Lit the cape with a blueish light. */
draw_lit_sprite(buffer, colored_cape, x, y, 64);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-draw_sprite/">draw_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_rle_sprite/">draw_lit_rle_sprite</a></code>(3), <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-bitmap_mask_color/">bitmap_mask_color</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3) </p>
<h2>Index</h2>
