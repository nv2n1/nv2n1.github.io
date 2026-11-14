---
title: "stepback(3)"
name: "stepback"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stepback/"
description: "QuantLib::BlackScholesLattice – Simple binomial lattice approximating the Black-Scholes model."
---

<p>QuantLib::BlackScholesLattice &#8211; Simple binomial lattice approximating the Black-Scholes model. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/methods/lattices/bsmlattice.hpp&gt;</code></pre>
<p> Inherits <code>TreeLattice1D&lt; BlackScholesLattice&lt; T &gt; &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BlackScholesLattice</code> (const boost::shared_ptr&lt; T &gt; &amp;tree, Rate riskFreeRate, Time end, Size steps) </p>
<p> Size <code>size</code> (Size i) const </p>
<p> <code>DiscountFactor</code> <code>discount</code> (Size, Size) const </p>
<p> void <code>stepback</code> (Size i, const <code>Array</code> &amp;values, <code>Array</code> &amp;newValues) const </p>
<p> Real <code>underlying</code> (Size i, Size index) const </p>
<p> Size <code>descendant</code> (Size i, Size index, Size branch) const </p>
<p> Real <code>probability</code> (Size i, Size index, Size branch) const</p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::BlackScholesLattice&lt; T &gt;</h3>
<p>Simple binomial lattice approximating the Black-Scholes model.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
