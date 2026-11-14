---
title: "withlowertriggers(3)"
name: "withlowertriggers"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withlowertriggers/"
description: "QuantLib::RangeAccrualLeg – helper class building a sequence of range-accrual floating-rate coupons"
---

<p>QuantLib::RangeAccrualLeg &#8211; helper class building a sequence of range-accrual floating-rate coupons </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/cashflows/rangeaccrual.hpp&gt;</code></pre>
<h3>Public Member Functions</h3>
<p><code>RangeAccrualLeg</code> (const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withNotionals</code> (<code>Real</code> notional) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;notionals) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withPaymentDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withFixingDays</code> (<code>Natural</code> fixingDays) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withFixingDays</code> (const std::vector&lt; <code>Natural</code> &gt; &amp;fixingDays) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withGearings</code> (<code>Real</code> gearing) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withGearings</code> (const std::vector&lt; <code>Real</code> &gt; &amp;gearings) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withSpreads</code> (<code>Spread</code> spread) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withSpreads</code> (const std::vector&lt; <code>Spread</code> &gt; &amp;spreads) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withLowerTriggers</code> (<code>Rate</code> trigger) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withLowerTriggers</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;triggers) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withUpperTriggers</code> (<code>Rate</code> trigger) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withUpperTriggers</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;triggers) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withObservationTenor</code> (const <code>Period</code> &amp;) </p>
<p> <code>RangeAccrualLeg</code> &amp; <code>withObservationConvention</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>operator Leg</code> () const</p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of range-accrual floating-rate coupons</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
