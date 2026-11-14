---
title: "analyticcliquetengine(3)"
name: "analyticcliquetengine"
section: "3"
letter: "a"
url: "/docs/linux/man/3-analyticcliquetengine/"
description: "QuantLib::AnalyticCliquetEngine – Pricing engine for Cliquet options using analytical formulae."
---

<p>QuantLib::AnalyticCliquetEngine &#8211; Pricing engine for Cliquet options using analytical formulae. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/cliquet/analyticcliquetengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::CliquetOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticCliquetEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for Cliquet options using analytical formulae. </p>
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
