---
title: "withcaps(3)"
name: "withcaps"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withcaps/"
---

QuantLib::CmsLeg - helper class building a sequence of capped/floored cms-rate coupons 

<h2>Synopsis</h2>

<pre><code>CmsLeg (const Schedule &amp;schedule, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex)



CmsLeg &amp; withNotionals (Real notional)



CmsLeg &amp; withNotionals (const std::vector&lt; Real &gt; &amp;notionals)



CmsLeg &amp; withPaymentDayCounter (const DayCounter &amp;)



CmsLeg &amp; withPaymentAdjustment (BusinessDayConvention)



CmsLeg &amp; withFixingDays (Natural fixingDays)



CmsLeg &amp; withFixingDays (const std::vector&lt; Natural &gt; &amp;fixingDays)



CmsLeg &amp; withGearings (Real gearing)



CmsLeg &amp; withGearings (const std::vector&lt; Real &gt; &amp;gearings)



CmsLeg &amp; withSpreads (Spread spread)



CmsLeg &amp; withSpreads (const std::vector&lt; Spread &gt; &amp;spreads)



CmsLeg &amp; withCaps (Rate cap)



CmsLeg &amp; withCaps (const std::vector&lt; Rate &gt; &amp;caps)



CmsLeg &amp; withFloors (Rate floor)



CmsLeg &amp; withFloors (const std::vector&lt; Rate &gt; &amp;floors)



CmsLeg &amp; inArrears (bool flag=true)



CmsLeg &amp; withZeroPayments (bool flag=true)



operator Leg () const</code></pre>

<h3>Public Member Functions</h3>

<pre><code>CmsLeg (const Schedule &amp;schedule, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex)



CmsLeg &amp; withNotionals (Real notional)



CmsLeg &amp; withNotionals (const std::vector&lt; Real &gt; &amp;notionals)



CmsLeg &amp; withPaymentDayCounter (const DayCounter &amp;)



CmsLeg &amp; withPaymentAdjustment (BusinessDayConvention)



CmsLeg &amp; withFixingDays (Natural fixingDays)



CmsLeg &amp; withFixingDays (const std::vector&lt; Natural &gt; &amp;fixingDays)



CmsLeg &amp; withGearings (Real gearing)



CmsLeg &amp; withGearings (const std::vector&lt; Real &gt; &amp;gearings)



CmsLeg &amp; withSpreads (Spread spread)



CmsLeg &amp; withSpreads (const std::vector&lt; Spread &gt; &amp;spreads)



CmsLeg &amp; withCaps (Rate cap)



CmsLeg &amp; withCaps (const std::vector&lt; Rate &gt; &amp;caps)



CmsLeg &amp; withFloors (Rate floor)



CmsLeg &amp; withFloors (const std::vector&lt; Rate &gt; &amp;floors)



CmsLeg &amp; inArrears (bool flag=true)



CmsLeg &amp; withZeroPayments (bool flag=true)



operator Leg () const</code></pre>

<h2>Detailed Description</h2>

helper class building a sequence of capped/floored cms-rate coupons

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
