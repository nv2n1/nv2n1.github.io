---
title: "quantlib_treecallablezerocouponbondengine(3)"
name: "quantlib_treecallablezerocouponbondengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_treecallablezerocouponbondengine/"
description: "QuantLib::TreeCallableZeroCouponBondEngine – Numerical lattice engine for callable zero coupon bonds."
---

<p>QuantLib::TreeCallableZeroCouponBondEngine &#8211; Numerical lattice engine for callable zero coupon bonds. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/treecallablebondengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::TreeCallableFixedRateBondEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>TreeCallableZeroCouponBondEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, const Size timeSteps, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>TreeCallableZeroCouponBondEngine</code> (const boost::shared_ptr&lt; <code>ShortRateModel</code> &gt; &amp;model, const <code>TimeGrid</code> &amp;timeGrid, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>Numerical lattice engine for callable zero coupon bonds. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
