---
title: "quantlib_haltonrsg(3)"
name: "quantlib_haltonrsg"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_haltonrsg/"
description: "QuantLib::HaltonRsg – Halton low-discrepancy sequence generator."
---

<p>QuantLib::HaltonRsg &#8211; Halton low-discrepancy sequence generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/haltonrsg.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>HaltonRsg</code> (Size dimensionality, unsigned long seed=0, bool randomStart=true, bool randomShift=false) </p>
<p> const <code>sample_type</code> &amp; <code>nextSequence</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<p>Halton low-discrepancy sequence generator. </p>
<p> Halton algorithm for low-discrepancy sequence. For more details see chapter 8, paragraph 2 of &#8216;Monte Carlo Methods in Finance&#8217;, by Peter J�ckel </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned values is tested by reproducing known good values.</p>
<dt>*</p>
<dd>the correctness of the returned values is tested by checking their discrepancy against known good values.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
