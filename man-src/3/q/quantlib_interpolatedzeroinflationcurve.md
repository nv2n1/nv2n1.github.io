---
title: "quantlib_interpolatedzeroinflationcurve(3)"
name: "quantlib_interpolatedzeroinflationcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolatedzeroinflationcurve/"
description: "QuantLib::InterpolatedZeroInflationCurve – Inflation term structure based on the interpolation of zero rates."
---

<p>QuantLib::InterpolatedZeroInflationCurve &#8211; Inflation term structure based on the interpolation of zero rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflation/interpolatedzeroinflationcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::ZeroInflationTermStructure</code>, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>InterpolatedZeroInflationCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; Rate &gt; &amp;rates, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InflationTermStructure interface</code> </p>
<p> <code>Date</code> <code>baseDate</code> () const<br />
 <i>minimum (base) date </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>Inspectors</code> </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; Rate &gt; &amp; <code>rates</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, Rate &gt; &gt; <code>nodes</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>InterpolatedZeroInflationCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, Rate baseZeroRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yTS, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>ZeroInflationTermStructure Interface</code> </p>
<p> Rate <code>zeroRateImpl</code> (Time t) const<br />
 <i>to be defined in derived classes </i></p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; Rate &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> Interpolator <code>interpolator_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedZeroInflationCurve&lt; Interpolator &gt;</h3>
<p>Inflation term structure based on the interpolation of zero rates. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>InterpolatedZeroInflationCurve</code> (const <code>Date</code> &amp; referenceDate, const <code>Calendar</code> &amp; calendar, const <code>DayCounter</code> &amp; dayCounter, const <code>Period</code> &amp; lag, <code>Frequency</code> frequency, Rate baseZeroRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; yTS, const Interpolator &amp; interpolator = Interpolator()) [protected]</h3>
<p>Protected version for use when descendents don&#8217;t want to (or can&#8217;t) provide the points for interpolation on construction.</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> baseDate () const [virtual]</h3>
<p>minimum (base) date </p>
<p> Important in inflation since it starts before nominal reference date. </p>
<p> Implements <code>InflationTermStructure</code>. </p>
<p> Reimplemented in <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
