---
title: "yoyrateimpl(3)"
name: "yoyrateimpl"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yoyrateimpl/"
description: "QuantLib::InterpolatedYoYInflationCurve – Inflation term structure based on interpolated year-on-year rates."
---

<p>QuantLib::InterpolatedYoYInflationCurve &#8211; Inflation term structure based on interpolated year-on-year rates. </p>
<h2>Synopsis</h2>
<pre><code>const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Rate &gt; &amp; rates () const



std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const



Protected Member Functions
InterpolatedYoYInflationCurve (const Date &amp;referenceDate, const Calendar &amp;calendar, const DayCounter &amp;dayCounter, const Period &amp;lag, Frequency frequency, Rate baseYoYRate, const Handle&lt; YieldTermStructure &gt; &amp;yTS, const Interpolator &amp;interpolator=Interpolator())</code></pre>
<p> Inherits <code>QuantLib::YoYInflationTermStructure</code>, and boost::noncopyable.</p>
<h3>Public Member Functions</h3>
<p>const std::vector&lt; Date &gt; &amp; dates () const</p>
<p>const std::vector&lt; Time &gt; &amp; times () const</p>
<p>const std::vector&lt; Rate &gt; &amp; rates () const</p>
<p>std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const</p>
<p>Protected Member Functions<br />
InterpolatedYoYInflationCurve (const Date &amp;referenceDate, const Calendar &amp;calendar, const DayCounter &amp;dayCounter, const Period &amp;lag, Frequency frequency, Rate baseYoYRate, const Handle&lt; YieldTermStructure &gt; &amp;yTS, const Interpolator &amp;interpolator=Interpolator()) <code>InflationTermStructure interface</code><br />
 const std::vector&lt; Date &gt; &amp; dates () const</p>
<p>const std::vector&lt; Time &gt; &amp; times () const</p>
<p>const std::vector&lt; Rate &gt; &amp; rates () const</p>
<p>std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const</p>
<p>Protected Member Functions<br />
InterpolatedYoYInflationCurve (const Date &amp;referenceDate, const Calendar &amp;calendar, const DayCounter &amp;dayCounter, const Period &amp;lag, Frequency frequency, Rate baseYoYRate, const Handle&lt; YieldTermStructure &gt; &amp;yTS, const Interpolator &amp;interpolator=Interpolator()) <code>Inspectors</code> </p>
<pre><code>const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Rate &gt; &amp; rates () const



std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const



Protected Member Functions
InterpolatedYoYInflationCurve (const Date &amp;referenceDate, const Calendar &amp;calendar, const DayCounter &amp;dayCounter, const Period &amp;lag, Frequency frequency, Rate baseYoYRate, const Handle&lt; YieldTermStructure &gt; &amp;yTS, const Interpolator &amp;interpolator=Interpolator())</code></pre>
<p> <code>YoYInflationTermStructure interface</code> </p>
<p> Rate <code>yoyRateImpl</code> (Time t) const<br />
 <i>to be defined in derived classes </i></p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; Rate &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> Interpolator <code>interpolator_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedYoYInflationCurve&lt; Interpolator &gt;</h3>
<p>Inflation term structure based on interpolated year-on-year rates. </p>
<p> <code>Note:</code></p>
<dl>
<dd>The provided rates are not YY inflation-swap quotes.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>InterpolatedYoYInflationCurve</code> (const <code>Date</code> &amp; referenceDate, const <code>Calendar</code> &amp; calendar, const <code>DayCounter</code> &amp; dayCounter, const <code>Period</code> &amp; lag, <code>Frequency</code> frequency, Rate baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; yTS, const Interpolator &amp; interpolator = Interpolator()) [protected]</h3>
<p>Protected version for use when descendents don&#8217;t want to (or can&#8217;t) provide the points for interpolation on construction.</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> baseDate () const [virtual]</h3>
<p>minimum (base) date </p>
<p> Important in inflation since it starts before nominal reference date. </p>
<p> Implements <code>InflationTermStructure</code>. </p>
<p> Reimplemented in <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
