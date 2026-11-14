---
title: "vanillaoption(3)"
name: "vanillaoption"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vanillaoption/"
description: "QuantLib::VanillaOption – Vanilla option (no discrete dividends, no barriers) on a single asset."
---

<p>QuantLib::VanillaOption &#8211; Vanilla option (no discrete dividends, no barriers) on a single asset. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/vanillaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<p> Inherited by <code>EuropeanOption</code>. </p>
<h3>Public Member Functions</h3>
<p><code>VanillaOption</code> (const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;) </p>
<p> <code>Volatility</code> <code>impliedVolatility</code> (<code>Real</code> price, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, <code>Real</code> accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const </p>
<h2>Detailed Description</h2>
<p>Vanilla option (no discrete dividends, no barriers) on a single asset. </p>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> impliedVolatility (<code>Real</code> price, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp; process, <code>Real</code> accuracy = 1.0e-4, Size maxEvaluations = 100, <code>Volatility</code> minVol = 1.0e-7, <code>Volatility</code> maxVol = 4.0) const</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>currently, this method returns the Black-Scholes implied volatility using analytic formulas for European options and a finite-difference method for American and Bermudan options. It will give unconsistent results if the pricing was performed with any other methods (such as jump-diffusion models.)</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>options with a gamma that changes sign (e.g., binary options) have values that are <code>not</code> monotonic in the volatility. In these cases, the calculation can fail and the result (if any) is almost meaningless. Another possible source of failure is to have a target value that is not attainable with any volatility, e.g., a target value lower than the intrinsic value in the case of American options.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
