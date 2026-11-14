---
title: "rgb_map(3)"
name: "rgb_map"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rgb_map/"
description: "rgb_map – Look up table to speed up reducing RGB values to palette colors. Allegro game programming library."
---

<p>rgb_map &#8211; Look up table to speed up reducing RGB values to palette colors. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>extern RGB_MAP *rgb_map;</code></p>
<h2>Description</h2>
<p>To speed up reducing RGB values to 8-bit paletted colors, Allegro uses a 32k lookup table (5 bits for each color component). You must set up this table before using the gouraud shading routines, and if present the table will also vastly accelerate the makecol8() and some create_*_table() functions. RGB tables can be precalculated with the rgbmap utility, or generated at runtime with create_rgb_table(). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-create_rgb_table/">create_rgb_table</a></code>(3), <code><a href="/docs/linux/man/3-makecol8/">makecol8</a></code>(3), <code><a href="/docs/linux/man/3-create_trans_table/">create_trans_table</a></code>(3), <code><a href="/docs/linux/man/3-create_light_table/">create_light_table</a></code>(3), <code><a href="/docs/linux/man/3-create_color_table/">create_color_table</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-excolmap/">excolmap</a></code>(3), <code><a href="/docs/linux/man/3-exrgbhsv/">exrgbhsv</a></code>(3), <code><a href="/docs/linux/man/3-exshade/">exshade</a></code>(3), <code><a href="/docs/linux/man/3-extrans/">extrans</a></code>(3) </p>
