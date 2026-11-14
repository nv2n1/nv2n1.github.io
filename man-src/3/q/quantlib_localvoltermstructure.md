---
title: "quantlib_localvoltermstructure(3)"
name: "quantlib_localvoltermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_localvoltermstructure/"
description: "QuantLib::LocalVolTermStructure –"
---

<p>QuantLib::LocalVolTermStructure &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/localvoltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>LocalConstantVol</code>, <code>LocalVolCurve</code>, and <code>LocalVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>LocalVolTermStructure</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>LocalVolTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>LocalVolTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Local Volatility</code> </p>
<p> <code>Volatility</code> <code>localVol</code> (const <code>Date</code> &amp;d, Real underlyingLevel, bool extrapolate=false) const </p>
<p> <code>Volatility</code> <code>localVol</code> (Time t, Real underlyingLevel, bool extrapolate=false) const </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>Calculations</code><br />
 These methods must be implemented in derived classes to perform the actual volatility calculations. When they are called, range check has already been performed; therefore, they must assume that extrapolation is required. </p>
<p> virtual <code>Volatility</code> <code>localVolImpl</code> (Time t, Real strike) const =0<br />
 <i>local vol calculation </i></p>
<h2>Detailed Description</h2>
<p>This abstract class defines the interface of concrete local-volatility term structures which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>LocalVolTermStructure</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
