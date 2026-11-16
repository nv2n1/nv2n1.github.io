---
title: "eurex(3)"
name: "eurex"
section: "3"
letter: "e"
url: "/docs/linux/man/3-eurex/"
description: "QuantLib::Germany – German calendars."
---

<p>QuantLib::Germany &#8211; German calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/germany.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>FrankfurtStockExchange</code>, <code>Xetra</code>, <code>Eurex</code> }<br />
 <i>German calendars. </i></p>
<h3>Public Member Functions</h3>
<p><code>Germany</code> (<code>Market</code> market=FrankfurtStockExchange) </p>
<h2>Detailed Description</h2>
<p>German calendars. </p>
<p> Public holidays: </p>
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
<dd>Ascension Thursday</dd>
<dt>*</dt>
<dd>Whit Monday</dd>
<dt>*</dt>
<dd>Corpus Christi</dd>
<dt>*</dt>
<dd>Labour Day, May 1st</dd>
<dt>*</dt>
<dd>National Day, October 3rd</dd>
<dt>*</dt>
<dd>Christmas Eve, December 24th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th</dd>
<dt>*</dt>
<dd>New Year&#8217;s Eve, December 31st</dd></dl>
<p> Holidays for the Frankfurt <code>Stock</code> exchange (data from <a rel="nofollow" href="http://deutsche-boerse.com/">http://deutsche-boerse.com/</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Christmas Holiday, December 26th</dd>
<dt>*</dt>
<dd>New Year&#8217;s Eve, December 31st</dd></dl>
<p> Holidays for the Xetra exchange (data from <a rel="nofollow" href="http://deutsche-boerse.com/">http://deutsche-boerse.com/</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Christmas Holiday, December 26th</dd>
<dt>*</dt>
<dd>New Year&#8217;s Eve, December 31st</dd></dl>
<p> Holidays for the Eurex exchange (data from <a rel="nofollow" href="http://www.eurexchange.com/index.html">http://www.eurexchange.com/index.html</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Christmas Holiday, December 26th</dd>
<dt>*</dt>
<dd>New Year&#8217;s Eve, December 31st</dd></dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>German calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>generic settlement calendar</dd>
<dt><i>FrankfurtStockExchange </i></dt>
<dd>Frankfurt stock-exchange.</dd>
<dt><i>Xetra </i></dt>
<dd>Xetra.</dd>
<dt><i>Eurex </i></dt>
<dd>Eurex. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
