---
title: "witheffectivedate(3)"
name: "witheffectivedate"
section: "3"
letter: "w"
url: "/docs/linux/man/3-witheffectivedate/"
---

QuantLib::MakeCapFloor - helper class 

<h2>Synopsis</h2>

<pre><code>MakeCapFloor (CapFloor::Type capFloorType, const Period &amp;capFloorTenor, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Rate strike=Null&lt; Rate &gt;(), const Period &amp;forwardStart=0 *Days)



operator CapFloor () const



operator boost::shared_ptr&lt; CapFloor &gt; () const



MakeCapFloor &amp; withNominal (Real n)



MakeCapFloor &amp; withEffectiveDate (const Date &amp;effectiveDate, bool firstCapletExcluded)



MakeCapFloor &amp; withTenor (const Period &amp;t)



MakeCapFloor &amp; withCalendar (const Calendar &amp;cal)



MakeCapFloor &amp; withConvention (BusinessDayConvention bdc)



MakeCapFloor &amp; withTerminationDateConvention (BusinessDayConvention bdc)



MakeCapFloor &amp; withRule (DateGeneration::Rule r)



MakeCapFloor &amp; withEndOfMonth (bool flag=true)



MakeCapFloor &amp; withFirstDate (const Date &amp;d)



MakeCapFloor &amp; withNextToLastDate (const Date &amp;d)



MakeCapFloor &amp; withDayCount (const DayCounter &amp;dc)



MakeCapFloor &amp; withPricingEngine (const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine)</code></pre>

<h3>Public Member Functions</h3>

<pre><code>MakeCapFloor (CapFloor::Type capFloorType, const Period &amp;capFloorTenor, const boost::shared_ptr&lt; IborIndex &gt; &amp;iborIndex, Rate strike=Null&lt; Rate &gt;(), const Period &amp;forwardStart=0 *Days)



operator CapFloor () const



operator boost::shared_ptr&lt; CapFloor &gt; () const



MakeCapFloor &amp; withNominal (Real n)



MakeCapFloor &amp; withEffectiveDate (const Date &amp;effectiveDate, bool firstCapletExcluded)



MakeCapFloor &amp; withTenor (const Period &amp;t)



MakeCapFloor &amp; withCalendar (const Calendar &amp;cal)



MakeCapFloor &amp; withConvention (BusinessDayConvention bdc)



MakeCapFloor &amp; withTerminationDateConvention (BusinessDayConvention bdc)



MakeCapFloor &amp; withRule (DateGeneration::Rule r)



MakeCapFloor &amp; withEndOfMonth (bool flag=true)



MakeCapFloor &amp; withFirstDate (const Date &amp;d)



MakeCapFloor &amp; withNextToLastDate (const Date &amp;d)



MakeCapFloor &amp; withDayCount (const DayCounter &amp;dc)



MakeCapFloor &amp; withPricingEngine (const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine)</code></pre>

<h2>Detailed Description</h2>

helper class 

 This class provides a more comfortable way to instantiate standard market cap and floor.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
