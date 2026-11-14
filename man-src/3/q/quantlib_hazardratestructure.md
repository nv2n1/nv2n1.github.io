---
title: "quantlib_hazardratestructure(3)"
name: "quantlib_hazardratestructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_hazardratestructure/"
description: "QuantLib::HazardRateStructure – hazard-rate adapter for default-probability term structures"
---

<p>QuantLib::HazardRateStructure &#8211; hazard-rate adapter for default-probability term structures </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/hazardratestructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::DefaultProbabilityTermStructure</code>. </p>
<p> Inherited by <code>FlatHazardRate</code>, and <code>InterpolatedHazardRateCurve&lt; Interpolator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>HazardRateStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>HazardRateStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>HazardRateStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i></p>
<h3>Protected Member Functions</h3>
<p>Probability <code>survivalProbabilityImpl</code> (Time) const<br />
 <i>probability of survival between today (t = 0) and a given time </i><br />
 <code>Real</code> <code>defaultDensityImpl</code> (Time) const<br />
 <i>instantaneous default density at a given time </i></p>
<h2>Detailed Description</h2>
<p>hazard-rate adapter for default-probability term structures</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>HazardRateStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>Probability survivalProbabilityImpl (Time) const [protected, virtual]</h3>
<p>probability of survival between today (t = 0) and a given time </p>
<p> implemented in terms of the hazard rate $ h(t) $ as [ S(t) = 
