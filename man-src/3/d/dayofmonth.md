---
title: "dayofmonth(3)"
name: "dayofmonth"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dayofmonth/"
description: "QuantLib::Date – Concrete date class."
---

<p>QuantLib::Date &#8211; Concrete date class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/date.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>constructors</code> </p>
<p> <code>Date</code> ()<br />
 <i>Default constructor returning a null date. </i><br />
 <code>Date</code> (<code>BigInteger</code> serialNumber)<br />
 <i>Constructor taking a serial number as given by Applix or Excel. </i><br />
 <code>Date</code> (Day d, <code>Month</code> m, Year y)<br />
 <i>More traditional constructor. </i> </p>
<p> <code>inspectors</code> </p>
<p> <code>Weekday</code> <code>weekday</code> () const </p>
<p> Day <code>dayOfMonth</code> () const </p>
<p> Day <code>dayOfYear</code> () const<br />
 <i>One-based (Jan 1st = 1). </i><br />
 <code>Month</code> <code>month</code> () const </p>
<p> Year <code>year</code> () const </p>
<p> <code>BigInteger</code> <code>serialNumber</code> () const </p>
<p> <code>date algebra</code> </p>
<p> <code>Date</code> &amp; <code>operator+=</code> (<code>BigInteger</code> days)<br />
 <i>increments date by the given number of days </i><br />
 <code>Date</code> &amp; <code>operator+=</code> (const <code>Period</code> &amp;)<br />
 <i>increments date by the given period </i><br />
 <code>Date</code> &amp; <code>operator-=</code> (<code>BigInteger</code> days)<br />
 <i>decrement date by the given number of days </i><br />
 <code>Date</code> &amp; <code>operator-=</code> (const <code>Period</code> &amp;)<br />
 <i>decrements date by the given period </i><br />
 <code>Date</code> &amp; <code>operator++</code> ()<br />
 <i>1-day pre-increment </i><br />
 <code>Date</code> <code>operator++</code> (int)<br />
 <i>1-day post-increment </i><br />
 <code>Date</code> &amp; <code>operator&#8211;</code> ()<br />
 <i>1-day pre-decrement </i><br />
 <code>Date</code> <code>operator&#8211;</code> (int)<br />
 <i>1-day post-decrement </i><br />
 <code>Date</code> <code>operator+</code> (<code>BigInteger</code> days) const<br />
 <i>returns a new date incremented by the given number of days </i><br />
 <code>Date</code> <code>operator+</code> (const <code>Period</code> &amp;) const<br />
 <i>returns a new date incremented by the given period </i><br />
 <code>Date</code> <code>operator-</code> (<code>BigInteger</code> days) const<br />
 <i>returns a new date decremented by the given number of days </i><br />
 <code>Date</code> <code>operator-</code> (const <code>Period</code> &amp;) const<br />
 <i>returns a new date decremented by the given period </i></p>
<h3>Static Public Member Functions</h3>
<p><code>static methods</code> </p>
<p> static <code>Date</code> <code>todaysDate</code> ()<br />
 <i>today&#8217;s date. </i><br />
 static <code>Date</code> <code>minDate</code> ()<br />
 <i>earliest allowed date </i><br />
 static <code>Date</code> <code>maxDate</code> ()<br />
 <i>latest allowed date </i><br />
 static bool <code>isLeap</code> (Year y)<br />
 <i>whether the given year is a leap one </i><br />
 static <code>Date</code> <code>endOfMonth</code> (const <code>Date</code> &amp;d)<br />
 <i>last day of the month to which the given date belongs </i><br />
 static bool <code>isEndOfMonth</code> (const <code>Date</code> &amp;d)<br />
 <i>whether a date is the last day of its month </i><br />
 static <code>Date</code> <code>nextWeekday</code> (const <code>Date</code> &amp;d, <code>Weekday</code> w)<br />
 <i>next given weekday following or equal to the given date </i><br />
 static <code>Date</code> <code>nthWeekday</code> (Size n, <code>Weekday</code> w, <code>Month</code> m, Year y)<br />
 <i>n-th given weekday in the given month and year </i></p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 <code>BigInteger</code> <code>operator-</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;)<br />
 <i>Difference in days between dates. </i><br />
 bool <code>operator==</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> bool <code>operator&lt;</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> bool <code>operator&lt;=</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> bool <code>operator&gt;</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> bool <code>operator&gt;=</code> (const <code>Date</code> &amp;, const <code>Date</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Date</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Concrete date class. </p>
<p> This class provides methods to inspect dates as well as methods and operators which implement a limited date algebra (increasing and decreasing dates, and calculating their difference). </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>self-consistency of dates, serial numbers, days of month, months, and weekdays is checked over the whole date range.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, <code>Replication.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>Date</code> nextWeekday (const <code>Date</code> &amp; d, <code>Weekday</code> w) [static]</h3>
<p>next given weekday following or equal to the given date </p>
<p> E.g., the Friday following Tuesday, January 15th, 2002 was January 18th, 2002. </p>
<p> see <a rel="nofollow" href="http://www.cpearson.com/excel/DateTimeWS.htm">http://www.cpearson.com/excel/DateTimeWS.htm</a></p>
<h3>static <code>Date</code> nthWeekday (Size n, <code>Weekday</code> w, <code>Month</code> m, Year y) [static]</h3>
<p>n-th given weekday in the given month and year </p>
<p> E.g., the 4th Thursday of March, 1998 was March 26th, 1998. </p>
<p> see <a rel="nofollow" href="http://www.cpearson.com/excel/DateTimeWS.htm">http://www.cpearson.com/excel/DateTimeWS.htm</a></p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>bool operator&lt; (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>bool operator&lt;= (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>bool operator&gt; (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>bool operator&gt;= (const <code>Date</code> &amp;, const <code>Date</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Date</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
