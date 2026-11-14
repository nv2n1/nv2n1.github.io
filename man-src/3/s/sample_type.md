---
title: "sample_type(3)"
name: "sample_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sample_type/"
description: "QuantLib::BoxMullerGaussianRng – Gaussian random number generator."
---

<p>QuantLib::BoxMullerGaussianRng &#8211; Gaussian random number generator. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/randomnumbers/boxmullergaussianrng.hpp&gt;</code></pre>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code> </p>
<p> typedef RNG <code>urng_type</code></p>
<h3>Public Member Functions</h3>
<p><code>BoxMullerGaussianRng</code> (const RNG &amp;uniformGenerator) </p>
<p> <code>sample_type</code> <code>next</code> () const<br />
 <i>returns a sample from a Gaussian distribution </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG&gt; class QuantLib::BoxMullerGaussianRng&lt; RNG &gt;</h3>
<p>Gaussian random number generator. </p>
<p> It uses the well-known Box-Muller transformation to return a normal distributed Gaussian deviate with average 0.0 and standard deviation of 1.0, from a uniform deviate in (0,1) supplied by RNG. </p>
<p> Class RNG must implement the following interface: </p>
<pre> RNG::sample_type RNG::next() const;</pre>
<p>&nbsp;<wbr></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
