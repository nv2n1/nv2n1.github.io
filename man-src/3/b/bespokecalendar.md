---
title: "bespokecalendar(3)"
name: "bespokecalendar"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bespokecalendar/"
description: "QuantLib::BespokeCalendar – Bespoke calendar."
---

<p>QuantLib::BespokeCalendar &#8211; Bespoke calendar. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/bespokecalendar.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BespokeCalendar</code> (const std::string &amp;name=&#8221;) </p>
<p> void <code>addWeekend</code> (<code>Weekday</code>)<br />
 <i>marks the passed day as part of the weekend </i></p>
<h2>Detailed Description</h2>
<p>Bespoke calendar. </p>
<p> This calendar has no predefined set of business days. Holidays and weekdays can be defined by means of the provided interface. Instances constructed by copying remain linked to the original one; adding a new holiday or weekday will affect all linked instances.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BespokeCalendar</code> (const std::string &amp; name = &#8221;)</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>different bespoke calendars created with the same name (or different bespoke calendars created with no name) will compare as equal.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
