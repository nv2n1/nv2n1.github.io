---
title: "residualtime(3)"
name: "residualtime"
section: "3"
letter: "r"
url: "/docs/linux/man/3-residualtime/"
description: "QuantLib::ReplicatingVarianceSwapEngine – Variance-swap pricing engine using replicating cost,."
---

<p>QuantLib::ReplicatingVarianceSwapEngine &#8211; Variance-swap pricing engine using replicating cost,. </p>
<h2>Synopsis</h2>
<pre><code>ReplicatingVarianceSwapEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real dk=5.0, const std::vector&lt; Real &gt; &amp;callStrikes=std::vector&lt; Real &gt;(), const std::vector&lt; Real &gt; &amp;putStrikes=std::vector&lt; Real &gt;())



void calculate () const



Protected Member Functions
void computeOptionWeights (const std::vector&lt; Real &gt; &amp;, const Option::Type, weights_type &amp;optionWeights) const



Real computeLogPayoff (const Real, const Real) const



Real computeReplicatingPortfolio (const weights_type &amp;optionWeights) const



Rate riskFreeRate () const



DiscountFactor riskFreeDiscount () const



Real underlying () const



Time residualTime () const</code></pre>
<p> Inherits <code>QuantLib::VarianceSwap::engine</code>.</p>
<h3>Public Types</h3>
<p>typedef std::vector&lt; std::pair&lt; boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt;, Real &gt; &gt; <code>weights_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>ReplicatingVarianceSwapEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Real dk=5.0, const std::vector&lt; Real &gt; &amp;callStrikes=std::vector&lt; Real &gt;(), const std::vector&lt; Real &gt; &amp;putStrikes=std::vector&lt; Real &gt;())



void calculate () const



Protected Member Functions
void computeOptionWeights (const std::vector&lt; Real &gt; &amp;, const Option::Type, weights_type &amp;optionWeights) const



Real computeLogPayoff (const Real, const Real) const



Real computeReplicatingPortfolio (const weights_type &amp;optionWeights) const



Rate riskFreeRate () const



DiscountFactor riskFreeDiscount () const



Real underlying () const



Time residualTime () const</code></pre>
<h2>Detailed Description</h2>
<p>Variance-swap pricing engine using replicating cost,. </p>
<p> as described in Demeterfi, Derman, Kamal &amp; Zou, &#8216;A Guide to Volatility and Variance Swaps&#8217;, 1999 </p>
<p> <code>Tests</code></p>
<dl>
<dd>returned variances verified against results from literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
