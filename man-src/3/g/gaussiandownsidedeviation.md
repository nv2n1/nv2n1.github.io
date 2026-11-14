---
title: "gaussiandownsidedeviation(3)"
name: "gaussiandownsidedeviation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gaussiandownsidedeviation/"
description: "QuantLib::GenericGaussianStatistics – Statistics tool for gaussian-assumption risk measures."
---

<p>QuantLib::GenericGaussianStatistics &#8211; Statistics tool for gaussian-assumption risk measures. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/statistics/gaussianstatistics.hpp&gt; </p>
<p> Inherits Stat. </p>
<h3>Public Types</h3>
<p>typedef Stat::value_type <code>value_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>GenericGaussianStatistics</code> (const Stat &amp;s) </p>
<p> <code>Gaussian risk measures</code> </p>
<p> Real <code>gaussianDownsideVariance</code> () const </p>
<p> Real <code>gaussianDownsideDeviation</code> () const </p>
<p> Real <code>gaussianRegret</code> (Real target) const </p>
<p> Real <code>gaussianPercentile</code> (Real percentile) const </p>
<p> Real <code>gaussianTopPercentile</code> (Real percentile) const </p>
<p> Real <code>gaussianPotentialUpside</code> (Real percentile) const<br />
 <i>gaussian-assumption Potential-Upside at a given percentile </i><br />
 Real <code>gaussianValueAtRisk</code> (Real percentile) const<br />
 <i>gaussian-assumption Value-At-Risk at a given percentile </i><br />
 Real <code>gaussianExpectedShortfall</code> (Real percentile) const<br />
 <i>gaussian-assumption Expected Shortfall at a given percentile </i><br />
 Real <code>gaussianShortfall</code> (Real target) const<br />
 <i>gaussian-assumption Shortfall (observations below target) </i><br />
 Real <code>gaussianAverageShortfall</code> (Real target) const<br />
 <i>gaussian-assumption </i><code>Average</code> Shortfall (averaged shortfallness)</p>
<h2>Detailed Description</h2>
<h3>template&lt;class Stat&gt; class QuantLib::GenericGaussianStatistics&lt; Stat &gt;</h3>
<p>Statistics tool for gaussian-assumption risk measures. </p>
<p> This class wraps a somewhat generic statistic tool and adds a number of gaussian risk measures (e.g.: value-at-risk, expected shortfall, etc.) based on the mean and variance provided by the underlying statistic tool.</p>
<h2>Member Function Documentation</h2>
<h3>Real gaussianDownsideVariance () const</h3>
<p>returns the downside variance, defined as [ ac{N}{N-1} imes ac{ um_{i=1}^{N} heta imes x_i^{2}}{ um_{i=1}^{N} w_i} ], where $ heta $ = 0 if x &gt; 0 and $ heta $ =1 if x &lt;0</p>
<h3>Real gaussianDownsideDeviation () const</h3>
<p>returns the downside deviation, defined as the square root of the downside variance.</p>
<h3>Real gaussianRegret (Real target) const</h3>
<p>returns the variance of observations below target [ ac{um w_i (min(0, x_i-target))^2 }{um w_i}. ] </p>
<p> See Dembo, Freeman &#8216;The Rules Of Risk&#8217;, Wiley (2001)</p>
<h3>Real gaussianPercentile (Real percentile) const</h3>
<p>gaussian-assumption y-th percentile, defined as the value x such that [ y = ac{1}{qrt{2<br />
 i}} int_{-infty}^{x} 
