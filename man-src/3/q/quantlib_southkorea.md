---
title: "quantlib_southkorea(3)"
name: "quantlib_southkorea"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_southkorea/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Independence Day, March 1st</p>
<dt>*</p>
<dd>Arbour Day, April 5th (until 2005)</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>Children&#8217;s Day, May 5th</p>
<dt>*</p>
<dd>Memorial Day, June 6th</p>
<dt>*</p>
<dd>Constitution Day, July 17th (until 2007)</p>
<dt>*</p>
<dd>Liberation Day, August 15th</p>
<dt>*</p>
<dd>National Fondation Day, October 3th</p>
<dt>*</p>
<dd>Christmas Day, December 25th</dl>
<p> Other holidays for which no rule is given (data available for 2004-2010 only:) </p>
<dl COMPACT>
<dt>*</p>
<dd>Lunar New Year, the last day of the previous lunar year, January 1st, 2nd in lunar calendar</p>
<dt>*</p>
<dd>Election Days</p>
<dt>*</p>
<dd>National Assemblies</p>
<dt>*</p>
<dd>Presidency</p>
<dt>*</p>
<dd>Regional Election Days</p>
<dt>*</p>
<dd>Buddha&#8217;s birthday, April 8th in lunar calendar</p>
<dt>*</p>
<dd>Harvest Moon Day, August 14th, 15th, 16th in lunar calendar</dl>
<p> Holidays for the Korea exchange (data from &lt;<a rel="nofollow" href="http://www.krx.co.kr">http://www.krx.co.kr</a>&gt; or &lt;<a href="http://www.dooriworld.com/daishin/holiday/holiday.html">http://www.dooriworld.com/daishin/holiday/holiday.html</a>&gt;): </p>
<dl COMPACT>
<dt>*</p>
<dd>Public holidays as listed above</p>
<dt>*</p>
<dd>Year-end closing</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>Public holidays.</p>
<dt><i>KRX </i></p>
<dd>Korea exchange. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
