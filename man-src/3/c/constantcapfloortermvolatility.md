---
title: "constantcapfloortermvolatility(3)"
name: "constantcapfloortermvolatility"
section: "3"
letter: "c"
url: "/docs/linux/man/3-constantcapfloortermvolatility/"
description: "QuantLib::ConstantCapFloorTermVolatility – Constant caplet volatility, no time-strike dependence."
---

<p>QuantLib::ConstantCapFloorTermVolatility &#8211; Constant caplet volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/capfloor/constantcapfloortermvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::CapFloorTermVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ConstantCapFloorTermVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, floating market data </i><br />
 <code>ConstantCapFloorTermVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>fixed reference date, floating market data </i><br />
 <code>ConstantCapFloorTermVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, fixed market data </i><br />
 <code>ConstantCapFloorTermVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>fixed reference date, fixed market data </i> </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i></p>
<h3>Protected Member Functions</h3>
<p><code>Volatility</code> <code>volatilityImpl</code> (Time, Rate) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Constant caplet volatility, no time-strike dependence. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
