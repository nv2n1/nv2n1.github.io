---
title: "quantlib_interpolateddiscountcurve(3)"
name: "quantlib_interpolateddiscountcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolateddiscountcurve/"
description: "QuantLib::InterpolatedDiscountCurve – Term structure based on interpolation of discount factors."
---

<p>QuantLib::InterpolatedDiscountCurve &#8211; Term structure based on interpolation of discount factors. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/discountcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::YieldTermStructure</code>, and boost::noncopyable. </p>
<p> Inherited by <code>ExtendedDiscountCurve</code>. </p>
<h3>Public Member Functions</h3>
<p><code>InterpolatedDiscountCurve</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>DiscountFactor</code> &gt; &amp;dfs, const <code>DayCounter</code> &amp;dayCounter, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>Inspectors</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>DiscountFactor</code> &gt; &amp; <code>discounts</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>DiscountFactor</code> &gt; &gt; <code>nodes</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>InterpolatedDiscountCurve</code> (const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedDiscountCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedDiscountCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>DiscountFactor</code> <code>discountImpl</code> (Time) const<br />
 <i>discount calculation </i></p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; <code>DiscountFactor</code> &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> Interpolator <code>interpolator_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedDiscountCurve&lt; Interpolator &gt;</h3>
<p>Term structure based on interpolation of discount factors. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
