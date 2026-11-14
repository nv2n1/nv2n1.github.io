---
title: "quantlib_extendedtrigeorgis(3)"
name: "quantlib_extendedtrigeorgis"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedtrigeorgis/"
description: "QuantLib::ExtendedTrigeorgis – Trigeorgis (additive equal jumps) binomial tree"
---

<p>QuantLib::ExtendedTrigeorgis &#8211; Trigeorgis (additive equal jumps) binomial tree </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>ExtendedEqualJumpsBinomialTree&lt; ExtendedTrigeorgis &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedTrigeorgis</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;, Time end, Size steps, Real strike) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>dxStep</code> (Time stepTime) const </p>
<p> Real <code>probUp</code> (Time stepTime) const </p>
<h2>Detailed Description</h2>
<p>Trigeorgis (additive equal jumps) binomial tree </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
