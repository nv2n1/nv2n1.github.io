---
title: "blackengine_(3)"
name: "blackengine_"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackengine_/"
description: "QuantLib::CallableBond – Callable bond base class."
---

<p>QuantLib::CallableBond &#8211; Callable bond base class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/callablebond.hpp&gt; </p>
<p> Inherits <code>QuantLib::Bond</code>. </p>
<p> Inherited by <code>CallableFixedRateBond</code>. </p>
<h3>Classes</h3>
<p>class <code>engine</code><br />
 <i>base class for callable fixed rate bond </i><code>engine</code><br />
 class <code>results</code><br />
 <i></i><code>results</code> for a callable bond calculation</p>
<h3>Public Member Functions</h3>
<p>virtual void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<p> <code>Inspectors</code> </p>
<p> const CallabilitySchedule &amp; <code>callability</code> () const<br />
 <i>return the bond&#8217;s put/call schedule </i> </p>
<p> <code>Calculations</code> </p>
<p> <code>Volatility</code> <code>impliedVolatility</code> (<code>Real</code> targetValue, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, <code>Real</code> accuracy, Size maxEvaluations, <code>Volatility</code> minVol, <code>Volatility</code> maxVol) const<br />
 <i>returns the Black implied forward yield volatility </i></p>
<h3>Protected Member Functions</h3>
<p><code>CallableBond</code> (<code>Natural</code> settlementDays, <code>Real</code> faceAmount, const <code>Schedule</code> &amp;schedule, const <code>DayCounter</code> &amp;paymentDayCounter, <code>BusinessDayConvention</code> paymentConvention=Following, <code>Real</code> redemption=100.0, const <code>Date</code> &amp;issueDate=<code>Date</code>(), const CallabilitySchedule &amp;putCallSchedule=CallabilitySchedule()) </p>
<h3>Protected Attributes</h3>
<p><code>DayCounter</code> <code>paymentDayCounter_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> CallabilitySchedule <code>putCallSchedule_</code> </p>
<p> boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>blackEngine_</code><br />
 <i>must be set by derived classes for </i><code>impliedVolatility()</code> to work<br />
 <code>RelinkableHandle</code>&lt; <code>Quote</code> &gt; <code>blackVolQuote_</code><br />
 <i>Black fwd yield volatility quote handle to internal blackEngine_. </i><br />
 <code>RelinkableHandle</code>&lt; <code>YieldTermStructure</code> &gt; <code>blackDiscountCurve_</code><br />
 <i>Black fwd yield volatility quote handle to internal blackEngine_. </i></p>
<h3>Friends</h3>
<p>class <code>ImpliedVolHelper</code> </p>
<h2>Detailed Description</h2>
<p>Callable bond base class. </p>
<p> Base callable bond class for fixed and zero coupon bonds. Defines commonalities between fixed and zero coupon callable bonds. At present, only European and Bermudan put/call schedules supported (no American optionality), as defined by the <code>Callability</code> class. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
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
<p> Reimplemented in <code>CallableFixedRateBond</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
