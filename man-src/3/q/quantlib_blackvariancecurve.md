---
title: "quantlib_blackvariancecurve(3)"
name: "quantlib_blackvariancecurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackvariancecurve/"
description: "QuantLib::BlackVarianceCurve – Black volatility curve modelled as variance curve."
---

<p>QuantLib::BlackVarianceCurve &#8211; Black volatility curve modelled as variance curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackvariancecurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVarianceTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackVarianceCurve</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Volatility</code> &gt; &amp;blackVolCurve, const <code>DayCounter</code> &amp;dayCounter, bool forceMonotoneVariance=true) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Modifiers</code> </p>
<p> template&lt;class Interpolator &gt; void <code>setInterpolation</code> (const Interpolator &amp;i=Interpolator()) </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>virtual Real <code>blackVarianceImpl</code> (Time t, Real) const<br />
 <i>Black variance calculation. </i></p>
<h2>Detailed Description</h2>
<p>Black volatility curve modelled as variance curve. </p>
<p> This class calculates time-dependent Black volatilities using as input a vector of (ATM) Black volatilities observed in the market. </p>
<p> The calculation is performed interpolating on the variance curve. <code>Linear</code> interpolation is used as default; this can be changed by the setInterpolation() method. </p>
<p> For strike dependence, see <code>BlackVarianceSurface</code>. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check time extrapolation</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
