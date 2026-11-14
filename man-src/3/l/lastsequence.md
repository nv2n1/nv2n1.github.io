---
title: "lastsequence(3)"
name: "lastsequence"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lastsequence/"
description: "QuantLib::FaureRsg – Faure low-discrepancy sequence generator."
---

<p>QuantLib::FaureRsg &#8211; Faure low-discrepancy sequence generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/faurersg.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>FaureRsg</code> (Size dimensionality) </p>
<p> const std::vector&lt; long int &gt; &amp; <code>nextIntSequence</code> () const </p>
<p> const std::vector&lt; long int &gt; &amp; <code>lastIntSequence</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>nextSequence</code> () const </p>
<p> const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<p>Faure low-discrepancy sequence generator. </p>
<p> It is based on existing Fortran and C algorithms to calculate pascal matrix and gray transforms.</p>
<dl COMPACT>
<dt>1.</p>
<dd>E. Thiemard Economic generation of low-discrepancy sequences with a b-ary gray code.</p>
<dt>2.</p>
<dd>Algorithms 659, 647. <a rel="nofollow" href="http://www.netlib.org/toms/647,">http://www.netlib.org/toms/647,</a> <a href="http://www.netlib.org/toms/659">http://www.netlib.org/toms/659</a></dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by reproducing known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
