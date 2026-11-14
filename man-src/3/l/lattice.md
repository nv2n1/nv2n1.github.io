---
title: "lattice(3)"
name: "lattice"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lattice/"
description: "QuantLib::Lattice – Lattice (tree, finite-differences) base class"
---

<p>QuantLib::Lattice &#8211; Lattice (tree, finite-differences) base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/numericalmethod.hpp&gt; </p>
<p> Inherited by <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Lattice</code> (const <code>TimeGrid</code> &amp;timeGrid) </p>
<p> virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>grid</code> (Time) const =0 </p>
<p> <code>Inspectors</code> </p>
<p> const <code>TimeGrid</code> &amp; <code>timeGrid</code> () const </p>
<p> <code>Numerical method interface</code><br />
 These methods are to be used by discretized assets and must be overridden by developers implementing numerical methods. Users are advised to use the corresponding methods of <code>DiscretizedAsset</code> instead. </p>
<p> virtual void <code>initialize</code> (<code>DiscretizedAsset</code> &amp;, Time time) const =0<br />
 <i>initialize an asset at the given time. </i><br />
 virtual void <code>rollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const =0 </p>
<p> virtual void <code>partialRollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const =0 </p>
<p> virtual <code>Real</code> <code>presentValue</code> (<code>DiscretizedAsset</code> &amp;) const =0<br />
 <i>computes the present value of an asset. </i></p>
<h3>Protected Attributes</h3>
<p><code>TimeGrid</code> <code>t_</code> </p>
<h2>Detailed Description</h2>
<p>Lattice (tree, finite-differences) base class</p>
<h2>Member Function Documentation</h2>
<h3>virtual void rollback (<code>DiscretizedAsset</code> &amp;, Time to) const [pure virtual]</h3>
<p>Roll back an asset until the given time, performing any needed adjustment. </p>
<p> Implemented in <code>TreeLattice&lt; Impl &gt;</code>, <code>TsiveriotisFernandesLattice&lt; T &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>.</p>
<h3>virtual void partialRollback (<code>DiscretizedAsset</code> &amp;, Time to) const [pure virtual]</h3>
<p>Roll back an asset until the given time, but do not perform the final adjustment. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>In version 0.3.7 and earlier, this method was called rollAlmostBack method and performed pre-adjustment. This is no longer true; when migrating your code, you&#8217;ll have to replace calls such as:</dl>
<pre> method-&gt;rollAlmostBack(asset,t);</pre>
<p>&nbsp;<wbr>with the two statements:&nbsp;<wbr> </p>
<pre> method-&gt;partialRollback(asset,t);
 asset-&gt;preAdjustValues();</pre>
<p>&nbsp;<wbr> </p>
<p> Implemented in <code>TreeLattice&lt; Impl &gt;</code>, <code>TsiveriotisFernandesLattice&lt; T &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
