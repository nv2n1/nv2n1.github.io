---
title: "interpolatedzerocurve(3)"
name: "interpolatedzerocurve"
section: "3"
letter: "i"
url: "/docs/linux/man/3-interpolatedzerocurve/"
description: "QuantLib::InterpolatedZeroCurve – Term structure based on interpolation of zero yields."
---

<p>QuantLib::InterpolatedZeroCurve &#8211; Term structure based on interpolation of zero yields. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/zerocurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::ZeroYieldStructure</code>, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>InterpolatedZeroCurve</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Rate</code> &gt; &amp;yields, const <code>DayCounter</code> &amp;dayCounter, const Interpolator &amp;interpolator=Interpolator()) </p>
<h3>Inspectors</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; <code>Rate</code> &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> Interpolator <code>interpolator_</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>zeroRates</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Rate</code> &gt; &gt; <code>nodes</code> () const </p>
<p> <code>InterpolatedZeroCurve</code> (const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedZeroCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedZeroCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>Rate</code> <code>zeroYieldImpl</code> (Time t) const<br />
 <i>zero-yield calculation </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedZeroCurve&lt; Interpolator &gt;</h3>
<p>Term structure based on interpolation of zero yields. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
