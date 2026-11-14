---
title: "qwtpointmapper(3)"
name: "qwtpointmapper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpointmapper/"
description: "QwtPointMapper –"
---

<p>QwtPointMapper &#8211; </p>
<p> A helper class for translating a series of points.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_mapper.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>TransformationFlag</code> { <code>RoundPoints</code> = 0x01, <code>WeedOutPoints</code> = 0x02 }<br />
 <i>Flags affecting the transformation process. </i><br />
 typedef QFlags<br />
 &lt; <code>TransformationFlag</code> &gt; <code>TransformationFlags</code>&quot;<br />
 <i>Flags affecting the transformation process. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPointMapper</code> ()<br />
 <i>Constructor. </i><br />
 <code>~QwtPointMapper</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setFlags</code> (<code>TransformationFlags</code>) </p>
<p> <code>TransformationFlags</code> <code>flags</code> () const </p>
<p> void <code>setFlag</code> (<code>TransformationFlag</code>, bool on=true) </p>
<p> bool <code>testFlag</code> (<code>TransformationFlag</code>) const </p>
<p> void <code>setBoundingRect</code> (const QRectF &amp;) </p>
<p> QRectF <code>boundingRect</code> () const </p>
<p> QPolygonF <code>toPolygonF</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, int from, int to) const<br />
 <i>Translate a series of points into a QPolygonF. </i><br />
 QPolygon <code>toPolygon</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, int from, int to) const<br />
 <i>Translate a series of points into a QPolygon. </i><br />
 QPolygon <code>toPoints</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, int from, int to) const<br />
 <i>Translate a series of points into a QPolygon. </i><br />
 QPolygonF <code>toPointsF</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, int from, int to) const<br />
 <i>Translate a series into a QPolygonF. </i><br />
 QImage <code>toImage</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, int from, int to, const QPen &amp;, bool antialiased, uint numThreads) const<br />
 <i>Translate a series into a QImage. </i></p>
<h2>Detailed Description</h2>
<p>A helper class for translating a series of points. </p>
<p> <code>QwtPointMapper</code> is a collection of methods and optimizations for translating a series of points into paint device coordinates. It is used by <code>QwtPlotCurve</code> but might also be useful for similar plot items displaying a <code>QwtSeriesData&lt;QPointF&gt;</code>.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef QFlags&lt;<code>TransformationFlag</code>&gt; <code>QwtPointMapper::TransformationFlags</code></h3>
<p>Flags affecting the transformation process. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFlag()</code>, <code>setFlags()</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPointMapper::TransformationFlag</code></h3>
<p>Flags affecting the transformation process. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFlag()</code>, <code>setFlags()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>RoundPoints </i></p>
<dd>Round points to integer values.</p>
<dt><i>WeedOutPoints </i></p>
<dd>Try to remove points, that are translated to the same position.</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPointMapper::boundingRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBoundingRect()</code></dl>
<h3><code>QwtPointMapper::TransformationFlags</code> QwtPointMapper::flags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Flags affecting the transformation process</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFlags()</code>, <code>setFlag()</code></dl>
<h3>void QwtPointMapper::setBoundingRect (const QRectF &amp;rect)</h3>
<p>Set a bounding rectangle for the point mapping algorithm </p>
<p> A valid bounding rectangle can be used for optimizations </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>boundingRect()</code></dl>
<h3>void QwtPointMapper::setFlag (<code>TransformationFlag</code>flag, boolon = true)</h3>
<p>Modify a flag affecting the transformation process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag type<br />
 <i>on</i> Value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>flag(), <code>setFlags()</code></dl>
<h3>void QwtPointMapper::setFlags (<code>TransformationFlags</code>flags)</h3>
<p>Set the flags affecting the transformation process </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flags</i> Flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>flags()</code>, <code>setFlag()</code></dl>
<h3>bool QwtPointMapper::testFlag (<code>TransformationFlag</code>flag) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the flag is set</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag type</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFlag()</code>, <code>setFlags()</code></dl>
<h3>QImage QwtPointMapper::toImage (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, intfrom, intto, const QPen &amp;pen, boolantialiased, uintnumThreads) const</h3>
<p>Translate a series into a QImage. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>series</i> Series of points to be mapped<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted<br />
 <i>pen</i> Pen used for drawing a point of the image, where a point is mapped to<br />
 <i>antialiased</i> True, when the dots should be displayed antialiased<br />
 <i>numThreads</i> Number of threads to be used for rendering. If numThreads is set to 0, the system specific ideal thread count is used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Image displaying the series</dl>
<h3>QPolygon QwtPointMapper::toPoints (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, intfrom, intto) const</h3>
<p>Translate a series of points into a QPolygon.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>WeedOutPoints &amp; <code>boundingRect()</code>.isValid() All points that are mapped to the same position will be one point. Points outside of the bounding rectangle are ignored.</p>
<dt>&bull;</p>
<dd>WeedOutPoints &amp; !boundingRect().isValid() All consecutive points that are mapped to the same position will one point</p>
<dt>&bull;</p>
<dd>!WeedOutPoints &amp; <code>boundingRect()</code>.isValid() Points outside of the bounding rectangle are ignored.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>series</i> Series of points to be mapped<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated polygon</dl>
<h3>QPolygonF QwtPointMapper::toPointsF (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, intfrom, intto) const</h3>
<p>Translate a series into a QPolygonF.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>WeedOutPoints &amp; RoundPoints &amp; <code>boundingRect()</code>.isValid() All points that are mapped to the same position will be one point. Points outside of the bounding rectangle are ignored.</p>
<dt>&bull;</p>
<dd>WeedOutPoints &amp; RoundPoints &amp; !boundingRect().isValid() All consecutive points that are mapped to the same position will one point</p>
<dt>&bull;</p>
<dd>WeedOutPoints &amp; !RoundPoints All consecutive points that are mapped to the same position will one point</p>
<dt>&bull;</p>
<dd>!WeedOutPoints &amp; <code>boundingRect()</code>.isValid() Points outside of the bounding rectangle are ignored.</dl>
<p> When RoundPoints is set all points are rounded to integers but returned as PolygonF &#8211; what only makes sense when the further processing of the values need a QPolygonF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>series</i> Series of points to be mapped<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated polygon</dl>
<h3>QPolygon QwtPointMapper::toPolygon (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, intfrom, intto) const</h3>
<p>Translate a series of points into a QPolygon. When the WeedOutPoints flag is enabled consecutive points, that are mapped to the same position will be one point. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>series</i> Series of points to be mapped<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated polygon</dl>
<h3>QPolygonF QwtPointMapper::toPolygonF (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtSeriesData</code>&lt; QPointF &gt; *series, intfrom, intto) const</h3>
<p>Translate a series of points into a QPolygonF. When the WeedOutPoints flag is enabled consecutive points, that are mapped to the same position will be one point. </p>
<p> When RoundPoints is set all points are rounded to integers but returned as PolygonF &#8211; what only makes sense when the further processing of the values need a QPolygonF. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>series</i> Series of points to be mapped<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated polygon</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
