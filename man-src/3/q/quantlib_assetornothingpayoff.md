---
title: "quantlib_assetornothingpayoff(3)"
name: "quantlib_assetornothingpayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_assetornothingpayoff/"
description: "QuantLib::AssetOrNothingPayoff – Binary asset-or-nothing payoff."
---

<p>QuantLib::AssetOrNothingPayoff &#8211; Binary asset-or-nothing payoff. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::StrikedTypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AssetOrNothingPayoff</code> (Option::Type type, Real strike) </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Binary asset-or-nothing payoff. </p>
<p> Definitions of Binary path-independent payoffs used below, can be found in M. Rubinstein, E. Reiner:&#8217;Unscrambling The Binary Code&#8217;, Risk, Vol.4 no.9,1991. (see: <a rel="nofollow" href="http://www.in-the-money.com/artandpap/Binary%20Options.doc)">http://www.in-the-money.com/artandpap/Binary%20Options.doc)</a></p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
