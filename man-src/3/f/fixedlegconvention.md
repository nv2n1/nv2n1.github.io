---
title: "fixedlegconvention(3)"
name: "fixedlegconvention"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixedlegconvention/"
description: "QuantLib::SwapIndex – base class for swap-rate indexes"
---

<p>QuantLib::SwapIndex &#8211; base class for swap-rate indexes </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swapindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::InterestRateIndex</code>. </p>
<p> Inherited by <code>ChfLiborSwapIsdaFix</code>, <code>EuriborSwapIfrFix</code>, <code>EuriborSwapIsdaFixA</code>, <code>EuriborSwapIsdaFixB</code>, <code>EurLiborSwapIfrFix</code>, <code>EurLiborSwapIsdaFixA</code>, <code>EurLiborSwapIsdaFixB</code>, <code>GbpLiborSwapIsdaFix</code>, <code>JpyLiborSwapIsdaFixAm</code>, <code>JpyLiborSwapIsdaFixPm</code>, <code>UsdLiborSwapIsdaFixAm</code>, and <code>UsdLiborSwapIsdaFixPm</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SwapIndex</code> (const std::string &amp;familyName, const <code>Period</code> &amp;tenor, <code>Natural</code> settlementDays, <code>Currency</code> currency, const <code>Calendar</code> &amp;calendar, const <code>Period</code> &amp;fixedLegTenor, <code>BusinessDayConvention</code> fixedLegConvention, const <code>DayCounter</code> &amp;fixedLegDayCounter, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>InterestRateIndex interface</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const </p>
<p> <code>Inspectors</code> </p>
<p> <code>Period</code> <code>fixedLegTenor</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>fixedLegConvention</code> () const </p>
<p> boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>iborIndex</code> () const </p>
<p> boost::shared_ptr&lt; <code>VanillaSwap</code> &gt; <code>underlyingSwap</code> (const <code>Date</code> &amp;fixingDate) const </p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>forecastFixing</code> (const <code>Date</code> &amp;fixingDate) const </p>
<h3>Protected Attributes</h3>
<p><code>Period</code> <code>tenor_</code> </p>
<p> boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>iborIndex_</code> </p>
<p> <code>Period</code> <code>fixedLegTenor_</code> </p>
<p> <code>BusinessDayConvention</code> <code>fixedLegConvention_</code> </p>
<h2>Detailed Description</h2>
<p>base class for swap-rate indexes</p>
<h2>Member Function Documentation</h2>
<h3>boost::shared_ptr&lt;<code>VanillaSwap</code>&gt; underlyingSwap (const <code>Date</code> &amp; fixingDate) const</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>Relinking the term structure underlying the index will not have effect on the returned swap.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
