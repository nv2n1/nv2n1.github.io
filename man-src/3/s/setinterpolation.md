---
title: "setinterpolation(3)"
name: "setinterpolation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setinterpolation/"
description: "QuantLib::ExtendedBlackVarianceCurve – Black volatility curve modelled as variance curve."
---

<p>QuantLib::ExtendedBlackVarianceCurve &#8211; Black volatility curve modelled as variance curve. </p>
<h2>Synopsis</h2>
<pre><code>ExtendedBlackVarianceCurve (const Date &amp;referenceDate, const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Handle&lt; Quote &gt; &gt; &amp;volatilities, const DayCounter &amp;dayCounter, bool forceMonotoneVariance=true)



DayCounter dayCounter () const


the day counter used for date/time conversion


Date maxDate () const


the latest date for which the curve can return values


Real minStrike () const


the minimum strike for which the term structure can return vols


Real maxStrike () const


the maximum strike for which the term structure can return vols


template&lt;class Interpolator &gt; void setInterpolation (const Interpolator &amp;i=Interpolator())



void accept (AcyclicVisitor &amp;)



void update ()</code></pre>
<p> Inherits <code>QuantLib::BlackVarianceTermStructure</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ExtendedBlackVarianceCurve (const Date &amp;referenceDate, const std::vector&lt; Date &gt; &amp;dates, const std::vector&lt; Handle&lt; Quote &gt; &gt; &amp;volatilities, const DayCounter &amp;dayCounter, bool forceMonotoneVariance=true)



DayCounter dayCounter () const


the day counter used for date/time conversion


Date maxDate () const


the latest date for which the curve can return values


Real minStrike () const


the minimum strike for which the term structure can return vols


Real maxStrike () const


the maximum strike for which the term structure can return vols


template&lt;class Interpolator &gt; void setInterpolation (const Interpolator &amp;i=Interpolator())



void accept (AcyclicVisitor &amp;)



void update ()</code></pre>
<h2>Detailed Description</h2>
<p>Black volatility curve modelled as variance curve. </p>
<p> This class is similar to <code>BlackVarianceCurve</code>, but extends it to use quotes for the input volatilities.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
