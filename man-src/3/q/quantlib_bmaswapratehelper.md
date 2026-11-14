---
title: "quantlib_bmaswapratehelper(3)"
name: "quantlib_bmaswapratehelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_bmaswapratehelper/"
description: "QuantLib::BMASwapRateHelper – Rate helper for bootstrapping over BMA swap rates."
---

<p>QuantLib::BMASwapRateHelper &#8211; Rate helper for bootstrapping over BMA swap rates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>QuantLib::RelativeDateRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BMASwapRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;liborFraction, const <code>Period</code> &amp;tenor, <code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>Period</code> &amp;bmaPeriod, <code>BusinessDayConvention</code> bmaConvention, const <code>DayCounter</code> &amp;bmaDayCount, const boost::shared_ptr&lt; <code>BMAIndex</code> &gt; &amp;bmaIndex, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index) </p>
<p> <code>RateHelper interface</code> </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>YieldTermStructure</code> *) </p>
<p> <code>Visitability</code> </p>
<p> void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>void <code>initializeDates</code> () </p>
<h3>Protected Attributes</h3>
<p><code>Period</code> <code>tenor_</code> </p>
<p> <code>Natural</code> <code>settlementDays_</code> </p>
<p> <code>Calendar</code> <code>calendar_</code> </p>
<p> <code>Period</code> <code>bmaPeriod_</code> </p>
<p> <code>BusinessDayConvention</code> <code>bmaConvention_</code> </p>
<p> <code>DayCounter</code> <code>bmaDayCount_</code> </p>
<p> boost::shared_ptr&lt; <code>BMAIndex</code> &gt; <code>bmaIndex_</code> </p>
<p> boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>iborIndex_</code> </p>
<p> boost::shared_ptr&lt; <code>BMASwap</code> &gt; <code>swap_</code> </p>
<p> <code>RelinkableHandle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructureHandle_</code> </p>
<h2>Detailed Description</h2>
<p>Rate helper for bootstrapping over BMA swap rates. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
