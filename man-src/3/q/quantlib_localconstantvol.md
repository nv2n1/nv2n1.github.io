---
title: "quantlib_localconstantvol(3)"
name: "quantlib_localconstantvol"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_localconstantvol/"
description: "QuantLib::LocalConstantVol – Constant local volatility, no time-strike dependence."
---

<p>QuantLib::LocalConstantVol &#8211; Constant local volatility, no time-strike dependence. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/localconstantvol.hpp&gt; </p>
<p> Inherits <code>QuantLib::LocalVolTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LocalConstantVol</code> (const <code>Date</code> &amp;referenceDate, Volatility volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>LocalConstantVol</code> (const <code>Date</code> &amp;referenceDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>LocalConstantVol</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, Volatility volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>LocalConstantVol</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Constant local volatility, no time-strike dependence. </p>
<p> This class implements the LocalVolatilityTermStructure interface for a constant local volatility (no time/asset dependence). Local volatility and Black volatility are the same when volatility is at most time dependent, so this class is basically a proxy for <code>BlackVolatilityTermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
