---
title: "qwtnulltransform(3)"
name: "qwtnulltransform"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtnulltransform/"
description: "QwtNullTransform –"
---

<p>QwtNullTransform &#8211; </p>
<p> Null transformation.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_transform.h&gt; </p>
<p> Inherits <code>QwtTransform</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtNullTransform</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtNullTransform</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>transform</code> (double value) const </p>
<p> virtual double <code>invTransform</code> (double value) const </p>
<p> virtual <code>QwtTransform</code> * <code>copy</code> () const </p>
<h2>Detailed Description</h2>
<p>Null transformation. </p>
<p> <code>QwtNullTransform</code> returns the values unmodified.</p>
<h2>Member Function Documentation</h2>
<h3><code>QwtTransform</code> * QwtNullTransform::copy () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Clone of the transformation</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtNullTransform::invTransform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>value unmodified</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtNullTransform::transform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>value unmodified</dl>
<p> Implements <code>QwtTransform</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
