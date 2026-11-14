---
title: "atmforwardvariance(3)"
name: "atmforwardvariance"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atmforwardvariance/"
description: "QuantLib::EquityFXVolSurface – Equity/FX volatility (smile) surface."
---

<p>QuantLib::EquityFXVolSurface &#8211; Equity/FX volatility (smile) surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/equityfxvolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>EquityFXVolSurface</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>EquityFXVolSurface</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>EquityFXVolSurface</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Black Volatility</code> </p>
<p> <code>Volatility</code> <code>atmForwardVol</code> (const <code>Date</code> &amp;date1, const <code>Date</code> &amp;date2, bool extrapolate=false) const<br />
 <i>forward (at-the-money) volatility </i><br />
 <code>Volatility</code> <code>atmForwardVol</code> (<code>Time</code> time1, <code>Time</code> time2, bool extrapolate=false) const<br />
 <i>forward (at-the-money) volatility </i><br />
 <code>Real</code> <code>atmForwardVariance</code> (const <code>Date</code> &amp;date1, const <code>Date</code> &amp;date2, bool extrapolate=false) const<br />
 <i>forward (at-the-money) variance </i><br />
 <code>Real</code> <code>atmForwardVariance</code> (<code>Time</code> time1, <code>Time</code> time2, bool extrapolate=false) const<br />
 <i>forward (at-the-money) variance </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Equity/FX volatility (smile) surface. </p>
<p> This abstract class defines the interface of concrete Equity/FX volatility (smile) surfaces which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis. </p>
<p> It&#8217;s only in absence of smile that the concept of (at-the-money) forward volatility makes sense.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>EquityFXVolSurface</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
