---
title: "quantlib_analyticdividendeuropeanengine(3)"
name: "quantlib_analyticdividendeuropeanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticdividendeuropeanengine/"
description: "QuantLib::AnalyticDividendEuropeanEngine – Analytic pricing engine for European options with discrete dividends."
---

<p>QuantLib::AnalyticDividendEuropeanEngine &#8211; Analytic pricing engine for European options with discrete dividends. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analyticdividendeuropeanengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::DividendVanillaOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticDividendEuropeanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Analytic pricing engine for European options with discrete dividends. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
