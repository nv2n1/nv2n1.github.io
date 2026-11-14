---
title: "recoveryrate(3)"
name: "recoveryrate"
section: "3"
letter: "r"
url: "/docs/linux/man/3-recoveryrate/"
description: "QuantLib::DefaultEvent – Credit-default event."
---

<p>QuantLib::DefaultEvent &#8211; Credit-default event. </p>
<h2>Synopsis</h2>
<pre><code>DefaultEvent (const Date &amp;date, Real recoveryRate, Seniority seniority=AnySeniority, Restructuring restructuring=AnyRestructuring)



Date date () const


returns the date at which the event occurs


Real recoveryRate () const



Seniority seniority () const



Restructuring restructuring () const</code></pre>
<p> Inherits <code>QuantLib::Event</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DefaultEvent (const Date &amp;date, Real recoveryRate, Seniority seniority=AnySeniority, Restructuring restructuring=AnyRestructuring)



Date date () const


returns the date at which the event occurs


Real recoveryRate () const



Seniority seniority () const



Restructuring restructuring () const</code></pre>
<h2>Detailed Description</h2>
<p>Credit-default event.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
