---
title: "quantlib_forwardtypepayoff(3)"
name: "quantlib_forwardtypepayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_forwardtypepayoff/"
description: "QuantLib::ForwardTypePayoff – Class for forward type payoffs."
---

<p>QuantLib::ForwardTypePayoff &#8211; Class for forward type payoffs. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/forward.hpp&gt; </p>
<p> Inherits <code>QuantLib::Payoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ForwardTypePayoff</code> (Position::Type type, Real strike) </p>
<p> Position::Type <code>forwardType</code> () const </p>
<p> Real <code>strike</code> () const </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<p> std::string <code>description</code> () const </p>
<p> Real <code>operator()</code> (Real price) const </p>
<h3>Protected Attributes</h3>
<p>Position::Type <code>type_</code> </p>
<p> Real <code>strike_</code> </p>
<h2>Detailed Description</h2>
<p>Class for forward type payoffs.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Payoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
