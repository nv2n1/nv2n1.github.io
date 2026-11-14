---
title: "qwtscaletransformation(3)"
name: "qwtscaletransformation"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscaletransformation/"
description: "QwtScaleTransformation – Operations for linear or logarithmic (base 10) transformations."
---

<p>QwtScaleTransformation &#8211; Operations for linear or logarithmic (base 10) transformations. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_scale_map.h">qwt_scale_map.h</a>&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Linear</code>, <code>Log10</code>, <code>Other</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleTransformation</code> (Type type) </p>
<p> virtual <code>~QwtScaleTransformation</code> () </p>
<p> virtual double <code>xForm</code> (double x, double s1, double s2, double p1, double p2) const </p>
<p> virtual double <code>invXForm</code> (double x, double s1, double s2, double p1, double p2) const </p>
<p> Type <code>type</code> () const </p>
<p> virtual <code>QwtScaleTransformation</code> * <code>copy</code> () const </p>
<h2>Detailed Description</h2>
<p>Operations for linear or logarithmic (base 10) transformations.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleTransformation::QwtScaleTransformation (Type type)</h3>
<p>Constructor for a linear transformation. </p>
<h3>QwtScaleTransformation::~QwtScaleTransformation () [virtual]</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3><code>QwtScaleTransformation</code> * QwtScaleTransformation::copy () const [virtual]</h3>
<p>Create a clone of the transformation. </p>
<h3>double QwtScaleTransformation::invXForm (double p, double p1, double p2, double s1, double s2) const [virtual]</h3>
<p>Transform a value from a linear to a logarithmic interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> value related to the linear interval [p1, p2]<br />
 <i>p1</i> first border of linear interval<br />
 <i>p2</i> first border of linear interval<br />
 <i>s1</i> first border of logarithmic interval<br />
 <i>s2</i> first border of logarithmic interval</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>exp((x &#8211; p1) / (p2 &#8211; p1) * log(s2 / s1)) * s1; </code></p>
<dd></dl>
</dl>
<h3>Type QwtScaleTransformation::type () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Transformation type</dl>
<h3>double QwtScaleTransformation::xForm (double s, double s1, double s2, double p1, double p2) const [virtual]</h3>
<p>Transform a value between 2 linear intervals. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> value related to the interval [x1, x2]<br />
 <i>x1</i> first border of source interval<br />
 <i>x2</i> first border of source interval<br />
 <i>y1</i> first border of target interval<br />
 <i>y2</i> first border of target interval</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>linear mapping:</code></p>
<dd>y1 + (y2 &#8211; y1) / (x2 &#8211; x1) * (x &#8211; x1)</dl>
<dl COMPACT>
<dt><code>log10 mapping: </code></p>
<dd>p1 + (p2 &#8211; p1) / log(s2 / s1) * log(x / s1)</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
