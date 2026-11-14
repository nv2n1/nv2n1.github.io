---
title: "resetupperlimit(3)"
name: "resetupperlimit"
section: "3"
letter: "r"
url: "/docs/linux/man/3-resetupperlimit/"
description: "QuantLib::NumericHaganPricer – CMS-coupon pricer."
---

<p>QuantLib::NumericHaganPricer &#8211; CMS-coupon pricer. </p>
<h2>Synopsis</h2>
<pre><code>NumericHaganPricer (const Handle&lt; SwaptionVolatilityStructure &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const Handle&lt; Quote &gt; &amp;meanReversion, Rate lowerLimit=0.0, Rate upperLimit=1.0, Real precision=1.0e-6)



Real upperLimit ()



Real stdDeviations ()



Real integrate (Real a, Real b, const ConundrumIntegrand &amp;Integrand) const



virtual Real optionletPrice (Option::Type optionType, Rate strike) const



virtual Real swapletPrice () const



Real resetUpperLimit (Real stdDeviationsForUpperLimit) const



Real refineIntegration (Real integralValue, const ConundrumIntegrand &amp;integrand) const



Public Attributes</code></pre>
<p> Inherits <code>QuantLib::HaganPricer</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>NumericHaganPricer (const Handle&lt; SwaptionVolatilityStructure &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const Handle&lt; Quote &gt; &amp;meanReversion, Rate lowerLimit=0.0, Rate upperLimit=1.0, Real precision=1.0e-6)



Real upperLimit ()



Real stdDeviations ()



Real integrate (Real a, Real b, const ConundrumIntegrand &amp;Integrand) const



virtual Real optionletPrice (Option::Type optionType, Rate strike) const



virtual Real swapletPrice () const



Real resetUpperLimit (Real stdDeviationsForUpperLimit) const



Real refineIntegration (Real integralValue, const ConundrumIntegrand &amp;integrand) const



Public Attributes</code></pre>
<p> Real <code>upperLimit_</code> </p>
<p> Real <code>stdDeviationsForUpperLimit_</code> </p>
<p> const Real <code>lowerLimit_</code> </p>
<p> const Real <code>requiredStdDeviations_</code> </p>
<p> const Real <code>precision_</code> </p>
<p> const Real <code>refiningIntegrationTolerance_</code></p>
<h2>Detailed Description</h2>
<p>CMS-coupon pricer. </p>
<p> Prices a cms coupon via static replication as in Hagan&#8217;s &#8216;Conundrums&#8230;&#8217; article via numerical integration based on prices of vanilla swaptions</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
