---
title: "gearing1_(3)"
name: "gearing1_"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gearing1_/"
description: "QuantLib::DoubleStickyRatchetPayoff – Intermediate class for single/double sticky/ratchet payoffs."
---

<h2 class="name">NAME</h2>
<p> QuantLib::DoubleStickyRatchetPayoff &#8211; Intermediate class for single/double sticky/ratchet payoffs. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/stickyratchet.hpp&gt; </p>
<p> Inherits <code>QuantLib::Payoff</code>. </p>
<p> Inherited by <code>RatchetMaxPayoff</code>, <code>RatchetMinPayoff</code>, <code>RatchetPayoff</code>, <code>StickyMaxPayoff</code>, <code>StickyMinPayoff</code>, and <code>StickyPayoff</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>DoubleStickyRatchetPayoff</code> (Real type1, Real type2, Real gearing1, Real gearing2, Real gearing3, Real spread1, Real spread2, Real spread3, Real initialValue1, Real initialValue2, Real accrualFactor) </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> Real <code>operator()</code> (Real forward) const </p>
<p> std::string <code>description</code> () const </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p> Real <code>type1_</code> </p>
<p> Real <code>type2_</code> </p>
<p> Real <code>gearing1_</code> </p>
<p> Real <code>gearing2_</code> </p>
<p> Real <code>gearing3_</code> </p>
<p> Real <code>spread1_</code> </p>
<p> Real <code>spread2_</code> </p>
<p> Real <code>spread3_</code> </p>
<p> Real <code>initialValue1_</code> </p>
<p> Real <code>initialValue2_</code> </p>
<p> Real <code>accrualFactor_</code> </p>
<h2>Detailed Description</h2>
<p> Intermediate class for single/double sticky/ratchet payoffs.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<p> Reimplemented in <code>RatchetPayoff</code>, <code>StickyPayoff</code>, <code>RatchetMaxPayoff</code>, <code>RatchetMinPayoff</code>, <code>StickyMaxPayoff</code>, and <code>StickyMinPayoff</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
