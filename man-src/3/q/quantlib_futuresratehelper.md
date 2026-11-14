---
title: "quantlib_futuresratehelper(3)"
name: "quantlib_futuresratehelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_futuresratehelper/"
description: "QuantLib::FuturesRateHelper – Rate helper for bootstrapping over IborIndex futures prices."
---

<p>QuantLib::FuturesRateHelper &#8211; Rate helper for bootstrapping over <code>IborIndex</code> futures prices. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>BootstrapHelper&lt; YieldTermStructure &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FuturesRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;price, const <code>Date</code> &amp;immDate, <code>Natural</code> lengthInMonths, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;convexityAdjustment=<code>Handle</code>&lt; <code>Quote</code> &gt;()) </p>
<p> <code>FuturesRateHelper</code> (<code>Real</code> price, const <code>Date</code> &amp;immDate, <code>Natural</code> lengthInMonths, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter, <code>Rate</code> convexityAdjustment=0.0) </p>
<p> <code>FuturesRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;price, const <code>Date</code> &amp;immDate, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;convexityAdjustment=<code>Handle</code>&lt; <code>Quote</code> &gt;()) </p>
<p> <code>FuturesRateHelper</code> (<code>Real</code> price, const <code>Date</code> &amp;immDate, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, <code>Rate</code> convexityAdjustment=0.0) </p>
<p> <code>RateHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> <code>FuturesRateHelper inspectors</code> </p>
<p> <code>Real</code> <code>convexityAdjustment</code> () const </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Rate helper for bootstrapping over <code>IborIndex</code> futures prices. </p>
<p> <code>Examples: </code> </p>
<p> <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
