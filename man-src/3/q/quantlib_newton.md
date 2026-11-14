---
title: "quantlib_newton(3)"
name: "quantlib_newton"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_newton/"
description: "QuantLib::Newton – Newton 1-D solver"
---

<p>QuantLib::Newton &#8211; Newton 1-D solver </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/solvers1d/newton.hpp&gt; </p>
<p> Inherits <code>Solver1D&lt; Newton &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>template&lt;class F &gt; <code>Real</code> <code>solveImpl</code> (const F &amp;f, <code>Real</code> xAccuracy) const </p>
<h2>Detailed Description</h2>
<p>Newton 1-D solver </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This solver requires that the passed function object implement a method Real derivative(Real).</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking them against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
