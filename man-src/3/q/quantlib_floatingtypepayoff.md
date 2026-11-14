---
title: "quantlib_floatingtypepayoff(3)"
name: "quantlib_floatingtypepayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_floatingtypepayoff/"
description: "QuantLib::FloatingTypePayoff – Payoff based on a floating strike"
---

<p>QuantLib::FloatingTypePayoff &#8211; Payoff based on a floating strike </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/payoffs.hpp&gt; </p>
<p> Inherits <code>QuantLib::TypePayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FloatingTypePayoff</code> (Option::Type type) </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Payoff based on a floating strike</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
