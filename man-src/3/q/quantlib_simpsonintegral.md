---
title: "quantlib_simpsonintegral(3)"
name: "quantlib_simpsonintegral"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_simpsonintegral/"
description: "QuantLib::SimpsonIntegral – Integral of a one-dimensional function."
---

<p>QuantLib::SimpsonIntegral &#8211; Integral of a one-dimensional function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/simpsonintegral.hpp&gt; </p>
<p> Inherits <code>TrapezoidIntegral&lt; Default &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SimpsonIntegral</code> (Real accuracy, Size maxIterations) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<h2>Detailed Description</h2>
<p>Integral of a one-dimensional function. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the result is tested by checking it against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
