---
title: "quantlib_lecuyeruniformrng(3)"
name: "quantlib_lecuyeruniformrng"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lecuyeruniformrng/"
description: "QuantLib::LecuyerUniformRng – Uniform random number generator."
---

<p>QuantLib::LecuyerUniformRng &#8211; Uniform random number generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/lecuyeruniformrng.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Real</code> &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>LecuyerUniformRng</code> (long seed=0) </p>
<p> <code>sample_type</code> <code>next</code> () const </p>
<h2>Detailed Description</h2>
<p>Uniform random number generator. </p>
<p> Random number generator of L&#8217;Ecuyer with added Bays-Durham shuffle (know as ran2 in Numerical recipes) </p>
<p> For more details see Section 7.1 of Numerical Recipes in C, 2nd Edition, Cambridge University Press (available at <a rel="nofollow" href="http://www.nr.com/)">http://www.nr.com/)</a></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>LecuyerUniformRng</code> (long seed = 0) [explicit]</h3>
<p>if the given seed is 0, a random seed will be chosen based on clock()</p>
<h2>Member Function Documentation</h2>
<h3><code>sample_type</code> next () const</h3>
<p>returns a sample with weight 1.0 containing a random number uniformly chosen from (0.0,1.0) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
