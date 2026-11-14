---
title: "quantlib_extendedjarrowrudd(3)"
name: "quantlib_extendedjarrowrudd"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedjarrowrudd/"
description: "QuantLib::ExtendedJarrowRudd – Jarrow-Rudd (multiplicative) equal probabilities binomial tree."
---

<p>QuantLib::ExtendedJarrowRudd &#8211; Jarrow-Rudd (multiplicative) equal probabilities binomial tree. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>ExtendedEqualProbabilitiesBinomialTree&lt; ExtendedJarrowRudd &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedJarrowRudd</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;, Time end, Size steps, Real strike) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>upStep</code> (Time stepTime) const </p>
<h2>Detailed Description</h2>
<p>Jarrow-Rudd (multiplicative) equal probabilities binomial tree. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
