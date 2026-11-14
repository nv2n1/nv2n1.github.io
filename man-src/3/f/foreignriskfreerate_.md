---
title: "foreignriskfreerate_(3)"
name: "foreignriskfreerate_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-foreignriskfreerate_/"
description: "QuantLib::QuantoEngine – Quanto engine."
---

<p>QuantLib::QuantoEngine &#8211; Quanto engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/quanto/quantoengine.hpp&gt; </p>
<p> Inherits <code>GenericEngine&lt; Instr::arguments, QuantoOptionResults&lt; Instr::results &gt; &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QuantoEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;foreignRiskFreeRate, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;exchangeRateVolatility, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;correlation) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>foreignRiskFreeRate_</code> </p>
<p> <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; <code>exchangeRateVolatility_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>correlation_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Instr, class Engine&gt; class QuantLib::QuantoEngine&lt; Instr, Engine &gt;</h3>
<p>Quanto engine. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>for the time being, this engine will only work with simple Black-Scholes processes (i.e., no Merton.)</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
