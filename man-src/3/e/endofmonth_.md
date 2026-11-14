---
title: "endofmonth_(3)"
name: "endofmonth_"
section: "3"
letter: "e"
url: "/docs/linux/man/3-endofmonth_/"
description: "QuantLib::IborIndex – base class for Inter-Bank-Offered-Rate indexes (e.g. Libor, etc.)"
---

<p>QuantLib::IborIndex &#8211; base class for Inter-Bank-Offered-Rate indexes (e.g. Libor, etc.) </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/iborindex.hpp&gt; </p>
<p> Inherits <code>QuantLib::InterestRateIndex</code>. </p>
<p> Inherited by <code>Cdor</code>, <code>DailyTenorEuribor</code>, <code>DailyTenorEuribor365</code>, <code>DailyTenorEURLibor</code>, <code>DailyTenorLibor</code>, <code>Euribor</code>, <code>Euribor365</code>, <code>EURLibor</code>, <code>Jibar</code>, <code>Libor</code>, <code>Tibor</code>, <code>TRLibor</code>, and <code>Zibor</code>. </p>
<h3>Public Member Functions</h3>
<p><code>IborIndex</code> (const std::string &amp;familyName, const <code>Period</code> &amp;tenor, <code>Natural</code> settlementDays, const <code>Currency</code> &amp;currency, const <code>Calendar</code> &amp;fixingCalendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>InterestRateIndex interface</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure</code> () const </p>
<p> <code>Inspectors</code> </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> bool <code>endOfMonth</code> () const </p>
<p> <code>Date calculations</code> </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const </p>
<p> <code>Other methods</code> </p>
<p> virtual boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>clone</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h) const<br />
 <i>returns a copy of itself linked to a different forecast curve </i></p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>forecastFixing</code> (const <code>Date</code> &amp;fixingDate) const </p>
<h3>Protected Attributes</h3>
<p><code>BusinessDayConvention</code> <code>convention_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure_</code> </p>
<p> bool <code>endOfMonth_</code> </p>
<h2>Detailed Description</h2>
<p>base class for Inter-Bank-Offered-Rate indexes (e.g. Libor, etc.) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
