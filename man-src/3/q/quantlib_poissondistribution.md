---
title: "quantlib_poissondistribution(3)"
name: "quantlib_poissondistribution"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_poissondistribution/"
description: "QuantLib::PoissonDistribution – Normal distribution function."
---

<p>QuantLib::PoissonDistribution &#8211; Normal distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/poissondistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>PoissonDistribution</code> (Real mu) </p>
<p> Real <code>operator()</code> (BigNatural k) const </p>
<h2>Detailed Description</h2>
<p>Normal distribution function. </p>
<p> Given an integer $ k $, it returns its probability in a Poisson distribution. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
