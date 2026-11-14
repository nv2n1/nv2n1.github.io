---
title: "engine(3)"
name: "engine"
section: "3"
letter: "e"
url: "/docs/linux/man/3-engine/"
description: "QuantLib::QuantoVanillaOption – quanto version of a vanilla option"
---

<h2 class="name">NAME</h2>
<p> QuantLib::QuantoVanillaOption &#8211; quanto version of a vanilla option </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/quantovanillaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<h3>Public Types</h3>
<p> typedef <code>OneAssetOption::arguments</code> <code>arguments</code> </p>
<p> typedef <code>QuantoOptionResults</code>&lt; <code>OneAssetOption::results</code> &gt; <code>results</code> </p>
<p> typedef <code>GenericEngine</code>&lt; <code>arguments</code>, results &gt; <code>engine</code> </p>
<h3>Public Member Functions</h3>
<p> <code>QuantoVanillaOption</code> (const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;) </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<p> <code>greeks</code> </p>
<p> <code>Real</code> <code>qvega</code> () const </p>
<p> <code>Real</code> <code>qrho</code> () const </p>
<p> <code>Real</code> <code>qlambda</code> () const </p>
<h2>Detailed Description</h2>
<p> quanto version of a vanilla option </p>
<h2>Member Function Documentation</h2>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p> When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>OneAssetOption</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
