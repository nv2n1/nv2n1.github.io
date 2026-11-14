---
title: "quantlib_newtonsafe(3)"
name: "quantlib_newtonsafe"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_newtonsafe/"
description: "QuantLib::NewtonSafe – safe Newton 1-D solver"
---

<p>QuantLib::NewtonSafe &#8211; safe Newton 1-D solver </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/solvers1d/newtonsafe.hpp&gt; </p>
<p> Inherits <code>Solver1D&lt; NewtonSafe &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>template&lt;class F &gt; <code>Real</code> <code>solveImpl</code> (const F &amp;f, <code>Real</code> xAccuracy) const </p>
<h2>Detailed Description</h2>
<p>safe Newton 1-D solver </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This solver requires that the passed function object implement a method Real derivative(Real).</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking them against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
