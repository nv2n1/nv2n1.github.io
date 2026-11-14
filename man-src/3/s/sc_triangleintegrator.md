---
title: "sc_triangleintegrator(3)"
name: "sc_triangleintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_triangleintegrator/"
description: "sc::TriangleIntegrator –"
---

<p>sc::TriangleIntegrator &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::GaussTriangleIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TriangleIntegrator</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>TriangleIntegrator</code> (int n) </p>
<p> double <code>w</code> (int i) </p>
<p> double <code>r</code> (int i) </p>
<p> double <code>s</code> (int i) </p>
<p> int <code>n</code> () </p>
<p> virtual void <code>set_n</code> (int n) </p>
<p> <code>Ref</code>&lt; <code>TriInterpCoef</code> &gt; <code>coef</code> (int order, int i)</p>
<h3>Protected Member Functions</h3>
<pre><code>void set_r (int i, double r)



void set_s (int i, double s)



void set_w (int i, double w)



void init_coef ()



void clear_coef ()
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
