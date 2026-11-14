---
title: "withstepsperyear(3)"
name: "withstepsperyear"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withstepsperyear/"
---

QuantLib::MakeMCVarianceSwapEngine - Monte Carlo variance-swap engine factory. 

<h2>Synopsis</h2>

<pre><code>MakeMCVarianceSwapEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process)



MakeMCVarianceSwapEngine &amp; withSteps (Size steps)



MakeMCVarianceSwapEngine &amp; withStepsPerYear (Size steps)



MakeMCVarianceSwapEngine &amp; withBrownianBridge (bool b=true)



MakeMCVarianceSwapEngine &amp; withSamples (Size samples)



MakeMCVarianceSwapEngine &amp; withTolerance (Real tolerance)



MakeMCVarianceSwapEngine &amp; withMaxSamples (Size samples)



MakeMCVarianceSwapEngine &amp; withSeed (BigNatural seed)



MakeMCVarianceSwapEngine &amp; withAntitheticVariate (bool b=true)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>

<h3>Public Member Functions</h3>

<pre><code>MakeMCVarianceSwapEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process)



MakeMCVarianceSwapEngine &amp; withSteps (Size steps)



MakeMCVarianceSwapEngine &amp; withStepsPerYear (Size steps)



MakeMCVarianceSwapEngine &amp; withBrownianBridge (bool b=true)



MakeMCVarianceSwapEngine &amp; withSamples (Size samples)



MakeMCVarianceSwapEngine &amp; withTolerance (Real tolerance)



MakeMCVarianceSwapEngine &amp; withMaxSamples (Size samples)



MakeMCVarianceSwapEngine &amp; withSeed (BigNatural seed)



MakeMCVarianceSwapEngine &amp; withAntitheticVariate (bool b=true)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>

<h2>Detailed Description</h2>

<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCVarianceSwapEngine&lt; RNG, S &gt;</h3>

Monte Carlo variance-swap engine factory.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
