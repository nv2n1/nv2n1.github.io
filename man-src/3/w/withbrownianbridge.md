---
title: "withbrownianbridge(3)"
name: "withbrownianbridge"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withbrownianbridge/"
description: "QuantLib::MakeMCPathBasketEngine – Monte Carlo Path Basket engine factory."
---

<p>QuantLib::MakeMCPathBasketEngine &#8211; Monte Carlo <code>Path</code> <code>Basket</code> engine factory. </p>
<h2>Synopsis</h2>
<pre><code>MakeMCPathBasketEngine &amp; withSteps (Size steps)



MakeMCPathBasketEngine &amp; withBrownianBridge (bool b=true)



MakeMCPathBasketEngine &amp; withSamples (Size samples)



MakeMCPathBasketEngine &amp; withTolerance (Real tolerance)



MakeMCPathBasketEngine &amp; withMaxSamples (Size samples)



MakeMCPathBasketEngine &amp; withSeed (BigNatural seed)



MakeMCPathBasketEngine &amp; withAntitheticVariate (bool b=true)



MakeMCPathBasketEngine &amp; withControlVariate (bool b=true)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>
<h3>Public Member Functions</h3>
<pre><code>MakeMCPathBasketEngine &amp; withSteps (Size steps)



MakeMCPathBasketEngine &amp; withBrownianBridge (bool b=true)



MakeMCPathBasketEngine &amp; withSamples (Size samples)



MakeMCPathBasketEngine &amp; withTolerance (Real tolerance)



MakeMCPathBasketEngine &amp; withMaxSamples (Size samples)



MakeMCPathBasketEngine &amp; withSeed (BigNatural seed)



MakeMCPathBasketEngine &amp; withAntitheticVariate (bool b=true)



MakeMCPathBasketEngine &amp; withControlVariate (bool b=true)



operator boost::shared_ptr&lt; PricingEngine &gt; () const</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG = PseudoRandom, class S = Statistics&gt; class QuantLib::MakeMCPathBasketEngine&lt; RNG, S &gt;</h3>
<p>Monte Carlo <code>Path</code> <code>Basket</code> engine factory.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
