---
title: "quantlib_defaultevent(3)"
name: "quantlib_defaultevent"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_defaultevent/"
description: "QuantLib::DefaultEvent – Credit-default event."
---

<p>QuantLib::DefaultEvent &#8211; Credit-default event. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/default.hpp&gt; </p>
<p> Inherits <code>QuantLib::Event</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DefaultEvent</code> (const <code>Date</code> &amp;date, <code>Real</code> recoveryRate, Seniority seniority=AnySeniority, Restructuring restructuring=AnyRestructuring) </p>
<p> <code>Date</code> <code>date</code> () const<br />
 <i>returns the date at which the event occurs </i><br />
 <code>Real</code> <code>recoveryRate</code> () const </p>
<p> Seniority <code>seniority</code> () const </p>
<p> Restructuring <code>restructuring</code> () const </p>
<h2>Detailed Description</h2>
<p>Credit-default event. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
