---
title: "potentialupside(3)"
name: "potentialupside"
section: "3"
letter: "p"
url: "/docs/linux/man/3-potentialupside/"
description: "QuantLib::GenericRiskStatistics – empirical-distribution risk measures"
---

<p>QuantLib::GenericRiskStatistics &#8211; empirical-distribution risk measures </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/statistics/riskstatistics.hpp&gt;</code></pre>
<p> Inherits S.</p>
<h3>Public Types</h3>
<p>typedef S::value_type <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>Real <code>semiVariance</code> () const </p>
<p> Real <code>semiDeviation</code> () const </p>
<p> Real <code>downsideVariance</code> () const </p>
<p> Real <code>downsideDeviation</code> () const </p>
<p> Real <code>regret</code> (Real target) const </p>
<p> Real <code>potentialUpside</code> (Real percentile) const<br />
 <i>potential upside (the reciprocal of VAR) at a given percentile </i><br />
 Real <code>valueAtRisk</code> (Real percentile) const<br />
 <i>value-at-risk at a given percentile </i><br />
 Real <code>expectedShortfall</code> (Real percentile) const<br />
 <i>expected shortfall at a given percentile </i><br />
 Real <code>shortfall</code> (Real target) const </p>
<p> Real <code>averageShortfall</code> (Real target) const</p>
<h2>Detailed Description</h2>
<h3>template&lt;class S&gt; class QuantLib::GenericRiskStatistics&lt; S &gt;</h3>
<p>empirical-distribution risk measures </p>
<p> This class wraps a somewhat generic statistic tool and adds a number of risk measures (e.g.: value-at-risk, expected shortfall, etc.) based on the data distribution as reported by the underlying statistic tool. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add historical annualized volatility</dl>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>Real semiVariance () const</h3>
<p>returns the variance of observations below the mean, [ ac{N}{N-1} mathrm{E}</p>
<hr>
<p>)^2 ;|; x &lt; </p>
<hr>
<p>ngle ight]. ] </p>
<p> See Markowitz (1959).</p>
<h3>Real semiDeviation () const</h3>
<p>returns the semi deviation, defined as the square root of the semi variance.</p>
<h3>Real downsideVariance () const</h3>
<p>returns the variance of observations below 0.0, [ ac{N}{N-1} mathrm{E}</p>
<hr>
<p>al downsideDeviation () const&quot; </p>
<p> returns the downside deviation, defined as the square root of the downside variance.</p>
<h3>Real regret (Real target) const</h3>
<p>returns the variance of observations below target, [ ac{N}{N-1} mathrm{E}</p>
<hr>
<p>e Dembo and Freeman, &#8216;The Rules Of Risk&#8217;, Wiley (2001).</p>
<h3>Real potentialUpside (Real centile) const</h3>
<p>potential upside (the reciprocal of VAR) at a given percentile </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>percentile must be in range [90-100%)</dl>
<h3>Real valueAtRisk (Real centile) const</h3>
<p>value-at-risk at a given percentile </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>percentile must be in range [90-100%)</dl>
<h3>Real expectedShortfall (Real centile) const</h3>
<p>expected shortfall at a given percentile </p>
<p> returns the expected loss in case that the loss exceeded a VaR threshold, </p>
<p> [ mathrm{E}</p>
<hr>
<p> average of observations below the given percentile $ p $. Also know as conditional value-at-risk. </p>
<p> See Artzner, Delbaen, Eber and Heath, &#8216;Coherent measures of risk&#8217;, Mathematical Finance 9 (1999) </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>percentile must be in range [90-100%)</dl>
<h3>Real shortfall (Real target) const</h3>
<p>probability of missing the given target, defined as [ mathrm{E}</p>
<hr>
<p>ta ;|; (-infty,infty) ight] ] where [ Theta(x) = </p>
<hr>
<p>al averageShortfall (Real target) const&quot; </p>
<p> averaged shortfallness, defined as [ mathrm{E}</p>
<hr>
<p>nerated automatically by Doxygen for QuantLib from the source code.</p>
