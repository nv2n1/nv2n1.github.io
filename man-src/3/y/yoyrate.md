---
title: "yoyrate(3)"
name: "yoyrate"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yoyrate/"
description: "QuantLib::YoYInflationTermStructure – Base class for year-on-year inflation term structures."
---

<p>QuantLib::YoYInflationTermStructure &#8211; Base class for year-on-year inflation term structures. </p>
<h2>Synopsis</h2>
<pre><code>Rate yoyRate (const Date &amp;d, bool extrapolate=false) const


year-on-year inflation rate


Rate yoyRate (Time time, bool extrapolate=false) const



Protected Member Functions
virtual Rate yoyRateImpl (Time time) const =0


to be defined in derived classes</code></pre>
<p> Inherits <code>QuantLib::InflationTermStructure</code>. Inherited by <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, and <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>YoYInflationTermStructure</code> (const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> <code>YoYInflationTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> <code>YoYInflationTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS)<br />
 <code>Inspectors</code> </p>
<pre><code>Rate yoyRate (const Date &amp;d, bool extrapolate=false) const


year-on-year inflation rate


Rate yoyRate (Time time, bool extrapolate=false) const



Protected Member Functions
virtual Rate yoyRateImpl (Time time) const =0


to be defined in derived classes</code></pre>
<h2>Detailed Description</h2>
<p>Base class for year-on-year inflation term structures.</p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> yoyRate (const <code>Date</code> &amp; d, bool extrapolate = false) const</h3>
<p>year-on-year inflation rate </p>
<p> <code>Note:</code></p>
<dl>
<dd>this is not the year-on-year swap (YYIIS) rate.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
