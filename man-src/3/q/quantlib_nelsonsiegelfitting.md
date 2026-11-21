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
<p> Fits a discount function to the form $ d(t) = \xp^{-r t}, $ where the zero rate $r$ is defined as [ r \quiv c_0 + (c_0 + c_1)*(1 &#8211; exp^{-ppa*t}/(ppa t) &#8211; c_2 exp^{ &#8211; ppa t}. ] See: Nelson, C. and A. Siegel (1985): &#8216;Parsimonious modeling of yield curves for US Treasury bills.&#8216; NBER Working Paper Series, no 1594. </p>
<p> <code>Examples: </code> </p>
<p> <code>FittedBondCurve.cpp</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
