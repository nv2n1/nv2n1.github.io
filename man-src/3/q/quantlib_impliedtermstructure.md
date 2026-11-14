---
title: "quantlib_impliedtermstructure(3)"
name: "quantlib_impliedtermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_impliedtermstructure/"
description: "QuantLib::ImpliedTermStructure – Implied term structure at a given date in the future."
---

<p>QuantLib::ImpliedTermStructure &#8211; Implied term structure at a given date in the future. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/impliedtermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::YieldTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ImpliedTermStructure</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;, const <code>Date</code> &amp;referenceDate) </p>
<p> <code>YieldTermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Calendar</code> <code>calendar</code> () const<br />
 <i>the calendar used for reference and/or option date calculation </i><br />
 <code>Natural</code> <code>settlementDays</code> () const<br />
 <i>the settlementDays used for reference date calculation </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i></p>
<h3>Protected Member Functions</h3>
<p><code>DiscountFactor</code> <code>discountImpl</code> (Time) const<br />
 <i>returns the discount factor as seen from the evaluation date </i></p>
<h2>Detailed Description</h2>
<p>Implied term structure at a given date in the future. </p>
<p> The given date will be the implied reference date. </p>
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
<dd>observability against changes in the underlying term structure is checked.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
