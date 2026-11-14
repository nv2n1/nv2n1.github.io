---
title: "quantlib_brazil(3)"
name: "quantlib_brazil"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_brazil/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Tiradentes&#8217;s Day, April 21th</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>Independence Day, September 7th</p>
<dt>*</p>
<dd>Nossa Sra. Aparecida Day, October 12th</p>
<dt>*</p>
<dd>All Souls Day, November 2nd</p>
<dt>*</p>
<dd>Republic Day, November 15th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Passion of Christ</p>
<dt>*</p>
<dd>Carnival</p>
<dt>*</p>
<dd>Corpus Christi</dl>
<p> Holidays for the Bovespa stock exchange </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Sao Paulo City Day, January 25th</p>
<dt>*</p>
<dd>Tiradentes&#8217;s Day, April 21th</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>Revolution Day, July 9th</p>
<dt>*</p>
<dd>Independence Day, September 7th</p>
<dt>*</p>
<dd>Nossa Sra. Aparecida Day, October 12th</p>
<dt>*</p>
<dd>All Souls Day, November 2nd</p>
<dt>*</p>
<dd>Republic Day, November 15th</p>
<dt>*</p>
<dd>Black Consciousness Day, November 20th (since 2007)</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Passion of Christ</p>
<dt>*</p>
<dd>Carnival</p>
<dt>*</p>
<dd>Corpus Christi</p>
<dt>*</p>
<dd>the last business day of the year</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>Brazilian calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>Exchange </i></p>
<dd>BOVESPA calendar. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
