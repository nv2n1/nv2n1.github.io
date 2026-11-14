---
title: "analyticeuropeanengine(3)"
name: "analyticeuropeanengine"
section: "3"
letter: "a"
url: "/docs/linux/man/3-analyticeuropeanengine/"
description: "QuantLib::AnalyticEuropeanEngine – Pricing engine for European vanilla options using analytical formulae."
---

<p>QuantLib::AnalyticEuropeanEngine &#8211; Pricing engine for European vanilla options using analytical formulae. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analyticeuropeanengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticEuropeanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European vanilla options using analytical formulae. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</p>
<dt>*</p>
<dd>the correctness of the returned implied volatility is tested by using it for reproducing the target value.</p>
<dt>*</p>
<dd>the implied-volatility calculation is tested by checking that it does not modify the option.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of cash-or-nothing digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of asset-or-nothing digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of gap digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks in case of cash-or-nothing digital payoff is tested by reproducing numerical derivatives.</dl>
</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>, and <code>Replication.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
