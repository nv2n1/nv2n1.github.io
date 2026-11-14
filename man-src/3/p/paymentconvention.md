---
title: "paymentconvention(3)"
name: "paymentconvention"
section: "3"
letter: "p"
url: "/docs/linux/man/3-paymentconvention/"
description: "QuantLib::VanillaSwap – Plain-vanilla swap."
---

<p>QuantLib::VanillaSwap &#8211; Plain-vanilla swap. </p>
<h2>Synopsis</h2>
<pre><code>enum Type { Receiver = -1,
            Payer = 1 }

Public Member Functions
VanillaSwap(Type type, Real nominal, const Schedule &amp;fixedSchedule, Rate fixedRate, const DayCounter &amp;fixedDayCount, const Schedule &amp;floatSchedule, const boost::shared_ptr&lt;IborIndex&gt; &amp;iborIndex, Spread spread, const DayCounter &amp;floatingDayCount, BusinessDayConvention paymentConvention = Following)

    Real fixedLegBPS() const

    Real fixedLegNPV() const

    Rate fairRate() const

    Real floatingLegBPS() const

    Real floatingLegNPV() const

    Spread fairSpread() const

    Type type() const

    Real nominal() const

    const Schedule &amp;fixedSchedule() const

    Rate fixedRate() const

    const DayCounter &amp;fixedDayCount() const

    const Schedule &amp;floatingSchedule() const

    const boost::shared_ptr&lt;IborIndex&gt; &amp;iborIndex() const

    Spread spread() const

    const DayCounter &amp;floatingDayCount() const

    BusinessDayConvention paymentConvention() const

    const Leg &amp;fixedLeg() const

    const Leg &amp;floatingLeg() const

    void setupArguments(PricingEngine::arguments *args) const

    void fetchResults(const PricingEngine::results *) const</code></pre>
<p> Inherits <code>QuantLib::Swap</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for simple swap calculation </i><br />
 class <code>results</code><br />
 <i>Results from simple swap calculation </i></p>
<h3>Public Types</h3>
<pre><code>enum Type { Receiver = -1,
            Payer = 1 }

Public Member Functions
VanillaSwap(Type type, Real nominal, const Schedule &amp;fixedSchedule, Rate fixedRate, const DayCounter &amp;fixedDayCount, const Schedule &amp;floatSchedule, const boost::shared_ptr&lt;IborIndex&gt; &amp;iborIndex, Spread spread, const DayCounter &amp;floatingDayCount, BusinessDayConvention paymentConvention = Following)

    Real fixedLegBPS() const

    Real fixedLegNPV() const

    Rate fairRate() const

    Real floatingLegBPS() const

    Real floatingLegNPV() const

    Spread fairSpread() const

    Type type() const

    Real nominal() const

    const Schedule &amp;fixedSchedule() const

    Rate fixedRate() const

    const DayCounter &amp;fixedDayCount() const

    const Schedule &amp;floatingSchedule() const

    const boost::shared_ptr&lt;IborIndex&gt; &amp;iborIndex() const

    Spread spread() const

    const DayCounter &amp;floatingDayCount() const

    BusinessDayConvention paymentConvention() const

    const Leg &amp;fixedLeg() const

    const Leg &amp;floatingLeg() const

    void setupArguments(PricingEngine::arguments *args) const

    void fetchResults(const PricingEngine::results *) const</code></pre>
<h2>Detailed Description</h2>
<p>Plain-vanilla swap. </p>
<p> <code>Warning</code></p>
<dl>
<dd>if QL_TODAYS_PAYMENTS was defined (in userconfig.hpp or when calling ./configure; it is undefined by default) payments occurring at the settlement date of the swap are included in the NPV, and therefore affect the fair-rate and fair-spread calculation. This might not be what you want.</dl>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
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
<p> Reimplemented from <code>Swap</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
