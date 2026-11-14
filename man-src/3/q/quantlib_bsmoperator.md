---
title: "quantlib_bsmoperator(3)"
name: "quantlib_bsmoperator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_bsmoperator/"
description: "QuantLib::BSMOperator – Black-Scholes-Merton differential operator."
---

<p>QuantLib::BSMOperator &#8211; Black-Scholes-Merton differential operator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/bsmoperator.hpp&gt; </p>
<p> Inherits <code>QuantLib::TridiagonalOperator</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BSMOperator</code> (Size size, <code>Real</code> dx, <code>Rate</code> r, <code>Rate</code> q, <code>Volatility</code> sigma) </p>
<p> <code>BSMOperator</code> (const <code>Array</code> &amp;grid, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, <code>Time</code> residualTime) </p>
<h2>Detailed Description</h2>
<p>Black-Scholes-Merton differential operator. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
