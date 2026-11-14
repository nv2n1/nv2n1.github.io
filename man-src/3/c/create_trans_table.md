---
title: "create_trans_table(3)"
name: "create_trans_table"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_trans_table/"
description: "create_trans_table – Fills a color mapping table for translucency effects. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_trans_table &#8211; Fills a color mapping table for translucency effects. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void create_trans_table(COLOR_MAP *table, const PALETTE pal,</code> <code>int r, g, b, void (*callback)(int pos));</code></p>
<h2>DESCRIPTION</h2>
<p> Fills the specified color mapping table with lookup data for doing translucency effects with the specified palette. When combining the colors c1 and c2 with this table, the result will be a color somewhere between the two. The r, g, and b parameters specify the solidity of each color component, ranging from 0 (totally transparent) to 255 (totally solid). For 50% solidity, pass 128. </p>
<p> This function treats source color #0 as a special case, leaving the destination unchanged whenever a zero source pixel is encountered, so that masked sprites will draw correctly. This function will take advantage of the global rgb_map variable to speed up color conversions. If the callback function is not NULL, it will be called 256 times during the calculation, allowing you to display a progress indicator. Example: </p>
<pre><code>
COLOR_MAP trans_table;
...
    /* Build a color lookup table for translucent drawing. */
    create_trans_table(&amp;trans_table, pal, 128, 128, 128, NULL);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-create_light_table/">create_light_table</a></code>(3), <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-create_blender_table/">create_blender_table</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
<h2>Index</h2>
