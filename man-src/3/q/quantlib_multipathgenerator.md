---
title: "quantlib_multipathgenerator(3)"
name: "quantlib_multipathgenerator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_multipathgenerator/"
---

QuantLib::MultiPathGenerator - Generates a multipath from a random number generator. 

<h2>Synopsis</h2>#include &lt;ql/methods/montecarlo/multipathgenerator.hpp&gt; 

<h3>Public Types</h3>typedef <b>Sample</b>&lt; <b>MultiPath</b> &gt; <b>sample_type</b> 

<h3>Public Member Functions</h3><b>MultiPathGenerator</b> (const boost::shared_ptr&lt; <b>StochasticProcess</b> &gt; &amp;, const <b>TimeGrid</b> &amp;, GSG generator, bool brownianBridge=false) 
 
 const <b>sample_type</b> &amp; <b>next</b> () const 
 
 const <b>sample_type</b> &amp; <b>antithetic</b> () const 

<h2>Detailed Description</h2><h3>template&lt;class GSG&gt; class QuantLib::MultiPathGenerator&lt; GSG &gt;</h3>Generates a multipath from a random number generator. 

 RSG is a sample generator which returns a random sequence. It must have the minimal interface: 

 <pre> RSG {
 Sample&lt;Array&gt; next();
 };</pre><b>Tests</b>
<dl COMPACT><dd>the generated paths are checked against cached results</dl><h2>Author</h2>Generated automatically by Doxygen for QuantLib from the source code.
