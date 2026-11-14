---
title: "payoffs(3)"
name: "payoffs"
section: "3"
letter: "p"
url: "/docs/linux/man/3-payoffs/"
description: "ql/instruments/payoffs.hpp – Payoffs for various options."
---

<p>ql/instruments/payoffs.hpp &#8211; Payoffs for various options. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/option.hpp&gt;

#include &lt;ql/payoff.hpp&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>NullPayoff</code><br />
 <i>Dummy payoff class. </i><br />
 class <code>TypePayoff</code><br />
 <i>Intermediate class for put/call payoffs. </i><br />
 class <code>FloatingTypePayoff</code><br />
 <i>Payoff based on a floating strike </i><br />
 class <code>StrikedTypePayoff</code><br />
 <i>Intermediate class for payoffs based on a fixed strike. </i><br />
 class <code>PlainVanillaPayoff</code><br />
 <i>Plain-vanilla payoff. </i><br />
 class <code>PercentageStrikePayoff</code><br />
 <i>Payoff with strike expressed as percentage </i><br />
 class <code>AssetOrNothingPayoff</code><br />
 <i>Binary asset-or-nothing payoff. </i><br />
 class <code>CashOrNothingPayoff</code><br />
 <i>Binary cash-or-nothing payoff. </i><br />
 class <code>GapPayoff</code><br />
 <i>Binary gap payoff. </i><br />
 class <code>SuperFundPayoff</code><br />
 <i>Binary supershare and superfund payoffs. </i><br />
 class <code>SuperSharePayoff</code><br />
 <i>Binary supershare payoff. </i></p>
<h2>Detailed Description</h2>
<p>Payoffs for various options.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
