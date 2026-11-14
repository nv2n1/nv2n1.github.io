---
title: "generate_optimized_palette(3)"
name: "generate_optimized_palette"
section: "3"
letter: "g"
url: "/docs/linux/man/3-generate_optimized_palette/"
description: "generate_optimized_palette – Generates an optimized palette for a bitmap. Allegro game programming library."
---

<h2>NAME</h2>
<p> generate_optimized_palette &#8211; Generates an optimized palette for a bitmap. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int generate_optimized_palette(BITMAP *bmp, PALETTE pal,</code> <code>const char rsvd[PAL_SIZE]);</code></p>
<h2>DESCRIPTION</h2>
<p> Generates a 256-color palette suitable for making a reduced color version of the specified truecolor image. The rsvd parameter points to a table indicating which colors it is allowed to modify: zero for free colors which may be set to whatever the optimiser likes, negative values for reserved colors which cannot be used, and positive values for fixed palette entries that must not be changed, but can be used in the optimisation.</p>
<h2>RETURN VALUE</h2>
<p> Returns the number of different colors recognised in the provided bitmap, zero if the bitmap is not a truecolor image or there wasn&#8217;t enough memory to perform the operation, and negative if there was any internal error in the color reduction code. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-generate_332_palette/">generate_332_palette</a></code>(3), <code><a href="/docs/linux/man/3-set_color_depth/">set_color_depth</a></code>(3) </p>
<h2>Index</h2>
