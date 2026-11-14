---
title: "quantlib_makemcdigitalengine(3)"
name: "quantlib_makemcdigitalengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemcdigitalengine/"
description: "QuantLib::MakeMCDigitalEngine – Monte Carlo digital engine factory."
---

<p>QuantLib::MakeMCDigitalEngine &#8211; Monte Carlo digital engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mcdigitalengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCDigitalEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withSteps</code> (Size steps) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withStepsPerYear</code> (Size steps) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withBrownianBridge</code> (bool b=true) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>MakeMCDigitalEngine</code> &amp; <code>withControlVariate</code> (bool b=true) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCDigitalEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo digital engine factory. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
