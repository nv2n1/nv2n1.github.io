---
title: "marketmodelpathwisediscounter(3)"
name: "marketmodelpathwisediscounter"
section: "3"
letter: "m"
url: "/docs/linux/man/3-marketmodelpathwisediscounter/"
description: "QuantLib::MarketModelPathwiseDiscounter –"
---

<p>QuantLib::MarketModelPathwiseDiscounter &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwisediscounter.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MarketModelPathwiseDiscounter</code> (<code>Time</code> paymentTime, const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes) </p>
<p> void <code>getFactors</code> (const <code>Matrix</code> &amp;LIBORRates, const <code>Matrix</code> &amp;Discounts, Size currentStep, std::vector&lt; <code>Real</code> &gt; &amp;factors) const </p>
<h2>Detailed Description</h2>
<p>this class returns the number of units of the discretely compounding money market account that 1 unit of cash at the payment can buy using the LIBOR rates from current step. </p>
<p> It also returns the derivative of this number with respect to each of the rates. </p>
<p> disconuting is purely based on the LIBOR rates in the simulation, to get a discounting back to zero you need to multiply by the discount factor of t_0. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
