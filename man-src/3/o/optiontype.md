---
title: "optiontype(3)"
name: "optiontype"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optiontype/"
description: "QuantLib::TypePayoff – Intermediate class for put/call payoffs."
---

<p>QuantLib::TypePayoff &#8211; Intermediate class for put/call payoffs. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/instruments/payoffs.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::Payoff</code>. Inherited by <code>FloatingTypePayoff</code>, and <code>StrikedTypePayoff</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TypePayoff</code> (Option::Type type) </p>
<p> Option::Type <code>optionType</code> () const<br />
 <code>Payoff interface</code> </p>
<p> std::string <code>description</code> () const</p>
<h3>Protected Attributes</h3>
<p>Option::Type <code>type_</code></p>
<h2>Detailed Description</h2>
<p>Intermediate class for put/call payoffs.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
