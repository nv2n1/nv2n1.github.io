---
title: "italy(3)"
name: "italy"
section: "3"
letter: "i"
url: "/docs/linux/man/3-italy/"
description: "QuantLib::Italy – Italian calendars."
---

<p>QuantLib::Italy &#8211; Italian calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/italy.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>Exchange</code> }<br />
 <i>Italian calendars. </i></p>
<h3>Public Member Functions</h3>
<p><code>Italy</code> (<code>Market</code> market=<code>Settlement</code>) </p>
<h2>Detailed Description</h2>
<p>Italian calendars. </p>
<p> Public holidays: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Epiphany, January 6th</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Liberation Day, April 25th</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>Republic Day, June 2nd (since 2000)</dd>
<dt>*</dt>
<dd>Assumption, August 15th</dd>
<dt>*</dt>
<dd>All Saint&#8217;s Day, November 1st</dd>
<dt>*</dt>
<dd>Immaculate Conception Day, December 8th</dd>
<dt>*</dt>
<dd>Christmas Day, December 25th</dd>
<dt>*</dt>
<dd>St. Stephen&#8217;s Day, December 26th</dd></dl>
<p> Holidays for the stock exchange (data from <a rel="nofollow" href="http://www.borsaitalia.it">http://www.borsaitalia.it</a>): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>Assumption, August 15th</dd>
<dt>*</dt>
<dd>Christmas&#8217; Eve, December 24th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>St. Stephen, December 26th</dd>
<dt>*</dt>
<dd>New Year&#8217;s Eve, December 31st</dd></dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>Italian calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>generic settlement calendar</dd>
<dt><i>Exchange </i></dt>
<dd>Milan stock-exchange calendar. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
