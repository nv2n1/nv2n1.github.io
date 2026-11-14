---
title: "withcallatm(3)"
name: "withcallatm"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withcallatm/"
---

QuantLib::DigitalCmsLeg - helper class building a sequence of digital ibor-rate coupons 

<h2>Synopsis</h2>

<pre><code>DigitalCmsLeg (const Schedule &amp;schedule, const boost::shared_ptr&lt; SwapIndex &gt; &amp;index)



DigitalCmsLeg &amp; withNotionals (Real notional)



DigitalCmsLeg &amp; withNotionals (const std::vector&lt; Real &gt; &amp;notionals)



DigitalCmsLeg &amp; withPaymentDayCounter (const DayCounter &amp;)



DigitalCmsLeg &amp; withPaymentAdjustment (BusinessDayConvention)



DigitalCmsLeg &amp; withFixingDays (Natural fixingDays)



DigitalCmsLeg &amp; withFixingDays (const std::vector&lt; Natural &gt; &amp;fixingDays)



DigitalCmsLeg &amp; withGearings (Real gearing)



DigitalCmsLeg &amp; withGearings (const std::vector&lt; Real &gt; &amp;gearings)



DigitalCmsLeg &amp; withSpreads (Spread spread)



DigitalCmsLeg &amp; withSpreads (const std::vector&lt; Spread &gt; &amp;spreads)



DigitalCmsLeg &amp; inArrears (bool flag=true)



DigitalCmsLeg &amp; withCallStrikes (Rate strike)



DigitalCmsLeg &amp; withCallStrikes (const std::vector&lt; Rate &gt; &amp;strikes)



DigitalCmsLeg &amp; withLongCallOption (Position::Type)



DigitalCmsLeg &amp; withCallATM (bool flag=true)



DigitalCmsLeg &amp; withCallPayoffs (Rate payoff)



DigitalCmsLeg &amp; withCallPayoffs (const std::vector&lt; Rate &gt; &amp;payoffs)



DigitalCmsLeg &amp; withPutStrikes (Rate strike)



DigitalCmsLeg &amp; withPutStrikes (const std::vector&lt; Rate &gt; &amp;strikes)



DigitalCmsLeg &amp; withLongPutOption (Position::Type)



DigitalCmsLeg &amp; withPutATM (bool flag=true)



DigitalCmsLeg &amp; withPutPayoffs (Rate payoff)



DigitalCmsLeg &amp; withPutPayoffs (const std::vector&lt; Rate &gt; &amp;payoffs)



DigitalCmsLeg &amp; withReplication (const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication=boost::shared_ptr&lt; DigitalReplication &gt;())



operator Leg () const</code></pre>

<h3>Public Member Functions</h3>

<pre><code>DigitalCmsLeg (const Schedule &amp;schedule, const boost::shared_ptr&lt; SwapIndex &gt; &amp;index)



DigitalCmsLeg &amp; withNotionals (Real notional)



DigitalCmsLeg &amp; withNotionals (const std::vector&lt; Real &gt; &amp;notionals)



DigitalCmsLeg &amp; withPaymentDayCounter (const DayCounter &amp;)



DigitalCmsLeg &amp; withPaymentAdjustment (BusinessDayConvention)



DigitalCmsLeg &amp; withFixingDays (Natural fixingDays)



DigitalCmsLeg &amp; withFixingDays (const std::vector&lt; Natural &gt; &amp;fixingDays)



DigitalCmsLeg &amp; withGearings (Real gearing)



DigitalCmsLeg &amp; withGearings (const std::vector&lt; Real &gt; &amp;gearings)



DigitalCmsLeg &amp; withSpreads (Spread spread)



DigitalCmsLeg &amp; withSpreads (const std::vector&lt; Spread &gt; &amp;spreads)



DigitalCmsLeg &amp; inArrears (bool flag=true)



DigitalCmsLeg &amp; withCallStrikes (Rate strike)



DigitalCmsLeg &amp; withCallStrikes (const std::vector&lt; Rate &gt; &amp;strikes)



DigitalCmsLeg &amp; withLongCallOption (Position::Type)



DigitalCmsLeg &amp; withCallATM (bool flag=true)



DigitalCmsLeg &amp; withCallPayoffs (Rate payoff)



DigitalCmsLeg &amp; withCallPayoffs (const std::vector&lt; Rate &gt; &amp;payoffs)



DigitalCmsLeg &amp; withPutStrikes (Rate strike)



DigitalCmsLeg &amp; withPutStrikes (const std::vector&lt; Rate &gt; &amp;strikes)



DigitalCmsLeg &amp; withLongPutOption (Position::Type)



DigitalCmsLeg &amp; withPutATM (bool flag=true)



DigitalCmsLeg &amp; withPutPayoffs (Rate payoff)



DigitalCmsLeg &amp; withPutPayoffs (const std::vector&lt; Rate &gt; &amp;payoffs)



DigitalCmsLeg &amp; withReplication (const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication=boost::shared_ptr&lt; DigitalReplication &gt;())



operator Leg () const</code></pre>

<h2>Detailed Description</h2>

helper class building a sequence of digital ibor-rate coupons

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
