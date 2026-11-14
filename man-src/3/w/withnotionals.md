---
title: "withnotionals(3)"
name: "withnotionals"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withnotionals/"
description: "QuantLib::AverageBMALeg – helper class building a sequence of average BMA coupons"
---

<p>QuantLib::AverageBMALeg &#8211; helper class building a sequence of average BMA coupons </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/cashflows/averagebmacoupon.hpp&gt;</code></pre>
<h3>Public Member Functions</h3>
<p><code>AverageBMALeg</code> (const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>BMAIndex</code> &gt; &amp;index) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withNotionals</code> (<code>Real</code> notional) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withNotionals</code> (const std::vector&lt; <code>Real</code> &gt; &amp;notionals) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withPaymentDayCounter</code> (const <code>DayCounter</code> &amp;) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withPaymentAdjustment</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withGearings</code> (<code>Real</code> gearing) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withGearings</code> (const std::vector&lt; <code>Real</code> &gt; &amp;gearings) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withSpreads</code> (<code>Spread</code> spread) </p>
<p> <code>AverageBMALeg</code> &amp; <code>withSpreads</code> (const std::vector&lt; <code>Spread</code> &gt; &amp;spreads) </p>
<p> <code>operator Leg</code> () const</p>
<h2>Detailed Description</h2>
<p>helper class building a sequence of average BMA coupons</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
