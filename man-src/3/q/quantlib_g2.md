---
title: "quantlib_g2(3)"
name: "quantlib_g2"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_g2/"
description: "QuantLib::G2 – Two-additive-factor gaussian model class."
---

<p>QuantLib::G2 &#8211; Two-additive-factor gaussian model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/twofactormodels/g2.hpp&gt; </p>
<p> Inherits <code>QuantLib::TwoFactorModel</code>, <code>QuantLib::AffineModel</code>, and <code>QuantLib::TermStructureConsistentModel</code>. </p>
<h3>Classes</h3>
<p>class <code>FittingParameter</code><br />
 <i>Analytical term-structure fitting parameter $ ndle</i>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01, Real b=0.1, Real eta=0.01, Real rho=-0.75)&quot;</p>
<h3>Public Member Functions</h3>
<p><code>G2</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01, Real b=0.1, Real eta=0.01, Real rho=-0.75) </p>
<p> boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>Returns the short-rate dynamics. </i><br />
 virtual Real <code>discountBond</code> (Time now, Time maturity, <code>Array</code> factors) const </p>
<p> Real <code>discountBond</code> (Time, Time, <code>Rate</code>, <code>Rate</code>) const </p>
<p> Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<p> Real <code>swaption</code> (const <code>Swaption::arguments</code> &amp;arguments, <code>Rate</code> fixedRate, Real range, Size intervals) const </p>
<p> <code>DiscountFactor</code> <code>discount</code> (Time t) const<br />
 <i>Implied discount curve. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>generateArguments</code> () </p>
<p> Real <code>A</code> (Time t, Time T) const </p>
<p> Real <code>B</code> (Real x, Time t) const </p>
<h3>Friends</h3>
<p>class <code>SwaptionPricingFunction</code> </p>
<h2>Detailed Description</h2>
<p>Two-additive-factor gaussian model class. </p>
<p> This class implements a two-additive-factor model defined by [ dr_t = nd $ y_t $ are defined by [ dx_t = -a x_t dt + igma dW^1_t, x_0 = 0 ] [ dy_t = -b y_t dt + igma dW^2_t, y_0 = 0 ] and $ dW^1_t dW^2_t = ho dt $. </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>This class was not tested enough to guarantee its functionality.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
