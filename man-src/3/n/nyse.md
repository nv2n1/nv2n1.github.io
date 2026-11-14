---
title: "nyse(3)"
name: "nyse"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nyse/"
description: "QuantLib::UnitedStates – United States calendars."
---

<p>QuantLib::UnitedStates &#8211; United States calendars. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendars/unitedstates.hpp&gt; </p>
<p> Inherits <code>QuantLib::Calendar</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Market</code> { <code>Settlement</code>, <code>NYSE</code>, <code>GovernmentBond</code>, <code>NERC</code> }<br />
 <i>US calendars. </i></p>
<h3>Public Member Functions</h3>
<p><code>UnitedStates</code> (<code>Market</code> market=<code>Settlement</code>) </p>
<h2>Detailed Description</h2>
<p>United States calendars. </p>
<p> Public holidays (see: <a rel="nofollow" href="http://www.opm.gov/fedhol/">http://www.opm.gov/fedhol/</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday if actually on Sunday, or to Friday if on Saturday)</p>
<dt>*</p>
<dd>Martin Luther King&#8217;s birthday, third Monday in January</p>
<dt>*</p>
<dd>Presidents&#8217; Day (a.k.a. Washington&#8217;s birthday), third Monday in February</p>
<dt>*</p>
<dd>Memorial Day, last Monday in May</p>
<dt>*</p>
<dd>Independence Day, July 4th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Labor Day, first Monday in September</p>
<dt>*</p>
<dd>Columbus Day, second Monday in October</p>
<dt>*</p>
<dd>Veterans&#8217; Day, November 11th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Thanksgiving Day, fourth Thursday in November</p>
<dt>*</p>
<dd>Christmas, December 25th (moved to Monday if Sunday or Friday if Saturday)</dl>
<p> Holidays for the stock exchange (data from <a rel="nofollow" href="http://www.nyse.com">http://www.nyse.com</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday if actually on Sunday)</p>
<dt>*</p>
<dd>Martin Luther King&#8217;s birthday, third Monday in January (since 1998)</p>
<dt>*</p>
<dd>Presidents&#8217; Day (a.k.a. Washington&#8217;s birthday), third Monday in February</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Memorial Day, last Monday in May</p>
<dt>*</p>
<dd>Independence Day, July 4th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Labor Day, first Monday in September</p>
<dt>*</p>
<dd>Thanksgiving Day, fourth Thursday in November</p>
<dt>*</p>
<dd>Presidential election day, first Tuesday in November of election years (until 1980)</p>
<dt>*</p>
<dd>Christmas, December 25th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Special historic closings (see <a rel="nofollow" href="http://www.nyse.com/pdfs/closings.pdf)">http://www.nyse.com/pdfs/closings.pdf)</a></dl>
<p> Holidays for the government bond market (data from <a rel="nofollow" href="http://www.bondmarkets.com">http://www.bondmarkets.com</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday if actually on Sunday)</p>
<dt>*</p>
<dd>Martin Luther King&#8217;s birthday, third Monday in January</p>
<dt>*</p>
<dd>Presidents&#8217; Day (a.k.a. Washington&#8217;s birthday), third Monday in February</p>
<dt>*</p>
<dd>Good Friday</p>
<dt>*</p>
<dd>Memorial Day, last Monday in May</p>
<dt>*</p>
<dd>Independence Day, July 4th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Labor Day, first Monday in September</p>
<dt>*</p>
<dd>Columbus Day, second Monday in October</p>
<dt>*</p>
<dd>Veterans&#8217; Day, November 11th (moved to Monday if Sunday or Friday if Saturday)</p>
<dt>*</p>
<dd>Thanksgiving Day, fourth Thursday in November</p>
<dt>*</p>
<dd>Christmas, December 25th (moved to Monday if Sunday or Friday if Saturday)</dl>
<p> Holidays for the North American Energy Reliability Council (data from <a rel="nofollow" href="http://www.nerc.com/~oc/offpeaks.html">http://www.nerc.com/~oc/offpeaks.html</a>): </p>
<dl COMPACT>
<dt>*</p>
<dd>Saturdays</p>
<dt>*</p>
<dd>Sundays</p>
<dt>*</p>
<dd>New Year&#8217;s Day, January 1st (possibly moved to Monday if actually on Sunday)</p>
<dt>*</p>
<dd>Memorial Day, last Monday in May</p>
<dt>*</p>
<dd>Independence Day, July 4th (moved to Monday if Sunday)</p>
<dt>*</p>
<dd>Labor Day, first Monday in September</p>
<dt>*</p>
<dd>Thanksgiving Day, fourth Thursday in November</p>
<dt>*</p>
<dd>Christmas, December 25th (moved to Monday if Sunday)</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned results is tested against a list of known holidays.</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, and <code>CallableBonds.cpp</code>.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Market</code></h3>
<p>US calendars. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Settlement </i></p>
<dd>generic settlement calendar</p>
<dt><i>NYSE </i></p>
<dd>New York stock exchange calendar.</p>
<dt><i>GovernmentBond </i></p>
<dd>government-bond calendar</p>
<dt><i>NERC </i></p>
<dd>off-peak days for NERC </p>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
