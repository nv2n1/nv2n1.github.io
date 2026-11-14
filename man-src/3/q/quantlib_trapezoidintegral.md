---
title: "quantlib_trapezoidintegral(3)"
name: "quantlib_trapezoidintegral"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_trapezoidintegral/"
description: "QuantLib::TrapezoidIntegral – Integral of a one-dimensional function."
---

<p>QuantLib::TrapezoidIntegral &#8211; Integral of a one-dimensional function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/integrals/trapezoidintegral.hpp&gt; </p>
<p> Inherits QuantLib::Integrator. </p>
<h3>Public Member Functions</h3>
<p><code>TrapezoidIntegral</code> (Real accuracy, Size maxIterations) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>integrate</code> (const boost::function&lt; Real(Real)&gt; &amp;f, Real a, Real b) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class IntegrationPolicy&gt; class QuantLib::TrapezoidIntegral&lt; IntegrationPolicy &gt;</h3>
<p>Integral of a one-dimensional function. </p>
<p> Given a target accuracy $ \psilon $, the integral of a function $ f $ between $ a $ and $ b $ is calculated by means of the trapezoid formula [ int_{a}^{b} f mathrm{d}x = ac{1}{2} f(x_{0}) + f(x_{1}) + f(x_{2}) + ots + f(x_{N-1}) + ac{1}{2} f(x_{N}) ] where $ x_0 = a $, $ x_N = b $, and $ x_i = a+i Delta x $ with $ Delta x = (b-a)/N $. The number $ N $ of intervals is repeatedly increased until the target accuracy is reached. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the result is tested by checking it against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
