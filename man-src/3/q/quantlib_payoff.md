---
title: "quantlib_payoff(3)"
name: "quantlib_payoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_payoff/"
description: "QuantLib::Payoff – Abstract base class for option payoffs."
---

<p>QuantLib::Payoff &#8211; Abstract base class for option payoffs. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/payoff.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Real,Real&gt;. </p>
<p> Inherited by BasketPayoff, <code>DoubleStickyRatchetPayoff</code>, <code>ForwardTypePayoff</code>, <code>NullPayoff</code>, and <code>TypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Payoff interface</code> </p>
<p> virtual std::string <code>name</code> () const =0 </p>
<p> virtual std::string <code>description</code> () const =0 </p>
<p> virtual Real <code>operator()</code> (Real price) const =0 </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Abstract base class for option payoffs.</p>
<h2>Member Function Documentation</h2>
<h3>virtual std::string name () const [pure virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implemented in <code>ForwardTypePayoff</code>, <code>NullPayoff</code>, <code>FloatingTypePayoff</code>, <code>PlainVanillaPayoff</code>, <code>PercentageStrikePayoff</code>, <code>AssetOrNothingPayoff</code>, <code>CashOrNothingPayoff</code>, <code>GapPayoff</code>, <code>SuperFundPayoff</code>, <code>SuperSharePayoff</code>, <code>DoubleStickyRatchetPayoff</code>, <code>RatchetPayoff</code>, <code>StickyPayoff</code>, <code>RatchetMaxPayoff</code>, <code>RatchetMinPayoff</code>, <code>StickyMaxPayoff</code>, and <code>StickyMinPayoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
