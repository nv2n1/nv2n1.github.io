---
title: "quantlib_unitedkingdom(3)"
name: "quantlib_unitedkingdom"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_unitedkingdom/"
description: "QuantLib::UnitedKingdom – United Kingdom calendars."
---

<p>QuantLib::UnitedKingdom &#8211; United Kingdom calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/unitedkingdom.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>Exchange</code>, <code>Metals</code> }<br />
 <i>UK calendars. </i></p>
<h3>Public Member Functions</h3>
<p><code>UnitedKingdom</code> (<code>Market</code> market=<code>Settlement</code>) </p>
<h2>Detailed Description</h2>
<p>United Kingdom calendars. </p>
<p> Public holidays (data from <a rel="nofollow" href="http://www.dti.gov.uk/er/bankhol.htm">http://www.dti.gov.uk/er/bankhol.htm</a>): </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Early May Bank Holiday, first Monday of May</dd>
<dt>*</dt>
<dd>Spring Bank Holiday, last Monday of May</dd>
<dt>*</dt>
<dd>Summer Bank Holiday, last Monday of August</dd>
<dt>*</dt>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dd></dl>
<p> Holidays for the stock exchange: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Early May Bank Holiday, first Monday of May</dd>
<dt>*</dt>
<dd>Spring Bank Holiday, last Monday of May</dd>
<dt>*</dt>
<dd>Summer Bank Holiday, last Monday of August</dd>
<dt>*</dt>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dd></dl>
<p> Holidays for the metals exchange: </p>
<dl COMPACT>
<dt>*</dt>
<dd>Saturdays</dd>
<dt>*</dt>
<dd>Sundays</dd>
<dt>*</dt>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</dd>
<dt>*</dt>
<dd>Good Friday</dd>
<dt>*</dt>
<dd>Easter Monday</dd>
<dt>*</dt>
<dd>Early May Bank Holiday, first Monday of May</dd>
<dt>*</dt>
<dd>Spring Bank Holiday, last Monday of May</dd>
<dt>*</dt>
<dd>Summer Bank Holiday, last Monday of August</dd>
<dt>*</dt>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</dd>
<dt>*</dt>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dd></dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>add LIFFE</dd></dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>UK calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></dt>
<dd>generic settlement calendar</dd>
<dt><i>Exchange </i></dt>
<dd>London stock-exchange calendar. </dd>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
