---
title: "swaptionpricingfunction(3)"
name: "swaptionpricingfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swaptionpricingfunction/"
---

QuantLib::G2 - Two-additive-factor gaussian model class. 

<h2>Synopsis</h2>#include &lt;ql/models/shortrate/twofactormodels/g2.hpp&gt; 

 Inherits <b>QuantLib::TwoFactorModel</b>, <b>QuantLib::AffineModel</b>, and <b>QuantLib::TermStructureConsistentModel</b>. 

<h3>Classes</h3>class <b>FittingParameter</b> 
 <i>Analytical term-structure fitting parameter $ ndle</i>&lt; <b>YieldTermStructure</b> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01, Real b=0.1, Real eta=0.01, Real rho=-0.75)&quot;
<h3>Public Member Functions</h3><b>G2</b> (const <b>Handle</b>&lt; <b>YieldTermStructure</b> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01, Real b=0.1, Real eta=0.01, Real rho=-0.75) 
 
 boost::shared_ptr&lt; <b>ShortRateDynamics</b> &gt; <b>dynamics</b> () const 
 <i>Returns the short-rate dynamics. </i> 
 virtual Real <b>discountBond</b> (Time now, Time maturity, <b>Array</b> factors) const 
 
 Real <b>discountBond</b> (Time, Time, <b>Rate</b>, <b>Rate</b>) const 
 
 Real <b>discountBondOption</b> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const 
 
 Real <b>swaption</b> (const <b>Swaption::arguments</b> &amp;arguments, <b>Rate</b> fixedRate, Real range, Size intervals) const 
 
 <b>DiscountFactor</b> <b>discount</b> (Time t) const 
 <i>Implied discount curve. </i>
<h3>Protected Member Functions</h3>void <b>generateArguments</b> () 
 
 Real <b>A</b> (Time t, Time T) const 
 
 Real <b>B</b> (Real x, Time t) const 

<h3>Friends</h3>class <b>SwaptionPricingFunction</b> 

<h2>Detailed Description</h2>Two-additive-factor gaussian model class. 

 This class implements a two-additive-factor model defined by [ dr_t = nd $ y_t $ are defined by [ dx_t = -a x_t dt + igma dW^1_t, x_0 = 0 ] [ dy_t = -b y_t dt + igma dW^2_t, y_0 = 0 ] and $ dW^1_t dW^2_t = ho dt $. 

 <b>Bug</b>
<dl COMPACT><dd>This class was not tested enough to guarantee its functionality.</dl>
 

 

 

 <b>Examples: </b> 

 <b>BermudanSwaption.cpp</b>. 

<h2>Author</h2>Generated automatically by Doxygen for QuantLib from the source code.
