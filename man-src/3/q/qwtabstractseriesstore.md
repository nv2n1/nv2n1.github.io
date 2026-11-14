---
title: "qwtabstractseriesstore(3)"
name: "qwtabstractseriesstore"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtabstractseriesstore/"
description: "QwtAbstractSeriesStore –"
---

<p>QwtAbstractSeriesStore &#8211; </p>
<p> Bridge between <code>QwtSeriesStore</code> and <code>QwtPlotSeriesItem</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_series_store.h&gt; </p>
<p> Inherited by <code>QwtPlotSeriesItem</code> [virtual], <code>QwtSeriesStore&lt; T &gt;</code> [virtual], <code>QwtSeriesStore&lt; QPointF &gt;</code> [virtual], <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code> [virtual], <code>QwtSeriesStore&lt; QwtOHLCSample &gt;</code> [virtual], <code>QwtSeriesStore&lt; QwtPoint3D &gt;</code> [virtual], and <code>QwtSeriesStore&lt; QwtSetSample &gt;</code> [virtual].</p>
<h3>Protected Member Functions</h3>
<p>virtual <code>~QwtAbstractSeriesStore</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>dataChanged</code> ()=0<br />
 <i></i><code>dataChanged()</code> indicates, that the series has been changed.<br />
 virtual void <code>setRectOfInterest</code> (const QRectF &amp;)=0 </p>
<p> virtual QRectF <code>dataRect</code> () const =0 </p>
<p> virtual size_t <code>dataSize</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>Bridge between <code>QwtSeriesStore</code> and <code>QwtPlotSeriesItem</code>. </p>
<p> <code>QwtAbstractSeriesStore</code> is an abstract interface only to make it possible to isolate the template based methods ( <code>QwtSeriesStore</code> ) from the regular methods ( <code>QwtPlotSeriesItem</code> ) to make it possible to derive from <code>QwtPlotSeriesItem</code> without any hassle with templates.</p>
<h2>Member Function Documentation</h2>
<h3>virtual QRectF QwtAbstractSeriesStore::dataRect () const [protected], [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the stored series</dl>
<p> Implemented in <code>QwtSeriesStore&lt; T &gt;</code>, <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code>, <code>QwtSeriesStore&lt; QwtOHLCSample &gt;</code>, <code>QwtSeriesStore&lt; QPointF &gt;</code>, <code>QwtSeriesStore&lt; QwtSetSample &gt;</code>, and <code>QwtSeriesStore&lt; QwtPoint3D &gt;</code>.</p>
<h3>virtual size_t QwtAbstractSeriesStore::dataSize () const [protected], [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of samples</dl>
<p> Implemented in <code>QwtSeriesStore&lt; T &gt;</code>, <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code>, <code>QwtSeriesStore&lt; QwtOHLCSample &gt;</code>, <code>QwtSeriesStore&lt; QPointF &gt;</code>, <code>QwtSeriesStore&lt; QwtSetSample &gt;</code>, and <code>QwtSeriesStore&lt; QwtPoint3D &gt;</code>.</p>
<h3>virtual void QwtAbstractSeriesStore::setRectOfInterest (const QRectF &amp;) [protected], [pure virtual]</h3>
<p>Set a the &#8216;rectangle of interest&#8217; for the stored series </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtSeriesData&lt;T&gt;::setRectOfInterest()</code></dl>
<p> Implemented in <code>QwtSeriesStore&lt; T &gt;</code>, <code>QwtSeriesStore&lt; QwtIntervalSample &gt;</code>, <code>QwtSeriesStore&lt; QwtOHLCSample &gt;</code>, <code>QwtSeriesStore&lt; QPointF &gt;</code>, <code>QwtSeriesStore&lt; QwtSetSample &gt;</code>, and <code>QwtSeriesStore&lt; QwtPoint3D &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
