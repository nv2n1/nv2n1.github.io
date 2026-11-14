---
title: "optionlet(3)"
name: "optionlet"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionlet/"
description: "QuantLib::CapFloor – Base class for cap-like instruments."
---

<p>QuantLib::CapFloor &#8211; Base class for cap-like instruments. </p>
<h2>Synopsis</h2>
<pre><code>CapFloor (Type type, const Leg &amp;floatingLeg, const std::vector&lt; Rate &gt; &amp;capRates, const std::vector&lt; Rate &gt; &amp;floorRates)



CapFloor (Type type, const Leg &amp;floatingLeg, const std::vector&lt; Rate &gt; &amp;strikes)



Rate atmRate (const YieldTermStructure &amp;discountCurve) const



Volatility impliedVolatility (Real price, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, Volatility guess, Real accuracy=1.0e-4, Natural maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const


implied term volatility</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>. Inherited by <code>Cap</code>, <code>Collar</code>, and <code>Floor</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for cap/floor calculation </i><br />
 class <code>engine</code><br />
 <i>base class for cap/floor engines </i></p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Cap</code>, <code>Floor</code>, <code>Collar</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>CapFloor (Type type, const Leg &amp;floatingLeg, const std::vector&lt; Rate &gt; &amp;capRates, const std::vector&lt; Rate &gt; &amp;floorRates)



CapFloor (Type type, const Leg &amp;floatingLeg, const std::vector&lt; Rate &gt; &amp;strikes)



Rate atmRate (const YieldTermStructure &amp;discountCurve) const



Volatility impliedVolatility (Real price, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, Volatility guess, Real accuracy=1.0e-4, Natural maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const


implied term volatility</code></pre>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const<br />
 <code>Inspectors</code> </p>
<p> Type <code>type</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>capRates</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>floorRates</code> () const </p>
<p> const Leg &amp; <code>floatingLeg</code> () const </p>
<p> <code>Date</code> <code>startDate</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> () const </p>
<p> boost::shared_ptr&lt; <code>FloatingRateCoupon</code> &gt; <code>lastFloatingRateCoupon</code> () const </p>
<p> boost::shared_ptr&lt; <code>CapFloor</code> &gt; <code>optionlet</code> (const Size n) const<br />
 <i>Returns the n-th optionlet as a new </i><code>CapFloor</code> with only one cash flow.</p>
<h2>Detailed Description</h2>
<p>Base class for cap-like instruments. </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a cap (resp. floor) decreases (resp. increases) with the strike rate.</p>
<dt>*</p>
<dd>the relationship between the values of caps, floors and the resulting collars is checked.</p>
<dt>*</p>
<dd>the put-call parity between the values of caps, floors and swaps is checked.</p>
<dt>*</p>
<dd>the correctness of the returned implied volatility is tested by using it for reproducing the target value.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking it against a known good value.</dl>
</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
