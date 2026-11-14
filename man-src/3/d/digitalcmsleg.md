---
title: "digitalcmsleg(3)"
name: "digitalcmsleg"
section: "3"
letter: "d"
url: "/docs/linux/man/3-digitalcmsleg/"
description: "QuantLib::DigitalCmsLeg – helper class building a sequence of digital ibor-rate coupons"
---

<p>QuantLib::DigitalCmsLeg &#8211; helper class building a sequence of digital ibor-rate coupons </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/digitalcmscoupon.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>DigitalCmsLeg</code> (const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;index) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withNotionals</code> (<code>Real</code> notional) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;notionals) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPaymentDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withFixingDays</code> (<code>Natural</code> fixingDays) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withFixingDays</code> (const std::vector&lt; <code>Natural</code> &gt; &amp;fixingDays) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withGearings</code> (<code>Real</code> gearing) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withGearings</code> (const std::vector&lt; <code>Real</code> &gt; &amp;gearings) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withSpreads</code> (<code>Spread</code> spread) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withSpreads</code> (const std::vector&lt; <code>Spread</code> &gt; &amp;spreads) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>inArrears</code> (bool flag=true) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withCallStrikes</code> (<code>Rate</code> strike) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withCallStrikes</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;strikes) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withLongCallOption</code> (Position::Type) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withCallATM</code> (bool flag=true) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withCallPayoffs</code> (<code>Rate</code> payoff) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withCallPayoffs</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;payoffs) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPutStrikes</code> (<code>Rate</code> strike) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPutStrikes</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;strikes) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withLongPutOption</code> (Position::Type) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPutATM</code> (bool flag=true) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPutPayoffs</code> (<code>Rate</code> payoff) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withPutPayoffs</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;payoffs) </p>
<p> <code>DigitalCmsLeg</code> &amp; <code>withReplication</code> (const boost::shared_ptr&lt; DigitalReplication &gt; &amp;replication=boost::shared_ptr&lt; DigitalReplication &gt;()) </p>
<p> <code>operator Leg</code> () const </p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of digital ibor-rate coupons </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
