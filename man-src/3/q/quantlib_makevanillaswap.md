---
title: "quantlib_makevanillaswap(3)"
name: "quantlib_makevanillaswap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makevanillaswap/"
description: "QuantLib::MakeVanillaSwap – helper class"
---

<p>QuantLib::MakeVanillaSwap &#8211; helper class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/makevanillaswap.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeVanillaSwap</code> (const <code>Period</code> &amp;swapTenor, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, <code>Rate</code> fixedRate=<code>Null</code>&lt; <code>Rate</code> &gt;(), const <code>Period</code> &amp;forwardStart=0 *Days) </p>
<p> <code>operator VanillaSwap</code> () const </p>
<p> <code>operator boost::shared_ptr&lt; VanillaSwap &gt;</code> () const </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>receiveFixed</code> (bool flag=true) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withType</code> (VanillaSwap::Type type) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withNominal</code> (<code>Real</code> n) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withEffectiveDate</code> (const <code>Date</code> &amp;) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withTerminationDate</code> (const <code>Date</code> &amp;) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegTenor</code> (const <code>Period</code> &amp;t) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegCalendar</code> (const <code>Calendar</code> &amp;cal) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegTerminationDateConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegEndOfMonth</code> (bool flag=true) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFixedLegDayCount</code> (const <code>DayCounter</code> &amp;dc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegTenor</code> (const <code>Period</code> &amp;t) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegCalendar</code> (const <code>Calendar</code> &amp;cal) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegTerminationDateConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegEndOfMonth</code> (bool flag=true) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegDayCount</code> (const <code>DayCounter</code> &amp;dc) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withFloatingLegSpread</code> (<code>Spread</code> sp) </p>
<p> <code>MakeVanillaSwap</code> &amp; <code>withDiscountingTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountingTermStructure) </p>
<h2>Detailed Description</h2>
<p>helper class </p>
<p> This class provides a more comfortable way to instantiate standard market swap. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
