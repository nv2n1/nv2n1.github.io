---
title: "results_(3)"
name: "results_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-results_/"
description: "QuantLib::GenericSequenceStatistics – Statistics analysis of N-dimensional (sequence) data."
---

<p>QuantLib::GenericSequenceStatistics &#8211; Statistics analysis of N-dimensional (sequence) data. </p>
<h2>Synopsis</h2>
<pre><code>void reset (Size dimension=0)



template&lt;class Sequence &gt; void add (const Sequence &amp;sample, Real weight=1.0)



template&lt;class Iterator &gt; void add (Iterator begin, Iterator end, Real weight=1.0)



Protected Attributes</code></pre>
<h3>Public Types</h3>
<p>typedef StatisticsType <code>statistics_type</code> </p>
<p> typedef std::vector&lt; typename StatisticsType::value_type &gt; <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>void reset (Size dimension=0)</p>
<p>template&lt;class Sequence &gt; void add (const Sequence &amp;sample, Real weight=1.0)</p>
<p>template&lt;class Iterator &gt; void add (Iterator begin, Iterator end, Real weight=1.0)</p>
<p>Protected Attributes <code>inspectors</code> </p>
<p> Size <code>size</code> () const<br />
 <code>covariance and correlation</code> </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> () const<br />
 <i>returns the covariance </i><code>Matrix</code><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>correlation</code> () const<br />
 <i>returns the correlation </i><code>Matrix</code> <code>1-D inspectors lifted from underlying statistics class</code> </p>
<p> Size <code>samples</code> () const </p>
<p> Real <code>weightSum</code> () const<br />
 <code>N-D inspectors lifted from underlying statistics class</code> </p>
<p> std::vector&lt; Real &gt; <code>mean</code> () const </p>
<p> std::vector&lt; Real &gt; <code>variance</code> () const </p>
<p> std::vector&lt; Real &gt; <code>standardDeviation</code> () const </p>
<p> std::vector&lt; Real &gt; <code>downsideVariance</code> () const </p>
<p> std::vector&lt; Real &gt; <code>downsideDeviation</code> () const </p>
<p> std::vector&lt; Real &gt; <code>semiVariance</code> () const </p>
<p> std::vector&lt; Real &gt; <code>semiDeviation</code> () const </p>
<p> std::vector&lt; Real &gt; <code>errorEstimate</code> () const </p>
<p> std::vector&lt; Real &gt; <code>skewness</code> () const </p>
<p> std::vector&lt; Real &gt; <code>kurtosis</code> () const </p>
<p> std::vector&lt; Real &gt; <code>min</code> () const </p>
<p> std::vector&lt; Real &gt; <code>max</code> () const </p>
<p> std::vector&lt; Real &gt; <code>gaussianPercentile</code> (Real y) const </p>
<p> std::vector&lt; Real &gt; <code>percentile</code> (Real y) const </p>
<p> std::vector&lt; Real &gt; <code>gaussianPotentialUpside</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>potentialUpside</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>gaussianValueAtRisk</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>valueAtRisk</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>gaussianExpectedShortfall</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>expectedShortfall</code> (Real percentile) const </p>
<p> std::vector&lt; Real &gt; <code>regret</code> (Real target) const </p>
<p> std::vector&lt; Real &gt; <code>gaussianShortfall</code> (Real target) const </p>
<p> std::vector&lt; Real &gt; <code>shortfall</code> (Real target) const </p>
<p> std::vector&lt; Real &gt; <code>gaussianAverageShortfall</code> (Real target) const </p>
<p> std::vector&lt; Real &gt; <code>averageShortfall</code> (Real target) const<br />
 <code>Modifiers</code> </p>
<pre><code>void reset (Size dimension=0)



template&lt;class Sequence &gt; void add (const Sequence &amp;sample, Real weight=1.0)



template&lt;class Iterator &gt; void add (Iterator begin, Iterator end, Real weight=1.0)



Protected Attributes</code></pre>
<p> Size <code>dimension_</code> </p>
<p> std::vector&lt; statistics_type &gt; <code>stats_</code> </p>
<p> std::vector&lt; Real &gt; <code>results_</code> </p>
<p> <code>Matrix</code> <code>quadraticSum_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class StatisticsType&gt; class QuantLib::GenericSequenceStatistics&lt; StatisticsType &gt;</h3>
<p>Statistics analysis of N-dimensional (sequence) data. </p>
<p> It provides 1-dimensional statistics as discrepancy plus N-dimensional (sequence) statistics (e.g. mean, variance, skewness, kurtosis, etc.) with one component for each dimension of the sample space. </p>
<p> For most of the statistics this class relies on the StatisticsType underlying class to provide 1-D methods that will be iterated for all the components of the N-D data. These lifted methods are the union of all the methods that might be requested to the 1-D underlying StatisticsType class, with the usual compile-time checks provided by the template approach. </p>
<p> <code>Tests</code></p>
<dl>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
