---
title: "depositratehelper(3)"
name: "depositratehelper"
section: "3"
letter: "d"
url: "/docs/linux/man/3-depositratehelper/"
description: "QuantLib::DepositRateHelper – Rate helper for bootstrapping over deposit rates."
---

<p>QuantLib::DepositRateHelper &#8211; Rate helper for bootstrapping over deposit rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>QuantLib::RelativeDateRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DepositRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, const <code>Period</code> &amp;tenor, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>DepositRateHelper</code> (<code>Rate</code> rate, const <code>Period</code> &amp;tenor, <code>Natural</code> fixingDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, bool endOfMonth, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>DepositRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;rate, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>DepositRateHelper</code> (<code>Rate</code> rate, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex) </p>
<p> <code>RateHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>YieldTermStructure</code> *) </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Rate helper for bootstrapping over deposit rates. </p>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
