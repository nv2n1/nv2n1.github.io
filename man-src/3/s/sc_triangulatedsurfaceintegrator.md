---
title: "sc_triangulatedsurfaceintegrator(3)"
name: "sc_triangulatedsurfaceintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_triangulatedsurfaceintegrator/"
---

sc::TriangulatedSurfaceIntegrator -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>TriangulatedSurfaceIntegrator (const Ref&lt; TriangulatedSurface &gt; &amp;)



void operator= (const TriangulatedSurfaceIntegrator &amp;)



TriangulatedSurfaceIntegrator (const TriangulatedSurfaceIntegrator &amp;i)



int n ()



void set_surface (const Ref&lt; TriangulatedSurface &gt; &amp;)



int vertex_number (int i)



double r () const



double s () const



double w () const



double surface_element () const



double weight () const



const SCVector3 &amp; dA () const



Ref&lt; Vertex &gt; current ()



int update ()



int operator&lt; (TriangulatedSurfaceIntegrator &amp;i)



void operator++ ()



void operator++ (int)



int operator= (int)



int itri () const



int irs () const



int n_in_tri () const



void distribute (const Ref&lt; MessageGrp &gt; &amp;)



void use_fast_integrator ()



void use_accurate_integrator ()



void use_default_integrator ()
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
