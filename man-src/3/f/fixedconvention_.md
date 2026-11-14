---
title: "fixedconvention_(3)"
name: "fixedconvention_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixedconvention_/"
description: "QuantLib::SwapRateHelper – Rate helper for bootstrapping over swap rates."
---

<p>QuantLib::SwapRateHelper &#8211; Rate helper for bootstrapping over swap rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>QuantLib::RelativeDateRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SwapRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread=<code>Handle</code>&lt; <code>Quote</code> &gt;(), const <code>Period</code> &amp;fwdStart=0 *Days) </p>
<p> <code>SwapRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, const <code>Period</code> &amp;tenor, const <code>Calendar</code> &amp;calendar, <code>Frequency</code> fixedFrequency, <code>BusinessDayConvention</code> fixedConvention, const <code>DayCounter</code> &amp;fixedDayCount, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread=<code>Handle</code>&lt; <code>Quote</code> &gt;(), const <code>Period</code> &amp;fwdStart=0 *Days) </p>
<p> <code>SwapRateHelper</code> (<code>Rate</code> rate, const <code>Period</code> &amp;tenor, const <code>Calendar</code> &amp;calendar, <code>Frequency</code> fixedFrequency, <code>BusinessDayConvention</code> fixedConvention, const <code>DayCounter</code> &amp;fixedDayCount, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread=<code>Handle</code>&lt; <code>Quote</code> &gt;(), const <code>Period</code> &amp;fwdStart=0 *Days) </p>
<p> <code>SwapRateHelper</code> (<code>Rate</code> rate, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread=<code>Handle</code>&lt; <code>Quote</code> &gt;(), const <code>Period</code> &amp;fwdStart=0 *Days) </p>
<p> <code>RateHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>YieldTermStructure</code> *) </p>
<p> <code>SwapRateHelper inspectors</code> </p>
<p> <code>Spread</code> <code>spread</code> () const </p>
<p> boost::shared_ptr&lt; <code>VanillaSwap</code> &gt; <code>swap</code> () const </p>
<p> const <code>Period</code> &amp; <code>forwardStart</code> () const </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>void <code>initializeDates</code> () </p>
<h3>Protected Attributes</h3>
<p><code>Period</code> <code>tenor_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> <code>BusinessDayConvention</code> <code>fixedConvention_</code> </p>
<p> <code>Frequency</code> <code>fixedFrequency_</code> </p>
<p> <code>DayCounter</code> <code>fixedDayCount_</code> </p>
<p> boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>iborIndex_</code> </p>
<p> boost::shared_ptr&lt; <code>VanillaSwap</code> &gt; <code>swap_</code> </p>
<p> <code>RelinkableHandle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructureHandle_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>spread_</code> </p>
<p> <code>Period</code> <code>fwdStart_</code> </p>
<h2>Detailed Description</h2>
<p>Rate helper for bootstrapping over swap rates. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>use input <code>SwapIndex</code> to create the swap</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
