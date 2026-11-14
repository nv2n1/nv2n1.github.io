---
title: "quantlib_extendedblackvariancecurve(3)"
name: "quantlib_extendedblackvariancecurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedblackvariancecurve/"
description: "QuantLib::ExtendedBlackVarianceCurve – Black volatility curve modelled as variance curve."
---

<p>QuantLib::ExtendedBlackVarianceCurve &#8211; Black volatility curve modelled as variance curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/extendedblackvariancecurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVarianceTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedBlackVarianceCurve</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; <code>Date</code> &gt; &amp;dates, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;volatilities, const <code>DayCounter</code> &amp;dayCounter, bool forceMonotoneVariance=true) </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i><br />
 template&lt;class Interpolator &gt; void <code>setInterpolation</code> (const Interpolator &amp;i=Interpolator()) </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<p> void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p>Black volatility curve modelled as variance curve. </p>
<p> This class is similar to <code>BlackVarianceCurve</code>, but extends it to use quotes for the input volatilities.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
