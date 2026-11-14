---
title: "quantlib_capfloortermvolcurve(3)"
name: "quantlib_capfloortermvolcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_capfloortermvolcurve/"
description: "QuantLib::CapFloorTermVolCurve – Cap/floor at-the-money term-volatility vector."
---

<p>QuantLib::CapFloorTermVolCurve &#8211; Cap/floor at-the-money term-volatility vector. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/capfloor/capfloortermvolcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::CapFloorTermVolatilityStructure</code>, <code>QuantLib::LazyObject</code>, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>CapFloorTermVolCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;vols, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>floating reference date, floating market data </i><br />
 <code>CapFloorTermVolCurve</code> (const <code>Date</code> &amp;settlementDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;vols, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>fixed reference date, floating market data </i><br />
 <code>CapFloorTermVolCurve</code> (const <code>Date</code> &amp;settlementDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Volatility</code> &gt; &amp;vols, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>fixed reference date, fixed market data </i><br />
 <code>CapFloorTermVolCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Volatility</code> &gt; &amp;vols, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>floating reference date, fixed market data </i> </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>update</code> () </p>
<p> void <code>performCalculations</code> () const </p>
<p> <code>some inspectors</code> </p>
<p> const std::vector&lt; <code>Period</code> &gt; &amp; <code>optionTenors</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>optionDates</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>optionTimes</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>Volatility</code> <code>volatilityImpl</code> (Time length, Rate) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Cap/floor at-the-money term-volatility vector. </p>
<p> This class provides the at-the-money volatility for a given cap by interpolating a volatility vector whose elements are the market volatilities of a set of caps/floors with given length.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
