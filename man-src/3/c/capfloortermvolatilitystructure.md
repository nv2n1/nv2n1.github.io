---
title: "capfloortermvolatilitystructure(3)"
name: "capfloortermvolatilitystructure"
section: "3"
letter: "c"
url: "/docs/linux/man/3-capfloortermvolatilitystructure/"
description: "QuantLib::CapFloorTermVolatilityStructure – Cap/floor term-volatility structure."
---

<p>QuantLib::CapFloorTermVolatilityStructure &#8211; Cap/floor term-volatility structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/capfloor/capfloortermvolatilitystructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, and <code>ConstantCapFloorTermVolatility</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>CapFloorTermVolatilityStructure</code> (const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>CapFloorTermVolatilityStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>CapFloorTermVolatilityStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Volatility</code> </p>
<p> <code>Volatility</code> <code>volatility</code> (const <code>Period</code> &amp;length, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given cap/floor length and strike rate </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Date</code> &amp;end, Rate strike, bool extrapolate=false) const </p>
<p> <code>Volatility</code> <code>volatility</code> (Time t, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given end time and strike rate </i></p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Volatility</code> <code>volatilityImpl</code> (Time length, Rate strike) const =0<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Cap/floor term-volatility structure. </p>
<p> This class is purely abstract and defines the interface of concrete structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CapFloorTermVolatilityStructure</code> (const <code>Calendar</code> &amp; cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
