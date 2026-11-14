---
title: "mtbrowniangenerator(3)"
name: "mtbrowniangenerator"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mtbrowniangenerator/"
description: "QuantLib::MTBrownianGenerator – Mersenne-twister Brownian generator for market-model simulations."
---

<p>QuantLib::MTBrownianGenerator &#8211; Mersenne-twister Brownian generator for market-model simulations. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/browniangenerators/mtbrowniangenerator.hpp&gt; </p>
<p> Inherits QuantLib::BrownianGenerator. </p>
<h3>Public Member Functions</h3>
<p><code>MTBrownianGenerator</code> (Size factors, Size steps, unsigned long seed=0) </p>
<p> Real <code>nextStep</code> (std::vector&lt; Real &gt; &amp;) </p>
<p> Real <code>nextPath</code> () </p>
<p> Size <code>numberOfFactors</code> () const </p>
<p> Size <code>numberOfSteps</code> () const </p>
<h2>Detailed Description</h2>
<p>Mersenne-twister Brownian generator for market-model simulations. </p>
<p> Incremental Brownian generator using a Mersenne-twister uniform generator and inverse-cumulative Gaussian method. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>At this time, generation of the underlying uniform sequence is eager, while its transformation into Gaussian variates is lazy. Further optimization might be possible by using the Mersenne twister directly instead of a <code>RandomSequenceGenerator</code>; however, it is not clear how much of a difference this would make when compared to the inverse-cumulative Gaussian calculation.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
