---
title: "makeacol32(3)"
name: "makeacol32"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makeacol32/"
description: "makeacol32 – Converts an RGBA color into a 32-bit display pixel format. Allegro game programming library."
---

<h2>NAME</h2>
<p> makeacol32 &#8211; Converts an RGBA color into a 32-bit display pixel format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int makeacol32(int r, int g, int b, int a);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts an RGBA color into a 32-bit display pixel format, which includes an alpha (transparency) value. There are no versions of this routine for other color depths, because only the 32-bit format has enough room to store a proper alpha channel. You should only use RGBA format colors as the input to draw_trans_sprite() or draw_trans_rle_sprite() after calling set_alpha_blender(), rather than drawing them directly to the screen. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-makeacol/">makeacol</a></code>(3), <code><a href="/docs/linux/man/3-set_alpha_blender/">set_alpha_blender</a></code>(3), <code><a href="/docs/linux/man/3-set_write_alpha_blender/">set_write_alpha_blender</a></code>(3) </p>
<h2>Index</h2>
