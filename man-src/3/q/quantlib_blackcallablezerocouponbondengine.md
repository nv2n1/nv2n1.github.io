---
title: "quantlib_blackcallablezerocouponbondengine(3)"
name: "quantlib_blackcallablezerocouponbondengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackcallablezerocouponbondengine/"
description: "QuantLib::BlackCallableZeroCouponBondEngine – Black-formula callable zero coupon bond engine."
---

<p>QuantLib::BlackCallableZeroCouponBondEngine &#8211; Black-formula callable zero coupon bond engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/blackcallablebondengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackCallableFixedRateBondEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackCallableZeroCouponBondEngine</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;fwdYieldVol, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve)<br />
 <i>volatility is the quoted fwd yield volatility, not price vol </i><br />
 <code>BlackCallableZeroCouponBondEngine</code> (const <code>Handle</code>&lt; <code>CallableBondVolatilityStructure</code> &gt; &amp;yieldVolStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve)<br />
 <i>volatility is the quoted fwd yield volatility, not price vol </i></p>
<h2>Detailed Description</h2>
<p>Black-formula callable zero coupon bond engine. </p>
<p> Callable zero coupon bond, where the embedded (European) option price is assumed to obey the Black formula. Follows &#8216;European bond option&#8217; treatment in Hull, Fourth Edition, Chapter 20. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This class has yet to be tested.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
