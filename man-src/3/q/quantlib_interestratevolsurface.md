---
title: "quantlib_interestratevolsurface(3)"
name: "quantlib_interestratevolsurface"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interestratevolsurface/"
description: "QuantLib::InterestRateVolSurface – Interest rate volatility (smile) surface."
---

<p>QuantLib::InterestRateVolSurface &#8211; Interest rate volatility (smile) surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/interestratevolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVolSurface</code>. </p>
<p> Inherited by <code>SabrVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p>const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp; <code>index</code> () const </p>
<p> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>InterestRateVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>()) </p>
<p> <code>InterestRateVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>InterestRateVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, <code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> <code>Date</code> <code>optionDateFromTenor</code> (const <code>Period</code> &amp;) const<br />
 <i>period/date conversion </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; <code>index_</code> </p>
<h2>Detailed Description</h2>
<p>Interest rate volatility (smile) surface. </p>
<p> This abstract class defines the interface of concrete Interest rate volatility (smile) surfaces which will be derived from this one. </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>InterestRateVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
