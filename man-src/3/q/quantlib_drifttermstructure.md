---
title: "quantlib_drifttermstructure(3)"
name: "quantlib_drifttermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_drifttermstructure/"
description: "QuantLib::DriftTermStructure – Drift term structure."
---

<p>QuantLib::DriftTermStructure &#8211; Drift term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/drifttermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::ZeroYieldStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DriftTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS) </p>
<p> <code>YieldTermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Calendar</code> <code>calendar</code> () const<br />
 <i>the calendar used for reference and/or option date calculation </i><br />
 <code>Natural</code> <code>settlementDays</code> () const<br />
 <i>the settlementDays used for reference date calculation </i><br />
 const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>zeroYieldImpl</code> (Time) const<br />
 <i>returns the discount factor as seen from the evaluation date </i></p>
<h2>Detailed Description</h2>
<p>Drift term structure. </p>
<p> Drift term structure for modelling the common drift term: riskFreeRate &#8211; dividendYield &#8211; 0.5*vol*vol </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This term structure will remain linked to the original structures, i.e., any changes in the latters will be reflected in this structure as well.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
