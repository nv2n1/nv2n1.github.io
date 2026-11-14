---
title: "quantlib_makemchullwhitecapfloorengine(3)"
name: "quantlib_makemchullwhitecapfloorengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemchullwhitecapfloorengine/"
description: "QuantLib::MakeMCHullWhiteCapFloorEngine – Monte Carlo Hull-White cap-floor engine factory."
---

<p>QuantLib::MakeMCHullWhiteCapFloorEngine &#8211; Monte Carlo Hull-White cap-floor engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/capfloor/mchullwhiteengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCHullWhiteCapFloorEngine</code> (const boost::shared_ptr&lt; <code>HullWhite</code> &gt; &amp;) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withBrownianBridge</code> (bool b=true) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCHullWhiteCapFloorEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCHullWhiteCapFloorEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo Hull-White cap-floor engine factory. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
