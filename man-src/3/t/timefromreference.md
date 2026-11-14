---
title: "timefromreference(3)"
name: "timefromreference"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timefromreference/"
description: "QuantLib::TermStructure – Basic term-structure functionality."
---

<p>QuantLib::TermStructure &#8211; Basic term-structure functionality. </p>
<h2>Synopsis</h2>
<pre><code>void update ()



Protected Member Functions
void checkRange (const Date &amp;d, bool extrapolate) const


date-range check


void checkRange (Time t, bool extrapolate) const


time-range check



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Observer</code>, <code>QuantLib::Observable</code>, and <code>QuantLib::Extrapolator</code>. Inherited by <code>CallableBondVolatilityStructure</code>, <code>CommodityCurve</code>, <code>DefaultProbabilityTermStructure</code>, <code>InflationTermStructure</code>, <code>VolatilityTermStructure</code>, and <code>YieldTermStructure</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 There are three ways in which a term structure can keep track of its reference date. The first is that such date is fixed; the second is that it is determined by advancing the current date of a given number of business days; and the third is that it is based on the reference date of some other structure. In the first case, the constructor taking a date is to be used; the default implementation of <code>referenceDate()</code> will then return such date. In the second case, the constructor taking a number of days and a calendar is to be used; <code>referenceDate()</code> will return a date calculated based on the current evaluation date, and the term structure and its observers will be notified when the evaluation date changes. In the last case, the <code>referenceDate()</code> method must be overridden in derived classes so that it fetches and return the appropriate date. void update ()</p>
<p>Protected Member Functions<br />
void checkRange (const Date &amp;d, bool extrapolate) const</p>
<p>date-range check</p>
<p>void checkRange (Time t, bool extrapolate) const</p>
<p>time-range check</p>
<p>Protected Attributes <code>Dates and Time</code><br />
 void update ()</p>
<p>Protected Member Functions<br />
void checkRange (const Date &amp;d, bool extrapolate) const</p>
<p>date-range check</p>
<p>void checkRange (Time t, bool extrapolate) const</p>
<p>time-range check</p>
<p>Protected Attributes <code>Observer interface</code> </p>
<pre><code>void update ()



Protected Member Functions
void checkRange (const Date &amp;d, bool extrapolate) const


date-range check


void checkRange (Time t, bool extrapolate) const


time-range check



Protected Attributes</code></pre>
<p> bool <code>moving_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code></p>
<h2>Detailed Description</h2>
<p>Basic term-structure functionality.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>TermStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>AbcdAtmVolCurve</code>, <code>ExtendedBlackVarianceCurve</code>, <code>ExtendedBlackVarianceSurface</code>, <code>SabrVolSurface</code>, <code>ExtendedDiscountCurve</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, <code>StrippedOptionletAdapter</code>, <code>FittedBondDiscountCurve</code>, <code>FlatForward</code>, and <code>PiecewiseZeroSpreadedTermStructure</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
