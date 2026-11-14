---
title: "extendedcoxrossrubinstein(3)"
name: "extendedcoxrossrubinstein"
section: "3"
letter: "e"
url: "/docs/linux/man/3-extendedcoxrossrubinstein/"
description: "QuantLib::ExtendedCoxRossRubinstein – Cox-Ross-Rubinstein (multiplicative) equal jumps binomial tree."
---

<p>QuantLib::ExtendedCoxRossRubinstein &#8211; Cox-Ross-Rubinstein (multiplicative) equal jumps binomial tree. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>ExtendedEqualJumpsBinomialTree&lt; ExtendedCoxRossRubinstein &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedCoxRossRubinstein</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;, Time end, Size steps, Real strike) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>dxStep</code> (Time stepTime) const </p>
<p> Real <code>probUp</code> (Time stepTime) const </p>
<h2>Detailed Description</h2>
<p>Cox-Ross-Rubinstein (multiplicative) equal jumps binomial tree. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
