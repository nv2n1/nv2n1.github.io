---
title: "quantlib_bilinearinterpolation(3)"
name: "quantlib_bilinearinterpolation"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_bilinearinterpolation/"
description: "QuantLib::BilinearInterpolation – bilinear interpolation between discrete points"
---

<p>QuantLib::BilinearInterpolation &#8211; bilinear interpolation between discrete points </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/bilinearinterpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Interpolation2D</code>. </p>
<h3>Public Member Functions</h3>
<p>template&lt;class I1 , class I2 , class M &gt; <code>BilinearInterpolation</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, const I2 &amp;yEnd, const M &amp;zData) </p>
<h2>Detailed Description</h2>
<p>bilinear interpolation between discrete points</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BilinearInterpolation</code> (const I1 &amp; xBegin, const I1 &amp; xEnd, const I2 &amp; yBegin, const I2 &amp; yEnd, const M &amp; zData)</h3>
<p><code>Precondition:</code></p>
<dl COMPACT>
<dd>the $ x $ and $ y $ values must be sorted.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
