---
title: "quantlib_treelattice1d(3)"
name: "quantlib_treelattice1d"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_treelattice1d/"
description: "QuantLib::TreeLattice1D – One-dimensional tree-based lattice."
---

<p>QuantLib::TreeLattice1D &#8211; One-dimensional tree-based lattice. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/lattice1d.hpp&gt; </p>
<p> Inherits <code>TreeLattice&lt; Impl &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>TreeLattice1D</code> (const <code>TimeGrid</code> &amp;timeGrid, Size n) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>grid</code> (Time t) const </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Impl&gt; class QuantLib::TreeLattice1D&lt; Impl &gt;</h3>
<p>One-dimensional tree-based lattice. </p>
<p> Derived classes must implement the following interface: </p>
<pre> Real underlying(Size i, Size index) const;</pre>
<p>&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
