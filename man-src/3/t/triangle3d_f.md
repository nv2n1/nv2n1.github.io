---
title: "triangle3d_f(3)"
name: "triangle3d_f"
section: "3"
letter: "t"
url: "/docs/linux/man/3-triangle3d_f/"
description: "triangle3d, triangle3d_f – Draws a 3d triangle onto the specified bitmap. Allegro game programming library."
---

<p>triangle3d, triangle3d_f &#8211; Draws a 3d triangle onto the specified bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void triangle3d(BITMAP *bmp, int type, BITMAP *tex, V3D *v1, *v2, *v3);
void triangle3d_f(BITMAP *bmp, int type, BITMAP *tex, V3D_f *v1, *v2, *v3);</code></pre>
<h2>Description</h2>
<p>Draw 3d triangles, using either fixed or floating point vertex structures. Unlike quad3d[_f](), triangle3d[_f]() functions are not wrappers of polygon3d[_f](). The triangle3d[_f]() functions use their own routines taking into account the constantness of the gradients. Therefore triangle3d[_f](bmp, type, tex, v1, v2, v3) is faster than polygon3d[_f](bmp, type, tex, 3, v[]). Read the beginning of chapter &quot;Polygon rendering&quot; for a list of rendering types you can use with this function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-quad3d/">quad3d</a></code>(3), <code><a href="/docs/linux/man/3-triangle/">triangle</a></code>(3) </p>
