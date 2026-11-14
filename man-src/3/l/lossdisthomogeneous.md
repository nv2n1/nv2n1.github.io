---
title: "lossdisthomogeneous(3)"
name: "lossdisthomogeneous"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lossdisthomogeneous/"
description: "QuantLib::LossDistHomogeneous – Loss Distribution for Homogeneous Pool."
---

<p>QuantLib::LossDistHomogeneous &#8211; Loss Distribution for Homogeneous Pool. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/lossdistribution.hpp&gt; </p>
<p> Inherits <code>QuantLib::LossDist</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LossDistHomogeneous</code> (Size nBuckets, Real maximum, Real epsilon=1e-6) </p>
<p> Distribution <code>operator()</code> (Real volume, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> Distribution <code>operator()</code> (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const </p>
<p> Size <code>buckets</code> () const </p>
<p> Real <code>maximum</code> () const </p>
<p> Size <code>size</code> () const </p>
<p> Real <code>volume</code> () const </p>
<p> std::vector&lt; Real &gt; <code>probability</code> () const </p>
<p> std::vector&lt; Real &gt; <code>excessProbability</code> () const </p>
<h2>Detailed Description</h2>
<p>Loss Distribution for Homogeneous Pool. </p>
<p> Loss Distribution for Homogeneous Pool </p>
<p> Loss distribution for equal volumes but varying probabilities of default. </p>
<p> The method builds the exact loss distribution for a homogeneous pool of underlyings iteratively by computing the convolution of the given loss distribution with the &#8216;loss distribution&#8217; of an additional credit following </p>
<p> Xiaofong Ma, &#8216;Numerical Methods for the Valuation of Synthetic Collateralized Debt Obligations&#8217;, PhD Thesis, Graduate Department of Computer Science, University of Toronto, 2007 <a rel="nofollow" href="http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf">http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf</a> (formula 2.1) </p>
<p> avoiding numerical instability of the algorithm by </p>
<p> John Hull and Alan White, &#8216;Valuation of a <code>CDO</code> and nth to default CDS without Monte Carlo simulation&#8217;, Journal of Derivatives 12, 2, 2004 </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
