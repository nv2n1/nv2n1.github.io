---
title: "qwtpowertransform(3)"
name: "qwtpowertransform"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpowertransform/"
description: "QwtPowerTransform –"
---

<p>QwtPowerTransform &#8211; </p>
<p> A transformation using pow()</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_transform.h&gt; </p>
<p> Inherits <code>QwtTransform</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPowerTransform</code> (double exponent) </p>
<p> virtual <code>~QwtPowerTransform</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>transform</code> (double value) const </p>
<p> virtual double <code>invTransform</code> (double value) const </p>
<p> virtual <code>QwtTransform</code> * <code>copy</code> () const </p>
<h2>Detailed Description</h2>
<p>A transformation using pow() </p>
<p> <code>QwtPowerTransform</code> preserves the sign of a value. F.e. a transformation with a factor of 2 transforms a value of -3 to -9 and v.v. Thus <code>QwtPowerTransform</code> can be used for scales including negative values.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPowerTransform::QwtPowerTransform (doubleexponent)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exponent</i> Exponent</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtTransform</code> * QwtPowerTransform::copy () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Clone of the transformation</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtPowerTransform::invTransform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Inverse exponentiation preserving the sign</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtPowerTransform::transform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Exponentiation preserving the sign</dl>
<p> Implements <code>QwtTransform</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
