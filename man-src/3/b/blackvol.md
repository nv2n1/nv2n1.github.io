---
title: "blackvol(3)"
name: "blackvol"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackvol/"
description: "QuantLib::BlackVolTermStructure – Black-volatility term structure."
---

<p>QuantLib::BlackVolTermStructure &#8211; Black-volatility term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackvoltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>BlackVarianceTermStructure</code>, and <code>BlackVolatilityTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>BlackVolTermStructure</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>BlackVolTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>BlackVolTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Black Volatility</code> </p>
<p> <code>Volatility</code> <code>blackVol</code> (const <code>Date</code> &amp;maturity, Real strike, bool extrapolate=false) const<br />
 <i>spot volatility </i><br />
 <code>Volatility</code> <code>blackVol</code> (Time maturity, Real strike, bool extrapolate=false) const<br />
 <i>spot volatility </i><br />
 Real <code>blackVariance</code> (const <code>Date</code> &amp;maturity, Real strike, bool extrapolate=false) const<br />
 <i>spot variance </i><br />
 Real <code>blackVariance</code> (Time maturity, Real strike, bool extrapolate=false) const<br />
 <i>spot variance </i><br />
 <code>Volatility</code> <code>blackForwardVol</code> (const <code>Date</code> &amp;date1, const <code>Date</code> &amp;date2, Real strike, bool extrapolate=false) const<br />
 <i>forward (at-the-money) volatility </i><br />
 <code>Volatility</code> <code>blackForwardVol</code> (Time time1, Time time2, Real strike, bool extrapolate=false) const<br />
 <i>forward (at-the-money) volatility </i><br />
 Real <code>blackForwardVariance</code> (const <code>Date</code> &amp;date1, const <code>Date</code> &amp;date2, Real strike, bool extrapolate=false) const<br />
 <i>forward (at-the-money) variance </i><br />
 Real <code>blackForwardVariance</code> (Time time1, Time time2, Real strike, bool extrapolate=false) const<br />
 <i>forward (at-the-money) variance </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>Calculations</code><br />
 These methods must be implemented in derived classes to perform the actual volatility calculations. When they are called, range check has already been performed; therefore, they must assume that extrapolation is required. </p>
<p> virtual Real <code>blackVarianceImpl</code> (Time t, Real strike) const =0<br />
 <i>Black variance calculation. </i><br />
 virtual <code>Volatility</code> <code>blackVolImpl</code> (Time t, Real strike) const =0<br />
 <i>Black volatility calculation. </i></p>
<h2>Detailed Description</h2>
<p>Black-volatility term structure. </p>
<p> This abstract class defines the interface of concrete Black-volatility term structures which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BlackVolTermStructure</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
