---
title: "qwtclipper(3)"
name: "qwtclipper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtclipper/"
description: "QwtClipper –"
---

<p>QwtClipper &#8211; </p>
<p> Some clipping algorithms.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_clipper.h&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static QPolygon <code>clipPolygon</code> (const QRect &amp;, const QPolygon &amp;, bool closePolygon=false) </p>
<p> static QPolygon <code>clipPolygon</code> (const QRectF &amp;, const QPolygon &amp;, bool closePolygon=false) </p>
<p> static QPolygonF <code>clipPolygonF</code> (const QRectF &amp;, const QPolygonF &amp;, bool closePolygon=false) </p>
<p> static QVector&lt; <code>QwtInterval</code> &gt; <code>clipCircle</code> (const QRectF &amp;, const QPointF &amp;, double radius) </p>
<h2>Detailed Description</h2>
<p>Some clipping algorithms.</p>
<h2>Member Function Documentation</h2>
<h3>QVector&lt; <code>QwtInterval</code> &gt; QwtClipper::clipCircle (const QRectF &amp;clipRect, const QPointF &amp;center, doubleradius) [static]</h3>
<p>Circle clipping </p>
<p> <code>clipCircle()</code> divides a circle into intervals of angles representing arcs of the circle. When the circle is completely inside the clip rectangle an interval [0.0, 2 * M_PI] is returned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>clipRect</i> Clip rectangle<br />
 <i>center</i> Center of the circle<br />
 <i>radius</i> Radius of the circle</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Arcs of the circle</dl>
<h3>QPolygon QwtClipper::clipPolygon (const QRect &amp;clipRect, const QPolygon &amp;polygon, boolclosePolygon = false) [static]</h3>
<p>Sutherland-Hodgman polygon clipping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>clipRect</i> Clip rectangle<br />
 <i>polygon</i> Polygon<br />
 <i>closePolygon</i> True, when the polygon is closed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Clipped polygon</dl>
<h3>QPolygon QwtClipper::clipPolygon (const QRectF &amp;clipRect, const QPolygon &amp;polygon, boolclosePolygon = false) [static]</h3>
<p>Sutherland-Hodgman polygon clipping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>clipRect</i> Clip rectangle<br />
 <i>polygon</i> Polygon<br />
 <i>closePolygon</i> True, when the polygon is closed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Clipped polygon</dl>
<h3>QPolygonF QwtClipper::clipPolygonF (const QRectF &amp;clipRect, const QPolygonF &amp;polygon, boolclosePolygon = false) [static]</h3>
<p>Sutherland-Hodgman polygon clipping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>clipRect</i> Clip rectangle<br />
 <i>polygon</i> Polygon<br />
 <i>closePolygon</i> True, when the polygon is closed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Clipped polygon</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
