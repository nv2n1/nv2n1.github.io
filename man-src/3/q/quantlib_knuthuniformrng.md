---
title: "quantlib_knuthuniformrng(3)"
name: "quantlib_knuthuniformrng"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_knuthuniformrng/"
description: "QuantLib::KnuthUniformRng – Uniform random number generator."
---

<p>QuantLib::KnuthUniformRng &#8211; Uniform random number generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/knuthuniformrng.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>KnuthUniformRng</code> (long seed=0) </p>
<p> <code>sample_type</code> <code>next</code> () const </p>
<h2>Detailed Description</h2>
<p>Uniform random number generator. </p>
<p> Random number generator by Knuth. For more details see Knuth, Seminumerical Algorithms, 3rd edition, Section 3.6. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is <code>not</code> Knuth&#8217;s original implementation which is available at <a rel="nofollow" href="http://www-cs-faculty.stanford.edu/~knuth/programs.html,">http://www-cs-faculty.stanford.edu/~knuth/programs.html,</a> but rather a slightly modified version wrapped in a C++ class. Such modifications did not affect the code but only the data structures used, which were converted to their standard C++ equivalents.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>KnuthUniformRng</code> (long seed = 0) [explicit]</h3>
<p>if the given seed is 0, a random seed will be chosen based on clock()</p>
<h2>Member Function Documentation</h2>
<h3><code>KnuthUniformRng::sample_type</code> next () const</h3>
<p>returns a sample with weight 1.0 containing a random number uniformly chosen from (0.0,1.0) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
