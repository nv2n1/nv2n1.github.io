---
title: "qwtpointpolar(3)"
name: "qwtpointpolar"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpointpolar/"
description: "QwtPointPolar –"
---

<p>QwtPointPolar &#8211; </p>
<p> A point in polar coordinates.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_polar.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtPointPolar</code> () </p>
<p> <code>QwtPointPolar</code> (double <code>azimuth</code>, double <code>radius</code>) </p>
<p> <code>QwtPointPolar</code> (const <code>QwtPointPolar</code> &amp;) </p>
<p> <code>QwtPointPolar</code> (const QPointF &amp;) </p>
<p> void <code>setPoint</code> (const QPointF &amp;) </p>
<p> QPointF <code>toPoint</code> () const </p>
<p> bool <code>isValid</code> () const<br />
 <i>Returns true if </i><code>radius()</code> &gt;= 0.0.<br />
 bool <code>isNull</code> () const<br />
 <i>Returns true if </i><code>radius()</code> &gt;= 0.0.<br />
 double <code>radius</code> () const<br />
 <i>Returns the radius. </i><br />
 double <code>azimuth</code> () const<br />
 <i>Returns the azimuth. </i><br />
 double &amp; <code>rRadius</code> ()<br />
 <i>Returns the radius. </i><br />
 double &amp; <code>rAzimuth</code> ()<br />
 <i>Returns the azimuth. </i><br />
 void <code>setRadius</code> (double)<br />
 <i>Sets the radius to radius. </i><br />
 void <code>setAzimuth</code> (double)<br />
 <i>Sets the atimuth to atimuth. </i><br />
 bool <code>operator==</code> (const <code>QwtPointPolar</code> &amp;) const<br />
 <i>Compare 2 points. </i><br />
 bool <code>operator!=</code> (const <code>QwtPointPolar</code> &amp;) const </p>
<p> <code>QwtPointPolar</code> <code>normalized</code> () const </p>
<h2>Detailed Description</h2>
<p>A point in polar coordinates. </p>
<p> In polar coordinates a point is determined by an angle and a distance. See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Polar_coordinate_system">http://en.wikipedia.org/wiki/Polar_coordinate_system</a></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPointPolar::QwtPointPolar () [inline]</h3>
<p>Constructs a null point, with a radius and azimuth set to 0.0. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPointF::isNull()</dl>
<h3>QwtPointPolar::QwtPointPolar (doubleazimuth, doubleradius) [inline]</h3>
<p>Constructs a point with coordinates specified by radius and azimuth. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>azimuth</i> Azimuth<br />
 <i>radius</i> Radius</dl>
<h3>QwtPointPolar::QwtPointPolar (const <code>QwtPointPolar</code> &amp;other) [inline]</h3>
<p>Constructs a point using the values of the point specified. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Other point</dl>
<h3>QwtPointPolar::QwtPointPolar (const QPointF &amp;p)</h3>
<p>Convert and assign values from a point in Cartesian coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> Point in Cartesian coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPoint()</code>, <code>toPoint()</code></dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtPointPolar</code> QwtPointPolar::normalized () const</h3>
<p>Normalize radius and azimuth </p>
<p> When the radius is &lt; 0.0 it is set to 0.0. The azimuth is a value &gt;= 0.0 and &lt; 2 * M_PI. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Normalized point</dl>
<h3>bool QwtPointPolar::operator!= (const <code>QwtPointPolar</code> &amp;other) const</h3>
<p>Compare 2 points </p>
<p> Two points are equal to each other if radius and azimuth-coordinates are the same. Points are not equal, when the azimuth differs, but other.azimuth() == <code>azimuth()</code> % (2 * PI). </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True if the point is not equal to other; otherwise return false.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>normalized()</code></dl>
<h3>bool QwtPointPolar::operator== (const <code>QwtPointPolar</code> &amp;other) const</h3>
<p>Compare 2 points. Two points are equal to each other if radius and azimuth-coordinates are the same. Points are not equal, when the azimuth differs, but other.azimuth() == <code>azimuth()</code> % (2 * PI). </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True if the point is equal to other; otherwise return false.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>normalized()</code></dl>
<h3>void QwtPointPolar::setPoint (const QPointF &amp;p)</h3>
<p>Convert and assign values from a point in Cartesian coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> Point in Cartesian coordinates</dl>
<h3>QPointF QwtPointPolar::toPoint () const</h3>
<p>Convert and return values in Cartesian coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Converted point in Cartesian coordinates</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Invalid or null points will be returned as QPointF(0.0, 0.0)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code>, <code>isNull()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
