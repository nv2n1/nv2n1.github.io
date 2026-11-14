---
title: "quantlib_linearleastsquaresregression(3)"
name: "quantlib_linearleastsquaresregression"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_linearleastsquaresregression/"
description: "QuantLib::LinearLeastSquaresRegression – general linear least squares regression"
---

<p>QuantLib::LinearLeastSquaresRegression &#8211; general linear least squares regression </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/linearleastsquaresregression.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>LinearLeastSquaresRegression</code> (const std::vector&lt; ArgumentType &gt; &amp;x, const std::vector&lt; Real &gt; &amp;y, const std::vector&lt; boost::function1&lt; Real, ArgumentType &gt; &gt; &amp;v) </p>
<p> const <code>Array</code> &amp; <code>a</code> () const </p>
<p> const <code>Array</code> &amp; <code>error</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class ArgumentType = Real&gt; class QuantLib::LinearLeastSquaresRegression&lt; ArgumentType &gt;</h3>
<p>general linear least squares regression </p>
<p> References: &#8216;Numerical Recipes in C&#8217;, 2nd edition, Press, Teukolsky, Vetterling, Flannery, </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking their properties.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
