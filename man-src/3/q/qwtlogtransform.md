---
title: "qwtlogtransform(3)"
name: "qwtlogtransform"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlogtransform/"
description: "QwtLogTransform –"
---

<p>QwtLogTransform &#8211; </p>
<p> Logarithmic transformation.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_transform.h&gt; </p>
<p> Inherits <code>QwtTransform</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtLogTransform</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtLogTransform</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>transform</code> (double value) const </p>
<p> virtual double <code>invTransform</code> (double value) const </p>
<p> virtual double <code>bounded</code> (double value) const </p>
<p> virtual <code>QwtTransform</code> * <code>copy</code> () const </p>
<h3>Public Attributes</h3>
<p>QT_STATIC_CONST double <code>LogMin</code> = 1.0e-150<br />
 <i>Smallest allowed value for logarithmic scales: 1.0e-150. </i><br />
 QT_STATIC_CONST double <code>LogMax</code> = 1.0e150<br />
 <i>Largest allowed value for logarithmic scales: 1.0e150. </i></p>
<h2>Detailed Description</h2>
<p>Logarithmic transformation. </p>
<p> <code>QwtLogTransform</code> modifies the values using log() and exp(). </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>In the calculations of <code>QwtScaleMap</code> the base of the log function has no effect on the mapping. So <code>QwtLogTransform</code> can be used for log2(), log10() or any other logarithmic scale.</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtLogTransform::bounded (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be bounded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>qBound( LogMin, value, LogMax )</dl>
<p> Reimplemented from <code>QwtTransform</code>.</p>
<h3><code>QwtTransform</code> * QwtLogTransform::copy () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Clone of the transformation</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtLogTransform::invTransform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>exp( value )</dl>
<p> Implements <code>QwtTransform</code>.</p>
<h3>double QwtLogTransform::transform (doublevalue) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be transformed</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>log( value )</dl>
<p> Implements <code>QwtTransform</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
