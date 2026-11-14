---
title: "qwttransform(3)"
name: "qwttransform"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwttransform/"
description: "QwtTransform –"
---

<p>QwtTransform &#8211; </p>
<p> A transformation between coordinate systems.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_transform.h&gt; </p>
<p> Inherited by <code>QwtLogTransform</code>, <code>QwtNullTransform</code>, and <code>QwtPowerTransform</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtTransform</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtTransform</code> ()<br />
 <i>Destructor. </i><br />
 virtual double <code>bounded</code> (double value) const </p>
<p> virtual double <code>transform</code> (double value) const =0 </p>
<p> virtual double <code>invTransform</code> (double value) const =0 </p>
<p> virtual <code>QwtTransform</code> * <code>copy</code> () const =0<br />
 <i>Virtualized copy operation. </i></p>
<h2>Detailed Description</h2>
<p>A transformation between coordinate systems. </p>
<p> <code>QwtTransform</code> manipulates values, when being mapped between the scale and the paint device coordinate system. </p>
<p> A transformation consists of 2 methods: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>transform</p>
<dt>&bull;</p>
<dd>invTransform</dl>
<p> where one is is the inverse function of the other. </p>
<p> When p1, p2 are the boundaries of the paint device coordinates and s1, s2 the boundaries of the scale, <code>QwtScaleMap</code> uses the following calculations: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>p = p1 + ( p2 &#8211; p1 ) * ( T( s ) &#8211; T( s1 ) / ( T( s2 ) &#8211; T( s1 ) );</p>
<dt>&bull;</p>
<dd>s = invT ( T( s1 ) + ( T( s2 ) &#8211; T( s1 ) ) * ( p &#8211; p1 ) / ( p2 &#8211; p1 ) );</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtTransform::bounded (doublevalue) const [virtual]</h3>
<p>Modify value to be a valid value for the transformation. The default implementation does nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to be bounded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>value unmodified</dl>
<p> Reimplemented in <code>QwtLogTransform</code>.</p>
<h3>virtual double QwtTransform::invTransform (doublevalue) const [pure virtual]</h3>
<p>Inverse transformation function </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Modified value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<p> Implemented in <code>QwtPowerTransform</code>, <code>QwtLogTransform</code>, and <code>QwtNullTransform</code>.</p>
<h3>virtual double QwtTransform::transform (doublevalue) const [pure virtual]</h3>
<p>Transformation function </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Modified value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<p> Implemented in <code>QwtPowerTransform</code>, <code>QwtLogTransform</code>, and <code>QwtNullTransform</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
