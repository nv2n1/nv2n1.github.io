---
title: "quantlib_cubic(3)"
name: "quantlib_cubic"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cubic/"
description: "QuantLib::Cubic – Cubic interpolation factory and traits"
---

<p>QuantLib::Cubic &#8211; Cubic interpolation factory and traits </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/cubicinterpolation.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Cubic</code> (<code>CubicInterpolation::DerivativeApprox</code> da=CubicInterpolation::Kruger, bool monotonic=false, <code>CubicInterpolation::BoundaryCondition</code> leftCondition=CubicInterpolation::SecondDerivative, <code>Real</code> leftConditionValue=0.0, <code>CubicInterpolation::BoundaryCondition</code> rightCondition=CubicInterpolation::SecondDerivative, <code>Real</code> rightConditionValue=0.0) </p>
<p> template&lt;class I1 , class I2 &gt; <code>Interpolation</code> <code>interpolate</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin) const </p>
<h3>Static Public Attributes</h3>
<p>static const bool <code>global</code> = true </p>
<p> static const Size <code>requiredPoints</code> = 2 </p>
<h2>Detailed Description</h2>
<p>Cubic interpolation factory and traits </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
