---
title: "qwtdata(3)"
name: "qwtdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdata/"
description: "QwtData – QwtData defines an interface to any type of curve data."
---

<p>QwtData &#8211; <code>QwtData</code> defines an interface to any type of curve data. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_data.h">qwt_data.h</a>&gt; </p>
<p> Inherited by <code>QwtArrayData</code>, <code>QwtCPointerData</code>, and <code>QwtPolygonFData</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtData</code> () </p>
<p> virtual <code>~QwtData</code> () </p>
<p> virtual <code>QwtData</code> * <code>copy</code> () const =0 </p>
<p> virtual size_t <code>size</code> () const =0 </p>
<p> virtual double <code>x</code> (size_t i) const =0 </p>
<p> virtual double <code>y</code> (size_t i) const =0 </p>
<p> virtual QwtDoubleRect <code>boundingRect</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>QwtData</code> &amp; <code>operator=</code> (const <code>QwtData</code> &amp;) </p>
<h2>Detailed Description</h2>
<p><code>QwtData</code> defines an interface to any type of curve data. </p>
<p> Classes, derived from <code>QwtData</code> may:</p>
<dl COMPACT>
<dt>*</p>
<dd>store the data in almost any type of container</p>
<dt>*</p>
<dd>calculate the data on the fly instead of storing it</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtData::QwtData ()</h3>
<p>Constructor. </p>
<h3>QwtData::~QwtData () [virtual]</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3>QwtDoubleRect QwtData::boundingRect () const [virtual]</h3>
<p>Returns the bounding rectangle of the data. If there is no bounding rect, like for empty data the rectangle is invalid: QwtDoubleRect::isValid() == false </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>This is an slow implementation iterating over all points. It is intended to be overloaded by derived classes. In case of auto scaling <code>boundingRect()</code> is called for every replot, so it might be worth to implement a cache, or use x(0), x(<code>size()</code> &#8211; 1) for ordered data &#8230;</dl>
<p> Reimplemented in <code>QwtArrayData</code>, and <code>QwtCPointerData</code>.</p>
<h3>virtual <code>QwtData</code>* QwtData::copy () const [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pointer to a copy (virtual copy constructor)</dl>
<p> Implemented in <code>QwtPolygonFData</code>, <code>QwtArrayData</code>, and <code>QwtCPointerData</code>.</p>
<h3><code>QwtData</code>&amp; QwtData::operator= (const <code>QwtData</code> &amp;) [protected]</h3>
<p>Assignment operator (virtualized)</p>
<h3>virtual size_t QwtData::size () const [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the data set</dl>
<p> Implemented in <code>QwtPolygonFData</code>, <code>QwtArrayData</code>, and <code>QwtCPointerData</code>.</p>
<h3>virtual double QwtData::x (size_t i) const [pure virtual]</h3>
<p>Return the x value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>x X value of data point i</dl>
<p> Implemented in <code>QwtPolygonFData</code>, <code>QwtArrayData</code>, and <code>QwtCPointerData</code>.</p>
<h3>virtual double QwtData::y (size_t i) const [pure virtual]</h3>
<p>Return the y value of data point i </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>i</i> Index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>y Y value of data point i</dl>
<p> Implemented in <code>QwtPolygonFData</code>, <code>QwtArrayData</code>, and <code>QwtCPointerData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
