---
title: "quantlib_mcamericanbasketengine(3)"
name: "quantlib_mcamericanbasketengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcamericanbasketengine/"
description: "QuantLib::MCAmericanBasketEngine – least-square Monte Carlo engine"
---

<p>QuantLib::MCAmericanBasketEngine &#8211; least-square Monte Carlo engine </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/basket/mcamericanbasketengine.hpp&gt; </p>
<p> Inherits <code>MCLongstaffSchwartzEngine&lt; BasketOption::engine, MultiVariate, RNG &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>MCAmericanBasketEngine</code> (const boost::shared_ptr&lt; <code>StochasticProcessArray</code> &gt; &amp;, Size timeSteps, Size timeStepsPerYear, bool brownianBridge, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed, Size nCalibrationSamples=<code>Null</code>&lt; Size &gt;()) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>LongstaffSchwartzPathPricer</code>&lt; <code>MultiPath</code> &gt; &gt; <code>lsmPathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom&gt; class QuantLib::MCAmericanBasketEngine&lt; RNG &gt;</h3>
<p>least-square Monte Carlo engine </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This method is intrinsically weak for out-of-the-money options.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
