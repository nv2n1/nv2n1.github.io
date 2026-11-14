---
title: "setcouponpricer(3)"
name: "setcouponpricer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setcouponpricer/"
description: "ql/cashflows/couponpricer.hpp – Coupon pricers."
---

<p>ql/cashflows/couponpricer.hpp &#8211; Coupon pricers. </p>
<h2>Synopsis</h2>
<pre><code>void setCouponPricer (const Leg &amp;leg, const boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &amp;)



void setCouponPricers (const Leg &amp;leg, const std::vector&lt; boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &gt; &amp;)</code></pre>
<h3>Classes</h3>
<p>class <code>FloatingRateCouponPricer</code><br />
 <i>generic pricer for floating-rate coupons </i><br />
 class <code>IborCouponPricer</code><br />
 <i>base pricer for capped/floored Ibor coupons </i><br />
 class <code>BlackIborCouponPricer</code><br />
 <i>Black-formula pricer for capped/floored Ibor coupons. </i><br />
 class <code>CmsCouponPricer</code><br />
 <i>base pricer for vanilla CMS coupons </i></p>
<h3>Functions</h3>
<pre><code>void setCouponPricer (const Leg &amp;leg, const boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &amp;)



void setCouponPricers (const Leg &amp;leg, const std::vector&lt; boost::shared_ptr&lt; FloatingRateCouponPricer &gt; &gt; &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>Coupon pricers.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
