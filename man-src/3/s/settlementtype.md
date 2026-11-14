---
title: "settlementtype(3)"
name: "settlementtype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-settlementtype/"
description: "QuantLib::Swaption – Swaption class"
---

<p>QuantLib::Swaption &#8211; Swaption class </p>
<h2>Synopsis</h2>
<pre><code>Swaption (const boost::shared_ptr&lt; VanillaSwap &gt; &amp;swap, const boost::shared_ptr&lt; Exercise &gt; &amp;exercise, Settlement::Type delivery=Settlement::Physical)



Volatility impliedVolatility (Real price, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, Volatility guess, Real accuracy=1.0e-4, Natural maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const


implied volatility</code></pre>
<p> Inherits <code>QuantLib::Option</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for swaption calculation </i><br />
 class <code>engine</code><br />
 <i>base class for swaption engines </i></p>
<h3>Public Member Functions</h3>
<pre><code>Swaption (const boost::shared_ptr&lt; VanillaSwap &gt; &amp;swap, const boost::shared_ptr&lt; Exercise &gt; &amp;exercise, Settlement::Type delivery=Settlement::Physical)



Volatility impliedVolatility (Real price, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, Volatility guess, Real accuracy=1.0e-4, Natural maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const


implied volatility</code></pre>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const<br />
 <code>Inspectors</code> </p>
<p> Settlement::Type <code>settlementType</code> () const </p>
<p> VanillaSwap::Type <code>type</code> () const </p>
<p> const boost::shared_ptr&lt; <code>VanillaSwap</code> &gt; &amp; <code>underlyingSwap</code> () const</p>
<h2>Detailed Description</h2>
<p>Swaption class </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a payer (resp. receiver) swaption decreases (resp. increases) with the strike.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking that the price of a payer (resp. receiver) swaption increases (resp. decreases) with the spread.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking it against that of a swaption on a swap with no spread and a correspondingly adjusted fixed rate.</p>
<dt>*</p>
<dd>the correctness of the returned value is tested by checking it against a known good value.</p>
<dt>*</p>
<dd>the correctness of the returned value of cash settled swaptions is tested by checking the modified annuity against a value calculated without using the <code>Swaption</code> class.</dl>
</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add greeks and explicit exercise lag</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
