---
title: "quantlib_randomsequencegenerator(3)"
name: "quantlib_randomsequencegenerator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_randomsequencegenerator/"
description: "QuantLib::RandomSequenceGenerator – Random sequence generator based on a pseudo-random number generator."
---

<p>QuantLib::RandomSequenceGenerator &#8211; Random sequence generator based on a pseudo-random number generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/randomsequencegenerator.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>RandomSequenceGenerator</code> (Size dimensionality, const RNG &amp;rng) </p>
<p> <code>RandomSequenceGenerator</code> (Size dimensionality, BigNatural seed=0) </p>
<p> const <code>sample_type</code> &amp; <code>nextSequence</code> () const </p>
<p> std::vector&lt; BigNatural &gt; <code>nextInt32Sequence</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG&gt; class QuantLib::RandomSequenceGenerator&lt; RNG &gt;</h3>
<p>Random sequence generator based on a pseudo-random number generator. </p>
<p> Random sequence generator based on a pseudo-random number generator RNG. </p>
<p> Class RNG must implement the following interface: </p>
<pre> RNG::sample_type RNG::next() const;</pre>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>do not use with low-discrepancy sequence generator.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
