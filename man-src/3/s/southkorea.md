---
title: "southkorea(3)"
name: "southkorea"
section: "3"
letter: "s"
url: "/docs/linux/man/3-southkorea/"
description: "QuantLib::SouthKorea – South Korean calendars."
---

<p>QuantLib::SouthKorea &#8211; South Korean calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/southkorea.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>KRX</code> } </p>
<h3>Public Member Functions</h3>
<p><code>SouthKorea</code> (<code>Market</code> m=KRX) </p>
<h2>Detailed Description</h2>
<p>South Korean calendars. </p>
<p> Public holidays: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Independence Day, March 1st</dd>
<dt>*</dt>
<dd>Arbour Day, April 5th (until 2005)</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>Children&#8217;s Day, May 5th</dd>
<dt>*</dt>
<dd>Memorial Day, June 6th</dd>
<dt>*</dt>
<dd>Constitution Day, July 17th (until 2007)</dd>
<dt>*</dt>
<dd>Liberation Day, August 15th</dd>
<dt>*</dt>
<dd>National Fondation Day, October 3th</dd>
<dt>*</dt>
<dd>Christmas Day, December 25th</dd></dl>
<p> Other holidays for which no rule is given (data available for 2004-2010 only:) </p>
<dl COMPACT>
<dt>*</dt>
<dd>Lunar New Year, the last day of the previous lunar year, January 1st, 2nd in lunar calendar</dd>
<dt>*</dt>
<dd>Election Days</dd>
<dt>*</dt>
<dd>National Assemblies</dd>
<dt>*</dt>
<dd>Presidency</dd>
<dt>*</dt>
<dd>Regional Election Days</dd>
<dt>*</dt>
<dd>Buddha&#8217;s birthday, April 8th in lunar calendar</dd>
<dt>*</dt>
<dd>Harvest Moon Day, August 14th, 15th, 16th in lunar calendar</dd></dl>
<p> Holidays for the Korea exchange (data from &lt;<a rel="nofollow" href="http://www.krx.co.kr">http://www.krx.co.kr</a>&gt; or &lt;<a href="http://www.dooriworld.com/daishin/holiday/holiday.html">http://www.dooriworld.com/daishin/holiday/holiday.html</a>&gt;): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Public holidays as listed above</dd>
<dt>*</dt>
<dd>Year-end closing</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>Public holidays.</dd>
<dt><i>KRX </i></dt>
<dd>Korea exchange. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
