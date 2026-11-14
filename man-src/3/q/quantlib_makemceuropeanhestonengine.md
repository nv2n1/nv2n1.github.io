---
title: "quantlib_makemceuropeanhestonengine(3)"
name: "quantlib_makemceuropeanhestonengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemceuropeanhestonengine/"
description: "QuantLib::MakeMCEuropeanHestonEngine – Monte Carlo Heston European engine factory."
---

<p>QuantLib::MakeMCEuropeanHestonEngine &#8211; Monte Carlo Heston European engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mceuropeanhestonengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCEuropeanHestonEngine</code> (const boost::shared_ptr&lt; <code>HestonProcess</code> &gt; &amp;) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withSteps</code> (Size steps) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withStepsPerYear</code> (Size steps) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCEuropeanHestonEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCEuropeanHestonEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo Heston European engine factory. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
