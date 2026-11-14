---
title: "tree1_(3)"
name: "tree1_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tree1_/"
description: "QuantLib::TreeLattice2D – Two-dimensional tree-based lattice."
---

<p>QuantLib::TreeLattice2D &#8211; Two-dimensional tree-based lattice. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/methods/lattices/lattice2d.hpp&gt;</code></pre>
<p> Inherits <code>TreeLattice&lt; Impl &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TreeLattice2D</code> (const boost::shared_ptr&lt; T &gt; &amp;tree1, const boost::shared_ptr&lt; T &gt; &amp;tree2, Real correlation) </p>
<p> Size <code>size</code> (Size i) const </p>
<p> Size <code>descendant</code> (Size i, Size index, Size branch) const </p>
<p> Real <code>probability</code> (Size i, Size index, Size branch) const</p>
<h3>Protected Member Functions</h3>
<p><code>Disposable</code>&lt; <code>Array</code> &gt; <code>grid</code> (Time) const</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; T &gt; <code>tree1_</code> </p>
<p> boost::shared_ptr&lt; T &gt; <code>tree2_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Impl, class T = TrinomialTree&gt; class QuantLib::TreeLattice2D&lt; Impl, T &gt;</h3>
<p>Two-dimensional tree-based lattice. </p>
<p> This lattice is based on two trinomial trees and primarily used for the <code>G2</code> short-rate model.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
