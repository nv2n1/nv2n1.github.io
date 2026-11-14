---
title: "plainvanillapayoff(3)"
name: "plainvanillapayoff"
section: "3"
letter: "p"
url: "/docs/linux/man/3-plainvanillapayoff/"
description: "QuantLib::PlainVanillaPayoff – Plain-vanilla payoff."
---

<p>QuantLib::PlainVanillaPayoff &#8211; Plain-vanilla payoff. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::StrikedTypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>PlainVanillaPayoff</code> (Option::Type type, Real strike) </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Plain-vanilla payoff. </p>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, and <code>Replication.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
