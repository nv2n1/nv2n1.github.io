---
title: "quantlib_mcamericanengine(3)"
name: "quantlib_mcamericanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mcamericanengine/"
description: "QuantLib::MCAmericanEngine – American Monte Carlo engine."
---

<p>QuantLib::MCAmericanEngine &#8211; American Monte Carlo engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mcamericanengine.hpp&gt; </p>
<p> Inherits <code>MCLongstaffSchwartzEngine&lt; VanillaOption::engine, SingleVariate, RNG, S &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>MCAmericanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps, Size timeStepsPerYear, bool antitheticVariate, bool controlVariate, Size requiredSamples, Real requiredTolerance, Size maxSamples, BigNatural seed, Size polynomOrder, LsmBasisSystem::PolynomType polynomType, Size nCalibrationSamples=<code>Null</code>&lt; Size &gt;()) </p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>LongstaffSchwartzPathPricer</code>&lt; <code>Path</code> &gt; &gt; <code>lsmPathPricer</code> () const </p>
<p> Real <code>controlVariateValue</code> () const </p>
<p> boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>controlPricingEngine</code> () const </p>
<p> boost::shared_ptr&lt; <code>PathPricer</code>&lt; <code>Path</code> &gt; &gt; <code>controlPathPricer</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MCAmericanEngine&lt; RNG, S &gt;</h3>
<p>American Monte Carlo engine. </p>
<p> References: </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
