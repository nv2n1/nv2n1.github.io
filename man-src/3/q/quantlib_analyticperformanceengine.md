---
title: "quantlib_analyticperformanceengine(3)"
name: "quantlib_analyticperformanceengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticperformanceengine/"
description: "QuantLib::AnalyticPerformanceEngine – Pricing engine for performance options using analytical formulae."
---

<p>QuantLib::AnalyticPerformanceEngine &#8211; Pricing engine for performance options using analytical formulae. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/cliquet/analyticperformanceengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::CliquetOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticPerformanceEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for performance options using analytical formulae. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
