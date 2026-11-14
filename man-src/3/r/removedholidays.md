---
title: "removedholidays(3)"
name: "removedholidays"
section: "3"
letter: "r"
url: "/docs/linux/man/3-removedholidays/"
description: "QuantLib::Calendar::Impl – abstract base class for calendar implementations"
---

<p>QuantLib::Calendar::Impl &#8211; abstract base class for calendar implementations </p>
<h2>Synopsis</h2>
<pre><code>virtual std::string name () const =0



virtual bool isBusinessDay (const Date &amp;) const =0



virtual bool isWeekend (Weekday) const =0



Public Attributes</code></pre>
<p> Inherited by Impl, <code>OrthodoxImpl</code>, <code>WesternImpl</code>, SseImpl, Impl, Impl, Impl, TadawulImpl, SettlementImpl, TsecImpl, and Impl.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual std::string name () const =0



virtual bool isBusinessDay (const Date &amp;) const =0



virtual bool isWeekend (Weekday) const =0



Public Attributes</code></pre>
<p> std::set&lt; <code>Date</code> &gt; <code>addedHolidays</code> </p>
<p> std::set&lt; <code>Date</code> &gt; <code>removedHolidays</code></p>
<h2>Detailed Description</h2>
<p>abstract base class for calendar implementations</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
