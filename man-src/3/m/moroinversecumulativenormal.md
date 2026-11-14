---
title: "moroinversecumulativenormal(3)"
name: "moroinversecumulativenormal"
section: "3"
letter: "m"
url: "/docs/linux/man/3-moroinversecumulativenormal/"
description: "QuantLib::MoroInverseCumulativeNormal – Moro Inverse cumulative normal distribution class."
---

<p>QuantLib::MoroInverseCumulativeNormal &#8211; Moro Inverse cumulative normal distribution class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/normaldistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>MoroInverseCumulativeNormal</code> (Real average=0.0, Real sigma=1.0) </p>
<p> Real <code>operator()</code> (Real x) const </p>
<h2>Detailed Description</h2>
<p>Moro Inverse cumulative normal distribution class. </p>
<p> Given x between zero and one as the integral value of a gaussian normal distribution this class provides the value y such that formula here &#8230; </p>
<p> It uses Beasly and Springer approximation, with an improved approximation for the tails. See Boris Moro, &#8216;The Full Monte&#8217;, 1995, Risk Magazine. </p>
<p> This class can also be used to generate a gaussian normal distribution from a uniform distribution. This is especially useful when a gaussian normal distribution is generated from a low discrepancy uniform distribution: in this case the traditional Box-Muller approach and its variants would not preserve the sequence&#8217;s low-discrepancy. </p>
<p> Peter J. Acklam&#8217;s approximation is better and is available as <code>QuantLib::InverseCumulativeNormal</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
