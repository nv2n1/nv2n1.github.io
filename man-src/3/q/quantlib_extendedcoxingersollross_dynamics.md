---
title: "quantlib_extendedcoxingersollross_dynamics(3)"
name: "quantlib_extendedcoxingersollross_dynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedcoxingersollross_dynamics/"
description: "QuantLib::ExtendedCoxIngersollRoss::Dynamics – Short-rate dynamics in the extended Cox-Ingersoll-Ross model."
---

<p>QuantLib::ExtendedCoxIngersollRoss::Dynamics &#8211; Short-rate dynamics in the extended Cox-Ingersoll-Ross model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/extendedcoxingersollross.hpp&gt; </p>
<p> Inherits <code>QuantLib::CoxIngersollRoss::Dynamics</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Dynamics</code> (const <code>Parameter</code> &amp;phi, Real theta, Real k, Real sigma, Real x0) </p>
<p> virtual Real <code>variable</code> (Time t, Rate r) const<br />
 <i>Compute state variable from short rate. </i><br />
 virtual Real <code>shortRate</code> (Time t, Real y) const<br />
 <i>Compute short rate from state variable. </i></p>
<h2>Detailed Description</h2>
<p>Short-rate dynamics in the extended Cox-Ingersoll-Ross model. </p>
<p> The short-rate is here [ r_t = meter used for term-structure fitting and $ y_t $ is the state variable, the square-root of a standard CIR process. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
