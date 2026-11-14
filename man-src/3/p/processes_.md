---
title: "processes_(3)"
name: "processes_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-processes_/"
description: "QuantLib::MCBasketEngine – Pricing engine for basket options using Monte Carlo simulation."
---

<p>QuantLib::MCBasketEngine &#8211; Pricing engine for basket options using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/pricingengines/basket/mcbasketengine.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::BasketOption::engine</code>, and <code>McSimulation&lt; MultiVariate, RNG, S &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code></p>
<h3>Public Member Functions</h3>
<p><code>MCBasketEngine</code> (const boost::shared_ptr&lt; <code>StochasticProcessArray</code> &gt; &amp;, Size maxTimeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> void <code>calculate</code> () const</p>
<h3>Protected Member Functions</h3>
<p><code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const </p>
<p> boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>StochasticProcessArray</code> &gt; <code>processes_</code> </p>
<p> Size <code>maxTimeStepsPerYear_</code> </p>
<p> Size <code>requiredSamples_</code> </p>
<p> Size <code>maxSamples_</code> </p>
<p> Real <code>requiredTolerance_</code> </p>
<p> bool <code>brownianBridge_</code> </p>
<p> BigNatural <code>seed_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCBasketEngine&lt; RNG, S &gt;</h3>
<p>Pricing engine for basket options using Monte Carlo simulation. </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
