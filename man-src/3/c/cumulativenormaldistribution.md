---
title: "cumulativenormaldistribution(3)"
name: "cumulativenormaldistribution"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cumulativenormaldistribution/"
description: "QuantLib::CumulativeNormalDistribution – Cumulative normal distribution function."
---

<p>QuantLib::CumulativeNormalDistribution &#8211; Cumulative normal distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/normaldistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>CumulativeNormalDistribution</code> (Real average=0.0, Real sigma=1.0) </p>
<p> Real <code>operator()</code> (Real x) const </p>
<p> Real <code>derivative</code> (Real x) const </p>
<h2>Detailed Description</h2>
<p>Cumulative normal distribution function. </p>
<p> Given x it provides an approximation to the integral of the gaussian normal distribution: formula here &#8230; </p>
<p> For this implementation see M. Abramowitz and I. Stegun, Handbook of Mathematical Functions, Dover Publications, New York (1972) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
