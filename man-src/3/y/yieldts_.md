---
title: "yieldts_(3)"
name: "yieldts_"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yieldts_/"
description: "QuantLib::InflationSwap – Abstract base class for inflation swaps."
---

<p>QuantLib::InflationSwap &#8211; Abstract base class for inflation swaps. </p>
<h2>Synopsis</h2>
<pre><code>InflationSwap (const Date &amp;start, const Date &amp;maturity, const Period &amp;lag, const Calendar &amp;calendar, BusinessDayConvention convention, const DayCounter &amp;dayCounter, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS)


the constructor sets common data members


virtual Rate fairRate () const =0</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>. Inherited by <code>YearOnYearInflationSwap</code>, and <code>ZeroCouponInflationSwap</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>InflationSwap (const Date &amp;start, const Date &amp;maturity, const Period &amp;lag, const Calendar &amp;calendar, BusinessDayConvention convention, const DayCounter &amp;dayCounter, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS)


the constructor sets common data members


virtual Rate fairRate () const =0</code></pre>
<p> <code>Inspectors</code> </p>
<p> <code>Date</code> <code>baseDate</code> () const </p>
<p> <code>Period</code> <code>lag</code> () const </p>
<p> <code>Date</code> <code>startDate</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> () const </p>
<p> <code>Calendar</code> <code>calendar</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const</p>
<h3>Protected Attributes</h3>
<p><code>Date</code> <code>start_</code> </p>
<p> <code>Date</code> <code>maturity_</code> </p>
<p> <code>Period</code> <code>lag_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> <code>BusinessDayConvention</code> <code>bdc_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>yieldTS_</code> </p>
<p> <code>Date</code> <code>baseDate_</code></p>
<h2>Detailed Description</h2>
<p>Abstract base class for inflation swaps. </p>
<p> Inflation swaps need two term structures: a yield curve, and an inflation term structure (either zero-based, i.e., the rate $ r(t) $ equals $ I(t)/I(t_0) &#8211; 1 $ where $ I $ if the index and $ t_0 $ is the base time, or year-on-year, i.e., $ r(t) = I(t)/I(t_p) &#8211; 1 $ where the previous time $ t_p $ is defined as $ t $ minus one year.)</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> baseDate () const</h3>
<p>The inflation rate is taken relative to the base date, which is a lag period before the start date of the swap.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
