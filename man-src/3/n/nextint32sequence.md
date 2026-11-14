---
title: "nextint32sequence(3)"
name: "nextint32sequence"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextint32sequence/"
description: "QuantLib::RandomSequenceGenerator – Random sequence generator based on a pseudo-random number generator."
---

<p>QuantLib::RandomSequenceGenerator &#8211; Random sequence generator based on a pseudo-random number generator. </p>
<h2>Synopsis</h2>
<pre><code>RandomSequenceGenerator (Size dimensionality, const RNG &amp;rng)



RandomSequenceGenerator (Size dimensionality, BigNatural seed=0)



const sample_type &amp; nextSequence () const



std::vector&lt; BigNatural &gt; nextInt32Sequence () const



const sample_type &amp; lastSequence () const



Size dimension () const</code></pre>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>RandomSequenceGenerator (Size dimensionality, const RNG &amp;rng)



RandomSequenceGenerator (Size dimensionality, BigNatural seed=0)



const sample_type &amp; nextSequence () const



std::vector&lt; BigNatural &gt; nextInt32Sequence () const



const sample_type &amp; lastSequence () const



Size dimension () const</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class RNG&gt; class QuantLib::RandomSequenceGenerator&lt; RNG &gt;</h3>
<p>Random sequence generator based on a pseudo-random number generator. </p>
<p> Random sequence generator based on a pseudo-random number generator RNG. </p>
<p> Class RNG must implement the following interface: </p>
<pre> RNG::sample_type RNG::next() const;</pre>
<p><code>Warning</code></p>
<dl>
<dd>do not use with low-discrepancy sequence generator.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
