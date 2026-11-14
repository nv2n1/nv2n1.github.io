---
title: "spot_(3)"
name: "spot_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spot_/"
description: "QuantLib::BlackScholesCalculator – Black-Scholes 1973 calculator class."
---

<p>QuantLib::BlackScholesCalculator &#8211; Black-Scholes 1973 calculator class. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/pricingengines/blackscholescalculator.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::BlackCalculator</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BlackScholesCalculator</code> (const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, Real spot, <code>DiscountFactor</code> growth, Real stdDev, <code>DiscountFactor</code> discount) </p>
<p> Real <code>delta</code> () const </p>
<p> Real <code>elasticity</code> () const </p>
<p> Real <code>gamma</code> () const </p>
<p> Real <code>theta</code> (<code>Time</code> maturity) const </p>
<p> Real <code>thetaPerDay</code> (<code>Time</code> maturity) const</p>
<h3>Protected Attributes</h3>
<p>Real <code>spot_</code> </p>
<p> <code>DiscountFactor</code> <code>growth_</code></p>
<h2>Detailed Description</h2>
<p>Black-Scholes 1973 calculator class.</p>
<h2>Member Function Documentation</h2>
<h3>Real delta () const</h3>
<p>Sensitivity to change in the underlying spot price.</p>
<h3>Real elasticity () const</h3>
<p>Sensitivity in percent to a percent change in the underlying spot price.</p>
<h3>Real gamma () const</h3>
<p>Second order derivative with respect to change in the underlying spot price.</p>
<h3>Real theta (<code>Time</code> maturity) const</h3>
<p>Sensitivity to time to maturity.</p>
<h3>Real thetaPerDay (<code>Time</code> maturity) const</h3>
<p>Sensitivity to time to maturity per day (assuming 365 day in a year).</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
