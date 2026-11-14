---
title: "sc_implicitsurfacepolygonizer(3)"
name: "sc_implicitsurfacepolygonizer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_implicitsurfacepolygonizer/"
description: "sc::ImplicitSurfacePolygonizer –"
---

<p>sc::ImplicitSurfacePolygonizer &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::IsosurfaceGen</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ImplicitSurfacePolygonizer</code> (const <code>Ref</code>&lt; <code>Volume</code> &gt; &amp;) </p>
<p> virtual void <code>isosurface</code> (double value, <code>TriangulatedSurface</code> &amp;surf)</p>
<h3>Static Public Member Functions</h3>
<pre><code>static int add_triangle_to_current (int, int, int, VERTICES)


For internal use only.


static double value_of_current (double x, double y, double z)


For internal use only.



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Volume</code> &gt; <code>_volume</code> </p>
<p> std::vector&lt; <code>Ref</code>&lt; <code>Vertex</code> &gt; &gt; <code>_tmp_vertices</code> </p>
<p> <code>TriangulatedSurface</code> * <code>_surf</code> </p>
<p> double <code>_value</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
