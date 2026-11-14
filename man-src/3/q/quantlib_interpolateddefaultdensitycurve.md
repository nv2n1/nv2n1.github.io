---
title: "quantlib_interpolateddefaultdensitycurve(3)"
name: "quantlib_interpolateddefaultdensitycurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolateddefaultdensitycurve/"
description: "QuantLib::InterpolatedDefaultDensityCurve – interpolated default-density curve"
---

<p>QuantLib::InterpolatedDefaultDensityCurve &#8211; interpolated default-density curve </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/interpolateddefaultdensitycurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::DefaultDensityStructure</code>, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>InterpolatedDefaultDensityCurve</code> (const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Real</code> &gt; &amp;densities, const <code>DayCounter</code> &amp;dayCounter, const <code>Calendar</code> &amp;calendar=<code>Calendar</code>(), const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>other inspectors</code> </p>
<p> const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>defaultDensities</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Real</code> &gt; &gt; <code>nodes</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>InterpolatedDefaultDensityCurve</code> (const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedDefaultDensityCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>InterpolatedDefaultDensityCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;, const Interpolator &amp;interpolator=Interpolator()) </p>
<p> <code>Real</code> <code>defaultDensityImpl</code> (Time) const<br />
 <i>instantaneous default density at a given time </i><br />
 Probability <code>survivalProbabilityImpl</code> (Time) const<br />
 <i>probability of survival between today (t = 0) and a given time </i></p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Date</code> &gt; <code>dates_</code> </p>
<p> std::vector&lt; Time &gt; <code>times_</code> </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>data_</code> </p>
<p> <code>Interpolation</code> <code>interpolation_</code> </p>
<p> Interpolator <code>interpolator_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Interpolator&gt; class QuantLib::InterpolatedDefaultDensityCurve&lt; Interpolator &gt;</h3>
<p>interpolated default-density curve</p>
<h2>Member Function Documentation</h2>
<h3>Probability survivalProbabilityImpl (Time) const [protected, virtual]</h3>
<p>probability of survival between today (t = 0) and a given time </p>
<p> implemented in terms of the default density $ p(t) $ as [ S(t) = 1 &#8211; int_0^t p( au) d au. ] </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This implementation uses numerical integration. Derived classes should override it if a more efficient formula is available.</dl>
<p> Reimplemented from <code>DefaultDensityStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
