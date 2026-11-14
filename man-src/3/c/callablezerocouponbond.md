---
title: "callablezerocouponbond(3)"
name: "callablezerocouponbond"
section: "3"
letter: "c"
url: "/docs/linux/man/3-callablezerocouponbond/"
description: "QuantLib::CallableZeroCouponBond – callable/puttable zero coupon bond"
---

<p>QuantLib::CallableZeroCouponBond &#8211; callable/puttable zero coupon bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/callablebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::CallableFixedRateBond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CallableZeroCouponBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Calendar</code> &amp;calendar, const <code>Date</code> &amp;maturityDate, const <code>DayCounter</code> &amp;dayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule()) </p>
<h2>Detailed Description</h2>
<p>callable/puttable zero coupon bond </p>
<p> Callable zero coupon bond class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
