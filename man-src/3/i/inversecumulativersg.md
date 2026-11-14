---
title: "inversecumulativersg(3)"
name: "inversecumulativersg"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inversecumulativersg/"
description: "QuantLib::InverseCumulativeRsg – Inverse cumulative random sequence generator."
---

<p>QuantLib::InverseCumulativeRsg &#8211; Inverse cumulative random sequence generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/inversecumulativersg.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>Sample</code>&lt; std::vector&lt; <code>Real</code> &gt; &gt; <code>sample_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>InverseCumulativeRsg</code> (const USG &amp;uniformSequenceGenerator) </p>
<p> <code>InverseCumulativeRsg</code> (const USG &amp;uniformSequenceGenerator, const IC &amp;inverseCumulative) </p>
<p> const <code>sample_type</code> &amp; <code>nextSequence</code> () const<br />
 <i>returns next sample from the Gaussian distribution </i><br />
 const <code>sample_type</code> &amp; <code>lastSequence</code> () const </p>
<p> Size <code>dimension</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class USG, class IC&gt; class QuantLib::InverseCumulativeRsg&lt; USG, IC &gt;</h3>
<p>Inverse cumulative random sequence generator. </p>
<p> It uses a sequence of uniform deviate in (0, 1) as the source of cumulative distribution values. Then an inverse cumulative distribution is used to calculate the distribution deviate. </p>
<p> The uniform deviate sequence is supplied by USG. </p>
<p> Class USG must implement the following interface: </p>
<pre> USG::sample_type USG::nextSequence() const;
 Size USG::dimension() const;</pre>
<p>The inverse cumulative distribution is supplied by IC. </p>
<p> Class IC must implement the following interface: </p>
<pre> IC::IC();
 Real IC::operator() const;</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
