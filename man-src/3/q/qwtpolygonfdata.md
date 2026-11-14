---
title: "qwtpolygonfdata(3)"
name: "qwtpolygonfdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpolygonfdata/"
description: "QwtPolygonFData – Data class containing a single QwtArray<QwtDoublePoint> object."
---

<p>QwtPolygonFData &#8211; Data class containing a single QwtArray&lt;QwtDoublePoint&gt; object. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_data.h">qwt_data.h</a>&gt; </p>
<p> Inherits <code>QwtData</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtPolygonFData</code> (const QPolygonF &amp;) </p>
<p> <code>QwtPolygonFData</code> &amp; <code>operator=</code> (const <code>QwtPolygonFData</code> &amp;) </p>
<p> virtual <code>QwtData</code> * <code>copy</code> () const </p>
<p> virtual size_t <code>size</code> () const </p>
<p> virtual double <code>x</code> (size_t i) const </p>
<p> virtual double <code>y</code> (size_t i) const </p>
<p> const QPolygonF &amp; <code>data</code> () const </p>
<h2>Detailed Description</h2>
<p>Data class containing a single QwtArray&lt;QwtDoublePoint&gt; object.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPolygonFData::QwtPolygonFData (const QPolygonF &amp; polygon)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>polygon</i> Polygon data</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code></dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtData</code> * QwtPolygonFData::copy () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to a copy (virtual copy constructor)</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>const QPolygonF &amp; QwtPolygonFData::data () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Point array</dl>
<h3><code>QwtPolygonFData</code> &amp; QwtPolygonFData::operator= (const <code>QwtPolygonFData</code> &amp; data)</h3>
<p>Assignment. </p>
<h3>size_t QwtPolygonFData::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the data set</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>double QwtPolygonFData::x (size_t i) const [virtual]</h3>
<p>Return the x value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>x X value of data point i</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>double QwtPolygonFData::y (size_t i) const [virtual]</h3>
<p>Return the y value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>y Y value of data point i</dl>
<p> Implements <code>QwtData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
