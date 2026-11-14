---
title: "sigma_(3)"
name: "sigma_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigma_/"
description: "QuantLib::Vasicek – Vasicek model class"
---

<p>QuantLib::Vasicek &#8211; Vasicek model class </p>
<h2>Synopsis</h2>
<pre><code>Vasicek (Rate r0=0.05, Real a=0.1, Real b=0.05, Real sigma=0.01, Real lambda=0.0)



virtual Real discountBondOption (Option::Type type, Real strike, Time maturity, Time bondMaturity) const



virtual boost::shared_ptr&lt; ShortRateDynamics &gt; dynamics () const


returns the short-rate dynamics



Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::OneFactorAffineModel</code>. Inherited by <code>HullWhite</code>.</p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Short-rate dynamics in the Vasicek model. </i></p>
<h3>Public Member Functions</h3>
<pre><code>Vasicek (Rate r0=0.05, Real a=0.1, Real b=0.05, Real sigma=0.01, Real lambda=0.0)



virtual Real discountBondOption (Option::Type type, Real strike, Time maturity, Time bondMaturity) const



virtual boost::shared_ptr&lt; ShortRateDynamics &gt; dynamics () const


returns the short-rate dynamics



Protected Member Functions</code></pre>
<p> virtual Real <code>A</code> (Time t, Time T) const </p>
<p> virtual Real <code>B</code> (Time t, Time T) const </p>
<p> Real <code>a</code> () const </p>
<p> Real <code>b</code> () const </p>
<p> Real <code>lambda</code> () const </p>
<p> Real <code>sigma</code> () const</p>
<h3>Protected Attributes</h3>
<p>Real <code>r0_</code> </p>
<p> <code>Parameter</code> &amp; <code>a_</code> </p>
<p> <code>Parameter</code> &amp; <code>b_</code> </p>
<p> <code>Parameter</code> &amp; <code>sigma_</code> </p>
<p> <code>Parameter</code> &amp; <code>lambda_</code></p>
<h2>Detailed Description</h2>
<p>Vasicek model class </p>
<p> This class implements the <code>Vasicek</code> model defined by [ dr_t = a(b &#8211; r_t)dt + igma dW_t , ] where $ a $, $ b $ and $ igma $ are constants; a risk premium $ </p>
<hr>
<p> $ can also be specified.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
