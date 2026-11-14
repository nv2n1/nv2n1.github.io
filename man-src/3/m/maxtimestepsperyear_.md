---
title: "maxtimestepsperyear_(3)"
name: "maxtimestepsperyear_"
section: "3"
letter: "m"
url: "/docs/linux/man/3-maxtimestepsperyear_/"
description: "QuantLib::MCDiscreteAveragingAsianEngine – Pricing engine for discrete average Asians using Monte Carlo simulation."
---

<p>QuantLib::MCDiscreteAveragingAsianEngine &#8211; Pricing engine for discrete average Asians using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/asian/mcdiscreteasianengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::DiscreteAveragingAsianOption::engine</code>, and <code>McSimulation&lt; SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>SingleVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCDiscreteAveragingAsianEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size maxTimeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const </p>
<p> Real <code>controlVariateValue</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> Size <code>maxTimeStepsPerYear_</code> </p>
<p> Size <code>requiredSamples_</code> </p>
<p> Size <code>maxSamples_</code> </p>
<p> Real <code>requiredTolerance_</code> </p>
<p> bool <code>brownianBridge_</code> </p>
<p> BigNatural <code>seed_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCDiscreteAveragingAsianEngine&lt; RNG, S &gt;</h3>
<p>Pricing engine for discrete average Asians using Monte Carlo simulation. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>control-variate calculation is disabled under VC++6.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
