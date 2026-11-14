---
title: "qwtarraydata(3)"
name: "qwtarraydata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtarraydata/"
description: "QwtArrayData – Data class containing two QwtArray<double> objects."
---

<p>QwtArrayData &#8211; Data class containing two QwtArray&lt;double&gt; objects. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_data.h">qwt_data.h</a>&gt; </p>
<p> Inherits <code>QwtData</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtArrayData</code> (const QwtArray&lt; double &gt; &amp;x, const QwtArray&lt; double &gt; &amp;y) </p>
<p> <code>QwtArrayData</code> (const double *x, const double *y, size_t size) </p>
<p> <code>QwtArrayData</code> &amp; <code>operator=</code> (const <code>QwtArrayData</code> &amp;) </p>
<p> virtual <code>QwtData</code> * <code>copy</code> () const </p>
<p> virtual size_t <code>size</code> () const </p>
<p> virtual double <code>x</code> (size_t i) const </p>
<p> virtual double <code>y</code> (size_t i) const </p>
<p> const QwtArray&lt; double &gt; &amp; <code>xData</code> () const </p>
<p> const QwtArray&lt; double &gt; &amp; <code>yData</code> () const </p>
<p> virtual QwtDoubleRect <code>boundingRect</code> () const </p>
<h2>Detailed Description</h2>
<p>Data class containing two QwtArray&lt;double&gt; objects.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtArrayData::QwtArrayData (const QwtArray&lt; double &gt; &amp; x, const QwtArray&lt; double &gt; &amp; y)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Array of x values<br />
 <i>y</i> Array of y values</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code></dl>
<h3>QwtArrayData::QwtArrayData (const double * x, const double * y, size_t size)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> Array of x values<br />
 <i>y</i> Array of y values<br />
 <i>size</i> Size of the x and y arrays</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCurve::setData()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QwtDoubleRect QwtArrayData::boundingRect () const [virtual]</h3>
<p>Returns the bounding rectangle of the data. If there is no bounding rect, like for empty data the rectangle is invalid: QwtDoubleRect::isValid() == false </p>
<p> Reimplemented from <code>QwtData</code>.</p>
<h3><code>QwtData</code> * QwtArrayData::copy () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to a copy (virtual copy constructor)</dl>
<p> Implements <code>QwtData</code>.</p>
<h3><code>QwtArrayData</code> &amp; QwtArrayData::operator= (const <code>QwtArrayData</code> &amp; data)</h3>
<p>Assignment. </p>
<h3>size_t QwtArrayData::size () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the data set</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>double QwtArrayData::x (size_t i) const [virtual]</h3>
<p>Return the x value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>x X value of data point i</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>const QwtArray&lt; double &gt; &amp; QwtArrayData::xData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the x-values</dl>
<h3>double QwtArrayData::y (size_t i) const [virtual]</h3>
<p>Return the y value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>y Y value of data point i</dl>
<p> Implements <code>QwtData</code>.</p>
<h3>const QwtArray&lt; double &gt; &amp; QwtArrayData::yData () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Array of the y-values</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
