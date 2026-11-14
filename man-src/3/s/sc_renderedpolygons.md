---
title: "sc_renderedpolygons(3)"
name: "sc_renderedpolygons"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_renderedpolygons/"
description: "sc::RenderedPolygons –"
---

<p>sc::RenderedPolygons &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RenderedObject</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Coloring</code> { <code>None</code>, <code>Vertex</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>RenderedPolygons (const Ref&lt; KeyVal &gt; &amp;)



void initialize (int nvertex, int nface, RenderedPolygons::Coloring c=RenderedPolygons::None)



void set_vertex (int, double x, double y, double z)



void set_vertex_rgb (int, double r, double g, double b)



void set_vertex_color (int i, const Color &amp;c)



void set_face (int iface, int v1, int v2, int v3)



void set_face (int iface, int v1, int v2, int v3, int v4)



int nvertex () const



int nface () const



int nvertex_in_face (int iface) const



const double * vertex (int i) const



double vertex (int i, int j) const



int face (int i, int j) const



double vertex_rgb (int i, int j) const



int have_vertex_rgb () const



Protected Member Functions
void render (const Ref&lt; Render &gt; &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
