---
title: "create_light_table(3)"
name: "create_light_table"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_light_table/"
description: "create_light_table – Fills a color mapping table for lighting effects. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_light_table &#8211; Fills a color mapping table for lighting effects. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void create_light_table(COLOR_MAP *table, const PALETTE pal,</code> <code>int r, g, b, void (*callback)(int pos));</code></p>
<h2>DESCRIPTION</h2>
<p> Fills the specified color mapping table with lookup data for doing lighting effects with the specified palette. When combining the colors c1 and c2 with this table, c1 is treated as a light level from 0-255. At light level 255 the table will output color c2 unchanged, at light level 0 it will output the r, g, b value you specify to this function, and at intermediate light levels it will output a color somewhere between the two extremes. The r, g, and b values are in the range 0-63. </p>
<p> This function will take advantage of the global rgb_ap variable to speed up color conversions. If the callback function is not NULL, it will be called 256 times during the calculation, allowing you to display a progress indicator. Example: </p>
<pre><code>
COLOR_MAP light_table;
...
    /* Build a color lookup table for lighting effects. */
    create_light_table(&amp;light_table, pal, 0, 0, 0, NULL);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-create_trans_table/">create_trans_table</a></code>(3), <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-create_blender_table/">create_blender_table</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
<h2>Index</h2>
