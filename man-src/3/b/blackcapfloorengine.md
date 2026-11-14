---
title: "blackcapfloorengine(3)"
name: "blackcapfloorengine"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackcapfloorengine/"
description: "QuantLib::BlackCapFloorEngine – Black-formula cap/floor engine."
---

<p>QuantLib::BlackCapFloorEngine &#8211; Black-formula cap/floor engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/capfloor/blackcapfloorengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::CapFloor::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackCapFloorEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, <code>Volatility</code> vol, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>()) </p>
<p> <code>BlackCapFloorEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;vol, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>()) </p>
<p> <code>BlackCapFloorEngine</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, const <code>Handle</code>&lt; <code>OptionletVolatilityStructure</code> &gt; &amp;vol) </p>
<p> void <code>calculate</code> () const </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure</code> () </p>
<p> <code>Handle</code>&lt; <code>OptionletVolatilityStructure</code> &gt; <code>volatility</code> () </p>
<h2>Detailed Description</h2>
<p>Black-formula cap/floor engine. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
