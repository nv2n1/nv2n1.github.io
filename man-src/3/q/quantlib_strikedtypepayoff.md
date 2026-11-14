---
title: "quantlib_strikedtypepayoff(3)"
name: "quantlib_strikedtypepayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_strikedtypepayoff/"
description: "QuantLib::StrikedTypePayoff – Intermediate class for payoffs based on a fixed strike."
---

<p>QuantLib::StrikedTypePayoff &#8211; Intermediate class for payoffs based on a fixed strike. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::TypePayoff</code>. </p>
<p> Inherited by <code>AssetOrNothingPayoff</code>, <code>CashOrNothingPayoff</code>, <code>GapPayoff</code>, <code>PercentageStrikePayoff</code>, <code>PlainVanillaPayoff</code>, <code>SuperFundPayoff</code>, and <code>SuperSharePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StrikedTypePayoff</code> (Option::Type type, <code>Real</code> strike) </p>
<p> <code>Real</code> <code>strike</code> () const </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>description</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>strike_</code> </p>
<h2>Detailed Description</h2>
<p>Intermediate class for payoffs based on a fixed strike. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
