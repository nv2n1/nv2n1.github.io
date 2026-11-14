---
title: "quantlib_analytichaganpricer(3)"
name: "quantlib_analytichaganpricer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analytichaganpricer/"
description: "QuantLib::AnalyticHaganPricer – CMS-coupon pricer."
---

<p>QuantLib::AnalyticHaganPricer &#8211; CMS-coupon pricer. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/conundrumpricer.hpp&gt; </p>
<p> Inherits <code>QuantLib::HaganPricer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticHaganPricer</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;swaptionVol, GFunctionFactory::YieldCurveModel modelOfYieldCurve, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>optionletPrice</code> (Option::Type optionType, Real strike) const </p>
<p> Real <code>swapletPrice</code> () const </p>
<h2>Detailed Description</h2>
<p>CMS-coupon pricer. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
