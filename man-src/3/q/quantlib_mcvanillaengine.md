---
title: "quantlib_mcvanillaengine(3)"
name: "quantlib_mcvanillaengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcvanillaengine/"
description: "QuantLib::MCVanillaEngine – Pricing engine for vanilla options using Monte Carlo simulation."
---

<p>QuantLib::MCVanillaEngine &#8211; Pricing engine for vanilla options using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mcvanillaengine.hpp&gt; </p>
<p> Inherits Inst::engine, and <code>McSimulation&lt; MC, RNG, S &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>calculate</code> () const </p>
<h3>Protected Types</h3>
<p>typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::result_type <code>result_type</code> </p>
<h3>Protected Member Functions</h3>
<p><code>MCVanillaEngine</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> <code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const </p>
<p> result_type <code>controlVariateValue</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; <code>process_</code> </p>
<p> Size <code>timeSteps_</code> </p>
<p> Size <code>timeStepsPerYear_</code> </p>
<p> Size <code>requiredSamples_</code> </p>
<p> Size <code>maxSamples_</code> </p>
<p> Real <code>requiredTolerance_</code> </p>
<p> bool <code>brownianBridge_</code> </p>
<p> BigNatural <code>seed_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;template&lt; class &gt; class MC, class RNG, class S = Statistics, class Inst = VanillaOption&gt; class QuantLib::MCVanillaEngine&lt; MC, RNG, S, Inst &gt;</h3>
<p>Pricing engine for vanilla options using Monte Carlo simulation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
