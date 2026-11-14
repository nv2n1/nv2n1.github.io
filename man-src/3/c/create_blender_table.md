---
title: "create_blender_table(3)"
name: "create_blender_table"
section: "3"
letter: "c"
url: "/docs/linux/man/3-create_blender_table/"
description: "create_blender_table – Emulates truecolor blender effects in paletted modes. Allegro game programming library."
---

<h2>NAME</h2>
<p> create_blender_table &#8211; Emulates truecolor blender effects in paletted modes. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void create_blender_table(COLOR_MAP *table, const PALETTE pal,</code> <code>void (*callback)(int pos));</code></p>
<h2>DESCRIPTION</h2>
<p> Fills the specified color mapping table with lookup data for doing a paletted equivalent of whatever truecolor blender mode is currently selected. After calling set_trans_blender(), set_blender_mode(), or any of the other truecolor blender mode routines, you can use this function to create an 8-bit mapping table that will have the same results as whatever 24-bit blending mode you have enabled. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-color_map/">color_map</a></code>(3), <code><a href="/docs/linux/man/3-create_light_table/">create_light_table</a></code>(3), <code><a href="/docs/linux/man/3-create_trans_table/">create_trans_table</a></code>(3), <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_blender_mode/">set_blender_mode</a></code>(3) </p>
<h2>Index</h2>
