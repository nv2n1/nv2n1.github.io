---
title: "quantlib_cubicbsplinesfitting(3)"
name: "quantlib_cubicbsplinesfitting"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cubicbsplinesfitting/"
description: "QuantLib::CubicBSplinesFitting – CubicSpline B-splines fitting method."
---

<p>QuantLib::CubicBSplinesFitting &#8211; CubicSpline B-splines fitting method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/nonlinearfittingmethods.hpp&gt; </p>
<p> Inherits <code>QuantLib::FittedBondDiscountCurve::FittingMethod</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CubicBSplinesFitting</code> (const std::vector&lt; Time &gt; &amp;knotVector, bool constrainAtZero=true) </p>
<p> <code>Real</code> <code>basisFunction</code> (<code>Integer</code> i, Time t) const<br />
 <i>cubic B-spline basis functions </i><br />
 std::auto_ptr&lt; <code>FittedBondDiscountCurve::FittingMethod</code> &gt; <code>clone</code> () const<br />
 <i>clone of the current object </i></p>
<h2>Detailed Description</h2>
<p>CubicSpline B-splines fitting method. </p>
<p> Fits a discount function to a set of cubic B-splines $ N_{i,3}(t) $, i.e., [ d(t) = um_{i=0}^{n} c_i * N_{i,3}(t) ] </p>
<p> See: McCulloch, J. 1971, &#8216;Measuring the Term Structure of Interest Rates.&#8217; Journal of Business, 44: 19-31 </p>
<p> McCulloch, J. 1975, &#8216;The tax adjusted yield curve.&#8217; Journal of Finance, XXX811-30 </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd></dl>
<p> <code>Examples: </code> </p>
<p> <code>FittedBondCurve.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
