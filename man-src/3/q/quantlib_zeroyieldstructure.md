---
title: "quantlib_zeroyieldstructure(3)"
name: "quantlib_zeroyieldstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_zeroyieldstructure/"
description: "QuantLib::ZeroYieldStructure – Zero-yield term structure."
---

<p>QuantLib::ZeroYieldStructure &#8211; Zero-yield term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/zeroyieldstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::YieldTermStructure</code>. </p>
<p> Inherited by <code>DriftTermStructure</code>, <code>InterpolatedZeroCurve&lt; Interpolator &gt;</code>, <code>PiecewiseZeroSpreadedTermStructure</code>, <code>QuantoTermStructure</code>, and <code>ZeroSpreadedTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>ZeroYieldStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>()) </p>
<p> <code>ZeroYieldStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>()) </p>
<p> <code>ZeroYieldStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>()) </p>
<h3>Protected Member Functions</h3>
<p><code>YieldTermStructure implementation</code> </p>
<p> <code>DiscountFactor</code> <code>discountImpl</code> (Time) const </p>
<p> virtual <code>Rate</code> <code>zeroYieldImpl</code> (Time) const =0<br />
 <i>zero-yield calculation </i></p>
<h2>Detailed Description</h2>
<p>Zero-yield term structure. </p>
<p> This abstract class acts as an adapter to <code>YieldTermStructure</code> allowing the programmer to implement only the zeroYieldImpl(Time, bool) method in derived classes. <code>Discount</code> and forward are calculated from zero yields. </p>
<p> Rates are assumed to be annual continuous compounding.</p>
<h2>Member Function Documentation</h2>
<h3><code>DiscountFactor</code> discountImpl (Time t) const [protected, virtual]</h3>
<p>Returns the discount factor for the given date calculating it from the zero yield. </p>
<p> Implements <code>YieldTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
