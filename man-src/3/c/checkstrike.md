---
title: "checkstrike(3)"
name: "checkstrike"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checkstrike/"
description: "QuantLib::VolatilityTermStructure – Volatility term structure."
---

<p>QuantLib::VolatilityTermStructure &#8211; Volatility term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/voltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructure</code>. </p>
<p> Inherited by <code>BlackAtmVolCurve</code>, <code>BlackVolTermStructure</code>, <code>CapFloorTermVolatilityStructure</code>, <code>LocalVolTermStructure</code>, <code>OptionletVolatilityStructure</code>, and <code>SwaptionVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const<br />
 <i>the business day convention used in tenor to date conversion </i><br />
 <code>Date</code> <code>optionDateFromTenor</code> (const <code>Period</code> &amp;) const<br />
 <i>period/date conversion </i><br />
 virtual <code>Rate</code> <code>minStrike</code> () const =0<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 virtual <code>Rate</code> <code>maxStrike</code> () const =0<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>VolatilityTermStructure</code> (const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>VolatilityTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>VolatilityTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>checkStrike</code> (<code>Rate</code> strike, bool extrapolate) const<br />
 <i>strike-range check </i></p>
<h2>Detailed Description</h2>
<p>Volatility term structure. </p>
<p> This abstract class defines the interface of concrete volatility structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>VolatilityTermStructure</code> (const <code>Calendar</code> &amp; cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
