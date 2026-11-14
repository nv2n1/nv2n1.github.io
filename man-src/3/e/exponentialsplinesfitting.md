---
title: "exponentialsplinesfitting(3)"
name: "exponentialsplinesfitting"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exponentialsplinesfitting/"
description: "QuantLib::ExponentialSplinesFitting – Exponential-splines fitting method."
---

<p>QuantLib::ExponentialSplinesFitting &#8211; Exponential-splines fitting method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/nonlinearfittingmethods.hpp&gt; </p>
<p> Inherits <code>QuantLib::FittedBondDiscountCurve::FittingMethod</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExponentialSplinesFitting</code> (bool constrainAtZero=true) </p>
<p> std::auto_ptr&lt; <code>FittedBondDiscountCurve::FittingMethod</code> &gt; <code>clone</code> () const<br />
 <i>clone of the current object </i></p>
<h2>Detailed Description</h2>
<p>Exponential-splines fitting method. </p>
<p> Fits a discount function to the exponential form [ d(t) = um_{i=1}^9 c_i 
