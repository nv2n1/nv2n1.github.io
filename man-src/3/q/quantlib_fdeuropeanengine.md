---
title: "quantlib_fdeuropeanengine(3)"
name: "quantlib_fdeuropeanengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fdeuropeanengine/"
description: "QuantLib::FDEuropeanEngine – Pricing engine for European options using finite-differences."
---

<p>QuantLib::FDEuropeanEngine &#8211; Pricing engine for European options using finite-differences. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/fdeuropeanengine.hpp&gt; </p>
<p> Inherits QuantLib::OneAssetOption::engine, and <code>QuantLib::FDVanillaEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FDEuropeanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps=100, Size gridPoints=100, bool timeDependent=false) </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European options using finite-differences. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against analytic results.</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
