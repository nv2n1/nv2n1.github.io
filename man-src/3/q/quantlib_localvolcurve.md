---
title: "quantlib_localvolcurve(3)"
name: "quantlib_localvolcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_localvolcurve/"
description: "QuantLib::LocalVolCurve – Local volatility curve derived from a Black curve."
---

<p>QuantLib::LocalVolCurve &#8211; Local volatility curve derived from a Black curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/localvolcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::LocalVolTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LocalVolCurve</code> (const <code>Handle</code>&lt; <code>BlackVarianceCurve</code> &gt; &amp;curve) </p>
<p> <code>TermStructure interface</code> </p>
<p> const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>Volatility</code> <code>localVolImpl</code> (Time, Real) const </p>
<h2>Detailed Description</h2>
<p>Local volatility curve derived from a Black curve.</p>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> localVolImpl (Time t, Real dummy) const [protected, virtual]</h3>
<p>The relation [ int_0^T igma_L^2(t)dt = igma_B^2 T ] holds, where $ igma_L(t) $ is the local volatility at time $ t $ and $ igma_B(T) $ is the Black volatility for maturity $ T $. From the above, the formula [ igma_L(t) = qrt{ac{mathrm{d}}{mathrm{d}t}igma_B^2(t)t} ] can be deduced which is here implemented. </p>
<p> Implements <code>LocalVolTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
