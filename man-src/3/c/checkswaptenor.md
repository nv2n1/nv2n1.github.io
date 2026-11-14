---
title: "checkswaptenor(3)"
name: "checkswaptenor"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checkswaptenor/"
description: "QuantLib::SwaptionVolatilityStructure – Swaption-volatility structure"
---

<p>QuantLib::SwaptionVolatilityStructure &#8211; Swaption-volatility structure </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/swaption/swaptionvolstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>ConstantSwaptionVolatility</code>, SpreadedSwaptionVolatility, and SwaptionVolatilityDiscrete. </p>
<h3>Public Member Functions</h3>
<p>Time <code>swapLength</code> (const <code>Period</code> &amp;swapTenor) const<br />
 <i>implements the conversion between swap tenor and swap (time) length </i><br />
 Time <code>swapLength</code> (const <code>Date</code> &amp;start, const <code>Date</code> &amp;end) const<br />
 <i>implements the conversion between swap dates and swap (time) length </i> </p>
<p> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>SwaptionVolatilityStructure</code> (const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>SwaptionVolatilityStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>SwaptionVolatilityStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Volatility, variance and smile</code> </p>
<p> <code>Volatility</code> <code>volatility</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option tenor and swap tenor </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option date and swap tenor </i><br />
 <code>Volatility</code> <code>volatility</code> (Time optionTime, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option time and swap tenor </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Period</code> &amp;optionTenor, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option tenor and swap length </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Date</code> &amp;optionDate, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option date and swap length </i><br />
 <code>Volatility</code> <code>volatility</code> (Time optionTime, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option time and swap length </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option tenor and swap tenor </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option date and swap tenor </i><br />
 <code>Real</code> <code>blackVariance</code> (Time optionTime, const <code>Period</code> &amp;swapTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option time and swap tenor </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Period</code> &amp;optionTenor, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option tenor and swap length </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Date</code> &amp;optionDate, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option date and swap length </i><br />
 <code>Real</code> <code>blackVariance</code> (Time optionTime, Time swapLength, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option time and swap length </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;swapTenor, bool extr=false) const<br />
 <i>returns the smile for a given option tenor and swap tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor, bool extr=false) const<br />
 <i>returns the smile for a given option date and swap tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (Time optionTime, const <code>Period</code> &amp;swapTenor, bool extr=false) const<br />
 <i>returns the smile for a given option time and swap tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Period</code> &amp;optionTenor, Time swapLength, bool extr=false) const<br />
 <i>returns the smile for a given option tenor and swap length </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Date</code> &amp;optionDate, Time swapLength, bool extr=false) const<br />
 <i>returns the smile for a given option date and swap length </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (Time optionTime, Time swapLength, bool extr=false) const<br />
 <i>returns the smile for a given option time and swap length </i> </p>
<p> <code>Limits</code> </p>
<p> virtual const <code>Period</code> &amp; <code>maxSwapTenor</code> () const =0<br />
 <i>the largest length for which the term structure can return vols </i><br />
 Time <code>maxSwapLength</code> () const<br />
 <i>the largest swapLength for which the term structure can return vols </i></p>
<h3>Protected Member Functions</h3>
<p>virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor) const </p>
<p> virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time optionTime, Time swapLength) const =0 </p>
<p> virtual <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor, Rate strike) const </p>
<p> virtual <code>Volatility</code> <code>volatilityImpl</code> (Time optionTime, Time swapLength, Rate strike) const =0 </p>
<p> void <code>checkSwapTenor</code> (const <code>Period</code> &amp;swapTenor, bool extrapolate) const </p>
<p> void <code>checkSwapTenor</code> (Time swapLength, bool extrapolate) const </p>
<h2>Detailed Description</h2>
<p>Swaption-volatility structure </p>
<p> This abstract class defines the interface of concrete swaption volatility structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>SwaptionVolatilityStructure</code> (const <code>Calendar</code> &amp; calendar, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
