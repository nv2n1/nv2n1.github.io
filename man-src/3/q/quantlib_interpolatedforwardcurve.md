---
title: "quantlib_interpolatedforwardcurve(3)"
name: "quantlib_interpolatedforwardcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolatedforwardcurve/"
description: "QuantLib::InterpolatedForwardCurve – Term structure based on interpolation of forward rates."
---

<p>QuantLib::InterpolatedForwardCurve &#8211; Term structure based on interpolation of forward rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/forwardcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::ForwardRateStructure</code>, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>InterpolatedForwardCurve</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Rate</code> &gt; &amp;forwards, const <code>DayCounter</code> &amp;dayCounter, const Interpolator &amp;interpolator=Interpolator()) </p>
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
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>forwards</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Rate</code> &gt; &gt; <code>nodes</code> () const </p>
<p> <code>InterpolatedForwardCurve</code> (const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedForwardCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedForwardCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>Rate</code> <code>forwardImpl</code> (Time t) const<br />
 <i>instantaneous forward-rate calculation </i><br />
 <code>Rate</code> <code>zeroYieldImpl</code> (Time t) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedForwardCurve&lt; Interpolator &gt;</h3>
<p>Term structure based on interpolation of forward rates. </p>
<h2>Member Function Documentation</h2>
<h3><code>Rate</code> zeroYieldImpl (Time t) const [protected, virtual]</h3>
<p>Returns the zero yield rate for the given date calculating it from the instantaneous forward rate. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This is just a default, highly inefficient and possibly wildly inaccurate implementation. Derived classes should implement their own zeroYield method.</dl>
<p> Reimplemented from <code>ForwardRateStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
