---
title: "quantlib_blackscholesmertonprocess(3)"
name: "quantlib_blackscholesmertonprocess"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackscholesmertonprocess/"
description: "QuantLib::BlackScholesMertonProcess – Merton (1973) extension to the Black-Scholes stochastic process."
---

<p>QuantLib::BlackScholesMertonProcess &#8211; Merton (1973) extension to the Black-Scholes stochastic process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/blackscholesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::GeneralizedBlackScholesProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackScholesMertonProcess</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;x0, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<h2>Detailed Description</h2>
<p>Merton (1973) extension to the Black-Scholes stochastic process. </p>
<p> This class describes the stochastic process for a stock or stock index paying a continuous dividend yield given by [ dS(t, S) = (r(t) &#8211; q(t) &#8211; ac{igma(t, S)^2}{2}) dt + igma dW_t. ] </p>
<p> <code>Examples: </code> </p>
<p> <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, and <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
