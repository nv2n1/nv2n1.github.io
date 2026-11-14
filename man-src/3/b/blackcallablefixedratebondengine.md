---
title: "blackcallablefixedratebondengine(3)"
name: "blackcallablefixedratebondengine"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackcallablefixedratebondengine/"
description: "QuantLib::BlackCallableFixedRateBondEngine – Black-formula callable fixed rate bond engine."
---

<p>QuantLib::BlackCallableFixedRateBondEngine &#8211; Black-formula callable fixed rate bond engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/blackcallablebondengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::CallableBond::engine</code>. </p>
<p> Inherited by <code>BlackCallableZeroCouponBondEngine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackCallableFixedRateBondEngine</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;fwdYieldVol, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve)<br />
 <i>volatility is the quoted fwd yield volatility, not price vol </i><br />
 <code>BlackCallableFixedRateBondEngine</code> (const <code>Handle</code>&lt; <code>CallableBondVolatilityStructure</code> &gt; &amp;yieldVolStructure, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve)<br />
 <i>volatility is the quoted fwd yield volatility, not price vol </i><br />
 void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Black-formula callable fixed rate bond engine. </p>
<p> Callable fixed rate bond Black engine. The embedded (European) option follows the Black &#8216;European bond option&#8217; treatment in Hull, Fourth Edition, Chapter 20. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>set additionalResults (e.g. vega, fairStrike, etc.)</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This class has yet to be tested</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
