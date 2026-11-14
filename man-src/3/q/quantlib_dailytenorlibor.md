---
title: "quantlib_dailytenorlibor(3)"
name: "quantlib_dailytenorlibor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dailytenorlibor/"
description: "QuantLib::DailyTenorLibor – base class for all O/N-S/N BBA LIBOR indexes but the EUR ones"
---

<p>QuantLib::DailyTenorLibor &#8211; base class for all O/N-S/N BBA LIBOR indexes but the EUR ones </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/libor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>CADLiborON</code>, <code>DailyTenorCHFLibor</code>, <code>DailyTenorGBPLibor</code>, <code>DailyTenorJPYLibor</code>, and <code>DailyTenorUSDLibor</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DailyTenorLibor</code> (const std::string &amp;familyName, <code>Natural</code> settlementDays, const <code>Currency</code> &amp;currency, const <code>Calendar</code> &amp;financialCenterCalendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>base class for all O/N-S/N BBA LIBOR indexes but the EUR ones </p>
<p> One day deposit LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
