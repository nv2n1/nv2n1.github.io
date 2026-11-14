---
title: "varianceimpl(3)"
name: "varianceimpl"
section: "3"
letter: "v"
url: "/docs/linux/man/3-varianceimpl/"
description: "QuantLib::SmileSection – interest rate volatility smile section"
---

<p>QuantLib::SmileSection &#8211; interest rate volatility smile section </p>
<h2>Synopsis</h2>
<pre><code>SmileSection (const Date &amp;d, const DayCounter &amp;dc=DayCounter(), const Date &amp;referenceDate=Date())



SmileSection (Time exerciseTime, const DayCounter &amp;dc=DayCounter())



virtual void update ()



virtual Real minStrike () const =0



virtual Real maxStrike () const =0



Real variance (Rate strike=Null&lt; Rate &gt;()) const



Volatility volatility (Rate strike=Null&lt; Rate &gt;()) const



virtual Real atmLevel () const =0



const Date &amp; exerciseDate () const



Time exerciseTime () const



const DayCounter &amp; dayCounter () const



void initializeExerciseTime () const



Protected Member Functions
Real varianceImpl (Rate strike) const



virtual Volatility volatilityImpl (Rate strike) const =0



Friends</code></pre>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>. Inherited by FlatSmileSection, InterpolatedSmileSection&lt; Interpolator &gt;, SabrInterpolatedSmileSection, SabrSmileSection, and SpreadedSmileSection.</p>
<h3>Public Member Functions</h3>
<pre><code>SmileSection (const Date &amp;d, const DayCounter &amp;dc=DayCounter(), const Date &amp;referenceDate=Date())



SmileSection (Time exerciseTime, const DayCounter &amp;dc=DayCounter())



virtual void update ()



virtual Real minStrike () const =0



virtual Real maxStrike () const =0



Real variance (Rate strike=Null&lt; Rate &gt;()) const



Volatility volatility (Rate strike=Null&lt; Rate &gt;()) const



virtual Real atmLevel () const =0



const Date &amp; exerciseDate () const



Time exerciseTime () const



const DayCounter &amp; dayCounter () const



void initializeExerciseTime () const



Protected Member Functions
Real varianceImpl (Rate strike) const



virtual Volatility volatilityImpl (Rate strike) const =0



Friends</code></pre>
<p> class <code>SpreadedSmileSection</code></p>
<h2>Detailed Description</h2>
<p>interest rate volatility smile section </p>
<p> This abstract class provides volatility smile section interface</p>
<h2>Member Function Documentation</h2>
<h3>virtual void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
