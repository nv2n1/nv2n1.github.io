---
title: "hkex(3)"
name: "hkex"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hkex/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Ching Ming Festival, April 5th</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Labor Day, May 1st</p>
<dt>*</p>
<dd>SAR Establishment Day, July 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>National Day, October 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday)</dl>
<p> Other holidays for which no rule is given (data available for 2004-2007 only:) </p>
<dl COMPACT>
<dt>*</p>
<dd>Lunar New Year</p>
<dt>*</p>
<dd>Chinese New Year</p>
<dt>*</p>
<dd>Buddha&#8217;s birthday</p>
<dt>*</p>
<dd>Tuen NG Festival</p>
<dt>*</p>
<dd>Mid-autumn Festival</p>
<dt>*</p>
<dd>Chung Yeung Festival</dl>
<p> Data from &lt;<a rel="nofollow" href="http://www.hkex.com.hk">http://www.hkex.com.hk</a>&gt;</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>HKEx </i></p>
<dd>Hong Kong stock exchange. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
