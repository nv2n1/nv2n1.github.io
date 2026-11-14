---
title: "addedholidays(3)"
name: "addedholidays"
section: "3"
letter: "a"
url: "/docs/linux/man/3-addedholidays/"
description: "QuantLib::Calendar::Impl – abstract base class for calendar implementations"
---

<p>QuantLib::Calendar::Impl &#8211; abstract base class for calendar implementations </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendar.hpp&gt; </p>
<p> Inherited by Impl, <code>OrthodoxImpl</code>, <code>WesternImpl</code>, SseImpl, Impl, Impl, Impl, TadawulImpl, SettlementImpl, TsecImpl, and Impl. </p>
<h3>Public Member Functions</h3>
<p>virtual std::string <code>name</code> () const =0 </p>
<p> virtual bool <code>isBusinessDay</code> (const <code>Date</code> &amp;) const =0 </p>
<p> virtual bool <code>isWeekend</code> (<code>Weekday</code>) const =0 </p>
<h3>Public Attributes</h3>
<p>std::set&lt; <code>Date</code> &gt; <code>addedHolidays</code> </p>
<p> std::set&lt; <code>Date</code> &gt; <code>removedHolidays</code> </p>
<h2>Detailed Description</h2>
<p>abstract base class for calendar implementations </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
