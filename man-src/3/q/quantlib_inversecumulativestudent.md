---
title: "quantlib_inversecumulativestudent(3)"
name: "quantlib_inversecumulativestudent"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_inversecumulativestudent/"
description: "QuantLib::InverseCumulativeStudent – Inverse cumulative Student t-distribution."
---

<p>QuantLib::InverseCumulativeStudent &#8211; Inverse cumulative Student t-distribution. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/studenttdistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>InverseCumulativeStudent</code> (<code>Integer</code> n, <code>Real</code> accuracy=1e-6, Size maxIterations=50) </p>
<p> <code>Real</code> <code>operator()</code> (<code>Real</code> x) const </p>
<h2>Detailed Description</h2>
<p>Inverse cumulative Student t-distribution. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>Find/implement an efficient algorithm for evaluating the cumulative Student t-distribution, replacing the <code>Newton</code> iteration</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
