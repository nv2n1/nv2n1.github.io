---
title: "quantlib_vasicek_dynamics(3)"
name: "quantlib_vasicek_dynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_vasicek_dynamics/"
description: "QuantLib::Vasicek::Dynamics – Short-rate dynamics in the Vasicek model."
---

<p>QuantLib::Vasicek::Dynamics &#8211; Short-rate dynamics in the Vasicek model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/vasicek.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorModel::ShortRateDynamics</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Dynamics</code> (Real a, Real b, Real sigma, Real r0) </p>
<p> virtual Real <code>variable</code> (Time, Rate r) const<br />
 <i>Compute state variable from short rate. </i><br />
 virtual Real <code>shortRate</code> (Time, Real x) const<br />
 <i>Compute short rate from state variable. </i></p>
<h2>Detailed Description</h2>
<p>Short-rate dynamics in the Vasicek model. </p>
<p> The short-rate follows an Ornstein-Uhlenbeck process with mean $ b $. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
