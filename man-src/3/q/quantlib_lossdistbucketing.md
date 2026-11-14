---
title: "quantlib_lossdistbucketing(3)"
name: "quantlib_lossdistbucketing"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lossdistbucketing/"
description: "QuantLib::LossDistBucketing – Loss distribution with Hull-White bucketing."
---

<p>QuantLib::LossDistBucketing &#8211; Loss distribution with Hull-White bucketing. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/lossdistribution.hpp&gt; </p>
<p> Inherits <code>QuantLib::LossDist</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LossDistBucketing</code> (Size nBuckets, Real maximum, Real epsilon=1e-6) </p>
<p> Distribution <code>operator()</code> (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> Size <code>buckets</code> () const </p>
<p> Real <code>maximum</code> () const </p>
<h2>Detailed Description</h2>
<p>Loss distribution with Hull-White bucketing. </p>
<p> Loss distribution with Hull-White bucketing </p>
<p> Loss distribution for varying volumes and probabilities of default, independence assumed. </p>
<p> The implementation of the loss distribution follows </p>
<p> John Hull and Alan White, &#8216;Valuation of a <code>CDO</code> and nth to default CDS without Monte Carlo simulation&#8217;, Journal of Derivatives 12, 2, 2004. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
