---
title: "quantlib_blackswaptionengine(3)"
name: "quantlib_blackswaptionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackswaptionengine/"
description: "QuantLib::BlackSwaptionEngine – Black-formula swaption engine."
---

<p>QuantLib::BlackSwaptionEngine &#8211; Black-formula swaption engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/swaption/blackswaptionengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::Swaption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackSwaptionEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, <code>Volatility</code> vol, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>()) </p>
<p> <code>BlackSwaptionEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;vol, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>()) </p>
<p> <code>BlackSwaptionEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;vol) </p>
<p> void <code>calculate</code> () const </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure</code> () </p>
<p> <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; <code>volatility</code> () </p>
<h2>Detailed Description</h2>
<p>Black-formula swaption engine. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
