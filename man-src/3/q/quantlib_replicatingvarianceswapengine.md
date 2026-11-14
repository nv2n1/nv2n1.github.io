---
title: "quantlib_replicatingvarianceswapengine(3)"
name: "quantlib_replicatingvarianceswapengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_replicatingvarianceswapengine/"
description: "QuantLib::ReplicatingVarianceSwapEngine – Variance-swap pricing engine using replicating cost,."
---

<p>QuantLib::ReplicatingVarianceSwapEngine &#8211; Variance-swap pricing engine using replicating cost,. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/forward/replicatingvarianceswapengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::VarianceSwap::engine</code>. </p>
<h3>Public Types</h3>
<p>typedef std::vector&lt; std::pair&lt; boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt;, Real &gt; &gt; <code>weights_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>ReplicatingVarianceSwapEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Real dk=5.0, const std::vector&lt; Real &gt; &amp;callStrikes=std::vector&lt; Real &gt;(), const std::vector&lt; Real &gt; &amp;putStrikes=std::vector&lt; Real &gt;()) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>computeOptionWeights</code> (const std::vector&lt; Real &gt; &amp;, const Option::Type, weights_type &amp;optionWeights) const </p>
<p> Real <code>computeLogPayoff</code> (const Real, const Real) const </p>
<p> Real <code>computeReplicatingPortfolio</code> (const weights_type &amp;optionWeights) const </p>
<p> <code>Rate</code> <code>riskFreeRate</code> () const </p>
<p> <code>DiscountFactor</code> <code>riskFreeDiscount</code> () const </p>
<p> Real <code>underlying</code> () const </p>
<p> <code>Time</code> <code>residualTime</code> () const </p>
<h2>Detailed Description</h2>
<p>Variance-swap pricing engine using replicating cost,. </p>
<p> as described in Demeterfi, Derman, Kamal &amp; Zou, &#8216;A Guide to Volatility and Variance Swaps&#8217;, 1999 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>returned variances verified against results from literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
