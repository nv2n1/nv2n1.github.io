---
title: "quantlib_abcdatmvolcurve(3)"
name: "quantlib_abcdatmvolcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_abcdatmvolcurve/"
description: "QuantLib::AbcdAtmVolCurve – Abcd-interpolated at-the-money (no-smile) volatility curve."
---

<p>QuantLib::AbcdAtmVolCurve &#8211; Abcd-interpolated at-the-money (no-smile) volatility curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/abcdatmvolcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackAtmVolCurve</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AbcdAtmVolCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;volsHandles, const std::vector&lt; bool &gt; inclusionInInterpolationFlag=std::vector&lt; bool &gt;(1, true), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>())<br />
 <i>floating reference date, floating market data </i><br />
 std::vector&lt; <code>Real</code> &gt; <code>k</code> () const<br />
 <i>Returns k adjustment factors for option tenors used in interpolation. </i><br />
 <code>Real</code> <code>k</code> (Time t) const<br />
 <i>Returns k adjustment factor at time t. </i><br />
 <code>Real</code> <code>a</code> () const </p>
<p> <code>Real</code> <code>b</code> () const </p>
<p> <code>Real</code> <code>c</code> () const </p>
<p> <code>Real</code> <code>d</code> () const </p>
<p> <code>Real</code> <code>rmsError</code> () const </p>
<p> <code>Real</code> <code>maxError</code> () const </p>
<p> EndCriteria::Type <code>endCriteria</code> () const </p>
<p> <code>TermStructure interface</code> </p>
<p> virtual <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>update</code> () </p>
<p> void <code>performCalculations</code> () const </p>
<p> <code>some inspectors</code> </p>
<p> const std::vector&lt; <code>Period</code> &gt; &amp; <code>optionTenors</code> () const </p>
<p> const std::vector&lt; <code>Period</code> &gt; &amp; <code>optionTenorsInInterpolation</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>optionDates</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>optionTimes</code> () const </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>BlackAtmVolCurve interface</code> </p>
<p> virtual <code>Real</code> <code>atmVarianceImpl</code> (Time t) const<br />
 <i>spot at-the-money variance calculation (k adjusted) </i><br />
 virtual <code>Volatility</code> <code>atmVolImpl</code> (Time t) const<br />
 <i>spot at-the-money volatility calculation (k adjusted) </i></p>
<h2>Detailed Description</h2>
<p>Abcd-interpolated at-the-money (no-smile) volatility curve. </p>
<p> blah blah</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
