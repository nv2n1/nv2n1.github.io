---
title: "argument_type(3)"
name: "argument_type"
section: "3"
letter: "a"
url: "/docs/linux/man/3-argument_type/"
description: "QuantLib::Interpolation – base class for 1-D interpolations."
---

<h2 class="name">NAME</h2>
<p> QuantLib::Interpolation &#8211; base class for 1-D interpolations. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/interpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Extrapolator</code>. </p>
<p> Inherited by <code>BackwardFlatInterpolation</code>, <code>ConvexMonotoneInterpolation&lt; I1, I2 &gt;</code>, <code>CubicInterpolation</code>, <code>ForwardFlatInterpolation</code>, <code>LinearInterpolation</code>, <code>LogCubicInterpolation</code>, <code>LogLinearInterpolation</code>, and <code>SABRInterpolation</code>. </p>
<h3>Classes</h3>
<p> class <code>Impl</code><br />
 <i>abstract base class for interpolation implementations </i><br />
 class <code>templateImpl</code><br />
 <i>basic template implementation </i></p>
<h3>Public Types</h3>
<p> typedef <code>Real</code> <code>argument_type</code> </p>
<p> typedef <code>Real</code> <code>result_type</code> </p>
<h3>Public Member Functions</h3>
<p> bool <code>empty</code> () const </p>
<p> <code>Real</code> <code>operator()</code> (<code>Real</code> x, bool allowExtrapolation=false) const </p>
<p> <code>Real</code> <code>primitive</code> (<code>Real</code> x, bool allowExtrapolation=false) const </p>
<p> <code>Real</code> <code>derivative</code> (<code>Real</code> x, bool allowExtrapolation=false) const </p>
<p> <code>Real</code> <code>secondDerivative</code> (<code>Real</code> x, bool allowExtrapolation=false) const </p>
<p> <code>Real</code> <code>xMin</code> () const </p>
<p> <code>Real</code> <code>xMax</code> () const </p>
<p> bool <code>isInRange</code> (<code>Real</code> x) const </p>
<p> void <code>update</code> () </p>
<h3>Protected Member Functions</h3>
<p> void <code>checkRange</code> (<code>Real</code> x, bool extrapolate) const </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<h2>Detailed Description</h2>
<p> base class for 1-D interpolations. </p>
<p> Classes derived from this class will provide interpolated values from two sequences of equal length, representing discretized values of a variable and a function of the former, respectively. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
