---
title: "scene_polygon3d(3)"
name: "scene_polygon3d"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scene_polygon3d/"
description: "scene_polygon3d, scene_polygon3d_f – Puts a polygon in the scene rendering list. Allegro game programming library."
---

<p>scene_polygon3d, scene_polygon3d_f &#8211; Puts a polygon in the scene rendering list. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int scene_polygon3d(int type, BITMAP *texture, int vc, V3D *vtx[]);
int scene_polygon3d_f(int type, BITMAP *texture, int vc, V3D_f *vtx[]);</code></pre>
<h2>Description</h2>
<p>Puts a polygon in the rendering list. Nothing is really rendered at this moment. Should be called between clear_scene() and render_scene(). </p>
<p> Arguments are the same as for polygon3d(), except the bitmap is missing. The one passed to clear_scene() will be used. </p>
<p> Unlike polygon3d(), the polygon may be concave or self-intersecting. Shapes that penetrate one another may look OK, but they are not really handled by this code. </p>
<p> Note that the texture is stored as a pointer only, and you should keep the actual bitmap around until render_scene(), where it is used. </p>
<p> Since the FLAT style is implemented with the low-level hline() function, the FLAT style is subject to DRAW_MODEs. All these modes are valid. Along with the polygon, this mode will be stored for the rendering moment, and also all the other related variables (color_map pointer, pattern pointer, anchor, blender values). </p>
<p> The settings of the CPU_MMX and CPU_3DNOW flags of the cpu_capabilities global variable on entry in this routine affect the choice of low-level asm routine that will be used by render_scene() for this polygon.</p>
<h2>Return Value</h2>
<p>Returns zero on success, or a negative number if it won&#8217;t be rendered for lack of a rendering routine. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-create_scene/">create_scene</a></code>(3), <code><a href="/docs/linux/man/3-clear_scene/">clear_scene</a></code>(3), <code><a href="/docs/linux/man/3-render_scene/">render_scene</a></code>(3), <code><a href="/docs/linux/man/3-destroy_scene/">destroy_scene</a></code>(3), <code><a href="/docs/linux/man/3-polygon3d/">polygon3d</a></code>(3), <code><a href="/docs/linux/man/3-cpu_capabilities/">cpu_capabilities</a></code>(3), <code><a href="/docs/linux/man/3-exscn3d/">exscn3d</a></code>(3) </p>
