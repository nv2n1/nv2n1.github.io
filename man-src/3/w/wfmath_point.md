---
title: "wfmath_point(3)"
name: "wfmath_point"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_point/"
description: "WFMath::Point – A dim dimensional point."
---

<p>WFMath::Point &#8211; A dim dimensional point. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/point.h">point.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Point</code> ()<br />
 <i>Construct an uninitialized point. </i><br />
 <code>Point</code> (const <code>Point</code> &amp;p)<br />
 <i>Construct a copy of a point. </i><br />
 <code>Point</code> (const AtlasInType &amp;a)<br />
 <i>Construct a point from an object passed by Atlas. </i><br />
 <code>Point</code> (const <code>Vector</code>&lt; dim &gt; vector)<br />
 <i>Construct a point from a vector. </i><br />
 AtlasOutType <code>toAtlas</code> () const<br />
 <i>Create an Atlas object from the point. </i><br />
 void <code>fromAtlas</code> (const AtlasInType &amp;a)<br />
 <i>Set the point&#8217;s value to that given by an Atlas object. </i><br />
 void <code>setValid</code> (bool valid=true)<br />
 <i>make isValid() return true if you&#8217;ve initialized the point by hand </i><br />
 <code>Point</code> &amp; <code>setToOrigin</code> ()<br />
 <i>Set point to (0,0,&#8230;,0). </i><br />
 <code>Point</code> &amp; <code>rotate</code> (const <code>RotMatrix</code>&lt; dim &gt; &amp;m, const <code>Point</code> &amp;p)<br />
 <i>Rotate about point p. </i><br />
 <code>CoordType</code> <code>operator[]</code> (const int i) const<br />
 <i>Access the i&#8217;th coordinate of the point. </i><br />
 <code>CoordType</code> &amp; <code>operator[]</code> (const int i)<br />
 <i>Access the i&#8217;th coordinate of the point. </i><br />
 <code>Point</code> (<code>CoordType</code> x, <code>CoordType</code> y)<br />
 <i>2D only: construct a point from its (x, y) coordinates </i><br />
 <code>Point</code> (<code>CoordType</code> x, <code>CoordType</code> y, <code>CoordType</code> z)<br />
 <i>3D only: construct a point from its (x, y, z) coordinates </i><br />
 <code>CoordType</code> <code>x</code> () const<br />
 <i>access the first component of a point </i><br />
 <code>CoordType</code> &amp; <code>x</code> ()<br />
 <i>access the first component of a point </i><br />
 <code>CoordType</code> <code>y</code> () const<br />
 <i>access the second component of a point </i><br />
 <code>CoordType</code> &amp; <code>y</code> ()<br />
 <i>access the second component of a point </i><br />
 <code>CoordType</code> <code>z</code> () const<br />
 <i>access the third component of a point </i><br />
 <code>CoordType</code> &amp; <code>z</code> ()<br />
 <i>access the third component of a point </i><br />
 <code>Point</code>&lt; 2 &gt; &amp; <code>polar</code> (<code>CoordType</code> r, <code>CoordType</code> theta)<br />
 <i>2D only: construct a vector from polar coordinates </i><br />
 void <code>asPolar</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta) const<br />
 <i>2D only: convert a vector to polar coordinates </i><br />
 <code>Point</code>&lt; 3 &gt; &amp; <code>polar</code> (<code>CoordType</code> r, <code>CoordType</code> theta, <code>CoordType</code> z)<br />
 <i>3D only: construct a vector from polar coordinates </i><br />
 void <code>asPolar</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta, <code>CoordType</code> &amp;z) const<br />
 <i>3D only: convert a vector to polar coordinates </i><br />
 <code>Point</code>&lt; 3 &gt; &amp; <code>spherical</code> (<code>CoordType</code> r, <code>CoordType</code> theta, <code>CoordType</code> phi)<br />
 <i>3D only: construct a vector from spherical coordinates </i><br />
 void <code>asSpherical</code> (<code>CoordType</code> &amp;r, <code>CoordType</code> &amp;theta, <code>CoordType</code> &amp;phi) const<br />
 <i>3D only: convert a vector to spherical coordinates </i></p>
<h3>Static Public Member Functions</h3>
<p>static const <code>Point</code>&lt; dim &gt; &amp; <code>ZERO</code> ()<br />
 <i>Provides a global instance preset to zero. </i></p>
<h3>Friends</h3>
<p><code>CoordType</code> <code>SquaredDistance</code> (const <code>Point</code> &amp;p1, const <code>Point</code> &amp;p2)<br />
 <i>Get the square of the distance from p1 to p2. </i><br />
 <code>Point</code>&lt; dim &gt; <code>Midpoint</code> (const <code>Point</code> &amp;p1, const <code>Point</code> &amp;p2, <code>CoordType</code> dist)<br />
 <i>Find a point on the line containing p1 and p2, by default the midpoint. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::Point&lt; dim &gt;</h3>
<p>A dim dimensional point. </p>
<p> This class implements the full shape interface, as described in the fake class <code>Shape</code>.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>template&lt;const int dim&gt; <code>Point</code>&lt;dim&gt; Midpoint (const <code>Point</code>&lt; dim &gt; &amp; p1, const <code>Point</code>&lt; dim &gt; &amp; p2, <code>CoordType</code> dist = 0.5) [friend]</h3>
<p>Find a point on the line containing p1 and p2, by default the midpoint. </p>
<p> The default value of 0.5 for dist gives the midpoint. A value of 0 gives p1, and 1 gives p2. Values of dist outside the [0, 1] range are allowed, and give points on the line which are not on the segment bounded by p1 and p2. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
