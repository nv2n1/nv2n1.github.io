---
title: "quantlib_blackvariancesurface(3)"
name: "quantlib_blackvariancesurface"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackvariancesurface/"
description: "QuantLib::BlackVarianceSurface – Black volatility surface modelled as variance surface."
---

<p>QuantLib::BlackVarianceSurface &#8211; Black volatility surface modelled as variance surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackvariancesurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVarianceTermStructure</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Extrapolation</code> { <code>ConstantExtrapolation</code>, <code>InterpolatorDefaultExtrapolation</code> } </p>
<h3>Public Member Functions</h3>
<p><code>BlackVarianceSurface</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; Real &gt; &amp;strikes, const <code>Matrix</code> &amp;blackVolMatrix, const <code>DayCounter</code> &amp;dayCounter, Extrapolation lowerExtrapolation=InterpolatorDefaultExtrapolation, Extrapolation upperExtrapolation=InterpolatorDefaultExtrapolation) </p>
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
<p>virtual Real <code>blackVarianceImpl</code> (Time t, Real strike) const<br />
 <i>Black variance calculation. </i></p>
<h2>Detailed Description</h2>
<p>Black volatility surface modelled as variance surface. </p>
<p> This class calculates time/strike dependent Black volatilities using as input a matrix of Black volatilities observed in the market. </p>
<p> The calculation is performed interpolating on the variance surface. <code>Bilinear</code> interpolation is used as default; this can be changed by the setInterpolation() method. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check time extrapolation</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
