---
title: "probabilityofnevents(3)"
name: "probabilityofnevents"
section: "3"
letter: "p"
url: "/docs/linux/man/3-probabilityofnevents/"
description: "QuantLib::LossDist – Probability formulas and algorithms."
---

<p>QuantLib::LossDist &#8211; Probability formulas and algorithms. </p>
<h2>Synopsis</h2>
<pre><code>virtual Distribution operator() (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const =0



virtual Size buckets () const =0



virtual Real maximum () const =0



Static Public Member Functions
static Real binomialProbabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static Real binomialProbabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static std::vector&lt; Real &gt; probabilityOfNEvents (std::vector&lt; Real &gt; &amp;p)



static Real probabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static Real probabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp;p)</code></pre>
<p> Inherited by <code>LossDistBinomial</code>, <code>LossDistBucketing</code>, <code>LossDistHomogeneous</code>, and <code>LossDistMonteCarlo</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual Distribution operator() (const std::vector&lt; Real &gt; &amp;volumes, const std::vector&lt; Real &gt; &amp;probabilities) const =0



virtual Size buckets () const =0



virtual Real maximum () const =0



Static Public Member Functions
static Real binomialProbabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static Real binomialProbabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static std::vector&lt; Real &gt; probabilityOfNEvents (std::vector&lt; Real &gt; &amp;p)



static Real probabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp;p)



static Real probabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp;p)</code></pre>
<h2>Detailed Description</h2>
<p>Probability formulas and algorithms.</p>
<h2>Member Function Documentation</h2>
<h3>static Real binomialProbabilityOfNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p>Binomial probability of n defaults using prob[0]</p>
<h3>static Real binomialProbabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p>Binomial probability of at least n defaults using prob[0]</p>
<h3>static std::vector&lt;Real&gt; probabilityOfNEvents (std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p>Probability of exactly n default events Xiaofong Ma, &#8216;Numerical Methods for the Valuation of Synthetic Collateralized Debt Obligations&#8217;, PhD Thesis, Graduate Department of Computer Science, University of Toronto, 2007 <a rel="nofollow" href="http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf">http://www.cs.toronto.edu/pub/reports/na/ma-07-phd.pdf</a> (formula 2.1)</p>
<h3>static Real probabilityOfAtLeastNEvents (int n, std::vector&lt; Real &gt; &amp; p) [static]</h3>
<p>Probability of at least n defaults</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
