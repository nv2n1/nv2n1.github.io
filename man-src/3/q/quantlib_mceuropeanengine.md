---
title: "quantlib_mceuropeanengine(3)"
name: "quantlib_mceuropeanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mceuropeanengine/"
description: "QuantLib::MCEuropeanEngine – European option pricing engine using Monte Carlo simulation."
---

<p>QuantLib::MCEuropeanEngine &#8211; European option pricing engine using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mceuropeanengine.hpp&gt; </p>
<p> Inherits <code>MCVanillaEngine&lt; SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCEuropeanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCEuropeanEngine&lt; RNG, S &gt;</h3>
<p>European option pricing engine using Monte Carlo simulation. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against analytic results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
