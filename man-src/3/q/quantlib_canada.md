---
title: "quantlib_canada(3)"
name: "quantlib_canada"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_canada/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Family Day, third Monday of February (since 2008)</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Victoria Day, The Monday on or preceding 24 May</p>
<dt>*</p>
<dd><code>Canada</code> Day, July 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Provincial Holiday, first Monday of August</p>
<dt>*</p>
<dd>Labour Day, first Monday of September</p>
<dt>*</p>
<dd>Thanksgiving Day, second Monday of October</p>
<dt>*</p>
<dd>Remembrance Day, November 11th (possibly moved to Monday)</p>
<dt>*</p>
<dd>Christmas, December 25th (possibly moved to Monday or Tuesday)</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dl>
<p> Holidays for the Toronto stock exchange (TSX): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Family Day, third Monday of February (since 2008)</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Victoria Day, The Monday on or preceding 24 May</p>
<dt>*</p>
<dd><code>Canada</code> Day, July 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Provincial Holiday, first Monday of August</p>
<dt>*</p>
<dd>Labour Day, first Monday of September</p>
<dt>*</p>
<dd>Thanksgiving Day, second Monday of October</p>
<dt>*</p>
<dd>Christmas, December 25th (possibly moved to Monday or Tuesday)</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>TSX </i></p>
<dd>Toronto stock exchange calendar. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
