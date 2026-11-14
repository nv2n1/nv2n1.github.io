---
title: "quantlib_supersharepayoff(3)"
name: "quantlib_supersharepayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_supersharepayoff/"
description: "QuantLib::SuperSharePayoff – Binary supershare payoff."
---

<p>QuantLib::SuperSharePayoff &#8211; Binary supershare payoff. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::StrikedTypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SuperSharePayoff</code> (Real strike, Real secondStrike, Real cashPayoff) </p>
<p> Real <code>strike</code> () const </p>
<p> Real <code>secondStrike</code> () const </p>
<p> Real <code>cashPayoff</code> () const </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> std::string <code>description</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p>Real <code>strike_</code> </p>
<p> Real <code>secondStrike_</code> </p>
<p> Real <code>cashPayoff_</code> </p>
<h2>Detailed Description</h2>
<p>Binary supershare payoff.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
