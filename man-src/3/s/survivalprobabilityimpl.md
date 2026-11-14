---
title: "survivalprobabilityimpl(3)"
name: "survivalprobabilityimpl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-survivalprobabilityimpl/"
description: "QuantLib::DefaultDensityStructure – default-density adapter for default-probability term structures"
---

<p>QuantLib::DefaultDensityStructure &#8211; default-density adapter for default-probability term structures </p>
<h2>Synopsis</h2>
<pre><code>DefaultDensityStructure (const DayCounter &amp;dc=DayCounter())


default constructor


DefaultDensityStructure (const Date &amp;referenceDate, const Calendar &amp;cal=Calendar(), const DayCounter &amp;dc=DayCounter())


initialize with a fixed reference date


DefaultDensityStructure (Natural settlementDays, const Calendar &amp;cal, const DayCounter &amp;dc=DayCounter())


calculate the reference date based on the global evaluation date




Protected Member Functions
Probability survivalProbabilityImpl (Time) const


probability of survival between today (t = 0) and a given time


Real hazardRateImpl (Time) const


instantaneous hazard rate at a given time</code></pre>
<p> Inherits <code>QuantLib::DefaultProbabilityTermStructure</code>. Inherited by <code>InterpolatedDefaultDensityCurve&lt; Interpolator &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<pre><code>DefaultDensityStructure (const DayCounter &amp;dc=DayCounter())


default constructor


DefaultDensityStructure (const Date &amp;referenceDate, const Calendar &amp;cal=Calendar(), const DayCounter &amp;dc=DayCounter())


initialize with a fixed reference date


DefaultDensityStructure (Natural settlementDays, const Calendar &amp;cal, const DayCounter &amp;dc=DayCounter())


calculate the reference date based on the global evaluation date




Protected Member Functions
Probability survivalProbabilityImpl (Time) const


probability of survival between today (t = 0) and a given time


Real hazardRateImpl (Time) const


instantaneous hazard rate at a given time</code></pre>
<h2>Detailed Description</h2>
<p>default-density adapter for default-probability term structures</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>DefaultDensityStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>Probability survivalProbabilityImpl (Time) const [protected, virtual]</h3>
<p>probability of survival between today (t = 0) and a given time </p>
<p> implemented in terms of the default density $ p(t) $ as [ S(t) = 1 &#8211; int_0^t p( au) d au. ] </p>
<p> <code>Note:</code></p>
<dl>
<dd>This implementation uses numerical integration. Derived classes should override it if a more efficient formula is available.</dl>
<p> Implements <code>DefaultProbabilityTermStructure</code>. </p>
<p> Reimplemented in <code>InterpolatedDefaultDensityCurve&lt; Interpolator &gt;</code>.</p>
<h3><code>Real</code> hazardRateImpl (Time) const [protected, virtual]</h3>
<p>instantaneous hazard rate at a given time </p>
<p> implemented in terms of the default density $ p(t) $ and the survival probability $ S(t) $ as $ h(t) = p(t)/S(t). $ </p>
<p> Implements <code>DefaultProbabilityTermStructure</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
