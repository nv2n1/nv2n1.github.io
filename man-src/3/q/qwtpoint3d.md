---
title: "qwtpoint3d(3)"
name: "qwtpoint3d"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpoint3d/"
description: "QwtPoint3D –"
---

<p>QwtPoint3D &#8211; </p>
<p> <code>QwtPoint3D</code> class defines a 3D point in double coordinates.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_3d.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtPoint3D</code> () </p>
<p> <code>QwtPoint3D</code> (double <code>x</code>, double <code>y</code>, double <code>z</code>)<br />
 <i>Constructs a point with coordinates specified by x, y and z. </i><br />
 <code>QwtPoint3D</code> (const <code>QwtPoint3D</code> &amp;) </p>
<p> <code>QwtPoint3D</code> (const QPointF &amp;) </p>
<p> bool <code>isNull</code> () const </p>
<p> double <code>x</code> () const </p>
<p> double <code>y</code> () const </p>
<p> double <code>z</code> () const </p>
<p> double &amp; <code>rx</code> () </p>
<p> double &amp; <code>ry</code> () </p>
<p> double &amp; <code>rz</code> () </p>
<p> void <code>setX</code> (double <code>x</code>)<br />
 <i>Sets the x-coordinate of the point to the value specified by x. </i><br />
 void <code>setY</code> (double <code>y</code>)<br />
 <i>Sets the y-coordinate of the point to the value specified by y. </i><br />
 void <code>setZ</code> (double <code>y</code>)<br />
 <i>Sets the z-coordinate of the point to the value specified by z. </i><br />
 QPointF <code>toPoint</code> () const </p>
<p> bool <code>operator==</code> (const <code>QwtPoint3D</code> &amp;) const </p>
<p> bool <code>operator!=</code> (const <code>QwtPoint3D</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPoint3D</code> class defines a 3D point in double coordinates.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPoint3D::QwtPoint3D () [inline]</h3>
<p>Constructs a null point. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isNull()</code></dl>
<h3>QwtPoint3D::QwtPoint3D (const <code>QwtPoint3D</code> &amp;other) [inline]</h3>
<p>Copy constructor. Constructs a point using the values of the point specified.</p>
<h3>QwtPoint3D::QwtPoint3D (const QPointF &amp;other) [inline]</h3>
<p>Constructs a point with x and y coordinates from a 2D point, and a z coordinate of 0.</p>
<h2>Member Function Documentation</h2>
<h3>bool QwtPoint3D::isNull () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True if the point is null; otherwise returns false.</dl>
<p> A point is considered to be null if x, y and z-coordinates are equal to zero.</p>
<h3>bool QwtPoint3D::operator!= (const <code>QwtPoint3D</code> &amp;other) const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True if this rect and other are different; otherwise returns false.</dl>
<h3>bool QwtPoint3D::operator== (const <code>QwtPoint3D</code> &amp;other) const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if this point and other are equal; otherwise returns false.</dl>
<h3>double &amp; QwtPoint3D::rx () [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A reference to the x-coordinate of the point.</dl>
<h3>double &amp; QwtPoint3D::ry () [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A reference to the y-coordinate of the point.</dl>
<h3>double &amp; QwtPoint3D::rz () [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A reference to the z-coordinate of the point.</dl>
<h3>QPointF QwtPoint3D::toPoint () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>2D point, where the z coordinate is dropped.</dl>
<h3>double QwtPoint3D::x () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The x-coordinate of the point.</dl>
<h3>double QwtPoint3D::y () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The y-coordinate of the point.</dl>
<h3>double QwtPoint3D::z () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The z-coordinate of the point.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
