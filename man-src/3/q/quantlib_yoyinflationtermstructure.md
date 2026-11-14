---
title: "quantlib_yoyinflationtermstructure(3)"
name: "quantlib_yoyinflationtermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_yoyinflationtermstructure/"
description: "QuantLib::YoYInflationTermStructure – Base class for year-on-year inflation term structures."
---

<p>QuantLib::YoYInflationTermStructure &#8211; Base class for year-on-year inflation term structures. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflationtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::InflationTermStructure</code>. </p>
<p> Inherited by <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, and <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>YoYInflationTermStructure</code> (const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> <code>YoYInflationTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> <code>YoYInflationTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Rate</code> <code>yoyRate</code> (const <code>Date</code> &amp;d, bool extrapolate=false) const<br />
 <i>year-on-year inflation rate </i><br />
 <code>Rate</code> <code>yoyRate</code> (Time time, bool extrapolate=false) const </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Rate</code> <code>yoyRateImpl</code> (Time time) const =0<br />
 <i>to be defined in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Base class for year-on-year inflation term structures.</p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> yoyRate (const <code>Date</code> &amp; d, bool extrapolate = false) const</h3>
<p>year-on-year inflation rate </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>this is not the year-on-year swap (YYIIS) rate.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
