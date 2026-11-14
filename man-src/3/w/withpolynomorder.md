---
title: "withpolynomorder(3)"
name: "withpolynomorder"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withpolynomorder/"
description: "QuantLib::MakeMCAmericanEngine – Monte Carlo American engine factory."
---

<p>QuantLib::MakeMCAmericanEngine &#8211; Monte Carlo American engine factory. </p>
<h2>Synopsis</h2>
<pre><code>MakeMCAmericanEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;)



MakeMCAmericanEngine &amp; withSteps (Size steps)



MakeMCAmericanEngine &amp; withStepsPerYear (Size steps)



MakeMCAmericanEngine &amp; withSamples (Size samples)



MakeMCAmericanEngine &amp; withTolerance (Real tolerance)



MakeMCAmericanEngine &amp; withMaxSamples (Size samples)



MakeMCAmericanEngine &amp; withSeed (BigNatural seed)



MakeMCAmericanEngine &amp; withAntitheticVariate (bool b=true)



MakeMCAmericanEngine &amp; withControlVariate (bool b=true)



MakeMCAmericanEngine &amp; withPolynomOrder (Size polynomOrer)



MakeMCAmericanEngine &amp; withBasisSystem (LsmBasisSystem::PolynomType)



MakeMCAmericanEngine &amp; withCalibrationSamples (Size calibrationSamples)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>
<h3>Public Member Functions</h3>
<pre><code>MakeMCAmericanEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;)



MakeMCAmericanEngine &amp; withSteps (Size steps)



MakeMCAmericanEngine &amp; withStepsPerYear (Size steps)



MakeMCAmericanEngine &amp; withSamples (Size samples)



MakeMCAmericanEngine &amp; withTolerance (Real tolerance)



MakeMCAmericanEngine &amp; withMaxSamples (Size samples)



MakeMCAmericanEngine &amp; withSeed (BigNatural seed)



MakeMCAmericanEngine &amp; withAntitheticVariate (bool b=true)



MakeMCAmericanEngine &amp; withControlVariate (bool b=true)



MakeMCAmericanEngine &amp; withPolynomOrder (Size polynomOrer)



MakeMCAmericanEngine &amp; withBasisSystem (LsmBasisSystem::PolynomType)



MakeMCAmericanEngine &amp; withCalibrationSamples (Size calibrationSamples)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCAmericanEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo American engine factory. </p>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
