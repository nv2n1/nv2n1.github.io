---
title: "quantlib_normaldistribution(3)"
name: "quantlib_normaldistribution"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_normaldistribution/"
description: "QuantLib::NormalDistribution – Normal distribution function."
---

<p>QuantLib::NormalDistribution &#8211; Normal distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/normaldistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>NormalDistribution</code> (Real average=0.0, Real sigma=1.0) </p>
<p> Real <code>operator()</code> (Real x) const </p>
<p> Real <code>derivative</code> (Real x) const </p>
<h2>Detailed Description</h2>
<p>Normal distribution function. </p>
<p> Given x, it returns its probability in a Gaussian normal distribution. It provides the first derivative too. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against numerical calculations. Cross-checks are also performed against the <code>CumulativeNormalDistribution</code> and <code>InverseCumulativeNormal</code> classes.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
