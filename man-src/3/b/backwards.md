---
title: "backwards(3)"
name: "backwards"
section: "3"
letter: "b"
url: "/docs/linux/man/3-backwards/"
description: "QuantLib::MakeSchedule – helper class"
---

<h2 class="name">NAME</h2>
<p> QuantLib::MakeSchedule &#8211; helper class </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/time/schedule.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p> <code>MakeSchedule</code> (const <code>Date</code> &amp;effectiveDate, const <code>Date</code> &amp;terminationDate, const <code>Period</code> &amp;tenor, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> convention) </p>
<p> <code>MakeSchedule</code> &amp; <code>withTerminationDateConvention</code> (<code>BusinessDayConvention</code>) </p>
<p> <code>MakeSchedule</code> &amp; <code>withRule</code> (<code>DateGeneration::Rule</code>) </p>
<p> <code>MakeSchedule</code> &amp; <code>forwards</code> () </p>
<p> <code>MakeSchedule</code> &amp; <code>backwards</code> () </p>
<p> <code>MakeSchedule</code> &amp; <code>endOfMonth</code> (bool flag=true) </p>
<p> <code>MakeSchedule</code> &amp; <code>withFirstDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>MakeSchedule</code> &amp; <code>withNextToLastDate</code> (const <code>Date</code> &amp;d) </p>
<p> <code>operator Schedule</code> () const </p>
<h2>Detailed Description</h2>
<p> helper class </p>
<p> This class provides a more comfortable interface to the argument list of Schedule&#8217;s constructor. </p>
<p> <code>Examples: </code> </p>
<p> <code>CDS.cpp</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
