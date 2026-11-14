---
title: "frequency_(3)"
name: "frequency_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-frequency_/"
---

<h2 class="name">NAME</h2>
 

 QuantLib::AmortizingFixedRateBond - amortizing fixed-rate bond 

<h2>SYNOPSIS</h2>

 
 

 #include &lt;ql/experimental/amortizingbonds/amortizingfixedratebond.hpp&gt; 

 Inherits <b>QuantLib::Bond</b>. 

<h3>Public Member Functions</h3>

 

 
 <b>AmortizingFixedRateBond</b> (<b>Natural</b> settlementDays, const std::vector&lt; <b>Real</b> &gt; &amp;notionals, const <b>Schedule</b> &amp;schedule, const std::vector&lt; <b>Rate</b> &gt; &amp;coupons, const <b>DayCounter</b> &amp;accrualDayCounter, <b>BusinessDayConvention</b> paymentConvention=Following, const std::vector&lt; <b>Real</b> &gt; &amp;redemption=std::vector&lt; <b>Real</b> &gt;(1, 100.0), const <b>Date</b> &amp;issueDate=<b>Date</b>()) 
 
 <b>AmortizingFixedRateBond</b> (<b>Natural</b> settlementDays, const <b>Calendar</b> &amp;calendar, <b>Real</b> faceAmount, const <b>Date</b> &amp;startDate, const <b>Period</b> &amp;bondTenor, const <b>Frequency</b> &amp;sinkingFrequency, const <b>Rate</b> coupon, const <b>DayCounter</b> &amp;accrualDayCounter, <b>BusinessDayConvention</b> paymentConvention=Following, const <b>Date</b> &amp;issueDate=<b>Date</b>()) 
 
 <b>Real</b> <b>IRR</b> () const 
 
 <b>Real</b> <b>cleanPriceFromIRR</b> (<b>Real</b> irr) const 
 
 <b>Frequency</b> <b>frequency</b> () const 
 
 const <b>DayCounter</b> &amp; <b>dayCounter</b> () const 

<h3>Protected Attributes</h3>

 

 
 <b>Frequency</b> <b>frequency_</b> 
 
 <b>DayCounter</b> <b>dayCounter_</b> 

<h2>Detailed Description</h2>

 

 amortizing fixed-rate bond

<h2>Constructor &amp; Destructor Documentation</h2>

 

<h3><b>AmortizingFixedRateBond</b> (<b>Natural</b> settlementDays, const <b>Calendar</b> &amp; calendar, <b>Real</b> faceAmount, const <b>Date</b> &amp; startDate, const <b>Period</b> &amp; bondTenor, const <b>Frequency</b> &amp; sinkingFrequency, const <b>Rate</b> coupon, const <b>DayCounter</b> &amp; accrualDayCounter, <b>BusinessDayConvention</b> paymentConvention = Following, const <b>Date</b> &amp; issueDate = <b>Date</b>())</h3>

 

 Automatically generates a set of equal coupons, with an amortizing bond. The coupons are equal and the accrual daycount is only used for quoting/settlement purposes - not for calculating the coupons. 

<h2>Author</h2>

 

 Generated automatically by Doxygen for QuantLib from the source code. 

<h2>Index</h2>



<dt><a HREF="#lbAI">Author</a>
<dd></dl>
