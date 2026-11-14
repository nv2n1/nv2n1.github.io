---
title: "mc_traits(3)"
name: "mc_traits"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mc_traits/"
description: "QuantLib::MonteCarloModel – General-purpose Monte Carlo model for path samples."
---

<h2 class="name">NAME</h2>
<p> QuantLib::MonteCarloModel &#8211; General-purpose Monte Carlo model for path samples. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/montecarlo/montecarlomodel.hpp&gt; </p>
<h3>Public Types</h3>
<p> typedef MC&lt; RNG &gt; <code>mc_traits</code> </p>
<p> typedef RNG <code>rng_traits</code> </p>
<p> typedef MC&lt; RNG &gt;::path_generator_type <code>path_generator_type</code> </p>
<p> typedef MC&lt; RNG &gt;::path_pricer_type <code>path_pricer_type</code> </p>
<p> typedef path_generator_type::sample_type <code>sample_type</code> </p>
<p> typedef path_pricer_type::result_type <code>result_type</code> </p>
<p> typedef S <code>stats_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>MonteCarloModel</code> (const boost::shared_ptr&lt; path_generator_type &gt; &amp;pathGenerator, const boost::shared_ptr&lt; path_pricer_type &gt; &amp;pathPricer, const stats_type &amp;sampleAccumulator, bool antitheticVariate, const boost::shared_ptr&lt; path_pricer_type &gt; &amp;cvPathPricer=boost::shared_ptr&lt; path_pricer_type &gt;(), result_type cvOptionValue=result_type(), const boost::shared_ptr&lt; path_generator_type &gt; &amp;cvPathGenerator=boost::shared_ptr&lt; path_generator_type &gt;()) </p>
<p> void <code>addSamples</code> (Size samples) </p>
<p> const stats_type &amp; <code>sampleAccumulator</code> (void) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;template&lt; class &gt; class MC, class RNG, class S = Statistics&gt; class QuantLib::MonteCarloModel&lt; MC, RNG, S &gt;</h3>
<p> General-purpose Monte Carlo model for path samples. </p>
<p> The template arguments of this class correspond to available policies for the particular model to be instantiated&#8212;i.e., whether it is single- or multi-asset, or whether it should use pseudo-random or low-discrepancy numbers for path generation. Such decisions are grouped in trait classes so as to be orthogonal&#8212;see <code>mctraits.hpp</code> for examples. </p>
<p> The constructor accepts two safe references, i.e. two smart pointers, one to a path generator and the other to a path pricer. In case of control variate technique the user should provide the additional control option, namely the option path pricer and the option value. </p>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
