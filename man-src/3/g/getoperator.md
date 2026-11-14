---
title: "getoperator(3)"
name: "getoperator"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getoperator/"
description: "QuantLib::OperatorFactory – Black-Scholes-Merton differential operator."
---

<p>QuantLib::OperatorFactory &#8211; Black-Scholes-Merton differential operator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/finitedifferences/operatorfactory.hpp&gt; </p>
<h3>Static Public Member Functions</h3>
<p>static <code>TridiagonalOperator</code> <code>getOperator</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, const <code>Array</code> &amp;grid, <code>Time</code> residualTime, bool timeDependent) </p>
<p> static <code>TridiagonalOperator</code> <code>getOperator</code> (const boost::shared_ptr&lt; <code>OneFactorModel::ShortRateDynamics</code> &gt; &amp;process, const <code>Array</code> &amp;grid) </p>
<h2>Detailed Description</h2>
<p>Black-Scholes-Merton differential operator. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>coefficients are tested against constant BSM operator</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
