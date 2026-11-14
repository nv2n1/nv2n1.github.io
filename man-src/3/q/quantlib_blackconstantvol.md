---
title: "quantlib_blackconstantvol(3)"
name: "quantlib_blackconstantvol"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackconstantvol/"
description: "QuantLib::BlackConstantVol – Constant Black volatility, no time-strike dependence."
---

<p>QuantLib::BlackConstantVol &#8211; Constant Black volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/blackconstantvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVolatilityTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BlackConstantVol</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;, Volatility volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>BlackConstantVol</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>BlackConstantVol</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, Volatility volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>BlackConstantVol</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>virtual Volatility <code>blackVolImpl</code> (Time t, Real) const<br />
 <i>Black volatility calculation. </i></p>
<h2>Detailed Description</h2>
<p>Constant Black volatility, no time-strike dependence. </p>
<p> This class implements the <code>BlackVolatilityTermStructure</code> interface for a constant Black volatility (no time/strike dependence). </p>
<p> <code>Examples: </code> </p>
<p> <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, and <code>Replication.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
