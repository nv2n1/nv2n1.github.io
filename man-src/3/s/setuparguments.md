---
title: "setuparguments(3)"
name: "setuparguments"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setuparguments/"
description: "QuantLib::CallableBond – Callable bond base class."
---

<p>QuantLib::CallableBond &#8211; Callable bond base class. </p>
<h2>Synopsis</h2>
<pre><code>CallableBond (Natural settlementDays, Real faceAmount, const Schedule &amp;schedule, const DayCounter &amp;paymentDayCounter, BusinessDayConvention paymentConvention=Following, Real redemption=100.0, const Date &amp;issueDate=Date(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule())



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Bond</code>. Inherited by <code>CallableFixedRateBond</code>.</p>
<h3>Classes</h3>
<p>class <code>engine</code><br />
 <i>base class for callable fixed rate bond </i><code>engine</code><br />
 class <code>results</code><br />
 <i></i><code>results</code> for a callable bond calculation</p>
<h3>Public Member Functions</h3>
<p>virtual void <code>setupArguments</code> (PricingEngine::arguments *args) const<br />
 <code>Inspectors</code><br />
 CallableBond (Natural settlementDays, Real faceAmount, const Schedule &amp;schedule, const DayCounter &amp;paymentDayCounter, BusinessDayConvention paymentConvention=Following, Real redemption=100.0, const Date &amp;issueDate=Date(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule())</p>
<p>Protected Attributes <code>Calculations</code> </p>
<p> <code>Volatility</code> <code>impliedVolatility</code> (<code>Real</code> targetValue, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, <code>Real</code> accuracy, Size maxEvaluations, <code>Volatility</code> minVol, <code>Volatility</code> maxVol) const<br />
 <i>returns the Black implied forward yield volatility </i></p>
<h3>Protected Member Functions</h3>
<pre><code>CallableBond (Natural settlementDays, Real faceAmount, const Schedule &amp;schedule, const DayCounter &amp;paymentDayCounter, BusinessDayConvention paymentConvention=Following, Real redemption=100.0, const Date &amp;issueDate=Date(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule())



Protected Attributes</code></pre>
<p> <code>DayCounter</code> <code>paymentDayCounter_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> CallabilitySchedule <code>putCallSchedule_</code> </p>
<p> boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>blackEngine_</code><br />
 <i>must be set by derived classes for </i><code>impliedVolatility()</code> to work<br />
 <code>RelinkableHandle</code>&lt; <code>Quote</code> &gt; <code>blackVolQuote_</code><br />
 <i>Black fwd yield volatility quote handle to internal blackEngine_. </i><br />
 <code>RelinkableHandle</code>&lt; <code>YieldTermStructure</code> &gt; <code>blackDiscountCurve_</code><br />
 <i>Black fwd yield volatility quote handle to internal blackEngine_. </i></p>
<h3>Friends</h3>
<p>class <code>ImpliedVolHelper</code></p>
<h2>Detailed Description</h2>
<p>Callable bond base class. </p>
<p> Base callable bond class for fixed and zero coupon bonds. Defines commonalities between fixed and zero coupon callable bonds. At present, only European and Bermudan put/call schedules supported (no American optionality), as defined by the <code>Callability</code> class. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>models/shortrate/calibrationHelpers </p>
<p> OAS/OAD </p>
<p> floating rate callable bonds ?</dl>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> impliedVolatility (<code>Real</code> targetValue, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; discountCurve, <code>Real</code> accuracy, Size maxEvaluations, <code>Volatility</code> minVol, <code>Volatility</code> maxVol) const</h3>
<p>returns the Black implied forward yield volatility </p>
<p> the forward yield volatility, see Hull, Fourth Edition, Chapter 20, pg 536). Relevant only to European put/call schedules</p>
<h3>virtual void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Bond</code>. </p>
<p> Reimplemented in <code>CallableFixedRateBond</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
