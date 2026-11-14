---
title: "excessprobability(3)"
name: "excessprobability"
section: "3"
letter: "e"
url: "/docs/linux/man/3-excessprobability/"
description: "QuantLib::LossDistBinomial – Binomial loss distribution."
---

<p>QuantLib::LossDistBinomial &#8211; Binomial loss distribution. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/lossdistribution.hpp&gt; </p>
<p> Inherits <code>QuantLib::LossDist</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LossDistBinomial</code> (Size nBuckets, Real maximum) </p>
<p> Distribution <code>operator()</code> (Size n, Real volume, Real probability) const </p>
<p> Distribution <code>operator()</code> (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> Size <code>buckets</code> () const </p>
<p> Real <code>maximum</code> () const </p>
<p> Real <code>volume</code> () const </p>
<p> Size <code>size</code> () const </p>
<p> std::vector&lt; Real &gt; <code>probability</code> () const </p>
<p> std::vector&lt; Real &gt; <code>excessProbability</code> () const </p>
<h2>Detailed Description</h2>
<p>Binomial loss distribution. </p>
<p> Binomial loss distribution </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
