---
title: "quantlib_inversecumulativenormal(3)"
name: "quantlib_inversecumulativenormal"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_inversecumulativenormal/"
description: "QuantLib::InverseCumulativeNormal – Inverse cumulative normal distribution function."
---

<p>QuantLib::InverseCumulativeNormal &#8211; Inverse cumulative normal distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/normaldistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>InverseCumulativeNormal</code> (Real average=0.0, Real sigma=1.0) </p>
<p> Real <code>operator()</code> (Real x) const </p>
<h2>Detailed Description</h2>
<p>Inverse cumulative normal distribution function. </p>
<p> Given x between zero and one as the integral value of a gaussian normal distribution this class provides the value y such that formula here &#8230; </p>
<p> It use Acklam&#8217;s approximation: by Peter J. Acklam, University of Oslo, Statistics Division. URL: <a rel="nofollow" href="http://home.online.no/~pjacklam/notes/invnorm/index.html">http://home.online.no/~pjacklam/notes/invnorm/index.html</a> </p>
<p> This class can also be used to generate a gaussian normal distribution from a uniform distribution. This is especially useful when a gaussian normal distribution is generated from a low discrepancy uniform distribution: in this case the traditional Box-Muller approach and its variants would not preserve the sequence&#8217;s low-discrepancy. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
