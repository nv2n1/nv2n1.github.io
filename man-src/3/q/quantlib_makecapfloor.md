---
title: "quantlib_makecapfloor(3)"
name: "quantlib_makecapfloor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_makecapfloor/"
description: "QuantLib::MakeCapFloor – helper class"
---

<p>QuantLib::MakeCapFloor &#8211; helper class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/makecapfloor.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeCapFloor</code> (CapFloor::Type capFloorType, const <code>Period</code> &amp;capFloorTenor, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, <code>Rate</code> strike=<code>Null</code>&lt; <code>Rate</code> &gt;(), const <code>Period</code> &amp;forwardStart=0 *Days) </p>
<p> <code>operator CapFloor</code> () const </p>
<p> <code>operator boost::shared_ptr&lt; CapFloor &gt;</code> () const </p>
<p> <code>MakeCapFloor</code> &amp; <code>withNominal</code> (Real n) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withEffectiveDate</code> (const <code>Date</code> &amp;effectiveDate, bool firstCapletExcluded) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withTenor</code> (const <code>Period</code> &amp;t) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withCalendar</code> (const <code>Calendar</code> &amp;cal) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withTerminationDateConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withRule</code> (<code>DateGeneration::Rule</code> r) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withEndOfMonth</code> (bool flag=true) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withDayCount</code> (const <code>DayCounter</code> &amp;dc) </p>
<p> <code>MakeCapFloor</code> &amp; <code>withPricingEngine</code> (const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp;engine) </p>
<h2>Detailed Description</h2>
<p>helper class </p>
<p> This class provides a more comfortable way to instantiate standard market cap and floor. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
