---
title: "quantlib_makemcamericanengine(3)"
name: "quantlib_makemcamericanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemcamericanengine/"
description: "QuantLib::MakeMCAmericanEngine – Monte Carlo American engine factory."
---

<p>QuantLib::MakeMCAmericanEngine &#8211; Monte Carlo American engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mcamericanengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCAmericanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withSteps</code> (Size steps) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withStepsPerYear</code> (Size steps) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withControlVariate</code> (bool b=true) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withPolynomOrder</code> (Size polynomOrer) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withBasisSystem</code> (LsmBasisSystem::PolynomType) </p>
<p> <code>MakeMCAmericanEngine</code> &amp; <code>withCalibrationSamples</code> (Size calibrationSamples) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCAmericanEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo American engine factory. </p>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
