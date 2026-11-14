---
title: "nominaltermstructure(3)"
name: "nominaltermstructure"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nominaltermstructure/"
description: "QuantLib::InflationTermStructure – Interface for inflation term structures."
---

<p>QuantLib::InflationTermStructure &#8211; Interface for inflation term structures. </p>
<h2>Synopsis</h2>
<pre><code>virtual Period lag () const



virtual Frequency frequency () const



virtual Rate baseRate () const



virtual Handle&lt; YieldTermStructure &gt; nominalTermStructure () const



virtual Date baseDate () const =0


minimum (base) date




Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::TermStructure</code>. Inherited by <code>YoYInflationTermStructure</code>, and <code>ZeroInflationTermStructure</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 virtual Period lag () const</p>
<p>virtual Frequency frequency () const</p>
<p>virtual Rate baseRate () const</p>
<p>virtual Handle&lt; YieldTermStructure &gt; nominalTermStructure () const</p>
<p>virtual Date baseDate () const =0</p>
<p>minimum (base) date</p>
<p>Protected Member Functions <code>Inflation interface</code> </p>
<pre><code>virtual Period lag () const



virtual Frequency frequency () const



virtual Rate baseRate () const



virtual Handle&lt; YieldTermStructure &gt; nominalTermStructure () const



virtual Date baseDate () const =0


minimum (base) date




Protected Member Functions</code></pre>
<p> virtual void <code>setBaseRate</code> (const <code>Rate</code> &amp;r) </p>
<p> void <code>checkRange</code> (const <code>Date</code> &amp;, bool extrapolate) const<br />
 <i>date-range check </i><br />
 void <code>checkRange</code> (Time t, bool extrapolate) const<br />
 <i>time-range check </i></p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>nominalTermStructure_</code> </p>
<p> <code>Period</code> <code>lag_</code> </p>
<p> <code>Frequency</code> <code>frequency_</code> </p>
<p> <code>Rate</code> <code>baseRate_</code></p>
<h2>Detailed Description</h2>
<p>Interface for inflation term structures.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Date</code> baseDate () const [pure virtual]</h3>
<p>minimum (base) date </p>
<p> Important in inflation since it starts before nominal reference date. </p>
<p> Implemented in <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>InterpolatedYoYInflationCurve&lt; Interpolator &gt;</code>, and <code>InterpolatedZeroInflationCurve&lt; Interpolator &gt;</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
