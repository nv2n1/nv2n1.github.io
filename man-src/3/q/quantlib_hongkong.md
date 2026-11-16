---
title: "quantlib_hongkong(3)"
name: "quantlib_hongkong"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_hongkong/"
description: "QuantLib::HongKong – Hong Kong calendars."
---

<p>QuantLib::HongKong &#8211; Hong Kong calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/hongkong.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>HKEx</code> } </p>
<h3>Public Member Functions</h3>
<p><code>HongKong</code> (<code>Market</code> m=HKEx) </p>
<h2>Detailed Description</h2>
<p>Hong Kong calendars. </p>
<p> Holidays: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Ching Ming Festival, April 5th</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Labor Day, May 1st</dd>
<dt>*</dt>
<dd>SAR Establishment Day, July 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>National Day, October 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Christmas, December 25th</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday)</dd></dl>
<p> Other holidays for which no rule is given (data available for 2004-2007 only:) </p>
<dl COMPACT>
<dt>*</dt>
<dd>Lunar New Year</dd>
<dt>*</dt>
<dd>Chinese New Year</dd>
<dt>*</dt>
<dd>Buddha&#8217;s birthday</dd>
<dt>*</dt>
<dd>Tuen NG Festival</dd>
<dt>*</dt>
<dd>Mid-autumn Festival</dd>
<dt>*</dt>
<dd>Chung Yeung Festival</dd></dl>
<p> Data from &lt;<a rel="nofollow" href="http://www.hkex.com.hk">http://www.hkex.com.hk</a>&gt;</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>HKEx </i></dt>
<dd>Hong Kong stock exchange. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
