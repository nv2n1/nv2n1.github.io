---
title: "quantlib_zeroinflationtermstructure(3)"
name: "quantlib_zeroinflationtermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zeroinflationtermstructure/"
description: "QuantLib::ZeroInflationTermStructure – Interface for zero inflation term structures."
---

<p>QuantLib::ZeroInflationTermStructure &#8211; Interface for zero inflation term structures. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflationtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::InflationTermStructure</code>. </p>
<p> Inherited by <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>, and <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>ZeroInflationTermStructure</code> (const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseZeroRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS) </p>
<p> <code>ZeroInflationTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseZeroRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS) </p>
<p> <code>ZeroInflationTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, <code>Rate</code> baseZeroRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Rate</code> <code>zeroRate</code> (const <code>Date</code> &amp;d, bool extrapolate=false) const<br />
 <i>zero-coupon inflation rate </i><br />
 <code>Rate</code> <code>zeroRate</code> (Time t, bool extrapolate=false) const </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Rate</code> <code>zeroRateImpl</code> (Time t) const =0<br />
 <i>to be defined in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Interface for zero inflation term structures.</p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> zeroRate (const <code>Date</code> &amp; d, bool extrapolate = false) const</h3>
<p>zero-coupon inflation rate </p>
<p> Essentially the fair rate for a zero-coupon inflation swap (by definition), i.e. the zero term structure uses yearly compounding, which is assumed for ZCIIS instrument quotes. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
