---
title: "color_map(3)"
name: "color_map"
section: "3"
letter: "c"
url: "/docs/linux/man/3-color_map/"
description: "color_map – Global pointer to the color mapping table. Allegro game programming library."
---

<h2>NAME</h2>
<p> color_map &#8211; Global pointer to the color mapping table. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern COLOR_MAP *color_map;</code></p>
<h2>DESCRIPTION</h2>
<p> Global pointer to the color mapping table. You must allocate your own COLOR_MAP either statically or dynamically and set color_map to it before using any translucent or lit drawing functions in a 256-color video mode! Example: </p>
<pre><code>
color_map = malloc(sizeof(COLOR_MAP));
if (!color_map)
    abort_on_error("Not enough memory for color map!");
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-create_light_table/">create_light_table</a></code>(3), <code><a href="/docs/linux/man/3-create_trans_table/">create_trans_table</a></code>(3), <code><a href="/docs/linux/man/3-create_blender_table/">create_blender_table</a></code>(3), <code><a href="/docs/linux/man/3-set_trans_blender/">set_trans_blender</a></code>(3), <code><a href="/docs/linux/man/3-draw_trans_sprite/">draw_trans_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_lit_sprite/">draw_lit_sprite</a></code>(3), <code><a href="/docs/linux/man/3-draw_gouraud_sprite/">draw_gouraud_sprite</a></code>(3), <code><a href="/docs/linux/man/3-drawing_mode/">drawing_mode</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
<h2>Index</h2>
