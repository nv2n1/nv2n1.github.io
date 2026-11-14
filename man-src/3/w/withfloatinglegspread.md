---
title: "withfloatinglegspread(3)"
name: "withfloatinglegspread"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withfloatinglegspread/"
---

QuantLib::MakeVanillaSwap - helper class 

<h2>Synopsis</h2>

<pre><code>MakeVanillaSwap (const Period &amp;swapTenor, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Rate fixedRate=Null&lt; Rate &gt;(), const Period &amp;forwardStart=0 *Days)



operator VanillaSwap () const



operator boost::shared_ptr&lt; VanillaSwap &gt; () const



MakeVanillaSwap &amp; receiveFixed (bool flag=true)



MakeVanillaSwap &amp; withType (VanillaSwap::Type type)



MakeVanillaSwap &amp; withNominal (Real n)



MakeVanillaSwap &amp; withEffectiveDate (const Date &amp;)



MakeVanillaSwap &amp; withTerminationDate (const Date &amp;)



MakeVanillaSwap &amp; withRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFixedLegTenor (const Period &amp;t)



MakeVanillaSwap &amp; withFixedLegCalendar (const Calendar &amp;cal)



MakeVanillaSwap &amp; withFixedLegConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFixedLegTerminationDateConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFixedLegRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFixedLegEndOfMonth (bool flag=true)



MakeVanillaSwap &amp; withFixedLegFirstDate (const Date &amp;d)



MakeVanillaSwap &amp; withFixedLegNextToLastDate (const Date &amp;d)



MakeVanillaSwap &amp; withFixedLegDayCount (const DayCounter &amp;dc)



MakeVanillaSwap &amp; withFloatingLegTenor (const Period &amp;t)



MakeVanillaSwap &amp; withFloatingLegCalendar (const Calendar &amp;cal)



MakeVanillaSwap &amp; withFloatingLegConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFloatingLegTerminationDateConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFloatingLegRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFloatingLegEndOfMonth (bool flag=true)



MakeVanillaSwap &amp; withFloatingLegFirstDate (const Date &amp;d)



MakeVanillaSwap &amp; withFloatingLegNextToLastDate (const Date &amp;d)



MakeVanillaSwap &amp; withFloatingLegDayCount (const DayCounter &amp;dc)



MakeVanillaSwap &amp; withFloatingLegSpread (Spread sp)



MakeVanillaSwap &amp; withDiscountingTermStructure (const Handle&lt; YieldTermStructure &gt; &amp;discountingTermStructure)</code></pre>

<h3>Public Member Functions</h3>

<pre><code>MakeVanillaSwap (const Period &amp;swapTenor, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Rate fixedRate=Null&lt; Rate &gt;(), const Period &amp;forwardStart=0 *Days)



operator VanillaSwap () const



operator boost::shared_ptr&lt; VanillaSwap &gt; () const



MakeVanillaSwap &amp; receiveFixed (bool flag=true)



MakeVanillaSwap &amp; withType (VanillaSwap::Type type)



MakeVanillaSwap &amp; withNominal (Real n)



MakeVanillaSwap &amp; withEffectiveDate (const Date &amp;)



MakeVanillaSwap &amp; withTerminationDate (const Date &amp;)



MakeVanillaSwap &amp; withRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFixedLegTenor (const Period &amp;t)



MakeVanillaSwap &amp; withFixedLegCalendar (const Calendar &amp;cal)



MakeVanillaSwap &amp; withFixedLegConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFixedLegTerminationDateConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFixedLegRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFixedLegEndOfMonth (bool flag=true)



MakeVanillaSwap &amp; withFixedLegFirstDate (const Date &amp;d)



MakeVanillaSwap &amp; withFixedLegNextToLastDate (const Date &amp;d)



MakeVanillaSwap &amp; withFixedLegDayCount (const DayCounter &amp;dc)



MakeVanillaSwap &amp; withFloatingLegTenor (const Period &amp;t)



MakeVanillaSwap &amp; withFloatingLegCalendar (const Calendar &amp;cal)



MakeVanillaSwap &amp; withFloatingLegConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFloatingLegTerminationDateConvention (BusinessDayConvention bdc)



MakeVanillaSwap &amp; withFloatingLegRule (DateGeneration::Rule r)



MakeVanillaSwap &amp; withFloatingLegEndOfMonth (bool flag=true)



MakeVanillaSwap &amp; withFloatingLegFirstDate (const Date &amp;d)



MakeVanillaSwap &amp; withFloatingLegNextToLastDate (const Date &amp;d)



MakeVanillaSwap &amp; withFloatingLegDayCount (const DayCounter &amp;dc)



MakeVanillaSwap &amp; withFloatingLegSpread (Spread sp)



MakeVanillaSwap &amp; withDiscountingTermStructure (const Handle&lt; YieldTermStructure &gt; &amp;discountingTermStructure)</code></pre>

<h2>Detailed Description</h2>

helper class 

 This class provides a more comfortable way to instantiate standard market swap.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
