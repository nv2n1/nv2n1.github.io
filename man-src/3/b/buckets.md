---
title: "buckets(3)"
name: "buckets"
section: "3"
letter: "b"
url: "/docs/linux/man/3-buckets/"
description: "QuantLib::LossDist – Probability formulas and algorithms."
---

<h2 class="name">NAME</h2>
<p> QuantLib::LossDist &#8211; Probability formulas and algorithms. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/experimental/credit/lossdistribution.hpp&gt; </p>
<p> Inherited by <code>LossDistBinomial</code>, <code>LossDistBucketing</code>, <code>LossDistHomogeneous</code>, and <code>LossDistMonteCarlo</code>. </p>
<h3>Public Member Functions</h3>
<p> virtual Distribution <code>operator()</code> (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const =0 </p>
<p> virtual Size <code>buckets</code> () const =0 </p>
<p> virtual Real <code>maximum</code> () const =0 </p>
<h3>Static Public Member Functions</h3>
<p> static Real <code>binomialProbabilityOfNEvents</code> (int n, std::vector&lt; Real &gt; &amp;p) </p>
<p> static Real <code>binomialProbabilityOfAtLeastNEvents</code> (int n, std::vector&lt; Real &gt; &amp;p) </p>
<p> static std::vector&lt; Real &gt; <code>probabilityOfNEvents</code> (std::vector&lt; Real &gt; &amp;p) </p>
<p> static Real <code>probabilityOfNEvents</code> (int n, std::vector&lt; Real &gt; &amp;p) </p>
<p> static Real <code>probabilityOfAtLeastNEvents</code> (int n, std::vector&lt; Real &gt; &amp;p) </p>
<h2>Detailed Description</h2>
<p> Probability formulas and algorithms.</p>
<h2>Member Function Documentation</h2>
<h3>static Real binomialProbabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p> Binomial probability of n defaults using prob[0]</p>
<h3>static Real binomialProbabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p> Binomial probability of at least n defaults using prob[0]</p>
<h3>static std::vector&lt;Real&gt; probabilityOfNEvents (std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p> Probability of exactly n default events Xiaofong Ma, &#8216;Numerical Methods for the Valuation of Synthetic Collateralized Debt Obligations&#8217;, PhD Thesis, Graduate Department of Computer Science, University of Toronto, 2007 <a rel="nofollow" href="http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf">http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf</a> (formula 2.1)</p>
<h3>static Real probabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p> Probability of at least n defaults </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
