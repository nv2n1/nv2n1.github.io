---
title: "quantlib_fixedrateleg(3)"
name: "quantlib_fixedrateleg"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fixedrateleg/"
description: "QuantLib::FixedRateLeg – helper class building a sequence of fixed rate coupons"
---

<p>QuantLib::FixedRateLeg &#8211; helper class building a sequence of fixed rate coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/fixedratecoupon.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>FixedRateLeg</code> (const <code>Schedule</code> &amp;schedule, const <code>DayCounter</code> &amp;paymentDayCounter) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withNotionals</code> (<code>Real</code>) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withCouponRates</code> (<code>Rate</code>) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withCouponRates</code> (const <code>InterestRate</code> &amp;) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withCouponRates</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withCouponRates</code> (const std::vector&lt; <code>InterestRate</code> &gt; &amp;) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>FixedRateLeg</code> &amp; <code>withFirstPeriodDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>operator Leg</code> () const </p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of fixed rate coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
