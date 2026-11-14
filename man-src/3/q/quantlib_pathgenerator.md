---
title: "quantlib_pathgenerator(3)"
name: "quantlib_pathgenerator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathgenerator/"
description: "QuantLib::PathGenerator – Generates random paths using a sequence generator."
---

<p>QuantLib::PathGenerator &#8211; Generates random paths using a sequence generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/pathgenerator.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; <code>Path</code> &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>PathGenerator</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;, Time length, Size timeSteps, const GSG &amp;generator, bool brownianBridge) </p>
<p> <code>PathGenerator</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;, const <code>TimeGrid</code> &amp;timeGrid, const GSG &amp;generator, bool brownianBridge) </p>
<p> <code>inspectors</code> </p>
<p> const <code>sample_type</code> &amp; <code>next</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>antithetic</code> () const </p>
<p> Size <code>size</code> () const </p>
<p> const <code>TimeGrid</code> &amp; <code>timeGrid</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class GSG&gt; class QuantLib::PathGenerator&lt; GSG &gt;</h3>
<p>Generates random paths using a sequence generator. </p>
<p> Generates random paths with drift(S,t) and variance(S,t) using a gaussian sequence generator </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the generated paths are checked against cached results</dl>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
