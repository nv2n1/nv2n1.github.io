---
title: "tsec(3)"
name: "tsec"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tsec/"
description: "QuantLib::Taiwan – Taiwanese calendars."
---

<p>QuantLib::Taiwan &#8211; Taiwanese calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/taiwan.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>TSEC</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Taiwan</code> (<code>Market</code> m=TSEC) </p>
<h2>Detailed Description</h2>
<p>Taiwanese calendars. </p>
<p> Holidays for the <code>Taiwan</code> stock exchange (data from &lt;<a rel="nofollow" href="http://www.tse.com.tw/en/trading/trading_days.php">http://www.tse.com.tw/en/trading/trading_days.php</a>&gt;): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st</dd>
<dt>*</dt>
<dd>Peace Memorial Day, February 28</dd>
<dt>*</dt>
<dd>Labor Day, May 1st</dd>
<dt>*</dt>
<dd>Double Tenth National Day, October 10th</dd></dl>
<p> Other holidays for which no rule is given (data available for 2002-2008 only:) </p>
<dl COMPACT>
<dt>*</dt>
<dd>Chinese Lunar New Year</dd>
<dt>*</dt>
<dd>Tomb Sweeping Day</dd>
<dt>*</dt>
<dd>Dragon Boat Festival</dd>
<dt>*</dt>
<dd>Moon Festival</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>TSEC </i></dt>
<dd><code>Taiwan</code> stock exchange. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
