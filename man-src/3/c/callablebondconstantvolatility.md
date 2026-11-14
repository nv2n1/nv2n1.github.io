---
title: "callablebondconstantvolatility(3)"
name: "callablebondconstantvolatility"
section: "3"
letter: "c"
url: "/docs/linux/man/3-callablebondconstantvolatility/"
description: "QuantLib::CallableBondConstantVolatility – Constant callable-bond volatility, no time-strike dependence."
---

<p>QuantLib::CallableBondConstantVolatility &#8211; Constant callable-bond volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/callablebondconstantvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::CallableBondVolatilityStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CallableBondConstantVolatility</code> (const <code>Date</code> &amp;referenceDate, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (const <code>Date</code> &amp;referenceDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>Volatility</code> volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>CallableBondConstantVolatility</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h3>CallableBondConstantVolatility interface</h3>
<p>const <code>Period</code> &amp; <code>maxBondTenor</code> () const<br />
 <i>the largest length for which the term structure can return vols </i><br />
 Time <code>maxBondLength</code> () const<br />
 <i>the largest bondLength for which the term structure can return vols </i><br />
 <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i><br />
 <code>Volatility</code> <code>volatilityImpl</code> (Time, Time, Rate) const<br />
 <i>implements the actual volatility calculation in derived classes </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time optionTime, Time bondLength) const<br />
 <i>return smile section </i><br />
 <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;, const <code>Period</code> &amp;, Rate) const </p>
<h2>Detailed Description</h2>
<p>Constant callable-bond volatility, no time-strike dependence. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
