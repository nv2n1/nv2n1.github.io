---
title: "blackiborcouponpricer(3)"
name: "blackiborcouponpricer"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackiborcouponpricer/"
description: "QuantLib::BlackIborCouponPricer – Black-formula pricer for capped/floored Ibor coupons."
---

<p>QuantLib::BlackIborCouponPricer &#8211; Black-formula pricer for capped/floored Ibor coupons. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/couponpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborCouponPricer</code>. </p>
<p> Inherited by BlackIborQuantoCouponPricer. </p>
<h3>Public Member Functions</h3>
<p><code>BlackIborCouponPricer</code> (const <code>Handle</code>&lt; <code>OptionletVolatilityStructure</code> &gt; &amp;v=<code>Handle</code>&lt; <code>OptionletVolatilityStructure</code> &gt;()) </p>
<p> virtual void <code>initialize</code> (const <code>FloatingRateCoupon</code> &amp;coupon) </p>
<p> Real <code>swapletPrice</code> () const </p>
<p> Rate <code>swapletRate</code> () const </p>
<p> Real <code>capletPrice</code> (Rate effectiveCap) const </p>
<p> Rate <code>capletRate</code> (Rate effectiveCap) const </p>
<p> Real <code>floorletPrice</code> (Rate effectiveFloor) const </p>
<p> Rate <code>floorletRate</code> (Rate effectiveFloor) const </p>
<h3>Protected Member Functions</h3>
<p>Real <code>optionletPrice</code> (Option::Type optionType, Real effStrike) const </p>
<p> virtual Rate <code>adjustedFixing</code> (Rate fixing=<code>Null</code>&lt; Rate &gt;()) const </p>
<h3>Protected Attributes</h3>
<p>const <code>IborCoupon</code> * <code>coupon_</code> </p>
<p> Real <code>discount_</code> </p>
<p> Real <code>gearing_</code> </p>
<p> <code>Spread</code> <code>spread_</code> </p>
<p> Real <code>spreadLegValue_</code> </p>
<h2>Detailed Description</h2>
<p>Black-formula pricer for capped/floored Ibor coupons. </p>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
