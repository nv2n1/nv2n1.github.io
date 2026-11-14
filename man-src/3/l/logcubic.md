---
title: "logcubic(3)"
name: "logcubic"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logcubic/"
description: "QuantLib::LogCubic – log-cubic interpolation factory and traits"
---

<p>QuantLib::LogCubic &#8211; log-cubic interpolation factory and traits </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/loginterpolation.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>LogCubic</code> (<code>CubicInterpolation::DerivativeApprox</code> da, bool monotonic=true, <code>CubicInterpolation::BoundaryCondition</code> leftCondition=CubicInterpolation::SecondDerivative, <code>Real</code> leftConditionValue=0.0, <code>CubicInterpolation::BoundaryCondition</code> rightCondition=CubicInterpolation::SecondDerivative, <code>Real</code> rightConditionValue=0.0) </p>
<p> template&lt;class I1 , class I2 &gt; <code>Interpolation</code> <code>interpolate</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin) const </p>
<h3>Static Public Attributes</h3>
<p>static const bool <code>global</code> = true </p>
<p> static const Size <code>requiredPoints</code> = 2 </p>
<h2>Detailed Description</h2>
<p>log-cubic interpolation factory and traits </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
