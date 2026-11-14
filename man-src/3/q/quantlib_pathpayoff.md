---
title: "quantlib_pathpayoff(3)"
name: "quantlib_pathpayoff"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathpayoff/"
description: "QuantLib::PathPayoff – Abstract base class for path-dependent option payoffs."
---

<p>QuantLib::PathPayoff &#8211; Abstract base class for path-dependent option payoffs. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/mcbasket/pathpayoff.hpp&gt; </p>
<p> Inherits std::unary_function&lt;Matrix,Array&gt;. </p>
<h3>Public Member Functions</h3>
<p><code>Payoff interface</code> </p>
<p> virtual std::string <code>name</code> () const =0 </p>
<p> virtual std::string <code>description</code> () const =0 </p>
<p> virtual <code>Real</code> <code>operator()</code> (const <code>Matrix</code> &amp;values) const =0 </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Abstract base class for path-dependent option payoffs.</p>
<h2>Member Function Documentation</h2>
<h3>virtual std::string name () const [pure virtual]</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between payoffs. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
