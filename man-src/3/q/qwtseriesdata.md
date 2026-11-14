---
title: "qwtseriesdata(3)"
name: "qwtseriesdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtseriesdata/"
description: "QwtSeriesData< T > –"
---

<p>QwtSeriesData&lt; T &gt; &#8211; </p>
<p> Abstract interface for iterating over samples.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_series_data.h&gt; </p>
<p> Inherited by <code>QwtArraySeriesData&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtSeriesData</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtSeriesData</code> ()<br />
 <i>Destructor. </i><br />
 virtual size_t <code>size</code> () const =0 </p>
<p> virtual T <code>sample</code> (size_t i) const =0 </p>
<p> virtual QRectF <code>boundingRect</code> () const =0 </p>
<p> virtual void <code>setRectOfInterest</code> (const QRectF &amp;rect) </p>
<h3>Protected Attributes</h3>
<p>QRectF <code>d_boundingRect</code><br />
 <i>Can be used to cache a calculated bounding rectangle. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename T&gt;class QwtSeriesData&lt; T &gt;</h3>
<p>Abstract interface for iterating over samples. </p>
<p> Qwt offers several implementations of the <code>QwtSeriesData</code> API, but in situations, where data of an application specific format needs to be displayed, without having to copy it, it is recommended to implement an individual data access. </p>
<p> A subclass of <code>QwtSeriesData&lt;QPointF&gt;</code> must implement: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>size()</code> </p>
<p>&nbsp;<wbr>Should return number of data points.</p>
<dt>&bull;</p>
<dd><code>sample()</code> </p>
<p>&nbsp;<wbr>Should return values x and y values of the sample at specific position as QPointF object.</p>
<dt>&bull;</p>
<dd><code>boundingRect()</code> </p>
<p>&nbsp;<wbr>Should return the bounding rectangle of the data series. It is used for autoscaling and might help certain algorithms for displaying the data. You can use qwtBoundingRect()&nbsp;<wbr>for an implementation but often it is possible to implement a more efficient algorithm depending on the characteristics of the series. The member d_boundingRect is intended for caching the calculated rectangle.&nbsp;<wbr></dl>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename T&gt; virtual QRectF <code>QwtSeriesData</code>&lt; T &gt;::boundingRect () const [pure virtual]</h3>
<p>Calculate the bounding rect of all samples </p>
<p> The bounding rect is necessary for autoscaling and can be used for a couple of painting optimizations. </p>
<p> qwtBoundingRect(&#8230;) offers slow implementations iterating over the samples. For large sets it is recommended to implement something faster f.e. by caching the bounding rectangle. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<p> Implemented in <code>QwtTradingChartData</code>, <code>QwtSetSeriesData</code>, <code>QwtIntervalSeriesData</code>, <code>QwtPoint3DSeriesData</code>, <code>QwtPointSeriesData</code>, <code>QwtSyntheticPointData</code>, <code>QwtCPointerData</code>, and <code>QwtPointArrayData</code>.</p>
<h3>template&lt;typename T&gt; virtual T <code>QwtSeriesData</code>&lt; T &gt;::sample (size_ti) const [pure virtual]</h3>
<p>Return a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at position i</dl>
<p> Implemented in <code>QwtArraySeriesData&lt; T &gt;</code>, <code>QwtArraySeriesData&lt; QwtIntervalSample &gt;</code>, <code>QwtArraySeriesData&lt; QwtOHLCSample &gt;</code>, <code>QwtArraySeriesData&lt; QPointF &gt;</code>, <code>QwtArraySeriesData&lt; QwtPoint3D &gt;</code>, <code>QwtArraySeriesData&lt; QwtSetSample &gt;</code>, <code>QwtSyntheticPointData</code>, <code>QwtCPointerData</code>, and <code>QwtPointArrayData</code>.</p>
<h3>template&lt;typename T &gt; void <code>QwtSeriesData</code>&lt; T &gt;::setRectOfInterest (const QRectF &amp;rect) [virtual]</h3>
<p>Set a the &#8216;rect of interest&#8217; </p>
<p> <code>QwtPlotSeriesItem</code> defines the current area of the plot canvas as &#8216;rectangle of interest&#8217; ( <code>QwtPlotSeriesItem::updateScaleDiv()</code> ). It can be used to implement different levels of details. </p>
<p> The default implementation does nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle of interest</dl>
<p> Reimplemented in <code>QwtSyntheticPointData</code>.</p>
<h3>template&lt;typename T&gt; virtual size_t <code>QwtSeriesData</code>&lt; T &gt;::size () const [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of samples</dl>
<p> Implemented in <code>QwtArraySeriesData&lt; T &gt;</code>, <code>QwtArraySeriesData&lt; QwtIntervalSample &gt;</code>, <code>QwtArraySeriesData&lt; QwtOHLCSample &gt;</code>, <code>QwtArraySeriesData&lt; QPointF &gt;</code>, <code>QwtArraySeriesData&lt; QwtPoint3D &gt;</code>, <code>QwtArraySeriesData&lt; QwtSetSample &gt;</code>, <code>QwtSyntheticPointData</code>, <code>QwtCPointerData</code>, and <code>QwtPointArrayData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
