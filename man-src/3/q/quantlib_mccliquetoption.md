---
title: "quantlib_mccliquetoption(3)"
name: "quantlib_mccliquetoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_mccliquetoption/"
description: "QuantLib::McCliquetOption – simple example of Monte Carlo pricer"
---

<p>QuantLib::McCliquetOption &#8211; simple example of Monte Carlo pricer </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/pricers/mccliquetoption.hpp&gt; </p>
<p> Inherits <code>McPricer&lt; SingleVariate, PseudoRandom &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>McCliquetOption</code> (Option::Type type, <code>Real</code> underlying, <code>Real</code> moneyness, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendYield, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeRate, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;volatility, const std::vector&lt; <code>Time</code> &gt; &amp;times, <code>Real</code> accruedCoupon, <code>Real</code> lastFixing, <code>Real</code> localCap, <code>Real</code> localFloor, <code>Real</code> globalCap, <code>Real</code> globalFloor, bool redemptionOnly, BigNatural seed=0) </p>
<h2>Detailed Description</h2>
<p>simple example of Monte Carlo pricer </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
