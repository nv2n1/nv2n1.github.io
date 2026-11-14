---
title: "quantlib_defaultdensitystructure(3)"
name: "quantlib_defaultdensitystructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_defaultdensitystructure/"
description: "QuantLib::DefaultDensityStructure – default-density adapter for default-probability term structures"
---

<p>QuantLib::DefaultDensityStructure &#8211; default-density adapter for default-probability term structures </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/defaultdensitystructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::DefaultProbabilityTermStructure</code>. </p>
<p> Inherited by <code>InterpolatedDefaultDensityCurve&lt; Interpolator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>DefaultDensityStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>DefaultDensityStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>DefaultDensityStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i></p>
<h3>Protected Member Functions</h3>
<p>Probability <code>survivalProbabilityImpl</code> (Time) const<br />
 <i>probability of survival between today (t = 0) and a given time </i><br />
 <code>Real</code> <code>hazardRateImpl</code> (Time) const<br />
 <i>instantaneous hazard rate at a given time </i></p>
<h2>Detailed Description</h2>
<p>default-density adapter for default-probability term structures</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>DefaultDensityStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>Probability survivalProbabilityImpl (Time) const [protected, virtual]</h3>
<p>probability of survival between today (t = 0) and a given time </p>
<p> implemented in terms of the default density $ p(t) $ as [ S(t) = 1 &#8211; int_0^t p( au) d au. ] </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This implementation uses numerical integration. Derived classes should override it if a more efficient formula is available.</dl>
<p> Implements <code>DefaultProbabilityTermStructure</code>. </p>
<p> Reimplemented in <code>InterpolatedDefaultDensityCurve&lt; Interpolator &gt;</code>.</p>
<h3><code>Real</code> hazardRateImpl (Time) const [protected, virtual]</h3>
<p>instantaneous hazard rate at a given time </p>
<p> implemented in terms of the default density $ p(t) $ and the survival probability $ S(t) $ as $ h(t) = p(t)/S(t). $ </p>
<p> Implements <code>DefaultProbabilityTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
