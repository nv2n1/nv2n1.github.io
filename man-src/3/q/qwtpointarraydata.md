---
title: "qwtpointarraydata(3)"
name: "qwtpointarraydata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpointarraydata/"
description: "QwtPointArrayData –"
---

<p>QwtPointArrayData &#8211; </p>
<p> Interface for iterating over two QVector&lt;double&gt; objects.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_data.h&gt; </p>
<p> Inherits <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPointArrayData</code> (const QVector&lt; double &gt; &amp;x, const QVector&lt; double &gt; &amp;y) </p>
<p> <code>QwtPointArrayData</code> (const double *x, const double *y, size_t <code>size</code>) </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Calculate the bounding rectangle. </i><br />
 virtual size_t <code>size</code> () const </p>
<p> virtual QPointF <code>sample</code> (size_t i) const </p>
<p> const QVector&lt; double &gt; &amp; <code>xData</code> () const </p>
<p> const QVector&lt; double &gt; &amp; <code>yData</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>Interface for iterating over two QVector&lt;double&gt; objects.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPointArrayData::QwtPointArrayData (const QVector&lt; double &gt; &amp;x, const QVector&lt; double &gt; &amp;y)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Array of x values<br />
 <i>y</i> Array of y values</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code>, <code>QwtPlotCurve::setSamples()</code></dl>
<h3>QwtPointArrayData::QwtPointArrayData (const double *x, const double *y, size_tsize)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Array of x values<br />
 <i>y</i> Array of y values<br />
 <i>size</i> Size of the x and y arrays</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code>, <code>QwtPlotCurve::setSamples()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPointArrayData::boundingRect () const [virtual]</h3>
<p>Calculate the bounding rectangle. The bounding rectangle is calculated once by iterating over all points and is stored for all following requests. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>QPointF QwtPointArrayData::sample (size_tindex) const [virtual]</h3>
<p>Return the sample at position i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at position i</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>size_t QwtPointArrayData::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the data set</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>const QVector&lt; double &gt; &amp; QwtPointArrayData::xData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the x-values</dl>
<h3>const QVector&lt; double &gt; &amp; QwtPointArrayData::yData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the y-values</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
