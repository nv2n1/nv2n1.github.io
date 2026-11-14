---
title: "analyticcontinuousgeometricaveragepriceasianengine(3)"
name: "analyticcontinuousgeometricaveragepriceasianengine"
section: "3"
letter: "a"
url: "/docs/linux/man/3-analyticcontinuousgeometricaveragepriceasianengine/"
description: "QuantLib::AnalyticContinuousGeometricAveragePriceAsianEngine – Pricing engine for European continuous geometric average price Asian."
---

<p>QuantLib::AnalyticContinuousGeometricAveragePriceAsianEngine &#8211; Pricing engine for European continuous geometric average price Asian. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/asian/analytic_cont_geom_av_price.hpp&gt; </p>
<p> Inherits <code>QuantLib::ContinuousAveragingAsianOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticContinuousGeometricAveragePriceAsianEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European continuous geometric average price Asian. </p>
<p> This class implements a continuous geometric average price Asian option with European exercise. The formula is from &#8216;Option Pricing Formulas&#8217;, E. G. Haug (1997) pag 96-97. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature, and results obtained using a discrete average approximation.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>handle seasoned options</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
