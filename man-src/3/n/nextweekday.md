---
title: "nextweekday(3)"
name: "nextweekday"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextweekday/"
description: "QuantLib::Date – Concrete date class."
---

<p>QuantLib::Date &#8211; Concrete date class. </p>
<h2>Synopsis</h2>
<pre><code>static Date todaysDate ()


today's date.


static Date minDate ()


earliest allowed date


static Date maxDate ()


latest allowed date


static bool isLeap (Year y)


whether the given year is a leap one


static Date endOfMonth (const Date &amp;d)


last day of the month to which the given date belongs


static bool isEndOfMonth (const Date &amp;d)


whether a date is the last day of its month


static Date nextWeekday (const Date &amp;d, Weekday w)


next given weekday following or equal to the given date


static Date nthWeekday (Size n, Weekday w, Month m, Year y)


n-th given weekday in the given month and year




Related Functions

(Note that these are not member functions.)


BigInteger operator- (const Date &amp;, const Date &amp;)


Difference in days between dates.


bool operator== (const Date &amp;, const Date &amp;)



bool operator!= (const Date &amp;, const Date &amp;)



bool operator&lt; (const Date &amp;, const Date &amp;)



bool operator&lt;= (const Date &amp;, const Date &amp;)



bool operator&gt; (const Date &amp;, const Date &amp;)



bool operator&gt;= (const Date &amp;, const Date &amp;)



std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Date &amp;)</code></pre>
<h3>Public Member Functions</h3>
<p><code>constructors</code> </p>
<p> <code>Date</code> ()<br />
 <i>Default constructor returning a null date. </i><br />
 <code>Date</code> (<code>BigInteger</code> serialNumber)<br />
 <i>Constructor taking a serial number as given by Applix or Excel. </i><br />
 <code>Date</code> (Day d, <code>Month</code> m, Year y)<br />
 <i>More traditional constructor. </i> <code>inspectors</code><br />
 static Date todaysDate ()</p>
<p>today&#8217;s date.</p>
<p>static Date minDate ()</p>
<p>earliest allowed date</p>
<p>static Date maxDate ()</p>
<p>latest allowed date</p>
<p>static bool isLeap (Year y)</p>
<p>whether the given year is a leap one</p>
<p>static Date endOfMonth (const Date &amp;d)</p>
<p>last day of the month to which the given date belongs</p>
<p>static bool isEndOfMonth (const Date &amp;d)</p>
<p>whether a date is the last day of its month</p>
<p>static Date nextWeekday (const Date &amp;d, Weekday w)</p>
<p>next given weekday following or equal to the given date</p>
<p>static Date nthWeekday (Size n, Weekday w, Month m, Year y)</p>
<p>n-th given weekday in the given month and year</p>
<p>Related Functions</p>
<p>(Note that these are not member functions.)</p>
<p>BigInteger operator- (const Date &amp;, const Date &amp;)</p>
<p>Difference in days between dates.</p>
<p>bool operator== (const Date &amp;, const Date &amp;)</p>
<p>bool operator!= (const Date &amp;, const Date &amp;)</p>
<p>bool operator&lt; (const Date &amp;, const Date &amp;)</p>
<p>bool operator&lt;= (const Date &amp;, const Date &amp;)</p>
<p>bool operator&gt; (const Date &amp;, const Date &amp;)</p>
<p>bool operator&gt;= (const Date &amp;, const Date &amp;)</p>
<p>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Date &amp;) <code>date algebra</code><br />
 static Date todaysDate ()</p>
<p>today&#8217;s date.</p>
<p>static Date minDate ()</p>
<p>earliest allowed date</p>
<p>static Date maxDate ()</p>
<p>latest allowed date</p>
<p>static bool isLeap (Year y)</p>
<p>whether the given year is a leap one</p>
<p>static Date endOfMonth (const Date &amp;d)</p>
<p>last day of the month to which the given date belongs</p>
<p>static bool isEndOfMonth (const Date &amp;d)</p>
<p>whether a date is the last day of its month</p>
<p>static Date nextWeekday (const Date &amp;d, Weekday w)</p>
<p>next given weekday following or equal to the given date</p>
<p>static Date nthWeekday (Size n, Weekday w, Month m, Year y)</p>
<p>n-th given weekday in the given month and year</p>
<p>Related Functions</p>
<p>(Note that these are not member functions.)</p>
<p>BigInteger operator- (const Date &amp;, const Date &amp;)</p>
<p>Difference in days between dates.</p>
<p>bool operator== (const Date &amp;, const Date &amp;)</p>
<p>bool operator!= (const Date &amp;, const Date &amp;)</p>
<p>bool operator&lt; (const Date &amp;, const Date &amp;)</p>
<p>bool operator&lt;= (const Date &amp;, const Date &amp;)</p>
<p>bool operator&gt; (const Date &amp;, const Date &amp;)</p>
<p>bool operator&gt;= (const Date &amp;, const Date &amp;)</p>
<p>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Date &amp;) <code>static methods</code> </p>
<pre><code>static Date todaysDate ()


today's date.


static Date minDate ()


earliest allowed date


static Date maxDate ()


latest allowed date


static bool isLeap (Year y)


whether the given year is a leap one


static Date endOfMonth (const Date &amp;d)


last day of the month to which the given date belongs


static bool isEndOfMonth (const Date &amp;d)


whether a date is the last day of its month


static Date nextWeekday (const Date &amp;d, Weekday w)


next given weekday following or equal to the given date


static Date nthWeekday (Size n, Weekday w, Month m, Year y)


n-th given weekday in the given month and year




Related Functions

(Note that these are not member functions.)


BigInteger operator- (const Date &amp;, const Date &amp;)


Difference in days between dates.


bool operator== (const Date &amp;, const Date &amp;)



bool operator!= (const Date &amp;, const Date &amp;)



bool operator&lt; (const Date &amp;, const Date &amp;)



bool operator&lt;= (const Date &amp;, const Date &amp;)



bool operator&gt; (const Date &amp;, const Date &amp;)



bool operator&gt;= (const Date &amp;, const Date &amp;)



std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Date &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>Concrete date class. </p>
<p> This class provides methods to inspect dates as well as methods and operators which implement a limited date algebra (increasing and decreasing dates, and calculating their difference). </p>
<p> <code>Tests</code></p>
<dl>
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
