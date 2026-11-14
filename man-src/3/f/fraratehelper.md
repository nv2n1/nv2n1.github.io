---
title: "fraratehelper(3)"
name: "fraratehelper"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fraratehelper/"
description: "QuantLib::FraRateHelper – Rate helper for bootstrapping over FRA rates."
---

<p>QuantLib::FraRateHelper &#8211; Rate helper for bootstrapping over FRA rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>QuantLib::RelativeDateRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FraRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, <code>Natural</code> monthsToStart, <code>Natural</code> monthsToEnd, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>FraRateHelper</code> (<code>Rate</code> rate, <code>Natural</code> monthsToStart, <code>Natural</code> monthsToEnd, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>FraRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, <code>Natural</code> monthsToStart, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>FraRateHelper</code> (<code>Rate</code> rate, <code>Natural</code> monthsToStart, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>FraRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, <code>Period</code> periodToStart, <code>Natural</code> lengthInMonths, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>FraRateHelper</code> (<code>Rate</code> rate, <code>Period</code> periodToStart, <code>Natural</code> lengthInMonths, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>FraRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, <code>Period</code> periodToStart, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>FraRateHelper</code> (<code>Rate</code> rate, <code>Period</code> periodToStart, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>RateHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>YieldTermStructure</code> *) </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Rate helper for bootstrapping over FRA rates. </p>
<p> <code>Examples: </code> </p>
<p> <code>FRA.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
