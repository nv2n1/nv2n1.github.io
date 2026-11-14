---
title: "polygon_z_normal(3)"
name: "polygon_z_normal"
section: "3"
letter: "p"
url: "/docs/linux/man/3-polygon_z_normal/"
description: "polygon_z_normal, polygon_z_normal_f – Finds the Z component of the normal vector to three vertices. Allegro game programming library."
---

<p>polygon_z_normal, polygon_z_normal_f &#8211; Finds the Z component of the normal vector to three vertices. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>fixed polygon_z_normal(const V3D *v1, const V3D *v2, const V3D *v3);</code> </p>
<pre><code>float polygon_z_normal_f(const V3D_f *v1, const V3D_f *v2, const V3D_f *v3);</code></pre>
<h2>Description</h2>
<p>Finds the Z component of the normal vector to the specified three vertices (which must be part of a convex polygon). This is used mainly in back-face culling. The back-faces of closed polyhedra are never visible to the viewer, therefore they never need to be drawn. This can cull on average half the polygons from a scene. If the normal is negative the polygon can safely be culled. If it is zero, the polygon is perpendicular to the screen. However, this method of culling back-faces must only be used once the X and Y coordinates have been projected into screen space using persp_project() (or if an orthographic (isometric) projection is being used). Note that this function will fail if the three vertices are co-linear (they lie on the same line) in 3D space. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cross_product/">cross_product</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3) </p>
