---
title: "sobolbrowniangenerator(3)"
name: "sobolbrowniangenerator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sobolbrowniangenerator/"
description: "QuantLib::SobolBrownianGenerator – Sobol Brownian generator for market-model simulations."
---

<p>QuantLib::SobolBrownianGenerator &#8211; Sobol Brownian generator for market-model simulations. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/browniangenerators/sobolbrowniangenerator.hpp&gt; </p>
<p> Inherits QuantLib::BrownianGenerator. </p>
<h3>Public Types</h3>
<p>enum <code>Ordering</code> { <code>Factors</code>, <code>Steps</code>, <code>Diagonal</code> } </p>
<h3>Public Member Functions</h3>
<p><code>SobolBrownianGenerator</code> (Size factors, Size steps, <code>Ordering</code> ordering, unsigned long seed=0, SobolRsg::DirectionIntegers directionIntegers=SobolRsg::Jaeckel) </p>
<p> Real <code>nextPath</code> () </p>
<p> Real <code>nextStep</code> (std::vector&lt; Real &gt; &amp;) </p>
<p> Size <code>numberOfFactors</code> () const </p>
<p> Size <code>numberOfSteps</code> () const </p>
<h2>Detailed Description</h2>
<p>Sobol Brownian generator for market-model simulations. </p>
<p> Incremental Brownian generator using a Sobol generator, inverse-cumulative Gaussian method, and Brownian bridging.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Ordering</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Factors </i></p>
<dd>The variates with the best quality will be used for the evolution of the first factor.</p>
<dt><i>Steps </i></p>
<dd>The variates with the best quality will be used for the largest steps of all factors.</p>
<dt><i>Diagonal </i></p>
<dd>A diagonal schema will be used to assign the variates with the best quality to the most important factors and the largest steps. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
