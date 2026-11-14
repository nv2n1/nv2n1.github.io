---
title: "quad3d(3)"
name: "quad3d"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quad3d/"
description: "quad3d, quad3d_f – Draws a 3d quad onto the specified bitmap. Allegro game programming library."
---

<p>quad3d, quad3d_f &#8211; Draws a 3d quad onto the specified bitmap. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void quad3d(BITMAP *bmp, int type, BITMAP *tex, V3D *v1, *v2, *v3, *v4);
void quad3d_f(BITMAP *bmp, int type, BITMAP *tex, V3D_f *v1, *v2, *v3, *v4);</code></pre>
<h2>Description</h2>
<p>Draw 3d quads, using either fixed or floating point vertex structures. These are equivalent to calling polygon3d(bmp, type, tex, 4, v[]) or polygon3d_f(bmp, type, tex, 4, v[]). Read the beginning of chapter &quot;Polygon rendering&quot; for a list of rendering types you can use with this function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-triangle3d/">triangle3d</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3) </p>
