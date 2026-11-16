---
title: "tsx(3)"
name: "tsx"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tsx/"
description: "QuantLib::Canada – Canadian calendar."
---

<p>QuantLib::Canada &#8211; Canadian calendar. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/canada.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>TSX</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Canada</code> (<code>Market</code> market=<code>Settlement</code>) </p>
<h2>Detailed Description</h2>
<p>Canadian calendar. </p>
<p> Banking holidays: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Family Day, third Monday of February (since 2008)</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Victoria Day, The Monday on or preceding 24 May</dd>
<dt>*</dt>
<dd><code>Canada</code> Day, July 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Provincial Holiday, first Monday of August</dd>
<dt>*</dt>
<dd>Labour Day, first Monday of September</dd>
<dt>*</dt>
<dd>Thanksgiving Day, second Monday of October</dd>
<dt>*</dt>
<dd>Remembrance Day, November 11th (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Christmas, December 25th (possibly moved to Monday or Tuesday)</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dd></dl>
<p> Holidays for the Toronto stock exchange (TSX): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Family Day, third Monday of February (since 2008)</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Victoria Day, The Monday on or preceding 24 May</dd>
<dt>*</dt>
<dd><code>Canada</code> Day, July 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Provincial Holiday, first Monday of August</dd>
<dt>*</dt>
<dd>Labour Day, first Monday of September</dd>
<dt>*</dt>
<dd>Thanksgiving Day, second Monday of October</dd>
<dt>*</dt>
<dd>Christmas, December 25th (possibly moved to Monday or Tuesday)</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>generic settlement calendar</dd>
<dt><i>TSX </i></dt>
<dd>Toronto stock exchange calendar. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
