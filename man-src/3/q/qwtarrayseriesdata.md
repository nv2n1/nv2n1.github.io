---
title: "qwtarrayseriesdata(3)"
name: "qwtarrayseriesdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtarrayseriesdata/"
description: "QwtArraySeriesData< T > –"
---

<p>QwtArraySeriesData&lt; T &gt; &#8211; </p>
<p> Template class for data, that is organized as QVector.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_series_data.h&gt; </p>
<p> Inherits <code>QwtSeriesData&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtArraySeriesData</code> ()<br />
 <i>Constructor. </i><br />
 <code>QwtArraySeriesData</code> (const QVector&lt; T &gt; &amp;<code>samples</code>) </p>
<p> void <code>setSamples</code> (const QVector&lt; T &gt; &amp;<code>samples</code>) </p>
<p> const QVector&lt; T &gt; <code>samples</code> () const </p>
<p> virtual size_t <code>size</code> () const </p>
<p> virtual T <code>sample</code> (size_t index) const </p>
<h3>Protected Attributes</h3>
<p>QVector&lt; T &gt; <code>d_samples</code><br />
 <i>Vector of samples. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename T&gt;class QwtArraySeriesData&lt; T &gt;</h3>
<p>Template class for data, that is organized as QVector. </p>
<p> QVector uses implicit data sharing and can be passed around as argument efficiently.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;typename T&gt; <code>QwtArraySeriesData</code>&lt; T &gt;::<code>QwtArraySeriesData</code> (const QVector&lt; T &gt; &amp;samples)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Array of samples</dl>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename T &gt; T <code>QwtArraySeriesData</code>&lt; T &gt;::sample (size_tindex) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at a specific position</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Sample at position index</dl>
<p> Implements <code>QwtSeriesData&lt; T &gt;</code>.</p>
<h3>template&lt;typename T &gt; const QVector&lt; T &gt; <code>QwtArraySeriesData</code>&lt; T &gt;::samples () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of samples</dl>
<h3>template&lt;typename T&gt; void <code>QwtArraySeriesData</code>&lt; T &gt;::setSamples (const QVector&lt; T &gt; &amp;samples)</h3>
<p>Assign an array of samples </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Array of samples</dl>
<h3>template&lt;typename T &gt; size_t <code>QwtArraySeriesData</code>&lt; T &gt;::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of samples</dl>
<p> Implements <code>QwtSeriesData&lt; T &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
