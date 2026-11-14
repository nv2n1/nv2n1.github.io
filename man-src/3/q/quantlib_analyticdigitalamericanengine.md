---
title: "quantlib_analyticdigitalamericanengine(3)"
name: "quantlib_analyticdigitalamericanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticdigitalamericanengine/"
description: "QuantLib::AnalyticDigitalAmericanEngine – Analytic pricing engine for American vanilla options with digital payoff."
---

<p>QuantLib::AnalyticDigitalAmericanEngine &#8211; Analytic pricing engine for American vanilla options with digital payoff. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analyticdigitalamericanengine.hpp&gt; </p>
<p> Inherits QuantLib::OneAssetOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticDigitalAmericanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Analytic pricing engine for American vanilla options with digital payoff. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>add more greeks (as of now only delta and rho available)</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value in case of cash-or-nothing at-hit digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of asset-or-nothing at-hit digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of cash-or-nothing at-expiry digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned value in case of asset-or-nothing at-expiry digital payoff is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks in case of cash-or-nothing at-hit digital payoff is tested by reproducing numerical derivatives.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
