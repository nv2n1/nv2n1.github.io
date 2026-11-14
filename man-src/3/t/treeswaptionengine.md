---
title: "treeswaptionengine(3)"
name: "treeswaptionengine"
section: "3"
letter: "t"
url: "/docs/linux/man/3-treeswaptionengine/"
description: "QuantLib::TreeSwaptionEngine – Numerical lattice engine for swaptions."
---

<p>QuantLib::TreeSwaptionEngine &#8211; Numerical lattice engine for swaptions. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/swaption/treeswaptionengine.hpp&gt; </p>
<p> Inherits <code>LatticeShortRateModelEngine&lt; Swaption::arguments, Swaption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>calculate</code> () const </p>
<p> <code>Constructors</code><br />
 <code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<p> <code>TreeSwaptionEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, Size timeSteps, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>TreeSwaptionEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, const <code>TimeGrid</code> &amp;timeGrid, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Numerical lattice engine for swaptions. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This engine is not guaranteed to work if the underlying swap has a start date in the past, i.e., before today&#8217;s date. When using this engine, prune the initial part of the swap so that it starts at $ t geq 0 $.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calculations are checked against cached results</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
