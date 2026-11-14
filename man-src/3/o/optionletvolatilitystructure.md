---
title: "optionletvolatilitystructure(3)"
name: "optionletvolatilitystructure"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionletvolatilitystructure/"
description: "QuantLib::OptionletVolatilityStructure – Optionlet (caplet/floorlet) volatility structure."
---

<p>QuantLib::OptionletVolatilityStructure &#8211; Optionlet (caplet/floorlet) volatility structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/optionletvolatilitystructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. </p>
<p> Inherited by <code>CapletVarianceCurve</code>, <code>ConstantOptionletVolatility</code>, SpreadedOptionletVolatility, and <code>StrippedOptionletAdapter</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>OptionletVolatilityStructure</code> (const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>OptionletVolatilityStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>OptionletVolatilityStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Volatility and Variance</code> </p>
<p> <code>Volatility</code> <code>volatility</code> (const <code>Period</code> &amp;optionTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option tenor and strike rate </i><br />
 <code>Volatility</code> <code>volatility</code> (const <code>Date</code> &amp;optionDate, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option date and strike rate </i><br />
 <code>Volatility</code> <code>volatility</code> (Time optionTime, Rate strike, bool extrapolate=false) const<br />
 <i>returns the volatility for a given option time and strike rate </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Period</code> &amp;optionTenor, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option tenor and strike rate </i><br />
 <code>Real</code> <code>blackVariance</code> (const <code>Date</code> &amp;optionDate, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option date and strike rate </i><br />
 <code>Real</code> <code>blackVariance</code> (Time optionTime, Rate strike, bool extrapolate=false) const<br />
 <i>returns the Black variance for a given option time and strike rate </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Period</code> &amp;optionTenor, bool extr=false) const<br />
 <i>returns the smile for a given option tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Date</code> &amp;optionDate, bool extr=false) const<br />
 <i>returns the smile for a given option date </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (Time optionTime, bool extr=false) const<br />
 <i>returns the smile for a given option time </i></p>
<h3>Protected Member Functions</h3>
<p>virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (const <code>Date</code> &amp;optionDate) const </p>
<p> virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time optionTime) const =0<br />
 <i>implements the actual smile calculation in derived classes </i><br />
 <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;optionDate, Rate strike) const </p>
<p> virtual <code>Volatility</code> <code>volatilityImpl</code> (Time optionTime, Rate strike) const =0<br />
 <i>implements the actual volatility calculation in derived classes </i></p>
<h2>Detailed Description</h2>
<p>Optionlet (caplet/floorlet) volatility structure. </p>
<p> This class is purely abstract and defines the interface of concrete structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>OptionletVolatilityStructure</code> (const <code>Calendar</code> &amp; cal, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
