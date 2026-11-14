---
title: "quantlib_makemceuropeangjrgarchengine(3)"
name: "quantlib_makemceuropeangjrgarchengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemceuropeangjrgarchengine/"
description: "QuantLib::MakeMCEuropeanGJRGARCHEngine – Monte Carlo GJR-GARCH European engine factory."
---

<p>QuantLib::MakeMCEuropeanGJRGARCHEngine &#8211; Monte Carlo GJR-GARCH European engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/mceuropeangjrgarchengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCEuropeanGJRGARCHEngine</code> (const boost::shared_ptr&lt; <code>GJRGARCHProcess</code> &gt; &amp;) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withSteps</code> (Size steps) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withStepsPerYear</code> (Size steps) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCEuropeanGJRGARCHEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCEuropeanGJRGARCHEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo GJR-GARCH European engine factory. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
