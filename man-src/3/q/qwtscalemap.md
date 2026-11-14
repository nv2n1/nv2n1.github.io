---
title: "qwtscalemap(3)"
name: "qwtscalemap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscalemap/"
description: "QwtScaleMap –"
---

<p>QwtScaleMap &#8211; </p>
<p> A scale map.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_map.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleMap</code> ()<br />
 <i>Constructor. </i><br />
 <code>QwtScaleMap</code> (const <code>QwtScaleMap</code> &amp;)<br />
 <i>Copy constructor. </i><br />
 <code>~QwtScaleMap</code> () </p>
<p> <code>QwtScaleMap</code> &amp; <code>operator=</code> (const <code>QwtScaleMap</code> &amp;)<br />
 <i>Assignment operator. </i><br />
 void <code>setTransformation</code> (<code>QwtTransform</code> *) </p>
<p> const <code>QwtTransform</code> * <code>transformation</code> () const<br />
 <i>Get the transformation. </i><br />
 void <code>setPaintInterval</code> (double <code>p1</code>, double <code>p2</code>)<br />
 <i>Specify the borders of the paint device interval. </i><br />
 void <code>setScaleInterval</code> (double <code>s1</code>, double <code>s2</code>)<br />
 <i>Specify the borders of the scale interval. </i><br />
 double <code>transform</code> (double s) const </p>
<p> double <code>invTransform</code> (double p) const </p>
<p> double <code>p1</code> () const </p>
<p> double <code>p2</code> () const </p>
<p> double <code>s1</code> () const </p>
<p> double <code>s2</code> () const </p>
<p> double <code>pDist</code> () const </p>
<p> double <code>sDist</code> () const </p>
<p> bool <code>isInverting</code> () const </p>
<h3>Static Public Member Functions</h3>
<p>static QRectF <code>transform</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QRectF &amp;) </p>
<p> static QRectF <code>invTransform</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QRectF &amp;) </p>
<p> static QPointF <code>transform</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QPointF &amp;) </p>
<p> static QPointF <code>invTransform</code> (const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QPointF &amp;) </p>
<h2>Detailed Description</h2>
<p>A scale map. </p>
<p> <code>QwtScaleMap</code> offers transformations from the coordinate system of a scale into the linear coordinate system of a paint device and vice versa.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleMap::QwtScaleMap ()</h3>
<p>Constructor. The scale and paint device intervals are both set to [0,1].</p>
<h3>QwtScaleMap::~QwtScaleMap ()</h3>
<p>Destructor</p>
<h2>Member Function Documentation</h2>
<h3>double QwtScaleMap::invTransform (doublep) const [inline]</h3>
<p>Transform an paint device value into a value in the interval of the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> Value relative to the coordinates of the paint device</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Transformed value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<h3>QRectF QwtScaleMap::invTransform (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) [static]</h3>
<p>Transform a rectangle from paint to scale coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X map<br />
 <i>yMap</i> Y map<br />
 <i>rect</i> Rectangle in paint coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle in scale coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<h3>QPointF QwtScaleMap::invTransform (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QPointF &amp;pos) [static]</h3>
<p>Transform a rectangle from paint to scale coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X map<br />
 <i>yMap</i> Y map<br />
 <i>pos</i> Position in paint coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position in scale coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<h3>bool QwtScaleMap::isInverting () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when ( <code>p1()</code> &lt; <code>p2()</code> ) != ( <code>s1()</code> &lt; <code>s2()</code> )</dl>
<h3>double QwtScaleMap::p1 () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>First border of the paint interval</dl>
<h3>double QwtScaleMap::p2 () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Second border of the paint interval</dl>
<h3>double QwtScaleMap::pDist () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>qwtAbs(<code>p2()</code> &#8211; <code>p1()</code>)</dl>
<h3>double QwtScaleMap::s1 () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>First border of the scale interval</dl>
<h3>double QwtScaleMap::s2 () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Second border of the scale interval</dl>
<h3>double QwtScaleMap::sDist () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>qwtAbs(<code>s2()</code> &#8211; <code>s1()</code>)</dl>
<h3>void QwtScaleMap::setPaintInterval (doublep1, doublep2)</h3>
<p>Specify the borders of the paint device interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p1</i> first border<br />
 <i>p2</i> second border</dl>
<h3>void QwtScaleMap::setScaleInterval (doubles1, doubles2)</h3>
<p>Specify the borders of the scale interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>s1</i> first border<br />
 <i>s2</i> second border</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>scales might be aligned to transformation depending boundaries</dl>
<h3>void QwtScaleMap::setTransformation (<code>QwtTransform</code> *transform)</h3>
<p>Initialize the map with a transformation</p>
<h3>double QwtScaleMap::transform (doubles) const [inline]</h3>
<p>Transform a point related to the scale interval into an point related to the interval of the paint device </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>s</i> Value relative to the coordinates of the scale</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Transformed value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<h3>QRectF QwtScaleMap::transform (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) [static]</h3>
<p>Transform a rectangle from scale to paint coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X map<br />
 <i>yMap</i> Y map<br />
 <i>rect</i> Rectangle in scale coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle in paint coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<h3>QPointF QwtScaleMap::transform (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QPointF &amp;pos) [static]</h3>
<p>Transform a point from scale to paint coordinates </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X map<br />
 <i>yMap</i> Y map<br />
 <i>pos</i> Position in scale coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position in paint coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
