---
title: "randomizedlds(3)"
name: "randomizedlds"
section: "3"
letter: "r"
url: "/docs/linux/man/3-randomizedlds/"
description: "QuantLib::RandomizedLDS – Randomized (random shift) low-discrepancy sequence."
---

<p>QuantLib::RandomizedLDS &#8211; Randomized (random shift) low-discrepancy sequence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/randomizedlds.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>RandomizedLDS</code> (const LDS &amp;ldsg, const PRS &amp;prsg) </p>
<p> <code>RandomizedLDS</code> (const LDS &amp;ldsg) </p>
<p> <code>RandomizedLDS</code> (Size dimensionality, BigNatural ldsSeed=0, BigNatural prsSeed=0) </p>
<p> const <code>sample_type</code> &amp; <code>nextSequence</code> () const<br />
 <i>returns next sample using a given randomizing vector </i><br />
 const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> void <code>nextRandomizer</code> () </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class LDS, class PRS = RandomSequenceGenerator&lt;MersenneTwisterUniformRng&gt;&gt; class QuantLib::RandomizedLDS&lt; LDS, PRS &gt;</h3>
<p>Randomized (random shift) low-discrepancy sequence. </p>
<p> Random-shifts a uniform low-discrepancy sequence of dimension $ N $ by adding (modulo 1 for each coordinate) a pseudo-random uniform deviate in $ (0, 1)^N. $ It is used for implementing Randomized Quasi Monte Carlo. </p>
<p> The uniform low discrepancy sequence is supplied by LDS; the uniform pseudo-random sequence is supplied by PRS. </p>
<p> Both class LDS and PRS must implement the following interface: </p>
<pre> LDS::sample_type LDS::nextSequence() const;
 Size LDS::dimension() const;</pre>
<p><code>Precondition:</code></p>
<dl COMPACT>
<dd>LDS and PRS must have the same dimension $ N $</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Inverting LDS and PRS is possible, but it doesn&#8217;t make sense.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>implement the other randomization algorithms</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>correct initialization is tested.</dl>
<h2>Member Function Documentation</h2>
<h3>void nextRandomizer ()</h3>
<p>update the randomizing vector and re-initialize the low discrepancy generator </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
