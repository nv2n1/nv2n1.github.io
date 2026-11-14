---
title: "quantlib_cumulativepoissondistribution(3)"
name: "quantlib_cumulativepoissondistribution"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cumulativepoissondistribution/"
description: "QuantLib::CumulativePoissonDistribution – Cumulative Poisson distribution function."
---

<p>QuantLib::CumulativePoissonDistribution &#8211; Cumulative Poisson distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/poissondistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>CumulativePoissonDistribution</code> (<code>Real</code> mu) </p>
<p> <code>Real</code> <code>operator()</code> (BigNatural k) const </p>
<h2>Detailed Description</h2>
<p>Cumulative Poisson distribution function. </p>
<p> This function provides an approximation of the integral of the Poisson distribution. </p>
<p> For this implementation see &#8216;Numerical Recipes in C&#8217;, 2nd edition, Press, Teukolsky, Vetterling, Flannery, chapter 6 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
