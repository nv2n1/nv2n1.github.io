---
title: "amortizingfixedratebond(3)"
name: "amortizingfixedratebond"
section: "3"
letter: "a"
url: "/docs/linux/man/3-amortizingfixedratebond/"
description: "QuantLib::AmortizingFixedRateBond – amortizing fixed-rate bond"
---

<p>QuantLib::AmortizingFixedRateBond &#8211; amortizing fixed-rate bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/amortizingbonds/amortizingfixedratebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AmortizingFixedRateBond</code> (<code>Natural</code> settlementDays, const std::vector&lt; <code>Real</code> &gt; &amp;notionals, const <code>Schedule</code> &amp;schedule, const std::vector&lt; <code>Rate</code> &gt; &amp;coupons, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, const std::vector&lt; <code>Real</code> &gt; &amp;redemption=std::vector&lt; <code>Real</code> &gt;(1, 100.0), const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<p> <code>AmortizingFixedRateBond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp;startDate, const <code>Period</code> &amp;bondTenor, const <code>Frequency</code> &amp;sinkingFrequency, const <code>Rate</code> coupon, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<p> <code>Real</code> <code>IRR</code> () const </p>
<p> <code>Real</code> <code>cleanPriceFromIRR</code> (<code>Real</code> irr) const </p>
<p> <code>Frequency</code> <code>frequency</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>dayCounter</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Frequency</code> <code>frequency_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<h2>Detailed Description</h2>
<p>amortizing fixed-rate bond</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>AmortizingFixedRateBond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp; calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp; startDate, const <code>Period</code> &amp; bondTenor, const <code>Frequency</code> &amp; sinkingFrequency, const <code>Rate</code> coupon, const <code>DayCounter</code> &amp; accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention = Following, const <code>Date</code> &amp; issueDate = <code>Date</code>())</h3>
<p>Automatically generates a set of equal coupons, with an amortizing bond. The coupons are equal and the accrual daycount is only used for quoting/settlement purposes &#8211; not for calculating the coupons. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
