---
title: "inversecumulativerng(3)"
name: "inversecumulativerng"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inversecumulativerng/"
description: "QuantLib::InverseCumulativeRng – Inverse cumulative random number generator."
---

<p>QuantLib::InverseCumulativeRng &#8211; Inverse cumulative random number generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/inversecumulativerng.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code> </p>
<p> typedef RNG <code>urng_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>InverseCumulativeRng</code> (const RNG &amp;uniformGenerator) </p>
<p> <code>sample_type</code> <code>next</code> () const<br />
 <i>returns a sample from a Gaussian distribution </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG, class IC&gt; class QuantLib::InverseCumulativeRng&lt; RNG, IC &gt;</h3>
<p>Inverse cumulative random number generator. </p>
<p> It uses a uniform deviate in (0, 1) as the source of cumulative distribution values. Then an inverse cumulative distribution is used to calculate the distribution deviate. </p>
<p> The uniform deviate is supplied by RNG. </p>
<p> Class RNG must implement the following interface: </p>
<pre> RNG::sample_type RNG::next() const;</pre>
<p>The inverse cumulative distribution is supplied by IC. </p>
<p> Class IC must implement the following interface: </p>
<pre> IC::IC();
 Real IC::operator() const;</pre>
<p>&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
