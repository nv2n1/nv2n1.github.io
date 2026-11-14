---
title: "quantlib_mcpagodaengine(3)"
name: "quantlib_mcpagodaengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcpagodaengine/"
description: "QuantLib::MCPagodaEngine – Pricing engine for pagoda options using Monte Carlo simulation."
---

<p>QuantLib::MCPagodaEngine &#8211; Pricing engine for pagoda options using Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/basket/mcpagodaengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::PagodaOption::engine</code>, and <code>McSimulation&lt; MultiVariate, RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>McSimulation</code>&lt; <code>MultiVariate</code>, RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCPagodaEngine</code> (const boost::shared_ptr&lt; <code>StochasticProcessArray</code> &gt; &amp;, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCPagodaEngine&lt; RNG, S &gt;</h3>
<p>Pricing engine for pagoda options using Monte Carlo simulation. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
