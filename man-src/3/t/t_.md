---
title: "t_(3)"
name: "t_"
section: "3"
letter: "t"
url: "/docs/linux/man/3-t_/"
description: "QuantLib::Lattice – Lattice (tree, finite-differences) base class"
---

<p>QuantLib::Lattice &#8211; Lattice (tree, finite-differences) base class </p>
<h2>Synopsis</h2>
<pre><code>virtual void initialize (DiscretizedAsset &amp;, Time time) const =0


initialize an asset at the given time.


virtual void rollback (DiscretizedAsset &amp;, Time to) const =0



virtual void partialRollback (DiscretizedAsset &amp;, Time to) const =0



virtual Real presentValue (DiscretizedAsset &amp;) const =0


computes the present value of an asset.




Protected Attributes</code></pre>
<p> Inherited by <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual void initialize (DiscretizedAsset &amp;, Time time) const =0</p>
<p>initialize an asset at the given time.</p>
<p>virtual void rollback (DiscretizedAsset &amp;, Time to) const =0</p>
<p>virtual void partialRollback (DiscretizedAsset &amp;, Time to) const =0</p>
<p>virtual Real presentValue (DiscretizedAsset &amp;) const =0</p>
<p>computes the present value of an asset.</p>
<p>Protected Attributes <code>Inspectors</code><br />
 virtual void initialize (DiscretizedAsset &amp;, Time time) const =0</p>
<p>initialize an asset at the given time.</p>
<p>virtual void rollback (DiscretizedAsset &amp;, Time to) const =0</p>
<p>virtual void partialRollback (DiscretizedAsset &amp;, Time to) const =0</p>
<p>virtual Real presentValue (DiscretizedAsset &amp;) const =0</p>
<p>computes the present value of an asset.</p>
<p>Protected Attributes <code>Numerical method interface</code><br />
 These methods are to be used by discretized assets and must be overridden by developers implementing numerical methods. Users are advised to use the corresponding methods of <code>DiscretizedAsset</code> instead. </p>
<pre><code>virtual void initialize (DiscretizedAsset &amp;, Time time) const =0


initialize an asset at the given time.


virtual void rollback (DiscretizedAsset &amp;, Time to) const =0



virtual void partialRollback (DiscretizedAsset &amp;, Time to) const =0



virtual Real presentValue (DiscretizedAsset &amp;) const =0


computes the present value of an asset.




Protected Attributes</code></pre>
<p> <code>TimeGrid</code> <code>t_</code></p>
<h2>Detailed Description</h2>
<p>Lattice (tree, finite-differences) base class</p>
<h2>Member Function Documentation</h2>
<h3>virtual void rollback (<code>DiscretizedAsset</code> &amp;, Time to) const [pure virtual]</h3>
<p>Roll back an asset until the given time, performing any needed adjustment. </p>
<p> Implemented in <code>TreeLattice&lt; Impl &gt;</code>, <code>TsiveriotisFernandesLattice&lt; T &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>.</p>
<h3>virtual void partialRollback (<code>DiscretizedAsset</code> &amp;, Time to) const [pure virtual]</h3>
<p>Roll back an asset until the given time, but do not perform the final adjustment. </p>
<p> <code>Warning</code></p>
<dl>
<dd>In version 0.3.7 and earlier, this method was called rollAlmostBack method and performed pre-adjustment. This is no longer true; when migrating your code, you&#8217;ll have to replace calls such as:</dl>
<pre> method-&gt;rollAlmostBack(asset,t);</pre>
<p>&nbsp;<wbr>with the two statements:&nbsp;<wbr> </p>
<pre> method-&gt;partialRollback(asset,t);
 asset-&gt;preAdjustValues();</pre>
<p>&nbsp;<wbr> </p>
<p> Implemented in <code>TreeLattice&lt; Impl &gt;</code>, <code>TsiveriotisFernandesLattice&lt; T &gt;</code>, <code>TreeLattice&lt; Impl &gt;</code>, <code>TreeLattice&lt; OneFactorModel::ShortRateTree &gt;</code>, <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>, and <code>TreeLattice&lt; TwoFactorModel::ShortRateTree &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
