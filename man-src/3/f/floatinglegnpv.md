---
title: "floatinglegnpv(3)"
name: "floatinglegnpv"
section: "3"
letter: "f"
url: "/docs/linux/man/3-floatinglegnpv/"
description: "QuantLib::VanillaSwap – Plain-vanilla swap."
---

<p>QuantLib::VanillaSwap &#8211; Plain-vanilla swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/vanillaswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Swap</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for simple swap calculation </i><br />
 class <code>results</code><br />
 <i>Results from simple swap calculation </i></p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Receiver</code> = -1, <code>Payer</code> = 1 } </p>
<h3>Public Member Functions</h3>
<p><code>VanillaSwap</code> (Type type, <code>Real</code> nominal, const <code>Schedule</code> &amp;fixedSchedule, <code>Rate</code> fixedRate, const <code>DayCounter</code> &amp;fixedDayCount, const <code>Schedule</code> &amp;floatSchedule, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, <code>Spread</code> spread, const <code>DayCounter</code> &amp;floatingDayCount, <code>BusinessDayConvention</code> paymentConvention=Following) </p>
<p> <code>Real</code> <code>fixedLegBPS</code> () const </p>
<p> <code>Real</code> <code>fixedLegNPV</code> () const </p>
<p> <code>Rate</code> <code>fairRate</code> () const </p>
<p> <code>Real</code> <code>floatingLegBPS</code> () const </p>
<p> <code>Real</code> <code>floatingLegNPV</code> () const </p>
<p> <code>Spread</code> <code>fairSpread</code> () const </p>
<p> Type <code>type</code> () const </p>
<p> <code>Real</code> <code>nominal</code> () const </p>
<p> const <code>Schedule</code> &amp; <code>fixedSchedule</code> () const </p>
<p> <code>Rate</code> <code>fixedRate</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>fixedDayCount</code> () const </p>
<p> const <code>Schedule</code> &amp; <code>floatingSchedule</code> () const </p>
<p> const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp; <code>iborIndex</code> () const </p>
<p> <code>Spread</code> <code>spread</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>floatingDayCount</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>paymentConvention</code> () const </p>
<p> const Leg &amp; <code>fixedLeg</code> () const </p>
<p> const Leg &amp; <code>floatingLeg</code> () const </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<h2>Detailed Description</h2>
<p>Plain-vanilla swap. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-rate and fair-spread calculation. This might not be what you want.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a swap paying the fair fixed rate is null.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a swap receiving the fair floating-rate spread is null.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a swap decreases with the paid fixed rate.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a swap increases with the received floating-rate spread.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking it against a known good value.</dl>
</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
