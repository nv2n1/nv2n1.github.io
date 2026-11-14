---
title: "quantlib_capfloortermvolsurface(3)"
name: "quantlib_capfloortermvolsurface"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_capfloortermvolsurface/"
description: "QuantLib::CapFloorTermVolSurface – Cap/floor smile volatility surface."
---

<p>QuantLib::CapFloorTermVolSurface &#8211; Cap/floor smile volatility surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/capfloor/capfloortermvolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::CapFloorTermVolatilityStructure</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CapFloorTermVolSurface</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; Rate &gt; &amp;strikes, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>floating reference date, floating market data </i><br />
 <code>CapFloorTermVolSurface</code> (const <code>Date</code> &amp;settlementDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; Rate &gt; &amp;strikes, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>fixed reference date, floating market data </i><br />
 <code>CapFloorTermVolSurface</code> (const <code>Date</code> &amp;settlementDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; Rate &gt; &amp;strikes, const <code>Matrix</code> &amp;volatilities, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>fixed reference date, fixed market data </i><br />
 <code>CapFloorTermVolSurface</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; Rate &gt; &amp;strikes, const <code>Matrix</code> &amp;volatilities, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
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
<p> const std::vector&lt; Rate &gt; &amp; <code>strikes</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>Volatility</code> <code>volatilityImpl</code> (Time t, Rate strike) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Cap/floor smile volatility surface. </p>
<p> This class provides the volatility for a given cap by interpolating a volatility surface whose elements are the market term volatilities of a set of caps/floors with given length and given strike.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
