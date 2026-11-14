---
title: "quantlib_vasicek(3)"
name: "quantlib_vasicek"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_vasicek/"
description: "QuantLib::Vasicek – Vasicek model class"
---

<p>QuantLib::Vasicek &#8211; Vasicek model class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/vasicek.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorAffineModel</code>. </p>
<p> Inherited by <code>HullWhite</code>. </p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Short-rate dynamics in the Vasicek model. </i></p>
<h3>Public Member Functions</h3>
<p><code>Vasicek</code> (<code>Rate</code> r0=0.05, Real a=0.1, Real b=0.05, Real sigma=0.01, Real lambda=0.0) </p>
<p> virtual Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<p> virtual boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>returns the short-rate dynamics </i></p>
<h3>Protected Member Functions</h3>
<p>virtual Real <code>A</code> (Time t, Time T) const </p>
<p> virtual Real <code>B</code> (Time t, Time T) const </p>
<p> Real <code>a</code> () const </p>
<p> Real <code>b</code> () const </p>
<p> Real <code>lambda</code> () const </p>
<p> Real <code>sigma</code> () const </p>
<h3>Protected Attributes</h3>
<p>Real <code>r0_</code> </p>
<p> <code>Parameter</code> &amp; <code>a_</code> </p>
<p> <code>Parameter</code> &amp; <code>b_</code> </p>
<p> <code>Parameter</code> &amp; <code>sigma_</code> </p>
<p> <code>Parameter</code> &amp; <code>lambda_</code> </p>
<h2>Detailed Description</h2>
<p>Vasicek model class </p>
<p> This class implements the <code>Vasicek</code> model defined by [ dr_t = a(b &#8211; r_t)dt + igma dW_t , ] where $ a $, $ b $ and $ igma $ are constants; a risk premium $ </p>
<hr>
<p> $ can also be specified. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
