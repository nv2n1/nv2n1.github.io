---
title: "withfloatinglegendofmonth(3)"
name: "withfloatinglegendofmonth"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withfloatinglegendofmonth/"
---

QuantLib::MakeCms - helper class for instantiating CMS 

<h2>Synopsis</h2>

<pre><code>MakeCms (const Period &amp;swapTenor, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Spread iborSpread=0.0, const Period &amp;forwardStart=0 *Days)



MakeCms (const Period &amp;swapTenor, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, Spread iborSpread=0.0, const Period &amp;forwardStart=0 *Days)



operator Swap () const



operator boost::shared_ptr&lt; Swap &gt; () const



MakeCms &amp; receiveCms (bool flag=true)



MakeCms &amp; withNominal (Real n)



MakeCms &amp; withEffectiveDate (const Date &amp;)



MakeCms &amp; withCmsLegTenor (const Period &amp;t)



MakeCms &amp; withCmsLegCalendar (const Calendar &amp;cal)



MakeCms &amp; withCmsLegConvention (BusinessDayConvention bdc)



MakeCms &amp; withCmsLegTerminationDateConvention (BusinessDayConvention)



MakeCms &amp; withCmsLegRule (DateGeneration::Rule r)



MakeCms &amp; withCmsLegEndOfMonth (bool flag=true)



MakeCms &amp; withCmsLegFirstDate (const Date &amp;d)



MakeCms &amp; withCmsLegNextToLastDate (const Date &amp;d)



MakeCms &amp; withCmsLegDayCount (const DayCounter &amp;dc)



MakeCms &amp; withFloatingLegTenor (const Period &amp;t)



MakeCms &amp; withFloatingLegCalendar (const Calendar &amp;cal)



MakeCms &amp; withFloatingLegConvention (BusinessDayConvention bdc)



MakeCms &amp; withFloatingLegTerminationDateConvention (BusinessDayConvention bdc)



MakeCms &amp; withFloatingLegRule (DateGeneration::Rule r)



MakeCms &amp; withFloatingLegEndOfMonth (bool flag=true)



MakeCms &amp; withFloatingLegFirstDate (const Date &amp;d)



MakeCms &amp; withFloatingLegNextToLastDate (const Date &amp;d)



MakeCms &amp; withFloatingLegDayCount (const DayCounter &amp;dc)



MakeCms &amp; withAtmSpread (bool flag=true)



MakeCms &amp; withDiscountingTermStructure (const Handle&lt; YieldTermStructure &gt; &amp;discountingTermStructure)



MakeCms &amp; withCmsCouponPricer (const boost::shared_ptr&lt; CmsCouponPricer &gt; &amp;couponPricer)</code></pre>

<h3>Public Member Functions</h3>

<pre><code>MakeCms (const Period &amp;swapTenor, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Spread iborSpread=0.0, const Period &amp;forwardStart=0 *Days)



MakeCms (const Period &amp;swapTenor, const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, Spread iborSpread=0.0, const Period &amp;forwardStart=0 *Days)



operator Swap () const



operator boost::shared_ptr&lt; Swap &gt; () const



MakeCms &amp; receiveCms (bool flag=true)



MakeCms &amp; withNominal (Real n)



MakeCms &amp; withEffectiveDate (const Date &amp;)



MakeCms &amp; withCmsLegTenor (const Period &amp;t)



MakeCms &amp; withCmsLegCalendar (const Calendar &amp;cal)



MakeCms &amp; withCmsLegConvention (BusinessDayConvention bdc)



MakeCms &amp; withCmsLegTerminationDateConvention (BusinessDayConvention)



MakeCms &amp; withCmsLegRule (DateGeneration::Rule r)



MakeCms &amp; withCmsLegEndOfMonth (bool flag=true)



MakeCms &amp; withCmsLegFirstDate (const Date &amp;d)



MakeCms &amp; withCmsLegNextToLastDate (const Date &amp;d)



MakeCms &amp; withCmsLegDayCount (const DayCounter &amp;dc)



MakeCms &amp; withFloatingLegTenor (const Period &amp;t)



MakeCms &amp; withFloatingLegCalendar (const Calendar &amp;cal)



MakeCms &amp; withFloatingLegConvention (BusinessDayConvention bdc)



MakeCms &amp; withFloatingLegTerminationDateConvention (BusinessDayConvention bdc)



MakeCms &amp; withFloatingLegRule (DateGeneration::Rule r)



MakeCms &amp; withFloatingLegEndOfMonth (bool flag=true)



MakeCms &amp; withFloatingLegFirstDate (const Date &amp;d)



MakeCms &amp; withFloatingLegNextToLastDate (const Date &amp;d)



MakeCms &amp; withFloatingLegDayCount (const DayCounter &amp;dc)



MakeCms &amp; withAtmSpread (bool flag=true)



MakeCms &amp; withDiscountingTermStructure (const Handle&lt; YieldTermStructure &gt; &amp;discountingTermStructure)



MakeCms &amp; withCmsCouponPricer (const boost::shared_ptr&lt; CmsCouponPricer &gt; &amp;couponPricer)</code></pre>

<h2>Detailed Description</h2>

helper class for instantiating CMS 

 This class provides a more comfortable way to instantiate standard market constant maturity swap.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
