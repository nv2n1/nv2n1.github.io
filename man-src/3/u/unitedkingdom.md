---
title: "unitedkingdom(3)"
name: "unitedkingdom"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unitedkingdom/"
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
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Early May Bank Holiday, first Monday of May</p>
<dt>*</p>
<dd>Spring Bank Holiday, last Monday of May</p>
<dt>*</p>
<dd>Summer Bank Holiday, last Monday of August</p>
<dt>*</p>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dl>
<p> Holidays for the stock exchange: </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Early May Bank Holiday, first Monday of May</p>
<dt>*</p>
<dd>Spring Bank Holiday, last Monday of May</p>
<dt>*</p>
<dd>Summer Bank Holiday, last Monday of August</p>
<dt>*</p>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dl>
<p> Holidays for the metals exchange: </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday)</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Easter Monday</p>
<dt>*</p>
<dd>Early May Bank Holiday, first Monday of May</p>
<dt>*</p>
<dd>Spring Bank Holiday, last Monday of May</p>
<dt>*</p>
<dd>Summer Bank Holiday, last Monday of August</p>
<dt>*</p>
<dd>Christmas Day, December 25th (possibly moved to Monday or Tuesday)</p>
<dt>*</p>
<dd>Boxing Day, December 26th (possibly moved to Monday or Tuesday)</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>add LIFFE</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>UK calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>Exchange </i></p>
<dd>London stock-exchange calendar. </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
