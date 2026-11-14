---
title: "quantlib_mclongstaffschwartzengine(3)"
name: "quantlib_mclongstaffschwartzengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mclongstaffschwartzengine/"
description: "QuantLib::MCLongstaffSchwartzEngine – Longstaff-Schwarz Monte Carlo engine for early exercise options."
---

<p>QuantLib::MCLongstaffSchwartzEngine &#8211; Longstaff-Schwarz Monte Carlo engine for early exercise options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/mclongstaffschwartzengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::GenericEngine</code>, and <code>McSimulation&lt; MC, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef MC&lt; RNG &gt;::path_type <code>path_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; MC, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCLongstaffSchwartzEngine</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;process, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed, Size nCalibrationSamples=<code>Null</code>&lt; Size &gt;()) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual boost::shared_ptr&lt; <code>LongstaffSchwartzPathPricer</code>&lt; path_type &gt; &gt; <code>lsmPathPricer</code> () const =0 </p>
<p> <code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<p> boost::shared_ptr&lt; path_generator_type &gt; <code>pathGenerator</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; <code>process_</code> </p>
<p> const Size <code>timeSteps_</code> </p>
<p> const Size <code>timeStepsPerYear_</code> </p>
<p> const bool <code>brownianBridge_</code> </p>
<p> const Size <code>requiredSamples_</code> </p>
<p> const Real <code>requiredTolerance_</code> </p>
<p> const Size <code>maxSamples_</code> </p>
<p> const Size <code>seed_</code> </p>
<p> const Size <code>nCalibrationSamples_</code> </p>
<p> boost::shared_ptr&lt; <code>LongstaffSchwartzPathPricer</code>&lt; path_type &gt; &gt; <code>pathPricer_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class GenericEngine, template&lt; class &gt; class MC, class RNG, class S = Statistics&gt; class QuantLib::MCLongstaffSchwartzEngine&lt; GenericEngine, MC, RNG, S &gt;</h3>
<p>Longstaff-Schwarz Monte Carlo engine for early exercise options. </p>
<p> References: </p>
<p> Francis Longstaff, Eduardo Schwartz, 2001. Valuing American Options by Simulation: A Simple Least-Squares Approach, The Review of Financial Studies, Volume 14, No. 1, 113-147 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
