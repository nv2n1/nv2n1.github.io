---
title: "quantlib_stulzengine(3)"
name: "quantlib_stulzengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_stulzengine/"
description: "QuantLib::StulzEngine – Pricing engine for 2D European Baskets."
---

<p>QuantLib::StulzEngine &#8211; Pricing engine for 2D European Baskets. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/basket/stulzengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::BasketOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StulzEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process1, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process2, <code>Real</code> correlation) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for 2D European Baskets. </p>
<p> This class implements formulae from &#8216;Options on the Minimum or the Maximum of Two Risky Assets&#8217;, Rene Stulz, Journal of Financial Ecomomics (1982) 10, 161-185. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
