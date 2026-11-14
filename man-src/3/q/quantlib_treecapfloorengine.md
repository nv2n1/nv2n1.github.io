---
title: "quantlib_treecapfloorengine(3)"
name: "quantlib_treecapfloorengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_treecapfloorengine/"
description: "QuantLib::TreeCapFloorEngine – Numerical lattice engine for cap/floors."
---

<p>QuantLib::TreeCapFloorEngine &#8211; Numerical lattice engine for cap/floors. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/capfloor/treecapfloorengine.hpp&gt; </p>
<p> Inherits <code>LatticeShortRateModelEngine&lt; CapFloor::arguments, CapFloor::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>calculate</code> () const </p>
<p> <code>Constructors</code><br />
 <code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<p> <code>TreeCapFloorEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, Size timeSteps, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>TreeCapFloorEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, const <code>TimeGrid</code> &amp;timeGrid, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Numerical lattice engine for cap/floors. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
