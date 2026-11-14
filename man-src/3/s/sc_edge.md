---
title: "sc_edge(3)"
name: "sc_edge"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_edge/"
description: "sc::Edge –"
---

<p>sc::Edge &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Edge</code> (const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p1, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p2) </p>
<p> <code>Edge</code> (const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p1, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p2, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p3) </p>
<p> <code>Edge</code> (const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p1, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p2, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p3, const <code>Ref</code>&lt; <code>Vertex</code> &gt; &amp;p4) </p>
<p> int <code>order</code> () const </p>
<p> double <code>straight_length</code> () </p>
<p> <code>Ref</code>&lt; <code>Vertex</code> &gt; <code>vertex</code> (int i) const </p>
<p> <code>Ref</code>&lt; <code>Vertex</code> &gt; <code>interior_vertex</code> (int i) const </p>
<p> void <code>add_vertices</code> (std::set&lt; <code>Ref</code>&lt; <code>Vertex</code> &gt; &gt; &amp;) </p>
<p> void <code>set_order</code> (int order, const <code>Ref</code>&lt; <code>Volume</code> &gt; &amp;vol, double isovalue) </p>
<p> int <code>interpolate</code> (double location, <code>SCVector3</code> &amp;<code>point</code>, <code>SCVector3</code> &amp;norm) </p>
<p> int <code>interpolate</code> (double location, <code>SCVector3</code> &amp;<code>point</code>, <code>SCVector3</code> &amp;norm, const <code>Ref</code>&lt; <code>Volume</code> &gt; &amp;vol, double isovalue) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
