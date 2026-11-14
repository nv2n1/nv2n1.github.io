---
title: "qwtintervaldata(3)"
name: "qwtintervaldata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtintervaldata/"
description: "QwtIntervalData – Series of samples of a value and an interval."
---

<p>QwtIntervalData &#8211; Series of samples of a value and an interval. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_interval_data.h">qwt_interval_data.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>QwtIntervalData</code> () </p>
<p> <code>QwtIntervalData</code> (const QwtArray&lt; <code>QwtDoubleInterval</code> &gt; &amp;, const QwtArray&lt; double &gt; &amp;) </p>
<p> <code>~QwtIntervalData</code> () </p>
<p> void <code>setData</code> (const QwtArray&lt; <code>QwtDoubleInterval</code> &gt; &amp;, const QwtArray&lt; double &gt; &amp;) </p>
<p> size_t <code>size</code> () const </p>
<p> const <code>QwtDoubleInterval</code> &amp; <code>interval</code> (size_t i) const </p>
<p> double <code>value</code> (size_t i) const </p>
<p> QwtDoubleRect <code>boundingRect</code> () const </p>
<h2>Detailed Description</h2>
<p>Series of samples of a value and an interval. </p>
<p> <code>QwtIntervalData</code> is a series of samples of a value and an interval. F.e. error bars are built from samples [x, y1-y2], while a histogram might consist of [x1-x2, y] samples.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtIntervalData::QwtIntervalData ()</h3>
<p>Constructor. </p>
<h3>QwtIntervalData::QwtIntervalData (const QwtArray&lt; <code>QwtDoubleInterval</code> &gt; &amp; intervals, const QwtArray&lt; double &gt; &amp; values)</h3>
<p>Constructor. </p>
<h3>QwtIntervalData::~QwtIntervalData ()</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3>QwtDoubleRect QwtIntervalData::boundingRect () const</h3>
<p>Calculate the bounding rectangle of the samples </p>
<p> The x coordinates of the rectangle are built from the intervals, the y coordinates from the values. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<h3>const <code>QwtDoubleInterval</code> &amp; QwtIntervalData::interval (size_t i) const [inline]</h3>
<p>Interval of a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Sample index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>value()</code>, <code>size()</code></dl>
<h3>void QwtIntervalData::setData (const QwtArray&lt; <code>QwtDoubleInterval</code> &gt; &amp; intervals, const QwtArray&lt; double &gt; &amp; values)</h3>
<p>Assign samples. </p>
<h3>size_t QwtIntervalData::size () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of samples</dl>
<h3>double QwtIntervalData::value (size_t i) const [inline]</h3>
<p>Value of a sample </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Sample index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Value</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>interval()</code>, <code>size()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
