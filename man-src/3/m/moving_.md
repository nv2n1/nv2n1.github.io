---
title: "moving_(3)"
name: "moving_"
section: "3"
letter: "m"
url: "/docs/linux/man/3-moving_/"
description: "QuantLib::TermStructure – Basic term-structure functionality."
---

<p>QuantLib::TermStructure &#8211; Basic term-structure functionality. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, <code>QuantLib::Observable</code>, and <code>QuantLib::Extrapolator</code>. </p>
<p> Inherited by <code>CallableBondVolatilityStructure</code>, <code>CommodityCurve</code>, <code>DefaultProbabilityTermStructure</code>, <code>InflationTermStructure</code>, <code>VolatilityTermStructure</code>, and <code>YieldTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 There are three ways in which a term structure can keep track of its reference date. The first is that such date is fixed; the second is that it is determined by advancing the current date of a given number of business days; and the third is that it is based on the reference date of some other structure. </p>
<p> In the first case, the constructor taking a date is to be used; the default implementation of <code>referenceDate()</code> will then return such date. In the second case, the constructor taking a number of days and a calendar is to be used; <code>referenceDate()</code> will return a date calculated based on the current evaluation date, and the term structure and its observers will be notified when the evaluation date changes. In the last case, the <code>referenceDate()</code> method must be overridden in derived classes so that it fetches and return the appropriate date. </p>
<p> <code>TermStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>TermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>TermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Dates and Time</code> </p>
<p> virtual <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 Time <code>timeFromReference</code> (const <code>Date</code> &amp;date) const<br />
 <i>date/time conversion </i><br />
 virtual <code>Date</code> <code>maxDate</code> () const =0<br />
 <i>the latest date for which the curve can return values </i><br />
 virtual Time <code>maxTime</code> () const<br />
 <i>the latest time for which the curve can return values </i><br />
 virtual const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 virtual <code>Calendar</code> <code>calendar</code> () const<br />
 <i>the calendar used for reference and/or option date calculation </i><br />
 virtual <code>Natural</code> <code>settlementDays</code> () const<br />
 <i>the settlementDays used for reference date calculation </i> </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Protected Member Functions</h3>
<p>void <code>checkRange</code> (const <code>Date</code> &amp;d, bool extrapolate) const<br />
 <i>date-range check </i><br />
 void <code>checkRange</code> (Time t, bool extrapolate) const<br />
 <i>time-range check </i></p>
<h3>Protected Attributes</h3>
<p>bool <code>moving_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<h2>Detailed Description</h2>
<p>Basic term-structure functionality.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>TermStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>AbcdAtmVolCurve</code>, <code>ExtendedBlackVarianceCurve</code>, <code>ExtendedBlackVarianceSurface</code>, <code>SabrVolSurface</code>, <code>ExtendedDiscountCurve</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, <code>StrippedOptionletAdapter</code>, <code>FittedBondDiscountCurve</code>, <code>FlatForward</code>, and <code>PiecewiseZeroSpreadedTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
