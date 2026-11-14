---
title: "mcdiscretegeometricapengine(3)"
name: "mcdiscretegeometricapengine"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mcdiscretegeometricapengine/"
description: "QuantLib::MCDiscreteGeometricAPEngine – Monte Carlo pricing engine for discrete geometric average price Asian."
---

<p>QuantLib::MCDiscreteGeometricAPEngine &#8211; Monte Carlo pricing engine for discrete geometric average price Asian. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/asian/mc_discr_geom_av_price.hpp&gt; </p>
<p> Inherits <code>MCDiscreteAveragingAsianEngine&lt; RNG, S &gt;</code>. </p>
<h3>Public Types</h3>
<p>typedef <code>MCDiscreteAveragingAsianEngine</code>&lt; RNG, S &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef <code>MCDiscreteAveragingAsianEngine</code>&lt; RNG, S &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef <code>MCDiscreteAveragingAsianEngine</code>&lt; RNG, S &gt;::stats_type <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>MCDiscreteGeometricAPEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size maxTimeStepPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; path_pricer_type &gt; <code>pathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCDiscreteGeometricAPEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo pricing engine for discrete geometric average price Asian. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
