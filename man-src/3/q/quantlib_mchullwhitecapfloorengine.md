---
title: "quantlib_mchullwhitecapfloorengine(3)"
name: "quantlib_mchullwhitecapfloorengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mchullwhitecapfloorengine/"
description: "QuantLib::MCHullWhiteCapFloorEngine – Monte Carlo Hull-White engine for cap/floors."
---

<p>QuantLib::MCHullWhiteCapFloorEngine &#8211; Monte Carlo Hull-White engine for cap/floors. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/capfloor/mchullwhiteengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::CapFloor::engine</code>, and <code>McSimulation&lt; SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>simulation::path_generator_type</code> <code>path_generator_type</code> </p>
<p> typedef <code>simulation::path_pricer_type</code> <code>path_pricer_type</code> </p>
<p> typedef simulation::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCHullWhiteCapFloorEngine</code> (const boost::shared_ptr&lt; <code>HullWhite</code> &gt; &amp;model, bool brownianBridge, bool antitheticVariate, Size requiredSamples, <code>Real</code> requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>path_pricer_type</code> &gt; <code>pathPricer</code> () const </p>
<p> <code>TimeGrid</code> <code>timeGrid</code> () const </p>
<p> boost::shared_ptr&lt; <code>path_generator_type</code> &gt; <code>pathGenerator</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCHullWhiteCapFloorEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo Hull-White engine for cap/floors. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
