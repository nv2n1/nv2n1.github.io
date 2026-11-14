---
title: "quantlib_target(3)"
name: "quantlib_target"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_target/"
description: "QuantLib::TARGET – TARGET calendar"
---

<p>QuantLib::TARGET &#8211; TARGET calendar </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/target.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h2>Detailed Description</h2>
<p>TARGET calendar </p>
<p> Holidays (see <a rel="nofollow" href="http://www.ecb.int">http://www.ecb.int</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st</p>
<dt>*</p>
<dd>Good Friday (since 2000)</p>
<dt>*</p>
<dd>Easter Monday (since 2000)</p>
<dt>*</p>
<dd>Labour Day, May 1st (since 2000)</p>
<dt>*</p>
<dd>Christmas, December 25th</p>
<dt>*</p>
<dd>Day of Goodwill, December 26th (since 2000)</p>
<dt>*</p>
<dd>December 31st (1998, 1999, and 2001)</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
