---
title: "quantlib_fixedratebond(3)"
name: "quantlib_fixedratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fixedratebond/"
description: "QuantLib::FixedRateBond – fixed-rate bond"
---

<p>QuantLib::FixedRateBond &#8211; fixed-rate bond </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/fixedratebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FixedRateBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Schedule</code> &amp;schedule, const std::vector&lt; <code>Rate</code> &gt; &amp;coupons, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<p> <code>FixedRateBond</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Real</code> faceAmount, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;maturityDate, const <code>Period</code> &amp;tenor, const std::vector&lt; <code>Rate</code> &gt; &amp;coupons, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> accrualConvention=Following, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const <code>Date</code> &amp;stubDate=<code>Date</code>(), <code>DateGeneration::Rule</code> rule=DateGeneration::Backward, bool endOfMonth=false) </p>
<p> <code>Frequency</code> <code>frequency</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>dayCounter</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Frequency</code> <code>frequency_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<h2>Detailed Description</h2>
<p>fixed-rate bond </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are tested by checking results against cached values.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, and <code>Repo.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
