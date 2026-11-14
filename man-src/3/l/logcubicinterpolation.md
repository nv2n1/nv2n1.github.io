---
title: "logcubicinterpolation(3)"
name: "logcubicinterpolation"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logcubicinterpolation/"
description: "QuantLib::LogCubicInterpolation – log-cubic interpolation between discrete points"
---

<p>QuantLib::LogCubicInterpolation &#8211; log-cubic interpolation between discrete points </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/loginterpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Interpolation</code>. </p>
<h3>Public Member Functions</h3>
<p>template&lt;class I1 , class I2 &gt; <code>LogCubicInterpolation</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, <code>CubicInterpolation::DerivativeApprox</code> da, bool monotonic, <code>CubicInterpolation::BoundaryCondition</code> leftC, <code>Real</code> leftConditionValue, <code>CubicInterpolation::BoundaryCondition</code> rightC, <code>Real</code> rightConditionValue) </p>
<h2>Detailed Description</h2>
<p>log-cubic interpolation between discrete points</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>LogCubicInterpolation</code> (const I1 &amp; xBegin, const I1 &amp; xEnd, const I2 &amp; yBegin, <code>CubicInterpolation::DerivativeApprox</code> da, bool monotonic, <code>CubicInterpolation::BoundaryCondition</code> leftC, <code>Real</code> leftConditionValue, <code>CubicInterpolation::BoundaryCondition</code> rightC, <code>Real</code> rightConditionValue)</h3>
<p><code>Precondition:</code></p>
<dl COMPACT>
<dd>the $ x $ values must be sorted.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
