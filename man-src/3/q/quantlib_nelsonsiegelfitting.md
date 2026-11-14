---
title: "quantlib_nelsonsiegelfitting(3)"
name: "quantlib_nelsonsiegelfitting"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_nelsonsiegelfitting/"
description: "QuantLib::NelsonSiegelFitting – Nelson-Siegel fitting method."
---

<p>QuantLib::NelsonSiegelFitting &#8211; Nelson-Siegel fitting method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/nonlinearfittingmethods.hpp&gt; </p>
<p> Inherits <code>QuantLib::FittedBondDiscountCurve::FittingMethod</code>. </p>
<h3>Public Member Functions</h3>
<p>std::auto_ptr&lt; <code>FittedBondDiscountCurve::FittingMethod</code> &gt; <code>clone</code> () const<br />
 <i>clone of the current object </i></p>
<h2>Detailed Description</h2>
<p>Nelson-Siegel fitting method. </p>
<p> Fits a discount function to the form $ d(t) = 
