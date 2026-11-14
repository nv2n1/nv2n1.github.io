---
title: "quantlib_strippedoptionletbase(3)"
name: "quantlib_strippedoptionletbase"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_strippedoptionletbase/"
description: "QuantLib::StrippedOptionletBase –"
---

<p>QuantLib::StrippedOptionletBase &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/strippedoptionletbase.hpp&gt; </p>
<p> Inherits <code>QuantLib::LazyObject</code>. </p>
<p> Inherited by OptionletStripper, and <code>StrippedOptionlet</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>optionletStrikes</code> (Size i) const =0 </p>
<p> virtual const std::vector&lt; <code>Volatility</code> &gt; &amp; <code>optionletVolatilities</code> (Size i) const =0 </p>
<p> virtual const std::vector&lt; <code>Date</code> &gt; &amp; <code>optionletFixingDates</code> () const =0 </p>
<p> virtual const std::vector&lt; <code>Time</code> &gt; &amp; <code>optionletFixingTimes</code> () const =0 </p>
<p> virtual Size <code>optionletMaturities</code> () const =0 </p>
<p> virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>atmOptionletRates</code> () const =0 </p>
<p> virtual <code>DayCounter</code> <code>dayCounter</code> () const =0 </p>
<p> virtual <code>Calendar</code> <code>calendar</code> () const =0 </p>
<p> virtual <code>Natural</code> <code>settlementDays</code> () const =0 </p>
<p> virtual <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>Abstract base class interface for a (time indexed) vector of (strike indexed) optionlet (i.e. caplet/floorlet) volatilities. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
