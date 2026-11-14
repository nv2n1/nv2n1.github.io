---
title: "quantlib_callablebondvolatilitystructure(3)"
name: "quantlib_callablebondvolatilitystructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_callablebondvolatilitystructure/"
description: "QuantLib::CallableBondVolatilityStructure – Callable-bond volatility structure."
---

<p>QuantLib::CallableBondVolatilityStructure &#8211; Callable-bond volatility structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/callablebonds/callablebondvolstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::TermStructure</code>. </p>
<p> Inherited by <code>CallableBondConstantVolatility</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual std::pair&lt; Time, Time &gt; <code>convertDates</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor) const<br />
 <i>implements the conversion between dates and times </i><br />
 virtual <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const<br />
 <i>the business day convention used for option date calculation </i><br />
 <code>Date</code> <code>optionDateFromTenor</code> (const <code>Period</code> &amp;optionTenor) const<br />
 <i>implements the conversion between optionTenors and optionDates </i> </p>
<p> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>CallableBondVolatilityStructure</code> (const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>(), <code>BusinessDayConvention</code> bdc=Following)<br />
 <i>default constructor </i><br />
 <code>CallableBondVolatilityStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar=<code>Calendar</code>(), const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>(), <code>BusinessDayConvention</code> bdc=Following)<br />
 <i>initialize with a fixed reference date </i><br />
 <code>CallableBondVolatilityStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>(), <code>BusinessDayConvention</code> bdc=Following)<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Volatility, variance and smile</code> </p>
<p> <code>Volatility</code> <code>volatility</code> (Time optionTime, Time bondLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option time and bondLength </i><br />
 <code>Real</code> <code>blackVariance</code> (Time optionTime, Time bondLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option time and bondLength </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option date and bond tenor </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option date and bond tenor </i><br />
 virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor) const </p>
<p> <code>Volatility</code> <code>volatility</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;bondTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option tenor and bond tenor </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;bondTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option tenor and bond tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;bondTenor) const </p>
<p> <code>Limits</code> </p>
<p> virtual const <code>Period</code> &amp; <code>maxBondTenor</code> () const =0<br />
 <i>the largest length for which the term structure can return vols </i><br />
 virtual Time <code>maxBondLength</code> () const<br />
 <i>the largest bondLength for which the term structure can return vols </i><br />
 virtual Rate <code>minStrike</code> () const =0<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 virtual Rate <code>maxStrike</code> () const =0<br />
 <i>the maximum strike for which the term structure can return vols </i></p>
<h3>Protected Member Functions</h3>
<p>virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time optionTime, Time bondLength) const =0<br />
 <i>return smile section </i><br />
 virtual <code>Volatility</code> <code>volatilityImpl</code> (Time optionTime, Time bondLength, Rate strike) const =0<br />
 <i>implements the actual volatility calculation in derived classes </i><br />
 virtual <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor, Rate strike) const </p>
<p> void <code>checkRange</code> (Time, Time, Rate strike, bool extrapolate) const </p>
<p> void <code>checkRange</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor, Rate strike, bool extrapolate) const </p>
<h2>Detailed Description</h2>
<p>Callable-bond volatility structure. </p>
<p> This class is purely abstract and defines the interface of concrete callable-bond volatility structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CallableBondVolatilityStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>(), <code>BusinessDayConvention</code> bdc = Following)</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
