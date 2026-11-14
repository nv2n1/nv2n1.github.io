---
title: "quantlib_piecewiseyoyinflationcurve(3)"
name: "quantlib_piecewiseyoyinflationcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_piecewiseyoyinflationcurve/"
description: "QuantLib::PiecewiseYoYInflationCurve – Piecewise year-on-year inflation term structure."
---

<p>QuantLib::PiecewiseYoYInflationCurve &#8211; Piecewise year-on-year inflation term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/inflation/piecewiseyoyinflationcurve.hpp&gt; </p>
<p> Inherits <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Types</h3>
<p>typedef Traits <code>traits_type</code> </p>
<p> typedef Interpolator <code>interpolator_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>PiecewiseYoYInflationCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Period</code> &amp;lag, <code>Frequency</code> frequency, Rate baseYoYRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;nominalTS, const std::vector&lt; boost::shared_ptr&lt; typename Traits::helper &gt; &gt; &amp;instruments, <code>Real</code> accuracy=1.0e-12, const Interpolator &amp;i=Interpolator()) </p>
<p> <code>Inflation interface</code> </p>
<p> <code>Date</code> <code>baseDate</code> () const<br />
 <i>minimum (base) date </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>Inspectors</code> </p>
<p> const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>data</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Real</code> &gt; &gt; <code>nodes</code> () const </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Friends</h3>
<p>class <code>Bootstrap&lt; this_curve &gt;</code> </p>
<p> class <code>BootstrapError&lt; this_curve &gt;</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator, template&lt; class &gt; class Bootstrap = IterativeBootstrap, class Traits = YoYInflationTraits&gt; class QuantLib::PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</h3>
<p>Piecewise year-on-year inflation term structure.</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> baseDate () const [virtual]</h3>
<p>minimum (base) date </p>
<p> Important in inflation since it starts before nominal reference date. </p>
<p> Reimplemented from <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
