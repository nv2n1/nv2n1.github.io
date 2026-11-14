---
title: "defaultdensity(3)"
name: "defaultdensity"
section: "3"
letter: "d"
url: "/docs/linux/man/3-defaultdensity/"
description: "QuantLib::DefaultProbabilityTermStructure – default probability term structure"
---

<p>QuantLib::DefaultProbabilityTermStructure &#8211; default probability term structure </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/defaulttermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructure</code>. </p>
<p> Inherited by <code>DefaultDensityStructure</code>, and <code>HazardRateStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>DefaultProbabilityTermStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>DefaultProbabilityTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>DefaultProbabilityTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Default probability</code> </p>
<p> Probability <code>defaultProbability</code> (const <code>Date</code> &amp;, bool extrapolate=false) const<br />
 <i>probability of default between today and a given date </i><br />
 Probability <code>defaultProbability</code> (Time, bool extrapolate=false) const<br />
 <i>probability of default between today (t = 0) and a given time </i><br />
 Probability <code>defaultProbability</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;, bool extrapolate=false) const<br />
 <i>probability of default between two given dates </i><br />
 Probability <code>defaultProbability</code> (Time, Time, bool extrapolate=false) const<br />
 <i>probability of default between two given times </i> </p>
<p> <code>Survival probability</code> </p>
<p> Probability <code>survivalProbability</code> (const <code>Date</code> &amp;, bool extrapolate=false) const<br />
 <i>probability of survival between today and a given date </i><br />
 Probability <code>survivalProbability</code> (Time, bool extrapolate=false) const<br />
 <i>probability of default between today (t = 0) and a given time </i> </p>
<p> <code>Default density</code> </p>
<p> <code>Real</code> <code>defaultDensity</code> (const <code>Date</code> &amp;, bool extrapolate=false) const<br />
 <i>default density at a given date </i><br />
 <code>Real</code> <code>defaultDensity</code> (Time, bool extrapolate=false) const<br />
 <i>default density at a given time </i> </p>
<p> <code>Hazard rate</code> </p>
<p> <code>Real</code> <code>hazardRate</code> (const <code>Date</code> &amp;, bool extrapolate=false) const<br />
 <i>hazard rate at a given date </i><br />
 <code>Real</code> <code>hazardRate</code> (Time, bool extrapolate=false) const<br />
 <i>hazard rate at a given time </i></p>
<h3>Protected Member Functions</h3>
<p>virtual Probability <code>survivalProbabilityImpl</code> (Time) const =0<br />
 <i>probability of survival between today (t = 0) and a given time </i><br />
 virtual <code>Real</code> <code>defaultDensityImpl</code> (Time) const =0<br />
 <i>instantaneous default density at a given time </i><br />
 virtual <code>Real</code> <code>hazardRateImpl</code> (Time) const =0<br />
 <i>instantaneous hazard rate at a given time </i></p>
<h2>Detailed Description</h2>
<p>default probability term structure</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>DefaultProbabilityTermStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
