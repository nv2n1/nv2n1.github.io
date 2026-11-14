---
title: "antithetic(3)"
name: "antithetic"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antithetic/"
description: "QuantLib::MultiPathGenerator – Generates a multipath from a random number generator."
---

<h2 class="name">NAME</h2>
<p> QuantLib::MultiPathGenerator &#8211; Generates a multipath from a random number generator. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/montecarlo/multipathgenerator.hpp&gt; </p>
<h3>Public Types</h3>
<p> typedef <code>Sample</code>&lt; <code>MultiPath</code> &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>MultiPathGenerator</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;, const <code>TimeGrid</code> &amp;, GSG generator, bool brownianBridge=false) </p>
<p> const <code>sample_type</code> &amp; <code>next</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>antithetic</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class GSG&gt; class QuantLib::MultiPathGenerator&lt; GSG &gt;</h3>
<p> Generates a multipath from a random number generator. </p>
<p> RSG is a sample generator which returns a random sequence. It must have the minimal interface: </p>
<pre><code>
RSG
{
    Sample&lt;Array&gt; next();
};
</code></pre>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> the generated paths are checked against cached results</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
