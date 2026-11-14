---
title: "couponpricer(3)"
name: "couponpricer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-couponpricer/"
description: "ql/cashflows/couponpricer.hpp – Coupon pricers."
---

<h2 class="name">NAME</h2>
<p> ql/cashflows/couponpricer.hpp &#8211; Coupon pricers. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/termstructures/volatility/optionlet/optionletvolatilitystructure.hpp&gt;<br />
 #include &lt;ql/termstructures/volatility/swaption/swaptionvolstructure.hpp&gt;<br />
 #include &lt;ql/cashflow.hpp&gt;<br />
 #include &lt;ql/option.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>FloatingRateCouponPricer</code><br />
 <i>generic pricer for floating-rate coupons </i><br />
 class <code>IborCouponPricer</code><br />
 <i>base pricer for capped/floored Ibor coupons </i><br />
 class <code>BlackIborCouponPricer</code><br />
 <i>Black-formula pricer for capped/floored Ibor coupons. </i><br />
 class <code>CmsCouponPricer</code><br />
 <i>base pricer for vanilla CMS coupons </i></p>
<h3>Functions</h3>
<p> void <code>setCouponPricer</code> (const Leg &amp;leg, const boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &amp;) </p>
<p> void <code>setCouponPricers</code> (const Leg &amp;leg, const std::vector&lt; boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &gt; &amp;) </p>
<h2>Detailed Description</h2>
<p> Coupon pricers. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
