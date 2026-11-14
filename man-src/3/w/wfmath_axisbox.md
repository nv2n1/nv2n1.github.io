---
title: "wfmath_axisbox(3)"
name: "wfmath_axisbox"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_axisbox/"
description: "WFMath::AxisBox – A dim dimensional axis-aligned box."
---

<p>WFMath::AxisBox &#8211; A dim dimensional axis-aligned box. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/axisbox.h">axisbox.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>AxisBox</code> ()<br />
 <i>Construct an uninitialized box. </i><br />
 <code>AxisBox</code> (const <code>Point</code>&lt; dim &gt; &amp;p1, const <code>Point</code>&lt; dim &gt; &amp;p2, bool ordered=false)<br />
 <i>Construct a box with opposite corners p1 and p2. </i><br />
 <code>AxisBox</code> (const <code>AxisBox</code> &amp;a)<br />
 <i>Construct a copy of a box. </i><br />
 <code>AxisBox</code> (const AtlasInType &amp;a)<br />
 <i>Construct a box from an object passed by Atlas. </i><br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the box. </i><br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the box&#8217;s value to that given by an Atlas object. </i><br />
 const <code>Point</code>&lt; dim &gt; &amp; <code>lowCorner</code> () const<br />
 <i>Get a reference to corner 0. </i><br />
 const <code>Point</code>&lt; dim &gt; &amp; <code>highCorner</code> () const<br />
 <i>Get a reference to corner (2^dim)-1. </i><br />
 <code>CoordType</code> <code>lowerBound</code> (const int axis) const<br />
 <i>Get the lower bound of the box on the i&#8217;th axis. </i><br />
 <code>CoordType</code> <code>upperBound</code> (const int axis) const<br />
 <i>Get the upper bound of the box on the i&#8217;th axis. </i><br />
 <code>AxisBox</code> &amp; <code>setCorners</code> (const <code>Point</code>&lt; dim &gt; &amp;p1, const <code>Point</code>&lt; dim &gt; &amp;p2, bool ordered=false)<br />
 <i>Set the box to have opposite corners p1 and p2. </i></p>
<h3>Friends</h3>
<p>bool <code>Intersection</code> (const <code>AxisBox</code> &amp;a1, const <code>AxisBox</code> &amp;a2, <code>AxisBox</code> &amp;out)<br />
 <i>Return true if the boxes intersect, and set &#8216;out&#8217; to their intersection. </i><br />
 <code>AxisBox</code> <code>Union</code> (const <code>AxisBox</code> &amp;a1, const <code>AxisBox</code> &amp;a2)<br />
 <i>Get the minimal box that contains a1 and a2. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::AxisBox&lt; dim &gt;</h3>
<p>A dim dimensional axis-aligned box. </p>
<p> This class implements the full shape interface, as described in the fake class <code>Shape</code>, with the exception of the rotation functions.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;const int dim&gt; <code>AxisBox</code>&lt; dim &gt; &amp; <code>WFMath::AxisBox</code>&lt; dim &gt;::setCorners (const <code>Point</code>&lt; dim &gt; &amp; p1, const <code>Point</code>&lt; dim &gt; &amp; p2, bool ordered = false) [inline]</h3>
<p>Set the box to have opposite corners p1 and p2. </p>
<p> The &#8216;ordered&#8217; variable may be set to true if p1[i] &lt;= p2[i] for all i. It is always safe to leave &#8216;ordered&#8217; as false, it is a speed optimization primarily intended for use inside the library. </p>
<p> Referenced by WFMath::AxisBox&lt; dim &gt;::AxisBox(). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
