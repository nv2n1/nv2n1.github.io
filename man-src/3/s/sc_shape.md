---
title: "sc_shape(3)"
name: "sc_shape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shape/"
description: "sc::Shape –"
---

<p>sc::Shape &#8211; </p>
<p> A <code>Shape</code> is a <code>Volume</code> represents an 3D solid.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;shape.h&gt;</code></pre>
<p> Inherits <code>sc::Volume</code>. Inherited by <code>sc::ConnollyShape</code>, <code>sc::SphereShape</code>, <code>sc::Uncapped5SphereExclusionShape</code>, <code>sc::UncappedTorusHoleShape</code>, and <code>sc::UnionShape</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Shape</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;keyval) </p>
<p> virtual double <code>distance_to_surface</code> (const <code>SCVector3</code> &amp;r, <code>SCVector3</code> *grad=0) const =0 </p>
<p> virtual int <code>is_outside</code> (const <code>SCVector3</code> &amp;r) const </p>
<p> void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i><br />
 void <code>interpolate</code> (const <code>SCVector3</code> &amp;p1, const <code>SCVector3</code> &amp;p2, double val, <code>SCVector3</code> &amp;result) </p>
<p> int <code>value_implemented</code> () const<br />
 <i>Information about the availability of values, gradients, and hessians. </i></p>
<h2>Detailed Description</h2>
<p>A <code>Shape</code> is a <code>Volume</code> represents an 3D solid. </p>
<p> The value of the <code>Shape</code> at each <code>point</code> in space is the distance to the surface. The distance is negative if the <code>point</code> is inside the solid. For <code>Shape</code> specializations that cannot compute the distance to the surface, the value will be 1.0 outside and -1.0 inside the solid.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::Shape::compute () [virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Volume</code>.</p>
<h3>int sc::Shape::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
