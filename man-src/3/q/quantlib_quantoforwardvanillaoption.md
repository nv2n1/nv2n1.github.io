---
title: "quantlib_quantoforwardvanillaoption(3)"
name: "quantlib_quantoforwardvanillaoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_quantoforwardvanillaoption/"
description: "QuantLib::QuantoForwardVanillaOption – Quanto version of a forward vanilla option."
---

<p>QuantLib::QuantoForwardVanillaOption &#8211; Quanto version of a forward vanilla option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/quantoforwardvanillaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::ForwardVanillaOption</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>ForwardVanillaOption::arguments</code> <code>arguments</code> </p>
<p> typedef <code>QuantoOptionResults</code>&lt; <code>ForwardVanillaOption::results</code> &gt; <code>results</code> </p>
<h3>Public Member Functions</h3>
<p><code>QuantoForwardVanillaOption</code> (<code>Real</code> moneyness, const <code>Date</code> &amp;resetDate, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;) </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<p> <code>greeks</code> </p>
<p> <code>Real</code> <code>qvega</code> () const </p>
<p> <code>Real</code> <code>qrho</code> () const </p>
<p> <code>Real</code> <code>qlambda</code> () const </p>
<h2>Detailed Description</h2>
<p>Quanto version of a forward vanilla option. </p>
<h2>Member Function Documentation</h2>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>ForwardVanillaOption</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
