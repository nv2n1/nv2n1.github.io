---
title: "create_color_table(3)"
name: "create_color_table"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_color_table/"
description: "create_color_table – Fills a color mapping table for customised effects. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_color_table &#8211; Fills a color mapping table for customised effects. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void create_color_table(COLOR_MAP *table, const PALETTE pal,</code> <code>void (*blend)(PALETTE pal, int x, int y, RGB *rgb),</code> <code>void (*callback)(int pos));</code></p>
<h2>DESCRIPTION</h2>
<p> Fills the specified color mapping table with lookup data for doing customised effects with the specified palette, calling the blend function to determine the results of each color combination. </p>
<p> Your blend routine will be passed a pointer to the palette and the two indices of the colors which are to be combined, and should fill in the RGB structure with the desired result in 0-63 format. Allegro will then search the palette for the closest match to the RGB color that you requested, so it doesn&#8217;t matter if the palette has no exact match for this color. </p>
<p> If the callback function is not NULL, it will be called 256 times during the calculation, allowing you to display a progress indicator. Example: </p>
<pre><code>
COLOR_MAP greyscale_table;
... void return_grey_color(const PALETTE pal,
                           int x, int y, RGB *rgb){
    ...}...
    /* Build a color lookup table for greyscale effect. */
    create_color_table(&amp;greyscale_table, pal,
                       return_grey_color, NULL);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-create_light_table/">create_light_table</a></code>(3), <code><a href="/docs/linux/man/3-create_trans_table/">create_trans_table</a></code>(3), <code><a href="/docs/linux/man/3-create_blender_table/">create_blender_table</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-rgb_map/">rgb_map</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3) </p>
<h2>Index</h2>
