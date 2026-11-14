---
title: "result_type(3)"
name: "result_type"
section: "3"
letter: "r"
url: "/docs/linux/man/3-result_type/"
description: "QuantLib::Interpolation – base class for 1-D interpolations."
---

<p>QuantLib::Interpolation &#8211; base class for 1-D interpolations. </p>
<h2>Synopsis</h2>
<pre><code>bool empty () const



Real operator() (Real x, bool allowExtrapolation=false) const



Real primitive (Real x, bool allowExtrapolation=false) const



Real derivative (Real x, bool allowExtrapolation=false) const



Real secondDerivative (Real x, bool allowExtrapolation=false) const



Real xMin () const



Real xMax () const



bool isInRange (Real x) const



void update ()



Protected Member Functions
void checkRange (Real x, bool extrapolate) const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Extrapolator</code>. Inherited by <code>BackwardFlatInterpolation</code>, <code>ConvexMonotoneInterpolation&lt; I1, I2 &gt;</code>, <code>CubicInterpolation</code>, <code>ForwardFlatInterpolation</code>, <code>LinearInterpolation</code>, <code>LogCubicInterpolation</code>, <code>LogLinearInterpolation</code>, and <code>SABRInterpolation</code>.</p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>abstract base class for interpolation implementations </i><br />
 class <code>templateImpl</code><br />
 <i>basic template implementation </i></p>
<h3>Public Types</h3>
<p>typedef <code>Real</code> <code>argument_type</code> </p>
<p> typedef <code>Real</code> <code>result_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>bool empty () const



Real operator() (Real x, bool allowExtrapolation=false) const



Real primitive (Real x, bool allowExtrapolation=false) const



Real derivative (Real x, bool allowExtrapolation=false) const



Real secondDerivative (Real x, bool allowExtrapolation=false) const



Real xMin () const



Real xMax () const



bool isInRange (Real x) const



void update ()



Protected Member Functions
void checkRange (Real x, bool extrapolate) const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code></p>
<h2>Detailed Description</h2>
<p>base class for 1-D interpolations. </p>
<p> Classes derived from this class will provide interpolated values from two sequences of equal length, representing discretized values of a variable and a function of the former, respectively.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
