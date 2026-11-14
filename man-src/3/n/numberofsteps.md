---
title: "numberofsteps(3)"
name: "numberofsteps"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numberofsteps/"
description: "QuantLib::MTBrownianGenerator – Mersenne-twister Brownian generator for market-model simulations."
---

<p>QuantLib::MTBrownianGenerator &#8211; Mersenne-twister Brownian generator for market-model simulations. </p>
<h2>Synopsis</h2>
<pre><code>MTBrownianGenerator (Size factors, Size steps, unsigned long seed=0)



Real nextStep (std::vector&lt; Real &gt; &amp;)



Real nextPath ()



Size numberOfFactors () const



Size numberOfSteps () const</code></pre>
<p> Inherits QuantLib::BrownianGenerator.</p>
<h3>Public Member Functions</h3>
<pre><code>MTBrownianGenerator (Size factors, Size steps, unsigned long seed=0)



Real nextStep (std::vector&lt; Real &gt; &amp;)



Real nextPath ()



Size numberOfFactors () const



Size numberOfSteps () const</code></pre>
<h2>Detailed Description</h2>
<p>Mersenne-twister Brownian generator for market-model simulations. </p>
<p> Incremental Brownian generator using a Mersenne-twister uniform generator and inverse-cumulative Gaussian method. </p>
<p> <code>Note:</code></p>
<dl>
<dd>At this time, generation of the underlying uniform sequence is eager, while its transformation into Gaussian variates is lazy. Further optimization might be possible by using the Mersenne twister directly instead of a <code>RandomSequenceGenerator</code>; however, it is not clear how much of a difference this would make when compared to the inverse-cumulative Gaussian calculation.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
