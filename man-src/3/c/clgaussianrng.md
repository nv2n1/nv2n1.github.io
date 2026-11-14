---
title: "clgaussianrng(3)"
name: "clgaussianrng"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clgaussianrng/"
description: "QuantLib::CLGaussianRng – Gaussian random number generator."
---

<p>QuantLib::CLGaussianRng &#8211; Gaussian random number generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/centrallimitgaussianrng.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code> </p>
<p> typedef RNG <code>urng_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>CLGaussianRng</code> (const RNG &amp;uniformGenerator) </p>
<p> <code>sample_type</code> <code>next</code> () const<br />
 <i>returns a sample from a Gaussian distribution </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG&gt; class QuantLib::CLGaussianRng&lt; RNG &gt;</h3>
<p>Gaussian random number generator. </p>
<p> It uses the well-known fact that the sum of 12 uniform deviate in (-.5,.5) is approximately a Gaussian deviate with average 0 and standard deviation 1. The uniform deviate is supplied by RNG. </p>
<p> Class RNG must implement the following interface: </p>
<pre> RNG::sample_type RNG::next() const;</pre>
<p>&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
