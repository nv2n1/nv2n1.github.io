---
title: "constantestimator(3)"
name: "constantestimator"
section: "3"
letter: "c"
url: "/docs/linux/man/3-constantestimator/"
description: "QuantLib::ConstantEstimator – Constant-estimator volatility model."
---

<p>QuantLib::ConstantEstimator &#8211; Constant-estimator volatility model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/volatility/constantestimator.hpp&gt; </p>
<p> Inherits QuantLib::VolatilityCompositor. </p>
<h3>Public Member Functions</h3>
<p><code>ConstantEstimator</code> (Size size) </p>
<p> <code>TimeSeries</code>&lt; Volatility &gt; <code>calculate</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;) </p>
<p> void <code>calibrate</code> (const <code>TimeSeries</code>&lt; Volatility &gt; &amp;) </p>
<h2>Detailed Description</h2>
<p>Constant-estimator volatility model. </p>
<p> Volatilities are assumed to be expressed on an annual basis. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
