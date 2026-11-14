---
title: "quantlib_cumulativestudentdistribution(3)"
name: "quantlib_cumulativestudentdistribution"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cumulativestudentdistribution/"
description: "QuantLib::CumulativeStudentDistribution – Cumulative Student t-distribution."
---

<p>QuantLib::CumulativeStudentDistribution &#8211; Cumulative Student t-distribution. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/studenttdistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>CumulativeStudentDistribution</code> (<code>Integer</code> n) </p>
<p> <code>Real</code> <code>operator()</code> (<code>Real</code> x) const </p>
<h2>Detailed Description</h2>
<p>Cumulative Student t-distribution. </p>
<p> Cumulative distribution function for $ n $ degrees of freedom (see mathworld.wolfram.com): [ F(x) = int_{-infty}^x,f(y),dy = ac{1}{2}, +,ac{1}{2},sgn(x), </p>
<hr>
<p> regularized incomplete beta function. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
