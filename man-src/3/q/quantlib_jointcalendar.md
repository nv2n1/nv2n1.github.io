---
title: "quantlib_jointcalendar(3)"
name: "quantlib_jointcalendar"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_jointcalendar/"
description: "QuantLib::JointCalendar – Joint calendar."
---

<p>QuantLib::JointCalendar &#8211; Joint calendar. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/jointcalendar.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Member Functions</h3>
<p><code>JointCalendar</code> (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, JointCalendarRule=JoinHolidays) </p>
<p> <code>JointCalendar</code> (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, JointCalendarRule=JoinHolidays) </p>
<p> <code>JointCalendar</code> (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;, JointCalendarRule=JoinHolidays) </p>
<h2>Detailed Description</h2>
<p>Joint calendar. </p>
<p> Depending on the chosen rule, this calendar has a set of business days given by either the union or the intersection of the sets of business days of the given calendars. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested by reproducing the calculations.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
