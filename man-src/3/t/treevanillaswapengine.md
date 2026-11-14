---
title: "treevanillaswapengine(3)"
name: "treevanillaswapengine"
section: "3"
letter: "t"
url: "/docs/linux/man/3-treevanillaswapengine/"
description: "QuantLib::TreeVanillaSwapEngine – Numerical lattice engine for simple swaps."
---

<p>QuantLib::TreeVanillaSwapEngine &#8211; Numerical lattice engine for simple swaps. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/swap/treeswapengine.hpp&gt; </p>
<p> Inherits <code>LatticeShortRateModelEngine&lt; VanillaSwap::arguments, VanillaSwap::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>calculate</code> () const </p>
<p> <code>Constructors</code><br />
 <code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<p> <code>TreeVanillaSwapEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, Size timeSteps, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>TreeVanillaSwapEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, const <code>TimeGrid</code> &amp;timeGrid, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Numerical lattice engine for simple swaps. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are checked against known good results</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
