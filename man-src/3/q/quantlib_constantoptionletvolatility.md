---
title: "quantlib_constantoptionletvolatility(3)"
name: "quantlib_constantoptionletvolatility"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_constantoptionletvolatility/"
description: "QuantLib::ConstantOptionletVolatility – Constant caplet volatility, no time-strike dependence."
---

<p>QuantLib::ConstantOptionletVolatility &#8211; Constant caplet volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/constantoptionletvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::OptionletVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ConstantOptionletVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, floating market data </i><br />
 <code>ConstantOptionletVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>fixed reference date, floating market data </i><br />
 <code>ConstantOptionletVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, fixed market data </i><br />
 <code>ConstantOptionletVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
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
<p>boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (const <code>Date</code> &amp;d) const </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time) const<br />
 <i>implements the actual smile calculation in derived classes </i><br />
 <code>Volatility</code> <code>volatilityImpl</code> (Time, Rate) const<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Constant caplet volatility, no time-strike dependence. </p>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
