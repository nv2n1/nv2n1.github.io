---
title: "quantlib_blackvariancetermstructure(3)"
name: "quantlib_blackvariancetermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackvariancetermstructure/"
description: "QuantLib::BlackVarianceTermStructure – Black variance term structure."
---

<p>QuantLib::BlackVarianceTermStructure &#8211; Black variance term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackvoltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVolTermStructure</code>. </p>
<p> Inherited by <code>BlackVarianceCurve</code>, <code>BlackVarianceSurface</code>, <code>ExtendedBlackVarianceCurve</code>, <code>ExtendedBlackVarianceSurface</code>, and <code>ImpliedVolTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. </p>
<p> <code>BlackVarianceTermStructure</code> (const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>default constructor </i><br />
 <code>BlackVarianceTermStructure</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;cal=<code>Calendar</code>(), <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>initialize with a fixed reference date </i><br />
 <code>BlackVarianceTermStructure</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, <code>BusinessDayConvention</code> bdc=Following, const <code>DayCounter</code> &amp;dc=<code>DayCounter</code>())<br />
 <i>calculate the reference date based on the global evaluation date </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p><code>Volatility</code> <code>blackVolImpl</code> (Time t, Real strike) const </p>
<h2>Detailed Description</h2>
<p>Black variance term structure. </p>
<p> This abstract class acts as an adapter to VolTermStructure allowing the programmer to implement only the blackVarianceImpl(Time, Real, bool) method in derived classes. </p>
<p> Volatility are assumed to be expressed on an annual basis.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BlackVarianceTermStructure</code> (const <code>Calendar</code> &amp; cal = <code>Calendar</code>(), <code>BusinessDayConvention</code> bdc = Following, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> blackVolImpl (Time t, Real strike) const [protected, virtual]</h3>
<p>Returns the volatility for the given strike and date calculating it from the variance. </p>
<p> Implements <code>BlackVolTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
