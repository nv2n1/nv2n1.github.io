---
title: "quantlib_analyticbarrierengine(3)"
name: "quantlib_analyticbarrierengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticbarrierengine/"
description: "QuantLib::AnalyticBarrierEngine – Pricing engine for barrier options using analytical formulae."
---

<p>QuantLib::AnalyticBarrierEngine &#8211; Pricing engine for barrier options using analytical formulae. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/barrier/analyticbarrierengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::BarrierOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticBarrierEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for barrier options using analytical formulae. </p>
<p> The formulas are taken from &#8216;Option pricing formulas&#8217;, E.G. Haug, McGraw-Hill, p.69 and following. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Replication.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
