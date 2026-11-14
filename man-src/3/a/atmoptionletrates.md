---
title: "atmoptionletrates(3)"
name: "atmoptionletrates"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atmoptionletrates/"
description: "QuantLib::StrippedOptionlet –"
---

<p>QuantLib::StrippedOptionlet &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/strippedoptionlet.hpp&gt; </p>
<p> Inherits <code>QuantLib::StrippedOptionletBase</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StrippedOptionlet</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, const std::vector&lt; <code>Date</code> &gt; &amp;optionletDates, const std::vector&lt; <code>Rate</code> &gt; &amp;strikes, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;, const <code>DayCounter</code> &amp;dc=<code>Actual365Fixed</code>()) </p>
<p> <code>StrippedOptionletBase interface</code> </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>optionletStrikes</code> (Size i) const </p>
<p> const std::vector&lt; <code>Volatility</code> &gt; &amp; <code>optionletVolatilities</code> (Size i) const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>optionletFixingDates</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>optionletFixingTimes</code> () const </p>
<p> Size <code>optionletMaturities</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>atmOptionletRates</code> () const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const </p>
<p> <code>Calendar</code> <code>calendar</code> () const </p>
<p> <code>Natural</code> <code>settlementDays</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<h2>Detailed Description</h2>
<p>Helper class to wrap in a <code>StrippedOptionletBase</code> object a matrix of exogenously calculated optionlet (i.e. caplet/floorlet) volatilities (a.k.a. forward-forward volatilities). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
