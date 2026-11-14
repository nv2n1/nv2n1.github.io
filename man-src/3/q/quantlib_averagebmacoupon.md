---
title: "quantlib_averagebmacoupon(3)"
name: "quantlib_averagebmacoupon"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_averagebmacoupon/"
description: "QuantLib::AverageBMACoupon – Average BMA coupon."
---

<p>QuantLib::AverageBMACoupon &#8211; <code>Average</code> BMA coupon. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/averagebmacoupon.hpp&gt; </p>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AverageBMACoupon</code> (const <code>Date</code> &amp;paymentDate, <code>Real</code> nominal, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate, const boost::shared_ptr&lt; <code>BMAIndex</code> &gt; &amp;index, <code>Real</code> gearing=1.0, <code>Spread</code> spread=0.0, const <code>Date</code> &amp;refPeriodStart=<code>Date</code>(), const <code>Date</code> &amp;refPeriodEnd=<code>Date</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>()) </p>
<p> <code>FloatingRateCoupon interface</code> </p>
<p> <code>Date</code> <code>fixingDate</code> () const<br />
 <i>not applicable here; use </i><code>fixingDates()</code> instead<br />
 std::vector&lt; <code>Date</code> &gt; <code>fixingDates</code> () const<br />
 <i>fixing dates of the rates to be averaged </i><br />
 <code>Rate</code> <code>indexFixing</code> () const<br />
 <i>not applicable here; use </i><code>indexFixings()</code> instead<br />
 std::vector&lt; <code>Rate</code> &gt; <code>indexFixings</code> () const<br />
 <i>fixings of the underlying index to be averaged </i><br />
 <code>Rate</code> <code>convexityAdjustment</code> () const<br />
 <i>not applicable here </i> </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p><code>Average</code> BMA coupon. </p>
<p> Coupon paying a BMA index, where the coupon rate is a weighted average of relevant fixings. </p>
<p> The weighted average is computed based on the actual calendar days for which a given fixing is valid and contributing to the given interest period. </p>
<p> Before weights are computed, the fixing schedule is adjusted for the index&#8217;s fixing day gap. See <code>rate()</code> method for details. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
