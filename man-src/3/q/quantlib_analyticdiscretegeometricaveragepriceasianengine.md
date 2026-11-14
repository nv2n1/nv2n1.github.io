---
title: "quantlib_analyticdiscretegeometricaveragepriceasianengine(3)"
name: "quantlib_analyticdiscretegeometricaveragepriceasianengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticdiscretegeometricaveragepriceasianengine/"
description: "QuantLib::AnalyticDiscreteGeometricAveragePriceAsianEngine – Pricing engine for European discrete geometric average price Asian."
---

<p>QuantLib::AnalyticDiscreteGeometricAveragePriceAsianEngine &#8211; Pricing engine for European discrete geometric average price Asian. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/asian/analytic_discr_geom_av_price.hpp&gt; </p>
<p> Inherits <code>QuantLib::DiscreteAveragingAsianOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticDiscreteGeometricAveragePriceAsianEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European discrete geometric average price Asian. </p>
<p> This class implements a discrete geometric average price Asian option, with European exercise. The formula is from &#8216;Asian Option&#8217;, E. Levy (1997) in &#8216;Exotic Options: The State of the Art&#8217;, edited by L. Clewlow, C. Strickland, pag 65-97 </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>implement correct theta, rho, and dividend-rho calculation</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the available greeks is tested against numerical calculations.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
