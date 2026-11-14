---
title: "qwtpointseriesdata(3)"
name: "qwtpointseriesdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpointseriesdata/"
description: "QwtPointSeriesData –"
---

<p>QwtPointSeriesData &#8211; </p>
<p> Interface for iterating over an array of points.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_series_data.h&gt; </p>
<p> Inherits <code>QwtArraySeriesData&lt; QPointF &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPointSeriesData</code> (const QVector&lt; QPointF &gt; &amp;=QVector&lt; QPointF &gt;()) </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Calculate the bounding rectangle. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>Interface for iterating over an array of points.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPointSeriesData::QwtPointSeriesData (const QVector&lt; QPointF &gt; &amp;samples = QVector&lt;QPointF&gt;())</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Samples</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPointSeriesData::boundingRect () const [virtual]</h3>
<p>Calculate the bounding rectangle. The bounding rectangle is calculated once by iterating over all points and is stored for all following requests. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> Implements <code>QwtSeriesData&lt; QPointF &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
