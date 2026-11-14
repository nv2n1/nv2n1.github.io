---
title: "sc_unionshape(3)"
name: "sc_unionshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_unionshape/"
description: "sc::UnionShape –"
---

<p>sc::UnionShape &#8211; </p>
<p> A <code>UnionShape</code> is volume enclosed by a set of Shape&#8217;s.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;shape.h&gt;</code></pre>
<p> Inherits <code>sc::Shape</code>. Inherited by <code>sc::DiscreteConnollyShape</code>, and <code>sc::VDWShape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void add_shape (Ref&lt; Shape &gt;)



double distance_to_surface (const SCVector3 &amp;r, SCVector3 *grad=0) const



int is_outside (const SCVector3 &amp;r) const



void boundingbox (double valuemin, double valuemax, SCVector3 &amp;p1, SCVector3 &amp;p2)



int gradient_implemented () const



Protected Attributes</code></pre>
<p> std::set&lt; <code>Ref</code>&lt; <code>Shape</code> &gt; &gt; <code>_shapes</code></p>
<h2>Detailed Description</h2>
<p>A <code>UnionShape</code> is volume enclosed by a set of Shape&#8217;s.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
