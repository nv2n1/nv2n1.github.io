---
title: "quantlib_juquadraticapproximationengine(3)"
name: "quantlib_juquadraticapproximationengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_juquadraticapproximationengine/"
description: "QuantLib::JuQuadraticApproximationEngine – Pricing engine for American options with Ju quadratic approximation."
---

<p>QuantLib::JuQuadraticApproximationEngine &#8211; Pricing engine for American options with Ju quadratic approximation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/juquadraticengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>JuQuadraticApproximationEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for American options with Ju quadratic approximation. </p>
<p> Reference: An Approximate Formula for Pricing American Options, Journal of Derivatives Winter 1999, Ju, N. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Barone-Adesi-Whaley critical commodity price calculation is used, it has not been modified to see whether the method of Ju is faster. Ju does not say how he solves the equation for the critical stock price, e.g. <code>Newton</code> method. He just gives the solution. The method of BAW gives answers to the same accuracy as in Ju (1999).</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
