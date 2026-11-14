---
title: "quantlib_extendeddiscountcurve(3)"
name: "quantlib_extendeddiscountcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendeddiscountcurve/"
description: "QuantLib::ExtendedDiscountCurve – Term structure based on loglinear interpolation of discount factors."
---

<p>QuantLib::ExtendedDiscountCurve &#8211; Term structure based on loglinear interpolation of discount factors. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/termstructures/extendeddiscountcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::InterpolatedDiscountCurve&lt; LogLinear &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedDiscountCurve</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; DiscountFactor &gt; &amp;dfs, const <code>Calendar</code> &amp;calendar, const <code>BusinessDayConvention</code> conv, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> void <code>update</code> () </p>
<p> <code>Rate</code> <code>compoundForward</code> (const <code>Date</code> &amp;d1, Integer f, bool extrapolate=false) const </p>
<p> <code>Rate</code> <code>compoundForward</code> (Time t1, Integer f, bool extrapolate=false) const </p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>compoundForwardImpl</code> (Time, Integer) const </p>
<p> <code>Rate</code> <code>zeroYieldImpl</code> (Time) const </p>
<p> void <code>calibrateNodes</code> () const </p>
<p> boost::shared_ptr&lt; <code>CompoundForward</code> &gt; <code>reversebootstrap</code> (Integer) const </p>
<p> boost::shared_ptr&lt; <code>CompoundForward</code> &gt; <code>forwardCurve</code> (Integer) const </p>
<h2>Detailed Description</h2>
<p>Term structure based on loglinear interpolation of discount factors. </p>
<p> Loglinear interpolation guarantees piecewise constant forward rates. </p>
<p> Rates are assumed to be annual continuos compounding.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>.</p>
<h3><code>Rate</code> compoundForwardImpl (Time, Integer) const [protected]</h3>
<p>Returns the forward rate at a specified compound frequency for the given date calculating it from the zero yield.</p>
<h3><code>Rate</code> zeroYieldImpl (Time) const [protected]</h3>
<p>Returns the zero yield rate for the given date calculating it from the discount. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
