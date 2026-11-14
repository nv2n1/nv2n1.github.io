---
title: "blackvolatilitytermstructure(3)"
name: "blackvolatilitytermstructure"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackvolatilitytermstructure/"
description: "QuantLib::BlackVolatilityTermStructure – Black-volatility term structure."
---

<p>QuantLib::BlackVolatilityTermStructure &#8211; Black-volatility term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackvoltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVolTermStructure</code>. </p>
<p> Inherited by <code>BlackConstantVol</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>BlackVolatilityTermStructure</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>BlackVolatilityTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>BlackVolatilityTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>Real <code>blackVarianceImpl</code> (Time maturity, Real strike) const </p>
<h2>Detailed Description</h2>
<p>Black-volatility term structure. </p>
<p> This abstract class acts as an adapter to <code>BlackVolTermStructure</code> allowing the programmer to implement only the blackVolImpl(Time, Real, bool) method in derived classes. </p>
<p> Volatility are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BlackVolatilityTermStructure</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3>Real blackVarianceImpl (Time maturity, Real strike) const [protected, virtual]</h3>
<p>Returns the variance for the given strike and date calculating it from the volatility. </p>
<p> Implements <code>BlackVolTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
