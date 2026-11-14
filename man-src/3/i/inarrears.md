---
title: "inarrears(3)"
name: "inarrears"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inarrears/"
description: "QuantLib::CmsLeg – helper class building a sequence of capped/floored cms-rate coupons"
---

<p>QuantLib::CmsLeg &#8211; helper class building a sequence of capped/floored cms-rate coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/cmscoupon.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>CmsLeg</code> (const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex) </p>
<p> <code>CmsLeg</code> &amp; <code>withNotionals</code> (<code>Real</code> notional) </p>
<p> <code>CmsLeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;notionals) </p>
<p> <code>CmsLeg</code> &amp; <code>withPaymentDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>CmsLeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>CmsLeg</code> &amp; <code>withFixingDays</code> (<code>Natural</code> fixingDays) </p>
<p> <code>CmsLeg</code> &amp; <code>withFixingDays</code> (const std::vector&lt; <code>Natural</code> &gt; &amp;fixingDays) </p>
<p> <code>CmsLeg</code> &amp; <code>withGearings</code> (<code>Real</code> gearing) </p>
<p> <code>CmsLeg</code> &amp; <code>withGearings</code> (const std::vector&lt; <code>Real</code> &gt; &amp;gearings) </p>
<p> <code>CmsLeg</code> &amp; <code>withSpreads</code> (<code>Spread</code> spread) </p>
<p> <code>CmsLeg</code> &amp; <code>withSpreads</code> (const std::vector&lt; <code>Spread</code> &gt; &amp;spreads) </p>
<p> <code>CmsLeg</code> &amp; <code>withCaps</code> (<code>Rate</code> cap) </p>
<p> <code>CmsLeg</code> &amp; <code>withCaps</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;caps) </p>
<p> <code>CmsLeg</code> &amp; <code>withFloors</code> (<code>Rate</code> floor) </p>
<p> <code>CmsLeg</code> &amp; <code>withFloors</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;floors) </p>
<p> <code>CmsLeg</code> &amp; <code>inArrears</code> (bool flag=true) </p>
<p> <code>CmsLeg</code> &amp; <code>withZeroPayments</code> (bool flag=true) </p>
<p> <code>operator Leg</code> () const </p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of capped/floored cms-rate coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
