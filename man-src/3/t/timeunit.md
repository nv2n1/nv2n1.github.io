---
title: "timeunit(3)"
name: "timeunit"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timeunit/"
description: "Date and time calculations –"
---

<p>Date and time calculations &#8211; </p>
<h3>Classes</h3>
<p>class <code>DateInterval</code><br />
 <i></i><code>Date</code> interval described by a number of a given time unit.<br />
 class <code>PricingPeriod</code><br />
 <i>Time pricingperiod described by a number of a given time unit. </i><br />
 class <code>Calendar</code><br />
 <i>calendar class </i><br />
 class <code>Date</code><br />
 <i>Concrete date class. </i><br />
 struct <code>DateGeneration</code><br />
 <i>Date-generation rule. </i><br />
 class <code>DayCounter</code><br />
 <i>day counter class </i><br />
 class <code>Period</code> </p>
<h3>Modules</h3>
<p><code>Calendars</code> </p>
<p> <code>Day counters</code> </p>
<h3>Typedefs</h3>
<p>typedef Integer <code>Day</code><br />
 <i>Day number. </i><br />
 typedef Integer <code>Year</code><br />
 <i>Year number. </i></p>
<h3>Enumerations</h3>
<p>enum <code>BusinessDayConvention</code> { <code>Following</code>, <code>ModifiedFollowing</code>, <code>Preceding</code>, <code>ModifiedPreceding</code>, <code>Unadjusted</code> }<br />
 <i>Business Day conventions. </i><br />
 enum <code>Month</code> { <code>January</code> = 1, <code>February</code> = 2, <code>March</code> = 3, <code>April</code> = 4, <code>May</code> = 5, <code>June</code> = 6, <code>July</code> = 7, <code>August</code> = 8, <code>September</code> = 9, <code>October</code> = 10, <code>November</code> = 11, <code>December</code> = 12, <code>Jan</code> = 1, <code>Feb</code> = 2, <code>Mar</code> = 3, <code>Apr</code> = 4, <code>Jun</code> = 6, <code>Jul</code> = 7, <code>Aug</code> = 8, <code>Sep</code> = 9, <code>Oct</code> = 10, <code>Nov</code> = 11, <code>Dec</code> = 12 }<br />
 <i>Month names. </i><br />
 enum <code>Frequency</code> { <code>NoFrequency</code> = -1, <code>Once</code> = 0, <code>Annual</code> = 1, <code>Semiannual</code> = 2, <code>EveryFourthMonth</code> = 3, <code>Quarterly</code> = 4, <code>Bimonthly</code> = 6, <code>Monthly</code> = 12, <code>EveryFourthWeek</code> = 13, <code>Biweekly</code> = 26, <code>Weekly</code> = 52, <code>Daily</code> = 365, <code>OtherFrequency</code> = 999 }<br />
 <i>Frequency of events. </i><br />
 enum <code>TimeUnit</code> { <code>Days</code>, <code>Weeks</code>, <code>Months</code>, <code>Years</code> }<br />
 <i>Units used to describe time periods. </i><br />
 enum <code>Weekday</code> { <code>Sunday</code> = 1, <code>Monday</code> = 2, <code>Tuesday</code> = 3, <code>Wednesday</code> = 4, <code>Thursday</code> = 5, <code>Friday</code> = 6, <code>Saturday</code> = 7, <code>Sun</code> = 1, <code>Mon</code> = 2, <code>Tue</code> = 3, <code>Wed</code> = 4, <code>Thu</code> = 5, <code>Fri</code> = 6, <code>Sat</code> = 7 } </p>
<h2>Detailed Description</h2>
<p>The concrete class <code>QuantLib::Date</code> implements the concept of date. Its functionalities include: </p>
<dl COMPACT>
<dt>*</p>
<dd>providing basic information such as weekday, day of the month, day of the year, month, and year;</dl>
<dl COMPACT>
<dt>*</p>
<dd>comparing two dates to determine whether they are equal, or which one is the earlier or later, or the difference between them expressed in days;</dl>
<dl COMPACT>
<dt>*</p>
<dd>incrementing or decrementing a date of a given number of days, or of a given period expressed in weeks, months, or years.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef Integer Day</h3>
<p>Day number. </p>
<h3>typedef Integer Year</h3>
<p>Year number. </p>
<h2>Enumeration Type Documentation</h2>
<h3>enum BusinessDayConvention</h3>
<p>Business Day conventions. </p>
<p> These conventions specify the algorithm used to adjust a date in case it is not a valid business day. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Following </i></p>
<dd>Choose the first business day after the given holiday.</p>
<dt><i>ModifiedFollowing </i></p>
<dd>Choose the first business day after the given holiday unless it belongs to a different month, in which case choose the first business day before the holiday.</p>
<dt><i>Preceding </i></p>
<dd>Choose the first business day before the given holiday.</p>
<dt><i>ModifiedPreceding </i></p>
<dd>Choose the first business day before the given holiday unless it belongs to a different month, in which case choose the first business day after the holiday.</p>
<dt><i>Unadjusted </i></p>
<dd>Do not adjust.</dl>
<h3>enum Month</h3>
<p>Month names. </p>
<h3>enum Frequency</h3>
<p>Frequency of events. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>NoFrequency </i></p>
<dd>null frequency</p>
<dt><i>Once </i></p>
<dd>only once, e.g., a zero-coupon</p>
<dt><i>Annual </i></p>
<dd>once a year</p>
<dt><i>Semiannual </i></p>
<dd>twice a year</p>
<dt><i>EveryFourthMonth </i></p>
<dd>every fourth month</p>
<dt><i>Quarterly </i></p>
<dd>every third month</p>
<dt><i>Bimonthly </i></p>
<dd>every second month</p>
<dt><i>Monthly </i></p>
<dd>once a month</p>
<dt><i>EveryFourthWeek </i></p>
<dd>every fourth week</p>
<dt><i>Biweekly </i></p>
<dd>every second week</p>
<dt><i>Weekly </i></p>
<dd>once a week</p>
<dt><i>Daily </i></p>
<dd>once a day</p>
<dt><i>OtherFrequency </i></p>
<dd>some other unknown frequency</dl>
<h3>enum TimeUnit</h3>
<p>Units used to describe time periods. </p>
<h3>enum Weekday</h3>
<p>Day&#8217;s serial number MOD 7; WEEKDAY Excel function is the same except for Sunday = 7.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
