---
title: "wfmath_rotbox(3)"
name: "wfmath_rotbox"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_rotbox/"
description: "WFMath::RotBox – A dim dimensional box, lying at an arbitrary angle."
---

<p>WFMath::RotBox &#8211; A dim dimensional box, lying at an arbitrary angle. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/rotbox.h">rotbox.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>RotBox</code> ()<br />
 <i>construct an uninitialized box </i><br />
 <code>RotBox</code> (const <code>Point</code>&lt; dim &gt; &amp;p, const <code>Vector</code>&lt; dim &gt; &amp;size, const <code>RotMatrix</code>&lt; dim &gt; &amp;orientation)<br />
 <i>construct a box from the given parameters </i><br />
 <code>RotBox</code> (const <code>RotBox</code> &amp;b)<br />
 <i>construct a copy of the box </i><br />
 <code>RotBox</code> (const AtlasInType &amp;a)<br />
 <i>Construct a rotbox from an object passed by Atlas. </i><br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the box. </i><br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the box&#8217;s value to that given by an Atlas object. </i><br />
 const <code>Point</code>&lt; dim &gt; &amp; <code>corner0</code> () const<br />
 <i>returns the base corner of the box </i><br />
 <code>Point</code>&lt; dim &gt; &amp; <code>corner0</code> ()<br />
 <i>returns the base corner of the box </i><br />
 const <code>Vector</code>&lt; dim &gt; &amp; <code>size</code> () const<br />
 <i>returns the size of the box </i><br />
 <code>Vector</code>&lt; dim &gt; &amp; <code>size</code> ()<br />
 <i>returns the size of the box </i><br />
 const <code>RotMatrix</code>&lt; dim &gt; &amp; <code>orientation</code> () const<br />
 <i>returns the orientation of the box </i><br />
 <code>RotMatrix</code>&lt; dim &gt; &amp; <code>orientation</code> ()<br />
 <i>returns the orientation of the box </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::RotBox&lt; dim &gt;</h3>
<p>A dim dimensional box, lying at an arbitrary angle. </p>
<p> This class implements the full shape interface, as described in the fake class <code>Shape</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;const int dim&gt; <code>WFMath::RotBox</code>&lt; dim &gt;::<code>RotBox</code> (const <code>Point</code>&lt; dim &gt; &amp; p, const <code>Vector</code>&lt; dim &gt; &amp; size, const <code>RotMatrix</code>&lt; dim &gt; &amp; orientation) [inline]</h3>
<p>construct a box from the given parameters </p>
<p> p gives corner 0 of the box, size gives the offset from corner 0 to the opposite corner (corner 2^dim &#8211; 1), orientation gives the rotation of the box relative to the coordinate axes </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
