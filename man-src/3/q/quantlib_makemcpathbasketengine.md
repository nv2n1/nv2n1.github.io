---
title: "quantlib_makemcpathbasketengine(3)"
name: "quantlib_makemcpathbasketengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makemcpathbasketengine/"
description: "QuantLib::MakeMCPathBasketEngine – Monte Carlo Path Basket engine factory."
---

<p>QuantLib::MakeMCPathBasketEngine &#8211; Monte Carlo <code>Path</code> <code>Basket</code> engine factory. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/mcbasket/mcpathbasketengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeMCPathBasketEngine</code> &amp; <code>withSteps</code> (Size steps) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withBrownianBridge</code> (bool b=true) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withSamples</code> (Size samples) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withTolerance</code> (Real tolerance) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withMaxSamples</code> (Size samples) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withSeed</code> (BigNatural seed) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withAntitheticVariate</code> (bool b=true) </p>
<p> <code>MakeMCPathBasketEngine</code> &amp; <code>withControlVariate</code> (bool b=true) </p>
<p> <code>operator boost::shared_ptr&lt; PricingEngine &gt;</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCPathBasketEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo <code>Path</code> <code>Basket</code> engine factory. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
