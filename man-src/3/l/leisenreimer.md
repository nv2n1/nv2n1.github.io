---
title: "leisenreimer(3)"
name: "leisenreimer"
section: "3"
letter: "l"
url: "/docs/linux/man/3-leisenreimer/"
description: "QuantLib::LeisenReimer – Leisen & Reimer tree: multiplicative approach."
---

<p>QuantLib::LeisenReimer &#8211; Leisen &amp; Reimer tree: multiplicative approach. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/binomialtree.hpp&gt; </p>
<p> Inherits <code>BinomialTree&lt; LeisenReimer &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LeisenReimer</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;, <code>Time</code> end, Size steps, <code>Real</code> strike) </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> <code>Real</code> <code>probability</code> (Size, Size, Size branch) const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>up_</code> </p>
<p> <code>Real</code> <code>down_</code> </p>
<p> <code>Real</code> <code>pu_</code> </p>
<p> <code>Real</code> <code>pd_</code> </p>
<h2>Detailed Description</h2>
<p>Leisen &amp; Reimer tree: multiplicative approach. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
