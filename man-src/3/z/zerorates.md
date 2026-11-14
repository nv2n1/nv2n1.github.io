---
title: "zerorates(3)"
name: "zerorates"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zerorates/"
description: "QuantLib::InterpolatedZeroCurve – Term structure based on interpolation of zero yields."
---

<p>QuantLib::InterpolatedZeroCurve &#8211; Term structure based on interpolation of zero yields. </p>
<h2>Synopsis</h2>
<pre><code>InterpolatedZeroCurve (const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Rate &gt; &amp;yields, const DayCounter &amp;dayCounter, const Interpolator &amp;interpolator=Interpolator())



Inspectors
std::vector&lt; Date &gt; dates_



std::vector&lt; Time &gt; times_



std::vector&lt; Rate &gt; data_



Interpolation interpolation_



Interpolator interpolator_



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Rate &gt; &amp; zeroRates () const



std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const



InterpolatedZeroCurve (const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



InterpolatedZeroCurve (const Date &amp;referenceDate, const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



InterpolatedZeroCurve (Natural settlementDays, const Calendar &amp;, const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



Rate zeroYieldImpl (Time t) const


zero-yield calculation</code></pre>
<p> Inherits <code>QuantLib::ZeroYieldStructure</code>, and boost::noncopyable.</p>
<h3>Public Member Functions</h3>
<pre><code>InterpolatedZeroCurve (const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Rate &gt; &amp;yields, const DayCounter &amp;dayCounter, const Interpolator &amp;interpolator=Interpolator())



Inspectors
std::vector&lt; Date &gt; dates_



std::vector&lt; Time &gt; times_



std::vector&lt; Rate &gt; data_



Interpolation interpolation_



Interpolator interpolator_



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Rate &gt; &amp; zeroRates () const



std::vector&lt; std::pair&lt; Date, Rate &gt; &gt; nodes () const



InterpolatedZeroCurve (const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



InterpolatedZeroCurve (const Date &amp;referenceDate, const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



InterpolatedZeroCurve (Natural settlementDays, const Calendar &amp;, const DayCounter &amp;, const Interpolator &amp;interpolator=Interpolator())



Rate zeroYieldImpl (Time t) const


zero-yield calculation</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedZeroCurve&lt; Interpolator &gt;</h3>
<p>Term structure based on interpolation of zero yields.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
