---
title: "quantlib_coxingersollross_dynamics(3)"
name: "quantlib_coxingersollross_dynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_coxingersollross_dynamics/"
description: "QuantLib::CoxIngersollRoss::Dynamics – Dynamics of the short-rate under the Cox-Ingersoll-Ross model"
---

<p>QuantLib::CoxIngersollRoss::Dynamics &#8211; Dynamics of the short-rate under the Cox-Ingersoll-Ross model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/coxingersollross.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorModel::ShortRateDynamics</code>. </p>
<p> Inherited by <code>Dynamics</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Dynamics</code> (Real theta, Real k, Real sigma, Real x0) </p>
<p> virtual Real <code>variable</code> (Time, Rate r) const<br />
 <i>Compute state variable from short rate. </i><br />
 virtual Real <code>shortRate</code> (Time, Real y) const<br />
 <i>Compute short rate from state variable. </i></p>
<h2>Detailed Description</h2>
<p>Dynamics of the short-rate under the Cox-Ingersoll-Ross model </p>
<p> The state variable $ y_t $ will here be the square-root of the short-rate. It satisfies the following stochastic equation [ dy_t=</p>
<hr>
<p>ta }{2}+ac{igma ^2}{8})ac{1}{y_t}- ac{k}{2}y_t ight] d_t+ ac{igma }{2}dW_{t} ]. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
