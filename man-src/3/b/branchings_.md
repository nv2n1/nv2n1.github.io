---
title: "branchings_(3)"
name: "branchings_"
section: "3"
letter: "b"
url: "/docs/linux/man/3-branchings_/"
description: "QuantLib::TrinomialTree – Recombining trinomial tree class."
---

<h2 class="name">NAME</h2>
<p> QuantLib::TrinomialTree &#8211; Recombining trinomial tree class. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/lattices/trinomialtree.hpp&gt; </p>
<p> Inherits <code>Tree&lt; TrinomialTree &gt;</code>. </p>
<h3>Public Types</h3>
<p> enum <code>Branches</code> { <code>branches</code> = 3 } </p>
<h3>Public Member Functions</h3>
<p> <code>TrinomialTree</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process, const <code>TimeGrid</code> &amp;timeGrid, bool isPositive=false) </p>
<p> <code>Real</code> <code>dx</code> (Size i) const </p>
<p> const <code>TimeGrid</code> &amp; <code>timeGrid</code> () const </p>
<p> Size <code>size</code> (Size i) const </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> Size <code>descendant</code> (Size i, Size index, Size branch) const </p>
<p> <code>Real</code> <code>probability</code> (Size i, Size index, Size branch) const </p>
<h3>Protected Attributes</h3>
<p> std::vector&lt; Branching &gt; <code>branchings_</code> </p>
<p> <code>Real</code> <code>x0_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>dx_</code> </p>
<p> <code>TimeGrid</code> <code>timeGrid_</code> </p>
<h2>Detailed Description</h2>
<p> Recombining trinomial tree class. </p>
<p> This class defines a recombining trinomial tree approximating a 1-D stochastic process. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> The diffusion term of the SDE must be independent of the underlying process.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
