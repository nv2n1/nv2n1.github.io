---
title: "floorletprice(3)"
name: "floorletprice"
section: "3"
letter: "f"
url: "/docs/linux/man/3-floorletprice/"
description: "QuantLib::HaganPricer – CMS-coupon pricer."
---

<p>QuantLib::HaganPricer &#8211; CMS-coupon pricer. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/conundrumpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::CmsCouponPricer</code>. </p>
<p> Inherited by <code>AnalyticHaganPricer</code>, and <code>NumericHaganPricer</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual Real <code>swapletPrice</code> () const =0 </p>
<p> virtual Rate <code>swapletRate</code> () const </p>
<p> virtual Real <code>capletPrice</code> (Rate effectiveCap) const </p>
<p> virtual Rate <code>capletRate</code> (Rate effectiveCap) const </p>
<p> virtual Real <code>floorletPrice</code> (Rate effectiveFloor) const </p>
<p> virtual Rate <code>floorletRate</code> (Rate effectiveFloor) const </p>
<p> Real <code>meanReversion</code> () const </p>
<p> void <code>setMeanReversion</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion) </p>
<h3>Protected Member Functions</h3>
<p><code>HaganPricer</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion) </p>
<p> void <code>initialize</code> (const <code>FloatingRateCoupon</code> &amp;coupon) </p>
<p> virtual Real <code>optionletPrice</code> (Option::Type optionType, Real strike) const =0 </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>YieldTermStructure</code> &gt; <code>rateCurve_</code> </p>
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
<p> boost::shared_ptr&lt; VanillaOptionPricer &gt; <code>vanillaOptionPricer_</code> </p>
<h2>Detailed Description</h2>
<p>CMS-coupon pricer. </p>
<p> Base class for the pricing of a CMS coupon via static replication as in Hagan&#8217;s &#8216;Conundrums&#8230;&#8217; article </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
