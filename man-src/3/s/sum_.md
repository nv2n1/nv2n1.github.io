---
title: "sum_(3)"
name: "sum_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sum_/"
description: "QuantLib::IncrementalStatistics – Statistics tool based on incremental accumulation."
---

<p>QuantLib::IncrementalStatistics &#8211; Statistics tool based on incremental accumulation. </p>
<h2>Synopsis</h2>
<pre><code>void add (Real value, Real weight=1.0)


adds a datum to the set, possibly with a weight


template&lt;class DataIterator &gt; void addSequence (DataIterator begin, DataIterator end)


adds a sequence of data to the set, with default weight


template&lt;class DataIterator , class WeightIterator &gt; void addSequence (DataIterator begin, DataIterator end, WeightIterator wbegin)


adds a sequence of data to the set, each with its weight


void reset ()


resets the data to a null set




Protected Attributes</code></pre>
<h3>Public Types</h3>
<p>typedef <code>Real</code> <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>Inspectors</code> </p>
<p> Size <code>samples</code> () const<br />
 <i>number of samples collected </i><br />
 <code>Real</code> <code>weightSum</code> () const<br />
 <i>sum of data weights </i><br />
 <code>Real</code> <code>mean</code> () const </p>
<p> <code>Real</code> <code>variance</code> () const </p>
<p> <code>Real</code> <code>standardDeviation</code> () const </p>
<p> <code>Real</code> <code>errorEstimate</code> () const </p>
<p> <code>Real</code> <code>skewness</code> () const </p>
<p> <code>Real</code> <code>kurtosis</code> () const </p>
<p> <code>Real</code> <code>min</code> () const </p>
<p> <code>Real</code> <code>max</code> () const </p>
<p> <code>Real</code> <code>downsideVariance</code> () const </p>
<p> <code>Real</code> <code>downsideDeviation</code> () const<br />
 <code>Modifiers</code> </p>
<pre><code>void add (Real value, Real weight=1.0)


adds a datum to the set, possibly with a weight


template&lt;class DataIterator &gt; void addSequence (DataIterator begin, DataIterator end)


adds a sequence of data to the set, with default weight


template&lt;class DataIterator , class WeightIterator &gt; void addSequence (DataIterator begin, DataIterator end, WeightIterator wbegin)


adds a sequence of data to the set, each with its weight


void reset ()


resets the data to a null set




Protected Attributes</code></pre>
<p> Size <code>sampleNumber_</code> </p>
<p> Size <code>downsideSampleNumber_</code> </p>
<p> <code>Real</code> <code>sampleWeight_</code> </p>
<p> <code>Real</code> <code>downsideSampleWeight_</code> </p>
<p> <code>Real</code> <code>sum_</code> </p>
<p> <code>Real</code> <code>quadraticSum_</code> </p>
<p> <code>Real</code> <code>downsideQuadraticSum_</code> </p>
<p> <code>Real</code> <code>cubicSum_</code> </p>
<p> <code>Real</code> <code>fourthPowerSum_</code> </p>
<p> <code>Real</code> <code>min_</code> </p>
<p> <code>Real</code> <code>max_</code></p>
<h2>Detailed Description</h2>
<p>Statistics tool based on incremental accumulation. </p>
<p> It can accumulate a set of data and return statistics (e.g: mean, variance, skewness, kurtosis, error estimation, etc.) </p>
<p> <code>Warning</code></p>
<dl>
<dd>high moments are numerically unstable for high average/standardDeviation ratios.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> mean () const</h3>
<p>returns the mean, defined as [ </p>
<hr>
<p>ngle = ac{um w_i x_i}{um w_i}. ]</p>
<h3><code>Real</code> variance () const</h3>
<p>returns the variance, defined as [ ac{N}{N-1} </p>
<hr>
<p>. ]</p>
<h3><code>Real</code> standardDeviation () const</h3>
<p>returns the standard deviation $ igma $, defined as the square root of the variance.</p>
<h3><code>Real</code> errorEstimate () const</h3>
<p>returns the error estimate $ \psilon $, defined as the square root of the ratio of the variance to the number of samples.</p>
<h3><code>Real</code> skewness () const</h3>
<p>returns the skewness, defined as [ ac{N^2}{(N-1)(N-2)} ac{</p>
<hr>
<p>}{igma^3}. ] The above evaluates to 0 for a Gaussian distribution.</p>
<h3><code>Real</code> kurtosis () const</h3>
<p>returns the excess kurtosis, defined as [ ac{N^2(N+1)}{(N-1)(N-2)(N-3)} ac{</p>
<hr>
<p>}{igma^4} &#8211; ac{3(N-1)^2}{(N-2)(N-3)}. ] The above evaluates to 0 for a Gaussian distribution.</p>
<h3><code>Real</code> min () const</h3>
<p>returns the minimum sample value</p>
<h3><code>Real</code> max () const</h3>
<p>returns the maximum sample value</p>
<h3><code>Real</code> downsideVariance () const</h3>
<p>returns the downside variance, defined as [ ac{N}{N-1} imes ac{ um_{i=1}^{N} heta imes x_i^{2}}{ um_{i=1}^{N} w_i} ], where $ heta $ = 0 if x &gt; 0 and $ heta $ =1 if x &lt;0</p>
<h3><code>Real</code> downsideDeviation () const</h3>
<p>returns the downside deviation, defined as the square root of the downside variance.</p>
<h3>void add (<code>Real</code> value, <code>Real</code> weight = 1.0)</h3>
<p>adds a datum to the set, possibly with a weight </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>weight must be positive or null</dl>
<h3>void addSequence (DataIterator begin, DataIterator end, WeightIterator wbegin)</h3>
<p>adds a sequence of data to the set, each with its weight </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>weights must be positive or null</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
