---
title: "numerichaganpricer(3)"
name: "numerichaganpricer"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numerichaganpricer/"
description: "QuantLib::NumericHaganPricer – CMS-coupon pricer."
---

<p>QuantLib::NumericHaganPricer &#8211; CMS-coupon pricer. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/conundrumpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::HaganPricer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>NumericHaganPricer</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion, Rate lowerLimit=0.0, Rate upperLimit=1.0, Real precision=1.0e-6) </p>
<p> Real <code>upperLimit</code> () </p>
<p> Real <code>stdDeviations</code> () </p>
<p> Real <code>integrate</code> (Real a, Real b, const ConundrumIntegrand &amp;Integrand) const </p>
<p> virtual Real <code>optionletPrice</code> (Option::Type optionType, Rate strike) const </p>
<p> virtual Real <code>swapletPrice</code> () const </p>
<p> Real <code>resetUpperLimit</code> (Real stdDeviationsForUpperLimit) const </p>
<p> Real <code>refineIntegration</code> (Real integralValue, const ConundrumIntegrand &amp;integrand) const </p>
<h3>Public Attributes</h3>
<p>Real <code>upperLimit_</code> </p>
<p> Real <code>stdDeviationsForUpperLimit_</code> </p>
<p> const Real <code>lowerLimit_</code> </p>
<p> const Real <code>requiredStdDeviations_</code> </p>
<p> const Real <code>precision_</code> </p>
<p> const Real <code>refiningIntegrationTolerance_</code> </p>
<h2>Detailed Description</h2>
<p>CMS-coupon pricer. </p>
<p> Prices a cms coupon via static replication as in Hagan&#8217;s &#8216;Conundrums&#8230;&#8217; article via numerical integration based on prices of vanilla swaptions </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
