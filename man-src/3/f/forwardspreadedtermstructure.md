---
title: "forwardspreadedtermstructure(3)"
name: "forwardspreadedtermstructure"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardspreadedtermstructure/"
description: "QuantLib::ForwardSpreadedTermStructure – Term structure with added spread on the instantaneous forward rate."
---

<p>QuantLib::ForwardSpreadedTermStructure &#8211; Term structure with added spread on the instantaneous forward rate. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/forwardspreadedtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::ForwardRateStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ForwardSpreadedTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread) </p>
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
 <i>the latest date for which the curve can return values </i><br />
 Time <code>maxTime</code> () const<br />
 <i>the latest time for which the curve can return values </i></p>
<h3>Protected Member Functions</h3>
<p><code>Rate</code> <code>forwardImpl</code> (Time) const<br />
 <i>returns the spreaded forward rate </i><br />
 <code>Rate</code> <code>zeroYieldImpl</code> (Time) const<br />
 <i>returns the spreaded zero yield rate </i></p>
<h2>Detailed Description</h2>
<p>Term structure with added spread on the instantaneous forward rate. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This term structure will remain linked to the original structure, i.e., any changes in the latter will be reflected in this structure as well.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</p>
<dt>*</p>
<dd>observability against changes in the underlying term structure and in the added spread is checked.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
