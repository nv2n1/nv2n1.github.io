---
title: "quantlib_callablefixedratebond(3)"
name: "quantlib_callablefixedratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_callablefixedratebond/"
description: "QuantLib::CallableFixedRateBond – callable/puttable fixed rate bond"
---

<p>QuantLib::CallableFixedRateBond &#8211; callable/puttable fixed rate bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/callablebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::CallableBond</code>. </p>
<p> Inherited by <code>CallableZeroCouponBond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CallableFixedRateBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Schedule</code> &amp;schedule, const std::vector&lt; <code>Rate</code> &gt; &amp;coupons, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule()) </p>
<p> virtual void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<h2>Detailed Description</h2>
<p>callable/puttable fixed rate bond </p>
<p> Callable fixed rate bond class. </p>
<p> <code> Example: </code> <code>CallableBonds.cpp</code> </p>
<p> <code>Examples: </code> </p>
<p> <code>CallableBonds.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>CallableBond</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
