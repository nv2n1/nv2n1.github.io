---
title: "tsiveriotisfernandeslattice(3)"
name: "tsiveriotisfernandeslattice"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tsiveriotisfernandeslattice/"
description: "QuantLib::TsiveriotisFernandesLattice – Binomial lattice approximating the Tsiveriotis-Fernandes model."
---

<p>QuantLib::TsiveriotisFernandesLattice &#8211; Binomial lattice approximating the Tsiveriotis-Fernandes model. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/tflattice.hpp&gt; </p>
<p> Inherits <code>BlackScholesLattice&lt; T &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>TsiveriotisFernandesLattice</code> (const boost::shared_ptr&lt; T &gt; &amp;tree, Rate riskFreeRate, Time end, Size steps, Real creditSpread, Volatility volatility, Spread divYield) </p>
<p> Rate <code>riskFreeRate</code> () const </p>
<p> Real <code>creditSpread</code> () const </p>
<p> Real <code>dt</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>stepback</code> (Size i, const <code>Array</code> &amp;values, const <code>Array</code> &amp;conversionProbability, const <code>Array</code> &amp;spreadAdjustedRate, <code>Array</code> &amp;newValues, <code>Array</code> &amp;newConversionProbability, <code>Array</code> &amp;newSpreadAdjustedRate) const </p>
<p> void <code>rollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const </p>
<p> void <code>partialRollback</code> (<code>DiscretizedAsset</code> &amp;, Time to) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::TsiveriotisFernandesLattice&lt; T &gt;</h3>
<p>Binomial lattice approximating the Tsiveriotis-Fernandes model. </p>
<h2>Member Function Documentation</h2>
<h3>void rollback (<code>DiscretizedAsset</code> &amp;, Time to) const [protected, virtual]</h3>
<p>Roll back an asset until the given time, performing any needed adjustment. </p>
<p> Reimplemented from <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>.</p>
<h3>void partialRollback (<code>DiscretizedAsset</code> &amp;, Time to) const [protected, virtual]</h3>
<p>Roll back an asset until the given time, but do not perform the final adjustment. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>In version 0.3.7 and earlier, this method was called rollAlmostBack method and performed pre-adjustment. This is no longer true; when migrating your code, you&#8217;ll have to replace calls such as:</dl>
<pre> method-&gt;rollAlmostBack(asset,t);</pre>
<p>&nbsp;<wbr>with the two statements:&nbsp;<wbr> </p>
<pre> method-&gt;partialRollback(asset,t);
 asset-&gt;preAdjustValues();</pre>
<p>&nbsp;<wbr> </p>
<p> Reimplemented from <code>TreeLattice&lt; BlackScholesLattice&lt; T &gt; &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
