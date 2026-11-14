---
title: "quantlib_italy(3)"
name: "quantlib_italy"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_italy/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Epiphany, January 6th</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Liberation Day, April 25th</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>Republic Day, June 2nd (since 2000)</p>
<dt>*</p>
<dd>Assumption, August 15th</p>
<dt>*</p>
<dd>All Saint&#8217;s Day, November 1st</p>
<dt>*</p>
<dd>Immaculate Conception Day, December 8th</p>
<dt>*</p>
<dd>Christmas Day, December 25th</p>
<dt>*</p>
<dd>St. Stephen&#8217;s Day, December 26th</dl>
<p> Holidays for the stock exchange (data from <a rel="nofollow" href="http://www.borsaitalia.it">http://www.borsaitalia.it</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>Assumption, August 15th</p>
<dt>*</p>
<dd>Christmas&#8217; Eve, December 24th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>St. Stephen, December 26th</p>
<dt>*</p>
<dd>New Year&#8217;s Eve, December 31st</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>Italian calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>Exchange </i></p>
<dd>Milan stock-exchange calendar. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
