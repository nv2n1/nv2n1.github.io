---
title: "paymentdate_(3)"
name: "paymentdate_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paymentdate_/"
description: "QuantLib::HaganPricer – CMS-coupon pricer."
---

<p>QuantLib::HaganPricer &#8211; CMS-coupon pricer. </p>
<h2>Synopsis</h2>
<pre><code>virtual Real swapletPrice () const =0



virtual Rate swapletRate () const



virtual Real capletPrice (Rate effectiveCap) const



virtual Rate capletRate (Rate effectiveCap) const



virtual Real floorletPrice (Rate effectiveFloor) const



virtual Rate floorletRate (Rate effectiveFloor) const



Real meanReversion () const



void setMeanReversion (const Handle&lt; Quote &gt; &amp;meanReversion)



Protected Member Functions
HaganPricer (const Handle&lt; SwaptionVolatilityStructure &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const Handle&lt; Quote &gt; &amp;meanReversion)



void initialize (const FloatingRateCoupon &amp;coupon)



virtual Real optionletPrice (Option::Type optionType, Real strike) const =0



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::CmsCouponPricer</code>. Inherited by <code>AnalyticHaganPricer</code>, and <code>NumericHaganPricer</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual Real swapletPrice () const =0



virtual Rate swapletRate () const



virtual Real capletPrice (Rate effectiveCap) const



virtual Rate capletRate (Rate effectiveCap) const



virtual Real floorletPrice (Rate effectiveFloor) const



virtual Rate floorletRate (Rate effectiveFloor) const



Real meanReversion () const



void setMeanReversion (const Handle&lt; Quote &gt; &amp;meanReversion)



Protected Member Functions
HaganPricer (const Handle&lt; SwaptionVolatilityStructure &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const Handle&lt; Quote &gt; &amp;meanReversion)



void initialize (const FloatingRateCoupon &amp;coupon)



virtual Real optionletPrice (Option::Type optionType, Real strike) const =0



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>YieldTermStructure</code> &gt; <code>rateCurve_</code> </p>
<p> GFunctionFactory::YieldCurveModel <code>modelOfYieldCurve_</code> </p>
<p> boost::shared_ptr&lt; GFunction &gt; <code>gFunction_</code> </p>
<p> const <code>CmsCoupon</code> * <code>coupon_</code> </p>
<p> <code>Date</code> <code>paymentDate_</code> </p>
<p> <code>Date</code> <code>fixingDate_</code> </p>
<p> Rate <code>swapRateValue_</code> </p>
<p> <code>DiscountFactor</code> <code>discount_</code> </p>
<p> Real <code>annuity_</code> </p>
<p> Real <code>gearing_</code> </p>
<p> <code>Spread</code> <code>spread_</code> </p>
<p> Real <code>spreadLegValue_</code> </p>
<p> Rate <code>cutoffForCaplet_</code> </p>
<p> Rate <code>cutoffForFloorlet_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>meanReversion_</code> </p>
<p> <code>Period</code> <code>swapTenor_</code> </p>
<p> boost::shared_ptr&lt; VanillaOptionPricer &gt; <code>vanillaOptionPricer_</code></p>
<h2>Detailed Description</h2>
<p>CMS-coupon pricer. </p>
<p> Base class for the pricing of a CMS coupon via static replication as in Hagan&#8217;s &#8216;Conundrums&#8230;&#8217; article</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
