---
title: "makeacol(3)"
name: "makeacol"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makeacol/"
description: "makeacol, makeacol_depth – Converts RGBA colors into display dependent pixel formats. Allegro game programming library."
---

<h2>NAME</h2>
<p> makeacol, makeacol_depth &#8211; Converts RGBA colors into display dependent pixel formats. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makeacol(int r, int g, int b, int a);</code> </p>
<p> <code>int makeacol_depth(int color_depth, int r, int g, int b, int a);</code></p>
<h2>DESCRIPTION</h2>
<p> Convert RGBA colors into display dependent pixel formats. In anything less than a 32-bit mode, these are the same as calling makecol() or makecol_depth(), but by using these routines it is possible to create 32-bit color values that contain a true 8 bit alpha channel along with the red, green, and blue components. You should only use RGBA format colors as the input to draw_trans_sprite() or draw_trans_rle_sprite() after calling set_alpha_blender(), rather than drawing them directly to the screen.</p>
<h2>RETURN VALUE</h2>
<p> Returns the requested RGBA quadruplet. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makecol/">makecol</a></code>(3), <code><a href="/docs/linux/man/3-makecol_depth/">makecol_depth</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_write_alpha_blender/">set_write_alpha_blender</a></code>(3) </p>
<h2>Index</h2>
