---
title: "quantlib_exponentialsplinesfitting(3)"
name: "quantlib_exponentialsplinesfitting"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_exponentialsplinesfitting/"
description: "QuantLib::ExponentialSplinesFitting – Exponential-splines fitting method."
---

<p>QuantLib::ExponentialSplinesFitting &#8211; Exponential-splines fitting method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/nonlinearfittingmethods.hpp&gt; </p>
<p> Inherits <code>QuantLib::FittedBondDiscountCurve::FittingMethod</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExponentialSplinesFitting</code> (bool constrainAtZero=true) </p>
<p> std::auto_ptr&lt; <code>FittedBondDiscountCurve::FittingMethod</code> &gt; <code>clone</code> () const<br/>
 <i>clone of the current object </i></p>
<h2>Detailed Description</h2>
<p>Exponential-splines fitting method. </p>
<p> Fits a discount function to the exponential form [ d(t) = um_{i=1}^9 c_i \xp^{-kappa i t} ] where the constants $ c_i $ and $ ppa $ are to be determined. See:Li, B., E. DeWetering, G. Lucas, R. Brenner and A. Shapiro (2001): &#8216;Merrill Lynch Exponential Spline Model.&#8216; Merrill Lynch Working Paper </p>
<p> <code>Warning</code> </p>
<dl>
<dd> <p> convergence may be slow </p>
 </dd></dl>
<p> <code>Examples: </code> </p>
<p> <code>FittedBondCurve.cpp</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
