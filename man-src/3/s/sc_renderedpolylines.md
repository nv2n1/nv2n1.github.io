---
title: "sc_renderedpolylines(3)"
name: "sc_renderedpolylines"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_renderedpolylines/"
description: "sc::RenderedPolylines –"
---

<p>sc::RenderedPolylines &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RenderedObject</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Coloring</code> { <code>None</code>, <code>Vertex</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>RenderedPolylines (const Ref&lt; KeyVal &gt; &amp;)



void initialize (int nvertex, int npolylines, RenderedPolylines::Coloring c=RenderedPolylines::None)



int npolyline ()



int nvertex ()



int nvertex_in_polyline (int i) const



double vertex (int i, int j) const



double vertex_rgb (int i, int j) const



int polyline (int i, int j) const



int have_vertex_rgb () const



void set_vertex (int, double x, double y, double z)



void set_vertex_rgb (int, double r, double g, double b)



void set_polyline (int i, int v1, int v2)



void set_polyline (int i, int v1, int v2, int v3)



void set_polyline (int i, int v1, int v2, int v3, int v4)



void render (const Ref&lt; Render &gt; &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
