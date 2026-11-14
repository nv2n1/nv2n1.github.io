---
title: "arguments(3)"
name: "arguments"
section: "3"
letter: "a"
url: "/docs/linux/man/3-arguments/"
description: "QuantLib::ForwardVanillaOption – Forward version of a vanilla option"
---

<h2 class="name">NAME</h2>
<p> QuantLib::ForwardVanillaOption &#8211; Forward version of a vanilla option </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/forwardvanillaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<p> Inherited by <code>QuantoForwardVanillaOption</code>. </p>
<h3>Public Types</h3>
<p> typedef <code>ForwardOptionArguments</code>&lt; <code>OneAssetOption::arguments</code> &gt; <code>arguments</code> </p>
<p> typedef <code>OneAssetOption::results</code> <code>results</code> </p>
<h3>Public Member Functions</h3>
<p> <code>ForwardVanillaOption</code> (<code>Real</code> moneyness, const <code>Date</code> &amp;resetDate, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<h2>Detailed Description</h2>
<p> Forward version of a vanilla option </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p> When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Option</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p> When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>OneAssetOption</code>. </p>
<p> Reimplemented in <code>QuantoForwardVanillaOption</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
