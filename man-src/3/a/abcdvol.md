---
title: "abcdvol(3)"
name: "abcdvol"
section: "3"
letter: "a"
url: "/docs/linux/man/3-abcdvol/"
description: "QuantLib::AbcdVol – Abcd-interpolated volatility structure"
---

<p>QuantLib::AbcdVol &#8211; Abcd-interpolated volatility structure </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/models/abcdvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AbcdVol</code> (<code>Real</code> a, <code>Real</code> b, <code>Real</code> c, <code>Real</code> d, const std::vector&lt; <code>Real</code> &gt; &amp;ks, const boost::shared_ptr&lt; PiecewiseConstantCorrelation &gt; &amp;corr, const <code>EvolutionDescription</code> &amp;evolution, const Size numberOfFactors, const std::vector&lt; <code>Rate</code> &gt; &amp;initialRates, const std::vector&lt; <code>Spread</code> &gt; &amp;displacements) </p>
<p> <code>MarketModel interface</code> </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>initialRates</code> () const </p>
<p> const std::vector&lt; <code>Spread</code> &gt; &amp; <code>displacements</code> () const </p>
<p> const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const </p>
<p> Size <code>numberOfRates</code> () const </p>
<p> Size <code>numberOfFactors</code> () const </p>
<p> Size <code>numberOfSteps</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>pseudoRoot</code> (Size i) const </p>
<h2>Detailed Description</h2>
<p>Abcd-interpolated volatility structure </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
