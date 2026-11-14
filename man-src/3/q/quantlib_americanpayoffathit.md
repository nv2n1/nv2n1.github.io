---
title: "quantlib_americanpayoffathit(3)"
name: "quantlib_americanpayoffathit"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_americanpayoffathit/"
description: "QuantLib::AmericanPayoffAtHit – Analytic formula for American exercise payoff at-hit options."
---

<p>QuantLib::AmericanPayoffAtHit &#8211; Analytic formula for American exercise payoff at-hit options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/americanpayoffathit.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>AmericanPayoffAtHit</code> (<code>Real</code> spot, <code>DiscountFactor</code> discount, <code>DiscountFactor</code> dividendDiscount, <code>Real</code> variance, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff) </p>
<p> <code>Real</code> <code>value</code> () const </p>
<p> <code>Real</code> <code>delta</code> () const </p>
<p> <code>Real</code> <code>gamma</code> () const </p>
<p> <code>Real</code> <code>rho</code> (<code>Time</code> maturity) const </p>
<h2>Detailed Description</h2>
<p>Analytic formula for American exercise payoff at-hit options. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>calculate greeks</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
