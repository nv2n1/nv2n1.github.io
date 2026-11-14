---
title: "quantlib_gammafunction(3)"
name: "quantlib_gammafunction"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gammafunction/"
description: "QuantLib::GammaFunction – Gamma function class."
---

<p>QuantLib::GammaFunction &#8211; Gamma function class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/gammadistribution.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<h3>Public Member Functions</h3>
<p>Real <code>logValue</code> (Real x) const </p>
<h2>Detailed Description</h2>
<p>Gamma function class. </p>
<p> This is a function defined by [ Gamma(z) = int_0^{infty}t^{z-1}e^{-t}dt ] </p>
<p> The implementation of the algorithm was inspired by &#8216;Numerical Recipes in C&#8217;, 2nd edition, Press, Teukolsky, Vetterling, Flannery, chapter 6 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
