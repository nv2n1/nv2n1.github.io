---
title: "exercisedate(3)"
name: "exercisedate"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exercisedate/"
description: "QuantLib::SmileSection – interest rate volatility smile section"
---

<p>QuantLib::SmileSection &#8211; interest rate volatility smile section </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/smilesection.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by FlatSmileSection, InterpolatedSmileSection&lt; Interpolator &gt;, SabrInterpolatedSmileSection, SabrSmileSection, and SpreadedSmileSection. </p>
<h3>Public Member Functions</h3>
<p><code>SmileSection</code> (const <code>Date</code> &amp;d, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>(), const <code>Date</code> &amp;referenceDate=<code>Date</code>()) </p>
<p> <code>SmileSection</code> (<code>Time</code> exerciseTime, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>()) </p>
<p> virtual void <code>update</code> () </p>
<p> virtual Real <code>minStrike</code> () const =0 </p>
<p> virtual Real <code>maxStrike</code> () const =0 </p>
<p> Real <code>variance</code> (Rate strike=<code>Null</code>&lt; Rate &gt;()) const </p>
<p> <code>Volatility</code> <code>volatility</code> (Rate strike=<code>Null</code>&lt; Rate &gt;()) const </p>
<p> virtual Real <code>atmLevel</code> () const =0 </p>
<p> const <code>Date</code> &amp; <code>exerciseDate</code> () const </p>
<p> <code>Time</code> <code>exerciseTime</code> () const </p>
<p> const <code>DayCounter</code> &amp; <code>dayCounter</code> () const </p>
<p> void <code>initializeExerciseTime</code> () const </p>
<h3>Protected Member Functions</h3>
<p>Real <code>varianceImpl</code> (Rate strike) const </p>
<p> virtual <code>Volatility</code> <code>volatilityImpl</code> (Rate strike) const =0 </p>
<h3>Friends</h3>
<p>class <code>SpreadedSmileSection</code> </p>
<h2>Detailed Description</h2>
<p>interest rate volatility smile section </p>
<p> This abstract class provides volatility smile section interface</p>
<h2>Member Function Documentation</h2>
<h3>virtual void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
