---
title: "quantlib_hullwhite_dynamics(3)"
name: "quantlib_hullwhite_dynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_hullwhite_dynamics/"
description: "QuantLib::HullWhite::Dynamics – Short-rate dynamics in the Hull-White model."
---

<p>QuantLib::HullWhite::Dynamics &#8211; Short-rate dynamics in the Hull-White model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/hullwhite.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorModel::ShortRateDynamics</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Dynamics</code> (const <code>Parameter</code> &amp;fitting, Real a, Real sigma) </p>
<p> Real <code>variable</code> (Time t, Rate r) const<br />
 <i>Compute state variable from short rate. </i><br />
 Real <code>shortRate</code> (Time t, Real x) const<br />
 <i>Compute short rate from state variable. </i></p>
<h2>Detailed Description</h2>
<p>Short-rate dynamics in the Hull-White model. </p>
<p> The short-rate is here [ r_t = meter used for term-structure fitting and $ x_t $ is the state variable following an Ornstein-Uhlenbeck process. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
