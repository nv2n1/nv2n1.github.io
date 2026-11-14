---
title: "quantlib_ratchetminpayoff(3)"
name: "quantlib_ratchetminpayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_ratchetminpayoff/"
description: "QuantLib::RatchetMinPayoff – RatchetMin payoff (double option)."
---

<p>QuantLib::RatchetMinPayoff &#8211; RatchetMin payoff (double option). </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/stickyratchet.hpp&gt; </p>
<p> Inherits <code>QuantLib::DoubleStickyRatchetPayoff</code>. </p>
<h3>Public Member Functions</h3>
<p><code>RatchetMinPayoff</code> (<code>Real</code> gearing1, <code>Real</code> gearing2, <code>Real</code> gearing3, <code>Real</code> spread1, <code>Real</code> spread2, <code>Real</code> spread3, <code>Real</code> initialValue1, <code>Real</code> initialValue2, <code>Real</code> accrualFactor) </p>
<p> <code>Payoff interface</code> </p>
<p> std::string <code>name</code> () const </p>
<h2>Detailed Description</h2>
<p>RatchetMin payoff (double option).</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Reimplemented from <code>DoubleStickyRatchetPayoff</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
