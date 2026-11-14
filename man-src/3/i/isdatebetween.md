---
title: "isdatebetween(3)"
name: "isdatebetween"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isdatebetween/"
description: "QuantLib::DateInterval – Date interval described by a number of a given time unit."
---

<p>QuantLib::DateInterval &#8211; <code>Date</code> interval described by a number of a given time unit. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/dateinterval.hpp&gt; </p>
<p> Inherited by <code>PricingPeriod</code>. </p>
<h3>Public Member Functions</h3>
<p><code>DateInterval</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) </p>
<p> const <code>Date</code> &amp; <code>startDate</code> () const </p>
<p> const <code>Date</code> &amp; <code>endDate</code> () const </p>
<p> bool <code>isDateBetween</code> (<code>Date</code> date, bool includeFirst=true, bool includeLast=true) const </p>
<p> <code>DateInterval</code> <code>intersection</code> (const <code>DateInterval</code> &amp;di) const </p>
<p> bool <code>operator==</code> (const <code>DateInterval</code> &amp;rhs) const </p>
<p> bool <code>operator!=</code> (const <code>DateInterval</code> &amp;rhs) const </p>
<h3>Friends</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>DateInterval</code> &amp;) </p>
<h2>Detailed Description</h2>
<p><code>Date</code> interval described by a number of a given time unit. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
