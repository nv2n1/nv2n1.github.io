---
title: "survivalprobability(3)"
name: "survivalprobability"
section: "3"
letter: "s"
url: "/docs/linux/man/3-survivalprobability/"
description: "QuantLib::DefaultProbabilityTermStructure – default probability term structure"
---

<p>QuantLib::DefaultProbabilityTermStructure &#8211; default probability term structure </p>
<h2>Synopsis</h2>
<pre><code>Real hazardRate (const Date &amp;, bool extrapolate=false) const


hazard rate at a given date


Real hazardRate (Time, bool extrapolate=false) const


hazard rate at a given time




Protected Member Functions
virtual Probability survivalProbabilityImpl (Time) const =0


probability of survival between today (t = 0) and a given time


virtual Real defaultDensityImpl (Time) const =0


instantaneous default density at a given time


virtual Real hazardRateImpl (Time) const =0


instantaneous hazard rate at a given time</code></pre>
<p> Inherits <code>QuantLib::TermStructure</code>. Inherited by <code>DefaultDensityStructure</code>, and <code>HazardRateStructure</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. Real hazardRate (const Date &amp;, bool extrapolate=false) const</p>
<p>hazard rate at a given date</p>
<p>Real hazardRate (Time, bool extrapolate=false) const</p>
<p>hazard rate at a given time</p>
<p>Protected Member Functions<br />
virtual Probability survivalProbabilityImpl (Time) const =0</p>
<p>probability of survival between today (t = 0) and a given time</p>
<p>virtual Real defaultDensityImpl (Time) const =0</p>
<p>instantaneous default density at a given time</p>
<p>virtual Real hazardRateImpl (Time) const =0</p>
<p>instantaneous hazard rate at a given time <code>Default probability</code><br />
 Real hazardRate (const Date &amp;, bool extrapolate=false) const</p>
<p>hazard rate at a given date</p>
<p>Real hazardRate (Time, bool extrapolate=false) const</p>
<p>hazard rate at a given time</p>
<p>Protected Member Functions<br />
virtual Probability survivalProbabilityImpl (Time) const =0</p>
<p>probability of survival between today (t = 0) and a given time</p>
<p>virtual Real defaultDensityImpl (Time) const =0</p>
<p>instantaneous default density at a given time</p>
<p>virtual Real hazardRateImpl (Time) const =0</p>
<p>instantaneous hazard rate at a given time <code>Survival probability</code><br />
 Real hazardRate (const Date &amp;, bool extrapolate=false) const</p>
<p>hazard rate at a given date</p>
<p>Real hazardRate (Time, bool extrapolate=false) const</p>
<p>hazard rate at a given time</p>
<p>Protected Member Functions<br />
virtual Probability survivalProbabilityImpl (Time) const =0</p>
<p>probability of survival between today (t = 0) and a given time</p>
<p>virtual Real defaultDensityImpl (Time) const =0</p>
<p>instantaneous default density at a given time</p>
<p>virtual Real hazardRateImpl (Time) const =0</p>
<p>instantaneous hazard rate at a given time <code>Default density</code><br />
 Real hazardRate (const Date &amp;, bool extrapolate=false) const</p>
<p>hazard rate at a given date</p>
<p>Real hazardRate (Time, bool extrapolate=false) const</p>
<p>hazard rate at a given time</p>
<p>Protected Member Functions<br />
virtual Probability survivalProbabilityImpl (Time) const =0</p>
<p>probability of survival between today (t = 0) and a given time</p>
<p>virtual Real defaultDensityImpl (Time) const =0</p>
<p>instantaneous default density at a given time</p>
<p>virtual Real hazardRateImpl (Time) const =0</p>
<p>instantaneous hazard rate at a given time <code>Hazard rate</code> </p>
<pre><code>Real hazardRate (const Date &amp;, bool extrapolate=false) const


hazard rate at a given date


Real hazardRate (Time, bool extrapolate=false) const


hazard rate at a given time




Protected Member Functions
virtual Probability survivalProbabilityImpl (Time) const =0


probability of survival between today (t = 0) and a given time


virtual Real defaultDensityImpl (Time) const =0


instantaneous default density at a given time


virtual Real hazardRateImpl (Time) const =0


instantaneous hazard rate at a given time</code></pre>
<h2>Detailed Description</h2>
<p>default probability term structure</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>DefaultProbabilityTermStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
