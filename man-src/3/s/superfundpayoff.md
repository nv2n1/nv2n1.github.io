---
title: "superfundpayoff(3)"
name: "superfundpayoff"
section: "3"
letter: "s"
url: "/docs/linux/man/3-superfundpayoff/"
description: "QuantLib::SuperFundPayoff – Binary supershare and superfund payoffs."
---

<p>QuantLib::SuperFundPayoff &#8211; Binary supershare and superfund payoffs. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::StrikedTypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SuperFundPayoff</code> (Real strike, Real secondStrike) </p>
<p> Real <code>secondStrike</code> () const </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p>Real <code>secondStrike_</code> </p>
<h2>Detailed Description</h2>
<p>Binary supershare and superfund payoffs. </p>
<p> Binary superfund payoff </p>
<p> Superfund sometimes also called &#8216;supershare&#8217;, which can lead to ambiguity; within QuantLib the terms supershare and superfund are used consistently according to the definitions in Bloomberg OVX function&#8217;s help pages. </p>
<p> This payoff is equivalent to being (1/lowerstrike) a) long (short) an AssetOrNothing Call (Put) at the lower strike and b) short (long) an AssetOrNothing Call (Put) at the higher strike</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
