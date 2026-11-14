---
title: "quantlib_blackvolsurface(3)"
name: "quantlib_blackvolsurface"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackvolsurface/"
description: "QuantLib::BlackVolSurface – Black volatility (smile) surface."
---

<p>QuantLib::BlackVolSurface &#8211; Black volatility (smile) surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/blackvolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackAtmVolCurve</code>. </p>
<p> Inherited by <code>EquityFXVolSurface</code>, and <code>InterestRateVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>BlackVolSurface</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>BlackVolSurface</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>BlackVolSurface</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Black spot volatility</code> </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Period</code> &amp;, bool extrapolate) const<br />
 <i>returns the smile for a given option tenor </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (const <code>Date</code> &amp;, bool extrapolate) const<br />
 <i>returns the smile for a given option date </i><br />
 boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSection</code> (Time, bool extrapolate) const<br />
 <i>returns the smile for a given option time </i> </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>BlackAtmVolCurve interface</code> </p>
<p> <code>Real</code> <code>atmVarianceImpl</code> (Time t) const<br />
 <i>spot at-the-money variance calculation </i><br />
 <code>Volatility</code> <code>atmVolImpl</code> (Time t) const<br />
 <i>spot at-the-money volatility calculation </i> </p>
<p> <code>Calculations</code><br />
 This method must be implemented in derived classes to perform the actual volatility calculations. When it is called, time check has already been performed; therefore, it must assume that time-extrapolation is allowed. </p>
<p> virtual boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time) const =0 </p>
<h2>Detailed Description</h2>
<p>Black volatility (smile) surface. </p>
<p> This abstract class defines the interface of concrete Black volatility (smile) surface which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BlackVolSurface</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
