---
title: "criticalprice(3)"
name: "criticalprice"
section: "3"
letter: "c"
url: "/docs/linux/man/3-criticalprice/"
description: "QuantLib::BaroneAdesiWhaleyApproximationEngine – Barone-Adesi and Whaley pricing engine for American options (1987)."
---

<p>QuantLib::BaroneAdesiWhaleyApproximationEngine &#8211; Barone-Adesi and Whaley pricing engine for American options (1987). </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/baroneadesiwhaleyengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>BaroneAdesiWhaleyApproximationEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Real</code> <code>criticalPrice</code> (const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, <code>DiscountFactor</code> riskFreeDiscount, <code>DiscountFactor</code> dividendDiscount, <code>Real</code> variance, <code>Real</code> tolerance=1e-6) </p>
<h2>Detailed Description</h2>
<p>Barone-Adesi and Whaley pricing engine for American options (1987). </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
