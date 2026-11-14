---
title: "americanpayoffatexpiry(3)"
name: "americanpayoffatexpiry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-americanpayoffatexpiry/"
description: "QuantLib::AmericanPayoffAtExpiry – Analytic formula for American exercise payoff at-expiry options."
---

<p>QuantLib::AmericanPayoffAtExpiry &#8211; Analytic formula for American exercise payoff at-expiry options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/americanpayoffatexpiry.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>AmericanPayoffAtExpiry</code> (Real spot, <code>DiscountFactor</code> discount, <code>DiscountFactor</code> dividendDiscount, Real variance, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff) </p>
<p> Real <code>value</code> () const </p>
<h2>Detailed Description</h2>
<p>Analytic formula for American exercise payoff at-expiry options. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>calculate greeks</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
