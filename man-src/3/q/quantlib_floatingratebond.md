---
title: "quantlib_floatingratebond(3)"
name: "quantlib_floatingratebond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_floatingratebond/"
description: "QuantLib::FloatingRateBond – floating-rate bond (possibly capped and/or floored)"
---

<p>QuantLib::FloatingRateBond &#8211; floating-rate bond (possibly capped and/or floored) </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/bonds/floatingratebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FloatingRateBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Schedule</code> &amp;schedule, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Natural</code> fixingDays=<code>Null</code>&lt; <code>Natural</code> &gt;(), const std::vector&lt; <code>Real</code> &gt; &amp;gearings=std::vector&lt; <code>Real</code> &gt;(1, 1.0), const std::vector&lt; <code>Spread</code> &gt; &amp;spreads=std::vector&lt; <code>Spread</code> &gt;(1, 0.0), const std::vector&lt; <code>Rate</code> &gt; &amp;caps=std::vector&lt; <code>Rate</code> &gt;(), const std::vector&lt; <code>Rate</code> &gt; &amp;floors=std::vector&lt; <code>Rate</code> &gt;(), bool inArrears=false, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>()) </p>
<p> <code>FloatingRateBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;maturityDate, <code>Frequency</code> couponFrequency, const <code>Calendar</code> &amp;calendar, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const <code>DayCounter</code> &amp;accrualDayCounter, <code>BusinessDayConvention</code> accrualConvention=Following, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Natural</code> fixingDays=<code>Null</code>&lt; <code>Natural</code> &gt;(), const std::vector&lt; <code>Real</code> &gt; &amp;gearings=std::vector&lt; <code>Real</code> &gt;(1, 1.0), const std::vector&lt; <code>Spread</code> &gt; &amp;spreads=std::vector&lt; <code>Spread</code> &gt;(1, 0.0), const std::vector&lt; <code>Rate</code> &gt; &amp;caps=std::vector&lt; <code>Rate</code> &gt;(), const std::vector&lt; <code>Rate</code> &gt; &amp;floors=std::vector&lt; <code>Rate</code> &gt;(), bool inArrears=false, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const <code>Date</code> &amp;stubDate=<code>Date</code>(), <code>DateGeneration::Rule</code> rule=DateGeneration::Backward, bool endOfMonth=false) </p>
<h2>Detailed Description</h2>
<p>floating-rate bond (possibly capped and/or floored) </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are tested by checking results against cached values.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
