---
title: "qwtcpointerdata(3)"
name: "qwtcpointerdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcpointerdata/"
description: "QwtCPointerData –"
---

<p>QwtCPointerData &#8211; </p>
<p> Data class containing two pointers to memory blocks of doubles.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_point_data.h&gt; </p>
<p> Inherits <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtCPointerData</code> (const double *x, const double *y, size_t <code>size</code>) </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Calculate the bounding rectangle. </i><br />
 virtual size_t <code>size</code> () const </p>
<p> virtual QPointF <code>sample</code> (size_t i) const </p>
<p> const double * <code>xData</code> () const </p>
<p> const double * <code>yData</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>Data class containing two pointers to memory blocks of doubles.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtCPointerData::QwtCPointerData (const double *x, const double *y, size_tsize)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Array of x values<br />
 <i>y</i> Array of y values<br />
 <i>size</i> Size of the x and y arrays</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The programmer must assure that the memory blocks referenced by the pointers remain valid during the lifetime of the QwtPlotCPointer object.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code>, <code>QwtPlotCurve::setRawSamples()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtCPointerData::boundingRect () const [virtual]</h3>
<p>Calculate the bounding rectangle. The bounding rectangle is calculated once by iterating over all points and is stored for all following requests. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>QPointF QwtCPointerData::sample (size_tindex) const [virtual]</h3>
<p>Return the sample at position i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at position i</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>size_t QwtCPointerData::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the data set</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>.</p>
<h3>const double * QwtCPointerData::xData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the x-values</dl>
<h3>const double * QwtCPointerData::yData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the y-values</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
