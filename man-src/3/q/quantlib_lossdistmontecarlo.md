---
title: "quantlib_lossdistmontecarlo(3)"
name: "quantlib_lossdistmontecarlo"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lossdistmontecarlo/"
description: "QuantLib::LossDistMonteCarlo – Loss distribution with Monte Carlo simulation."
---

<p>QuantLib::LossDistMonteCarlo &#8211; Loss distribution with Monte Carlo simulation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/lossdistribution.hpp&gt; </p>
<p> Inherits <code>QuantLib::LossDist</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LossDistMonteCarlo</code> (Size nBuckets, Real maximum, Size simulations, long seed=42, Real epsilon=1e-6) </p>
<p> Distribution <code>operator()</code> (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> Size <code>buckets</code> () const </p>
<p> Real <code>maximum</code> () const </p>
<h2>Detailed Description</h2>
<p>Loss distribution with Monte Carlo simulation. </p>
<p> Loss distribution for varying volumes and probabilities of default via Monte Carlo simulation of independent default events. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
