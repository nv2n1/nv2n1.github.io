---
title: "integralengine(3)"
name: "integralengine"
section: "3"
letter: "i"
url: "/docs/linux/man/3-integralengine/"
description: "QuantLib::IntegralEngine – Pricing engine for European vanilla options using integral approach."
---

<p>QuantLib::IntegralEngine &#8211; Pricing engine for European vanilla options using integral approach. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/integralengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>IntegralEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European vanilla options using integral approach. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>define tolerance for calculate()</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
