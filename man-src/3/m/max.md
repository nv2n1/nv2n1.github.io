---
title: "max(3)"
name: "max"
section: "3"
letter: "m"
url: "/docs/linux/man/3-max/"
description: "QuantLib::GeneralStatistics – Statistics tool."
---

<h2 class="name">NAME</h2>
<p> QuantLib::GeneralStatistics &#8211; Statistics tool. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/statistics/generalstatistics.hpp&gt; </p>
<h3>Public Types</h3>
<p> typedef Real <code>value_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>Inspectors</code> </p>
<p> Size <code>samples</code> () const<br />
 <i>number of samples collected </i><br />
 const std::vector&lt; std::pair&lt; Real, Real &gt; &gt; &amp; <code>data</code> () const<br />
 <i>collected data </i><br />
 Real <code>weightSum</code> () const<br />
 <i>sum of data weights </i><br />
 Real <code>mean</code> () const </p>
<p> Real <code>variance</code> () const </p>
<p> Real <code>standardDeviation</code> () const </p>
<p> Real <code>errorEstimate</code> () const </p>
<p> Real <code>skewness</code> () const </p>
<p> Real <code>kurtosis</code> () const </p>
<p> Real <code>min</code> () const </p>
<p> Real <code>max</code> () const </p>
<p> template&lt;class Func , class Predicate &gt; std::pair&lt; Real, Size &gt; <code>expectationValue</code> (const Func &amp;f, const Predicate &amp;inRange) const </p>
<p> Real <code>percentile</code> (Real y) const </p>
<p> Real <code>topPercentile</code> (Real y) const </p>
<p> <code>Modifiers</code> </p>
<p> void <code>add</code> (Real value, Real weight=1.0)<br />
 <i>adds a datum to the set, possibly with a weight </i><br />
 template&lt;class DataIterator &gt; void <code>addSequence</code> (DataIterator begin, DataIterator end)<br />
 <i>adds a sequence of data to the set, with default weight </i><br />
 template&lt;class DataIterator , class WeightIterator &gt; void <code>addSequence</code> (DataIterator begin, DataIterator end, WeightIterator wbegin)<br />
 <i>adds a sequence of data to the set, each with its weight </i><br />
 void <code>reset</code> ()<br />
 <i>resets the data to a null set </i><br />
 void <code>sort</code> () const<br />
 <i>sort the data set in increasing order </i></p>
<h2>Detailed Description</h2>
<p> Statistics tool. </p>
<p> This class accumulates a set of data and returns their statistics (e.g: mean, variance, skewness, kurtosis, error estimation, percentile, etc.) based on the empirical distribution (no gaussian assumption) </p>
<p> It doesn&#8217;t suffer the numerical instability problem of <code>IncrementalStatistics</code>. The downside is that it stores all samples, thus increasing the memory requirements.</p>
<h2>Member Function Documentation</h2>
<h3>Real mean () const</h3>
<p> returns the mean, defined as [ </p>
<hr>
<p>ngle = ac{um w_i x_i}{um w_i}. ]</p>
<h3>Real variance () const</h3>
<p> returns the variance, defined as [ igma^2 = ac{N}{N-1} </p>
<hr>
<p>. ]</p>
<h3>Real standardDeviation () const</h3>
<p> returns the standard deviation $ igma $, defined as the square root of the variance.</p>
<h3>Real errorEstimate () const</h3>
<p> returns the error estimate on the mean value, defined as $ \psilon = igma/qrt{N}. $</p>
<h3>Real skewness () const</h3>
<p> returns the skewness, defined as [ ac{N^2}{(N-1)(N-2)} ac{</p>
<hr>
<p>}{igma^3}. ] The above evaluates to 0 for a Gaussian distribution.</p>
<h3>Real kurtosis () const</h3>
<p> returns the excess kurtosis, defined as [ ac{N^2(N+1)}{(N-1)(N-2)(N-3)} ac{</p>
<hr>
<p>}{igma^4} &#8211; ac{3(N-1)^2}{(N-2)(N-3)}. ] The above evaluates to 0 for a Gaussian distribution.</p>
<h3>Real min () const</h3>
<p> returns the minimum sample value</p>
<h3>Real max () const</h3>
<p> returns the maximum sample value</p>
<h3>std::pair&lt;Real,Size&gt; expectationValue (const Func &amp; f, const Predicate &amp; inRange) const</h3>
<p> Expectation value of a function $ f $ on a given range $ mathcal{R} $, i.e., [ mathrm{E}</p>
<hr>
<p> range is passed as a boolean function returning true if the argument belongs to the range or false otherwise. </p>
<p> The function returns a pair made of the result and the number of observations in the given range.</p>
<h3>Real percentile (Real y) const</h3>
<p> $ y $-th percentile, defined as the value $ t [ y = ac{um_{x_i &lt; nge $ (0-1]. $ </p>
<h3>Real topPercentile (Real y) const</h3>
<p> $ y $-th top percentile, defined as the value $ t [ y = ac{um_{x_i &gt; nge $ (0-1]. $ </p>
<h3>void add (Real value, Real weight = 1.0)</h3>
<p> adds a datum to the set, possibly with a weight </p>
<p> <code>Precondition:</code></p>
<dl>
<dt>
<dd> weights must be positive or null</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
