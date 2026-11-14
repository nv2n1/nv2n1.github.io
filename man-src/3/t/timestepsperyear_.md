---
title: "timestepsperyear_(3)"
name: "timestepsperyear_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timestepsperyear_/"
description: "QuantLib::MCVarianceSwapEngine – Variance-swap pricing engine using Monte Carlo simulation,."
---

<p>QuantLib::MCVarianceSwapEngine &#8211; Variance-swap pricing engine using Monte Carlo simulation,. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/pricingengines/forward/mcvarianceswapengine.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::VarianceSwap::engine</code>, and <code>McSimulation&lt; SingleVariate, RNG, S &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code></p>
<h3>Public Member Functions</h3>
<p><code>MCVarianceSwapEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> void <code>calculate</code> () const</p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<p> <code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> Size <code>timeSteps_</code> </p>
<p> Size <code>timeStepsPerYear_</code> </p>
<p> Size <code>requiredSamples_</code> </p>
<p> Size <code>maxSamples_</code> </p>
<p> Real <code>requiredTolerance_</code> </p>
<p> bool <code>brownianBridge_</code> </p>
<p> BigNatural <code>seed_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCVarianceSwapEngine&lt; RNG, S &gt;</h3>
<p>Variance-swap pricing engine using Monte Carlo simulation,. </p>
<p> as described in Demeterfi, Derman, Kamal &amp; Zou, &#8216;A Guide to Volatility and Variance Swaps&#8217;, 1999 </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>define tolerance of numerical integral and incorporate it in errorEstimate</dl>
<p> <code>Tests</code></p>
<dl>
<dd>returned fair variances checked for consistency with implied volatility curve.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
