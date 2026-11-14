---
title: "baserate(3)"
name: "baserate"
section: "3"
letter: "b"
url: "/docs/linux/man/3-baserate/"
description: "QuantLib::InflationTermStructure – Interface for inflation term structures."
---

<p>QuantLib::InflationTermStructure &#8211; Interface for inflation term structures. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflationtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructure</code>. </p>
<p> Inherited by <code>YoYInflationTermStructure</code>, and <code>ZeroInflationTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>InflationTermStructure</code> (const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS, const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>()) </p>
<p> <code>InflationTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS, const <code>Calendar</code> &amp;calendar=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>()) </p>
<p> <code>InflationTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS, const <code>DayCounter</code> &amp;dayCounter=<code>DayCounter</code>()) </p>
<p> <code>Inflation interface</code> </p>
<p> virtual <code>Period</code> <code>lag</code> () const </p>
<p> virtual <code>Frequency</code> <code>frequency</code> () const </p>
<p> virtual <code>Rate</code> <code>baseRate</code> () const </p>
<p> virtual <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>nominalTermStructure</code> () const </p>
<p> virtual <code>Date</code> <code>baseDate</code> () const =0<br />
 <i>minimum (base) date </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>setBaseRate</code> (const <code>Rate</code> &amp;r) </p>
<p> void <code>checkRange</code> (const <code>Date</code> &amp;, bool extrapolate) const<br />
 <i>date-range check </i><br />
 void <code>checkRange</code> (Time t, bool extrapolate) const<br />
 <i>time-range check </i></p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>nominalTermStructure_</code> </p>
<p> <code>Period</code> <code>lag_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> <code>Rate</code> <code>baseRate_</code> </p>
<h2>Detailed Description</h2>
<p>Interface for inflation term structures. </p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Date</code> baseDate () const [pure virtual]</h3>
<p>minimum (base) date </p>
<p> Important in inflation since it starts before nominal reference date. </p>
<p> Implemented in <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, and <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
