---
title: "blackatmvolcurve(3)"
name: "blackatmvolcurve"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackatmvolcurve/"
description: "QuantLib::BlackAtmVolCurve – Black at-the-money (no-smile) volatility curve."
---

<p>QuantLib::BlackAtmVolCurve &#8211; Black at-the-money (no-smile) volatility curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/blackatmvolcurve.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>AbcdAtmVolCurve</code>, and <code>BlackVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>BlackAtmVolCurve</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>BlackAtmVolCurve</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>BlackAtmVolCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Black at-the-money spot volatility</code> </p>
<p> <code>Volatility</code> <code>atmVol</code> (const <code>Period</code> &amp;optionTenor, bool extrapolate=false) const<br />
 <i>spot at-the-money volatility </i><br />
 <code>Volatility</code> <code>atmVol</code> (const <code>Date</code> &amp;maturity, bool extrapolate=false) const<br />
 <i>spot at-the-money volatility </i><br />
 <code>Volatility</code> <code>atmVol</code> (Time maturity, bool extrapolate=false) const<br />
 <i>spot at-the-money volatility </i><br />
 <code>Real</code> <code>atmVariance</code> (const <code>Period</code> &amp;optionTenor, bool extrapolate=false) const<br />
 <i>spot at-the-money variance </i><br />
 <code>Real</code> <code>atmVariance</code> (const <code>Date</code> &amp;maturity, bool extrapolate=false) const<br />
 <i>spot at-the-money variance </i><br />
 <code>Real</code> <code>atmVariance</code> (Time maturity, bool extrapolate=false) const<br />
 <i>spot at-the-money variance </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>Calculations</code><br />
 These methods must be implemented in derived classes to perform the actual volatility calculations. When they are called, range check has already been performed; therefore, they must assume that extrapolation is required. </p>
<p> virtual <code>Real</code> <code>atmVarianceImpl</code> (Time t) const =0<br />
 <i>spot at-the-money variance calculation </i><br />
 virtual <code>Volatility</code> <code>atmVolImpl</code> (Time t) const =0<br />
 <i>spot at-the-money volatility calculation </i></p>
<h2>Detailed Description</h2>
<p>Black at-the-money (no-smile) volatility curve. </p>
<p> This abstract class defines the interface of concrete Black at-the-money (no-smile) volatility curves which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BlackAtmVolCurve</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
