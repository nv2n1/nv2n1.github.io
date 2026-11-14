---
title: "quantlib_cubicinterpolation(3)"
name: "quantlib_cubicinterpolation"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cubicinterpolation/"
description: "QuantLib::CubicInterpolation – Cubic interpolation between discrete points."
---

<p>QuantLib::CubicInterpolation &#8211; Cubic interpolation between discrete points. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/cubicinterpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Interpolation</code>. </p>
<p> Inherited by MonotonicNaturalCubicInterpolation, and NaturalCubicInterpolation. </p>
<h3>Public Types</h3>
<p>enum <code>DerivativeApprox</code> { <code>Spline</code>, <code>FourthOrder</code>, <code>Parabolic</code>, <code>ModifiedParabolic</code>, <code>FritschButland</code>, <code>Akima</code>, <code>Kruger</code> } </p>
<p> enum <code>BoundaryCondition</code> { <code>NotAKnot</code>, <code>FirstDerivative</code>, <code>SecondDerivative</code>, <code>Periodic</code>, <code>Lagrange</code> } </p>
<h3>Public Member Functions</h3>
<p>template&lt;class I1 , class I2 &gt; <code>CubicInterpolation</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, <code>CubicInterpolation::DerivativeApprox</code> da, bool monotonic, <code>CubicInterpolation::BoundaryCondition</code> leftCond, <code>Real</code> leftConditionValue, <code>CubicInterpolation::BoundaryCondition</code> rightCond, <code>Real</code> rightConditionValue) </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>primitiveConstants</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>aCoefficients</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>bCoefficients</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>cCoefficients</code> () const </p>
<p> const std::vector&lt; bool &gt; &amp; <code>monotonicityAdjustments</code> () const </p>
<h2>Detailed Description</h2>
<p>Cubic interpolation between discrete points. </p>
<p> <code>Cubic</code> interpolation is fully defined when the ${f_i}$ function values at points ${x_i}$ are supplemented with ${f_i}$ function derivative values. </p>
<p> Different type of first derivative approximations are implemented, both local and non-local. Local schemes (Fourth-order, Parabolic, Modified Parabolic, Fritsch-Butland, Akima, Kruger) use only $f$ values near $x_i$ to calculate $f_i$. Non-local schemes (Spline with different boundary conditions) use all ${f_i}$ values and obtain ${f_i}$ by solving a linear system of equations. Local schemes produce $C^1$ interpolants, while the spline scheme generates $C^2$ interpolants. </p>
<p> Hyman&#8217;s monotonicity constraint filter is also implemented: it can be applied to all schemes to ensure that in the regions of local monotoniticity of the input (three successive increasing or decreasing values) the interpolating cubic remains monotonic. If the interpolating cubic is already monotonic, the Hyman filter leaves it unchanged preserving all its original features. </p>
<p> In the case of $C^2$ interpolants the Hyman filter ensures local monotonicity at the expense of the second derivative of the interpolant which will no longer be continuous in the points where the filter has been applied. </p>
<p> While some non-linear schemes (Modified Parabolic, Fritsch-Butland, Kruger) are guaranteed to be locally monotone in their original approximation, all other schemes must be filtered according to the Hyman criteria at the expense of their linearity. </p>
<p> See R. L. Dougherty, A. Edelman, and J. M. Hyman, &#8216;Nonnegativity-, Monotonicity-, or Convexity-Preserving CubicSpline and Quintic Hermite Interpolation&#8217; Mathematics Of Computation, v. 52, n. 186, April 1989, pp. 471-494. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>implement missing schemes (FourthOrder and ModifiedParabolic) and missing boundary conditions (Periodic and Lagrange).</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>to be adapted from old ones.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>DerivativeApprox</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Spline </i></p>
<dd>Spline approximation (non-local, non-monotone, linear[?]). Different boundary conditions can be used on the left and right boundaries: see <code>BoundaryCondition</code>.</p>
<dt><i>FourthOrder </i></p>
<dd>Fourth-order approximation (local, non-monotone, linear).</p>
<dt><i>Parabolic </i></p>
<dd>Parabolic approximation (local, non-monotone, linear).</p>
<dt><i>ModifiedParabolic </i></p>
<dd>Modified-Parabolic approximation (local, monotone, non-linear).</p>
<dt><i>FritschButland </i></p>
<dd>Fritsch-Butland approximation (local, monotone, non-linear).</p>
<dt><i>Akima </i></p>
<dd>Akima approximation (local, non-monotone, non-linear).</p>
<dt><i>Kruger </i></p>
<dd>Kruger approximation (local, monotone, non-linear).</dl>
<h3>enum <code>BoundaryCondition</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>NotAKnot </i></p>
<dd>Make second(-last) point an inactive knot.</p>
<dt><i>FirstDerivative </i></p>
<dd>Match value of end-slope.</p>
<dt><i>SecondDerivative </i></p>
<dd>Match value of second derivative at end.</p>
<dt><i>Periodic </i></p>
<dd>Match first and second derivative at either end.</p>
<dt><i>Lagrange </i></p>
<dd>Match end-slope to the slope of the cubic that matches the first four data at the respective end</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CubicInterpolation</code> (const I1 &amp; xBegin, const I1 &amp; xEnd, const I2 &amp; yBegin, <code>CubicInterpolation::DerivativeApprox</code> da, bool monotonic, <code>CubicInterpolation::BoundaryCondition</code> leftCond, <code>Real</code> leftConditionValue, <code>CubicInterpolation::BoundaryCondition</code> rightCond, <code>Real</code> rightConditionValue)</h3>
<p><code>Precondition:</code></p>
<dl COMPACT>
<dd>the $ x $ values must be sorted.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
