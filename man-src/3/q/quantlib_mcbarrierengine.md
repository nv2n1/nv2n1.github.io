---
title: "quantlib_mcbarrierengine(3)"
name: "quantlib_mcbarrierengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcbarrierengine/"
description: "QuantLib::MCBarrierEngine – Pricing engine for barrier options using Monte Carlo simulation."
---

<p>QuantLib::MCBarrierEngine &#8211; Pricing engine for barrier options using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/barrier/mcbarrierengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::BarrierOption::engine</code>, and <code>McSimulation&lt; SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCBarrierEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size maxTimeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, bool isBiased, BigNatural seed) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const </p>
<p> boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> Size <code>maxTimeStepsPerYear_</code> </p>
<p> Size <code>requiredSamples_</code> </p>
<p> Size <code>maxSamples_</code> </p>
<p> Real <code>requiredTolerance_</code> </p>
<p> bool <code>isBiased_</code> </p>
<p> bool <code>brownianBridge_</code> </p>
<p> BigNatural <code>seed_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCBarrierEngine&lt; RNG, S &gt;</h3>
<p>Pricing engine for barrier options using Monte Carlo simulation. </p>
<p> Uses the Brownian-bridge correction for the barrier found in <i> Going to Extremes: Correcting Simulation Bias in Exotic </i><code>Option</code> Valuation &#8211; D.R. Beaglehole, P.H. Dybvig and G. Zhou Financial Analysts Journal; Jan/Feb 1997; 53, 1. pg. 62-68 and <i> Simulating path-dependent options: A new approach &#8211; M. El Babsiri and G. Noel Journal of Derivatives; Winter 1998; 6, 2; pg. 65-83 </i> </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
