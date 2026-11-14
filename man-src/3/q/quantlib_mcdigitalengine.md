---
title: "quantlib_mcdigitalengine(3)"
name: "quantlib_mcdigitalengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcdigitalengine/"
description: "QuantLib::MCDigitalEngine – Pricing engine for digital options using Monte Carlo simulation."
---

<p>QuantLib::MCDigitalEngine &#8211; Pricing engine for digital options using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mcdigitalengine.hpp&gt; </p>
<p> Inherits <code>MCVanillaEngine&lt; SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>MCVanillaEngine</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCDigitalEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCDigitalEngine&lt; RNG, S &gt;</h3>
<p>Pricing engine for digital options using Monte Carlo simulation. </p>
<p> Uses the Brownian Bridge correction for the barrier found in <i> Going to Extremes: Correcting Simulation Bias in Exotic </i><code>Option</code> Valuation &#8211; D.R. Beaglehole, P.H. Dybvig and G. Zhou Financial Analysts Journal; Jan/Feb 1997; 53, 1. pg. 62-68 and <i> Simulating path-dependent options: A new approach &#8211; M. El Babsiri and G. Noel Journal of Derivatives; Winter 1998; 6, 2; pg. 65-83 </i> </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value in case of cash-or-nothing at-hit digital payoff is tested by reproducing known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
