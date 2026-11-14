---
title: "iborleg(3)"
name: "iborleg"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iborleg/"
description: "QuantLib::IborLeg – helper class building a sequence of capped/floored ibor-rate coupons"
---

<p>QuantLib::IborLeg &#8211; helper class building a sequence of capped/floored ibor-rate coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/iborcoupon.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>IborLeg</code> (const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index) </p>
<p> <code>IborLeg</code> &amp; <code>withNotionals</code> (<code>Real</code> notional) </p>
<p> <code>IborLeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;notionals) </p>
<p> <code>IborLeg</code> &amp; <code>withPaymentDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>IborLeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>IborLeg</code> &amp; <code>withFixingDays</code> (<code>Natural</code> fixingDays) </p>
<p> <code>IborLeg</code> &amp; <code>withFixingDays</code> (const std::vector&lt; <code>Natural</code> &gt; &amp;fixingDays) </p>
<p> <code>IborLeg</code> &amp; <code>withGearings</code> (<code>Real</code> gearing) </p>
<p> <code>IborLeg</code> &amp; <code>withGearings</code> (const std::vector&lt; <code>Real</code> &gt; &amp;gearings) </p>
<p> <code>IborLeg</code> &amp; <code>withSpreads</code> (<code>Spread</code> spread) </p>
<p> <code>IborLeg</code> &amp; <code>withSpreads</code> (const std::vector&lt; <code>Spread</code> &gt; &amp;spreads) </p>
<p> <code>IborLeg</code> &amp; <code>withCaps</code> (<code>Rate</code> cap) </p>
<p> <code>IborLeg</code> &amp; <code>withCaps</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;caps) </p>
<p> <code>IborLeg</code> &amp; <code>withFloors</code> (<code>Rate</code> floor) </p>
<p> <code>IborLeg</code> &amp; <code>withFloors</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;floors) </p>
<p> <code>IborLeg</code> &amp; <code>inArrears</code> (bool flag=true) </p>
<p> <code>IborLeg</code> &amp; <code>withZeroPayments</code> (bool flag=true) </p>
<p> <code>operator Leg</code> () const </p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of capped/floored ibor-rate coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
