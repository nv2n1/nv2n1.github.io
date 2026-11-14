---
title: "quantlib_piecewisezerospreadedtermstructure(3)"
name: "quantlib_piecewisezerospreadedtermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_piecewisezerospreadedtermstructure/"
description: "QuantLib::PiecewiseZeroSpreadedTermStructure – Term structure with an added vector of spreads on the zero-yield rate."
---

<p>QuantLib::PiecewiseZeroSpreadedTermStructure &#8211; Term structure with an added vector of spreads on the zero-yield rate. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/piecewisezerospreadedtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::ZeroYieldStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>PiecewiseZeroSpreadedTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;spreads, const std::vector&lt; <code>Date</code> &gt; &amp;dates) </p>
<p> <code>YieldTermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Natural</code> <code>settlementDays</code> () const<br />
 <i>the settlementDays used for reference date calculation </i><br />
 <code>Calendar</code> <code>calendar</code> () const<br />
 <i>the calendar used for reference and/or option date calculation </i><br />
 const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>zeroYieldImpl</code> (Time) const<br />
 <i>returns the spreaded zero yield rate </i><br />
 void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p>Term structure with an added vector of spreads on the zero-yield rate. </p>
<p> The zero-yield spread at any given date is linearly interpolated between the input data. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This term structure will remain linked to the original structure, i.e., any changes in the latter will be reflected in this structure as well.</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [protected, virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
