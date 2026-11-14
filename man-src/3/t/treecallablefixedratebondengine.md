---
title: "treecallablefixedratebondengine(3)"
name: "treecallablefixedratebondengine"
section: "3"
letter: "t"
url: "/docs/linux/man/3-treecallablefixedratebondengine/"
description: "QuantLib::TreeCallableFixedRateBondEngine – Numerical lattice engine for callable fixed rate bonds."
---

<p>QuantLib::TreeCallableFixedRateBondEngine &#8211; Numerical lattice engine for callable fixed rate bonds. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/treecallablebondengine.hpp&gt; </p>
<p> Inherits <code>LatticeShortRateModelEngine&lt; CallableBond::arguments, CallableBond::results &gt;</code>. </p>
<p> Inherited by <code>TreeCallableZeroCouponBondEngine</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>calculate</code> () const </p>
<p> <code>Constructors</code><br />
 <code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<p> <code>TreeCallableFixedRateBondEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, const Size timeSteps, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>TreeCallableFixedRateBondEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;, const <code>TimeGrid</code> &amp;timeGrid, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Numerical lattice engine for callable fixed rate bonds. </p>
<p> <code>Examples: </code> </p>
<p> <code>CallableBonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
