---
title: "volatilityimpl(3)"
name: "volatilityimpl"
section: "3"
letter: "v"
url: "/docs/linux/man/3-volatilityimpl/"
description: "QuantLib::CallableBondConstantVolatility – Constant callable-bond volatility, no time-strike dependence."
---

<p>QuantLib::CallableBondConstantVolatility &#8211; Constant callable-bond volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<pre><code>DayCounter dayCounter () const


the day counter used for date/time conversion


Date maxDate () const


the latest date for which the curve can return values




CallableBondConstantVolatility interface
const Period &amp; maxBondTenor () const


the largest length for which the term structure can return vols


Time maxBondLength () const


the largest bondLength for which the term structure can return vols


Real minStrike () const


the minimum strike for which the term structure can return vols


Real maxStrike () const


the maximum strike for which the term structure can return vols


Volatility volatilityImpl (Time, Time, Rate) const


implements the actual volatility calculation in derived classes


boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const


return smile section


Volatility volatilityImpl (const Date &amp;, const Period &amp;, Rate) const</code></pre>
<p> Inherits <code>QuantLib::CallableBondVolatilityStructure</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CallableBondConstantVolatility</code> (const <code>Date</code> &amp;referenceDate, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter)<br />
 <code>TermStructure interface</code> </p>
<pre><code>DayCounter dayCounter () const


the day counter used for date/time conversion


Date maxDate () const


the latest date for which the curve can return values




CallableBondConstantVolatility interface
const Period &amp; maxBondTenor () const


the largest length for which the term structure can return vols


Time maxBondLength () const


the largest bondLength for which the term structure can return vols


Real minStrike () const


the minimum strike for which the term structure can return vols


Real maxStrike () const


the maximum strike for which the term structure can return vols


Volatility volatilityImpl (Time, Time, Rate) const


implements the actual volatility calculation in derived classes


boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const


return smile section


Volatility volatilityImpl (const Date &amp;, const Period &amp;, Rate) const</code></pre>
<h2>Detailed Description</h2>
<p>Constant callable-bond volatility, no time-strike dependence.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
