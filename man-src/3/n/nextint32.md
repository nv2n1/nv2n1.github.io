---
title: "nextint32(3)"
name: "nextint32"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextint32/"
description: "QuantLib::MersenneTwisterUniformRng – Uniform random number generator."
---

<p>QuantLib::MersenneTwisterUniformRng &#8211; Uniform random number generator. </p>
<h2>Synopsis</h2>
<pre><code>MersenneTwisterUniformRng (unsigned long seed=0)



MersenneTwisterUniformRng (const std::vector&lt; unsigned long &gt; &amp;seeds)



sample_type next () const



unsigned long nextInt32 () const


return a random number on [0,0xffffffff]-interval</code></pre>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>MersenneTwisterUniformRng (unsigned long seed=0)



MersenneTwisterUniformRng (const std::vector&lt; unsigned long &gt; &amp;seeds)



sample_type next () const



unsigned long nextInt32 () const


return a random number on [0,0xffffffff]-interval</code></pre>
<h2>Detailed Description</h2>
<p>Uniform random number generator. </p>
<p> Mersenne Twister random number generator of period 2**19937-1 </p>
<p> For more details see <a rel="nofollow" href="http://www.math.keio.ac.jp/matumoto/emt.html">http://www.math.keio.ac.jp/matumoto/emt.html</a> </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned values is tested by checking them against known good results.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>MersenneTwisterUniformRng</code> (unsigned long seed = 0) [explicit]</h3>
<p>if the given seed is 0, a random seed will be chosen based on clock()</p>
<h2>Member Function Documentation</h2>
<h3><code>sample_type</code> next () const</h3>
<p>returns a sample with weight 1.0 containing a random number on (0.0, 1.0)-real-interval</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
