---
title: "brazil(3)"
name: "brazil"
section: "3"
letter: "b"
url: "/docs/linux/man/3-brazil/"
description: "QuantLib::Brazil – Brazilian calendar."
---

<p>QuantLib::Brazil &#8211; Brazilian calendar. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/brazil.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>Exchange</code> }<br />
 <i>Brazilian calendars. </i></p>
<h3>Public Member Functions</h3>
<p><code>Brazil</code> (<code>Market</code> market=<code>Settlement</code>) </p>
<h2>Detailed Description</h2>
<p>Brazilian calendar. </p>
<p> Banking holidays: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Tiradentes&#8217;s Day, April 21th</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>Independence Day, September 7th</dd>
<dt>*</dt>
<dd>Nossa Sra. Aparecida Day, October 12th</dd>
<dt>*</dt>
<dd>All Souls Day, November 2nd</dd>
<dt>*</dt>
<dd>Republic Day, November 15th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Passion of Christ</dd>
<dt>*</dt>
<dd>Carnival</dd>
<dt>*</dt>
<dd>Corpus Christi</dd></dl>
<p> Holidays for the Bovespa stock exchange </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Sao Paulo City Day, January 25th</dd>
<dt>*</dt>
<dd>Tiradentes&#8217;s Day, April 21th</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>Revolution Day, July 9th</dd>
<dt>*</dt>
<dd>Independence Day, September 7th</dd>
<dt>*</dt>
<dd>Nossa Sra. Aparecida Day, October 12th</dd>
<dt>*</dt>
<dd>All Souls Day, November 2nd</dd>
<dt>*</dt>
<dd>Republic Day, November 15th</dd>
<dt>*</dt>
<dd>Black Consciousness Day, November 20th (since 2007)</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Passion of Christ</dd>
<dt>*</dt>
<dd>Carnival</dd>
<dt>*</dt>
<dd>Corpus Christi</dd>
<dt>*</dt>
<dd>the last business day of the year</dd></dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>Brazilian calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>generic settlement calendar</dd>
<dt><i>Exchange </i></dt>
<dd>BOVESPA calendar. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
