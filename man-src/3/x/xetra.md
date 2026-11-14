---
title: "xetra(3)"
name: "xetra"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xetra/"
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
<dd>Ascension Thursday</p>
<dt>*</p>
<dd>Whit Monday</p>
<dt>*</p>
<dd>Corpus Christi</p>
<dt>*</p>
<dd>Labour Day, May 1st</p>
<dt>*</p>
<dd>National Day, October 3rd</p>
<dt>*</p>
<dd>Christmas Eve, December 24th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Boxing Day, December 26th</p>
<dt>*</p>
<dd>New Year&#8217;s Eve, December 31st</dl>
<p> Holidays for the Frankfurt <code>Stock</code> exchange (data from <a rel="nofollow" href="http://deutsche-boerse.com/">http://deutsche-boerse.com/</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Christmas Holiday, December 26th</p>
<dt>*</p>
<dd>New Year&#8217;s Eve, December 31st</dl>
<p> Holidays for the Xetra exchange (data from <a rel="nofollow" href="http://deutsche-boerse.com/">http://deutsche-boerse.com/</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Christmas Holiday, December 26th</p>
<dt>*</p>
<dd>New Year&#8217;s Eve, December 31st</dl>
<p> Holidays for the Eurex exchange (data from <a rel="nofollow" href="http://www.eurexchange.com/index.html">http://www.eurexchange.com/index.html</a>): </p>
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
<dd>Christmas&#8217; Eve, December 24th</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Christmas Holiday, December 26th</p>
<dt>*</p>
<dd>New Year&#8217;s Eve, December 31st</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>German calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>FrankfurtStockExchange </i></p>
<dd>Frankfurt stock-exchange.</p>
<dt><i>Xetra </i></p>
<dd>Xetra.</p>
<dt><i>Eurex </i></p>
<dd>Eurex. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
