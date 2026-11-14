---
title: "qwtseriesstore(3)"
name: "qwtseriesstore"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtseriesstore/"
description: "QwtSeriesStore< T > –"
---

<p>QwtSeriesStore&lt; T &gt; &#8211; </p>
<p> Class storing a <code>QwtSeriesData</code> object.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_series_store.h&gt; </p>
<p> Inherits <code>QwtAbstractSeriesStore</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtSeriesStore</code> ()<br />
 <i>Constructor The store contains no series. </i><br />
 <code>~QwtSeriesStore</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setData</code> (<code>QwtSeriesData</code>&lt; T &gt; *series) </p>
<p> <code>QwtSeriesData</code>&lt; T &gt; * <code>data</code> () </p>
<p> const <code>QwtSeriesData</code>&lt; T &gt; * <code>data</code> () const </p>
<p> T <code>sample</code> (int index) const </p>
<p> virtual size_t <code>dataSize</code> () const </p>
<p> virtual QRectF <code>dataRect</code> () const </p>
<p> virtual void <code>setRectOfInterest</code> (const QRectF &amp;rect) </p>
<p> <code>QwtSeriesData</code>&lt; T &gt; * <code>swapData</code> (<code>QwtSeriesData</code>&lt; T &gt; *series) </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<h3>template&lt;typename T&gt;class QwtSeriesStore&lt; T &gt;</h3>
<p>Class storing a <code>QwtSeriesData</code> object. </p>
<p> <code>QwtSeriesStore</code> and <code>QwtPlotSeriesItem</code> are intended as base classes for all plot items iterating over a series of samples. Both classes share a virtual base class ( <code>QwtAbstractSeriesStore</code> ) to bridge between them. </p>
<p> <code>QwtSeriesStore</code> offers the template based part for the plot item API, so that <code>QwtPlotSeriesItem</code> can be derived without any hassle with templates.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename T &gt; <code>QwtSeriesData</code>&lt; T &gt; * <code>QwtSeriesStore</code>&lt; T &gt;::data () [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the the series data</dl>
<h3>template&lt;typename T &gt; const <code>QwtSeriesData</code>&lt; T &gt; * <code>QwtSeriesStore</code>&lt; T &gt;::data () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the the series data</dl>
<h3>template&lt;typename T &gt; QRectF <code>QwtSeriesStore</code>&lt; T &gt;::dataRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the series or an invalid rectangle, when no series is stored</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtSeriesData&lt;T&gt;::boundingRect()</code></dl>
<p> Implements <code>QwtAbstractSeriesStore</code>.</p>
<h3>template&lt;typename T &gt; size_t <code>QwtSeriesStore</code>&lt; T &gt;::dataSize () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of samples of the series</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setData()</code>, <code>QwtSeriesData&lt;T&gt;::size()</code></dl>
<p> Implements <code>QwtAbstractSeriesStore</code>.</p>
<h3>template&lt;typename T &gt; T <code>QwtSeriesStore</code>&lt; T &gt;::sample (intindex) const [inline]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at position index</dl>
<h3>template&lt;typename T&gt; void <code>QwtSeriesStore</code>&lt; T &gt;::setData (<code>QwtSeriesData</code>&lt; T &gt; *series)</h3>
<p>Assign a series of samples </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>series</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>template&lt;typename T &gt; void <code>QwtSeriesStore</code>&lt; T &gt;::setRectOfInterest (const QRectF &amp;rect) [virtual]</h3>
<p>Set a the &#8216;rect of interest&#8217; for the series </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle of interest</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtSeriesData&lt;T&gt;::setRectOfInterest()</code></dl>
<p> Implements <code>QwtAbstractSeriesStore</code>.</p>
<h3>template&lt;typename T&gt; <code>QwtSeriesData</code>&lt; T &gt; * <code>QwtSeriesStore</code>&lt; T &gt;::swapData (<code>QwtSeriesData</code>&lt; T &gt; *series)</h3>
<p>Replace a series without deleting the previous one </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>series</i> New series</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Previously assigned series</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
