---
title: "sc_triangulatedsurface(3)"
name: "sc_triangulatedsurface"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_triangulatedsurface/"
description: "sc::TriangulatedSurface –"
---

<p>sc::TriangulatedSurface &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::TriangulatedImplicitSurface</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>TriangulatedSurface (const Ref&lt; KeyVal &gt; &amp;)



int verbose () const



void verbose (int v)



void set_integrator (const Ref&lt; TriangleIntegrator &gt; &amp;)



void set_fast_integrator (const Ref&lt; TriangleIntegrator &gt; &amp;)



void set_accurate_integrator (const Ref&lt; TriangleIntegrator &gt; &amp;)



virtual Ref&lt; TriangleIntegrator &gt; integrator (int itri)



virtual Ref&lt; TriangleIntegrator &gt; fast_integrator (int itri)



virtual Ref&lt; TriangleIntegrator &gt; accurate_integrator (int itri)



void add_triangle (const Ref&lt; Vertex &gt; &amp;, const Ref&lt; Vertex &gt; &amp;, const Ref&lt; Vertex &gt; &amp;)



Ref&lt; Edge &gt; find_edge (const Ref&lt; Vertex &gt; &amp;, const Ref&lt; Vertex &gt; &amp;)



virtual void complete_surface ()



virtual void remove_short_edges (double cutoff_length=1.0e-6, const Ref&lt; Volume &gt; &amp;vol=0, double isoval=0.0)



virtual void remove_slender_triangles (int remove_slender, double height_cutoff, int remove_small, double area_cutoff, const Ref&lt; Volume &gt; &amp;vol=0, double isoval=0.0)



virtual void fix_orientation ()



virtual void clear ()



int nvertex () const



Ref&lt; Vertex &gt; vertex (int i) const



int vertex_index (const Ref&lt; Vertex &gt; &amp;o)



int nedge () const



Ref&lt; Edge &gt; edge (int i) const



int edge_index (const Ref&lt; Edge &gt; &amp;o)



int ntriangle () const



Ref&lt; Triangle &gt; triangle (int i) const



int triangle_index (const Ref&lt; Triangle &gt; &amp;o)



int triangle_vertex (int i, int j) const



int triangle_edge (int i, int j) const



int edge_vertex (int i, int j) const



void compute_values (Ref&lt; Volume &gt; &amp;)



virtual double flat_area ()



virtual double flat_volume ()



virtual double area ()



virtual double volume ()



virtual void print (std::ostream &amp;o=ExEnv::out0()) const


Print the object.


virtual void print_vertices_and_triangles (std::ostream &amp;o=ExEnv::out0()) const



virtual void print_geomview_format (std::ostream &amp;o=ExEnv::out0()) const



virtual void render (const Ref&lt; Render &gt; &amp;render)



void topology_info (std::ostream &amp;o=ExEnv::out0())



void topology_info (int nvertex, int nedge, int ntri, std::ostream &amp;o=ExEnv::out0())



Protected Member Functions
void clear_int_arrays ()



void complete_ref_arrays ()



void complete_int_arrays ()



void recompute_index_maps ()



void add_triangle (const Ref&lt; Triangle &gt; &amp;)



void add_vertex (const Ref&lt; Vertex &gt; &amp;)



void add_edge (const Ref&lt; Edge &gt; &amp;)



virtual Triangle * newTriangle (const Ref&lt; Edge &gt; &amp;, const Ref&lt; Edge &gt; &amp;, const Ref&lt; Edge &gt; &amp;, int orientation) const



virtual Edge * newEdge (const Ref&lt; Vertex &gt; &amp;, const Ref&lt; Vertex &gt; &amp;) const



Protected Attributes
int _verbose



int _debug



int _completed_surface



std::set&lt; Ref&lt; Vertex &gt; &gt; _vertices



std::set&lt; Ref&lt; Edge &gt; &gt; _edges



std::set&lt; Ref&lt; Triangle &gt; &gt; _triangles



std::map&lt; Ref&lt; Vertex &gt;, int &gt; _vertex_to_index



std::map&lt; Ref&lt; Edge &gt;, int &gt; _edge_to_index



std::map&lt; Ref&lt; Triangle &gt;, int &gt; _triangle_to_index



std::vector&lt; Ref&lt; Vertex &gt; &gt; _index_to_vertex



std::vector&lt; Ref&lt; Edge &gt; &gt; _index_to_edge



std::vector&lt; Ref&lt; Triangle &gt; &gt; _index_to_triangle



int ** _triangle_vertex



int ** _triangle_edge



int ** _edge_vertex



int _have_values



std::vector&lt; double &gt; _values



Ref&lt; TriangleIntegrator &gt; _integrator



Ref&lt; TriangleIntegrator &gt; _fast_integrator



Ref&lt; TriangleIntegrator &gt; _accurate_integrator



std::map&lt; Ref&lt; Vertex &gt;, std::set&lt; Ref&lt; Edge &gt; &gt; &gt; _tmp_edges
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
