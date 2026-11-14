---
title: "quantlib_treelattice(3)"
name: "quantlib_treelattice"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_treelattice/"
description: "QuantLib::TreeLattice – Tree-based lattice-method base class."
---

<p>QuantLib::TreeLattice &#8211; Tree-based lattice-method base class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/lattice.hpp&gt; </p>
<p> Inherits <code>QuantLib::Lattice</code>, and <code>CuriouslyRecurringTemplate&lt; Impl &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>TreeLattice</code> (const <code>TimeGrid</code> &amp;timeGrid, Size n) </p>
<p> const <code>Array</code> &amp; <code>statePrices</code> (Size i) const </p>
<p> void <code>stepback</code> (Size i, const <code>Array</code> &amp;values, <code>Array</code> &amp;newValues) const </p>
<p> <code>Lattice interface</code> </p>
<p> void <code>initialize</code> (<code>DiscretizedAsset</code> &amp;, Time t) const<br />
 <i>initialize an asset at the given time. </i><br />
 void <code>rollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const </p>
<p> void <code>partialRollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const </p>
<p> <code>Real</code> <code>presentValue</code> (<code>DiscretizedAsset</code> &amp;) const<br />
 <i>Computes the present value of an asset using Arrow-Debrew prices. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>computeStatePrices</code> (Size until) const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Array</code> &gt; <code>statePrices_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Impl&gt; class QuantLib::TreeLattice&lt; Impl &gt;</h3>
<p>Tree-based lattice-method base class. </p>
<p> This class defines a lattice method that is able to rollback (with discount) a discretized asset object. It will be based on one or more trees. </p>
<p> Derived classes must implement the following interface: </p>
<pre> public:
 DiscountFactor discount(Size i, Size index) const;
 Size descendant(Size i, Size index, Size branch) const;
 Real probability(Size i, Size index, Size branch) const;</pre>
<p>&nbsp;<wbr>and may implement the following:&nbsp;<wbr> </p>
<pre> public:
 void stepback(Size i,
 const Array&amp; values,
 Array&amp; newValues) const;</pre>
<p>&nbsp;<wbr></p>
<h2>Member Function Documentation</h2>
<h3>void rollback (<code>DiscretizedAsset</code> &amp;, Time to) const [virtual]</h3>
<p>Roll back an asset until the given time, performing any needed adjustment. </p>
<p> Implements <code>Lattice</code>. </p>
<p> Reimplemented in <code>TsiveriotisFernandesLattice&lt; T &gt;</code>.</p>
<h3>void partialRollback (<code>DiscretizedAsset</code> &amp;, Time to) const [virtual]</h3>
<p>Roll back an asset until the given time, but do not perform the final adjustment. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>In version 0.3.7 and earlier, this method was called rollAlmostBack method and performed pre-adjustment. This is no longer true; when migrating your code, you&#8217;ll have to replace calls such as:</dl>
<pre> method-&gt;rollAlmostBack(asset,t);</pre>
<p>&nbsp;<wbr>with the two statements:&nbsp;<wbr> </p>
<pre> method-&gt;partialRollback(asset,t);
 asset-&gt;preAdjustValues();</pre>
<p>&nbsp;<wbr> </p>
<p> Implements <code>Lattice</code>. </p>
<p> Reimplemented in <code>TsiveriotisFernandesLattice&lt; T &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
