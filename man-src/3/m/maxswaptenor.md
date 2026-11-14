---
title: "maxswaptenor(3)"
name: "maxswaptenor"
section: "3"
letter: "m"
url: "/docs/linux/man/3-maxswaptenor/"
description: "QuantLib::ConstantSwaptionVolatility – Constant swaption volatility, no time-strike dependence."
---

<p>QuantLib::ConstantSwaptionVolatility &#8211; Constant swaption volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/swaption/swaptionconstantvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwaptionVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ConstantSwaptionVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, floating market data </i><br />
 <code>ConstantSwaptionVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>fixed reference date, floating market data </i><br />
 <code>ConstantSwaptionVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>floating reference date, fixed market data </i><br />
 <code>ConstantSwaptionVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dc)<br />
 <i>fixed reference date, fixed market data </i> </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>SwaptionVolatilityStructure interface</code> </p>
<p> const <code>Period</code> &amp; <code>maxSwapTenor</code> () const<br />
 <i>the largest length for which the term structure can return vols </i></p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (const <code>Date</code> &amp;, const <code>Period</code> &amp;) const </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time, Time) const </p>
<p> <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;, const <code>Period</code> &amp;, Rate) const </p>
<p> <code>Volatility</code> <code>volatilityImpl</code> (Time, Time, Rate) const </p>
<h2>Detailed Description</h2>
<p>Constant swaption volatility, no time-strike dependence. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
