---
title: "quantlib_schedule(3)"
name: "quantlib_schedule"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_schedule/"
description: "QuantLib::Schedule – Payment schedule."
---

<p>QuantLib::Schedule &#8211; Payment schedule. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/schedule.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Schedule</code> (const std::vector&lt; <code>Date</code> &gt; &amp;, const <code>Calendar</code> &amp;calendar=<code>NullCalendar</code>(), <code>BusinessDayConvention</code> convention=Unadjusted) </p>
<p> <code>Schedule</code> (const <code>Date</code> &amp;effectiveDate, const <code>Date</code> &amp;terminationDate, const <code>Period</code> &amp;tenor, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention, <code>BusinessDayConvention</code> terminationDateConvention, <code>DateGeneration::Rule</code> rule, bool endOfMonth, const <code>Date</code> &amp;firstDate=<code>Date</code>(), const <code>Date</code> &amp;nextToLastDate=<code>Date</code>()) </p>
<p> <code>Date access</code> </p>
<p> Size <code>size</code> () const </p>
<p> const <code>Date</code> &amp; <code>operator[]</code> (Size i) const </p>
<p> const <code>Date</code> &amp; <code>at</code> (Size i) const </p>
<p> const <code>Date</code> &amp; <code>date</code> (Size i) const </p>
<p> <code>Date</code> <code>previousDate</code> (const <code>Date</code> &amp;refDate) const </p>
<p> <code>Date</code> <code>nextDate</code> (const <code>Date</code> &amp;refDate) const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> bool <code>isRegular</code> (Size i) const </p>
<p> <code>Other inspectors</code> </p>
<p> bool <code>empty</code> () const </p>
<p> const <code>Calendar</code> &amp; <code>calendar</code> () const </p>
<p> const <code>Date</code> &amp; <code>startDate</code> () const </p>
<p> const <code>Date</code> &amp; <code>endDate</code> () const </p>
<p> const <code>Period</code> &amp; <code>tenor</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const </p>
<p> <code>BusinessDayConvention</code> <code>terminationDateBusinessDayConvention</code> () const </p>
<p> <code>DateGeneration::Rule</code> <code>rule</code> () const </p>
<p> bool <code>endOfMonth</code> () const </p>
<h3>Iterators</h3>
<p>typedef std::vector&lt; <code>Date</code> &gt;::const_iterator <code>const_iterator</code> </p>
<p> const_iterator <code>begin</code> () const </p>
<p> const_iterator <code>end</code> () const </p>
<p> const_iterator <code>lower_bound</code> (const <code>Date</code> &amp;d=<code>Date</code>()) const </p>
<h2>Detailed Description</h2>
<p>Payment schedule. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
