---
title: "isholiday(3)"
name: "isholiday"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isholiday/"
description: "QuantLib::Calendar – calendar class"
---

<p>QuantLib::Calendar &#8211; calendar class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/calendar.hpp&gt; </p>
<p> Inherited by <code>Argentina</code>, <code>Australia</code>, <code>BespokeCalendar</code>, <code>Brazil</code>, <code>Canada</code>, <code>China</code>, <code>CzechRepublic</code>, <code>Denmark</code>, <code>Finland</code>, <code>Germany</code>, <code>HongKong</code>, <code>Hungary</code>, <code>Iceland</code>, <code>India</code>, <code>Indonesia</code>, <code>Italy</code>, <code>Japan</code>, <code>JointCalendar</code>, <code>Mexico</code>, <code>NewZealand</code>, <code>Norway</code>, <code>NullCalendar</code>, <code>Poland</code>, <code>SaudiArabia</code>, <code>Singapore</code>, <code>Slovakia</code>, <code>SouthAfrica</code>, <code>SouthKorea</code>, <code>Sweden</code>, <code>Switzerland</code>, <code>Taiwan</code>, <code>TARGET</code>, <code>Turkey</code>, <code>Ukraine</code>, <code>UnitedKingdom</code>, and <code>UnitedStates</code>. </p>
<h3>Classes</h3>
<p>class <code>Impl</code><br />
 <i>abstract base class for calendar implementations </i><br />
 class <code>OrthodoxImpl</code><br />
 <i>partial calendar implementation </i><br />
 class <code>WesternImpl</code><br />
 <i>partial calendar implementation </i></p>
<h3>Public Member Functions</h3>
<p><code>Calendar</code> () </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Calendar</code> &amp;) </p>
<h3>Calendar interface</h3>
<p>bool <code>empty</code> () const<br />
 <i>Returns whether or not the calendar is initialized. </i><br />
 std::string <code>name</code> () const<br />
 <i>Returns the name of the calendar. </i><br />
 bool <code>isBusinessDay</code> (const <code>Date</code> &amp;d) const </p>
<p> bool <code>isHoliday</code> (const <code>Date</code> &amp;d) const </p>
<p> bool <code>isWeekend</code> (<code>Weekday</code> w) const </p>
<p> bool <code>isEndOfMonth</code> (const <code>Date</code> &amp;d) const </p>
<p> <code>Date</code> <code>endOfMonth</code> (const <code>Date</code> &amp;d) const<br />
 <i>last business day of the month to which the given date belongs </i><br />
 void <code>addHoliday</code> (const <code>Date</code> &amp;) </p>
<p> void <code>removeHoliday</code> (const <code>Date</code> &amp;) </p>
<p> <code>Date</code> <code>adjust</code> (const <code>Date</code> &amp;, <code>BusinessDayConvention</code> convention=Following) const </p>
<p> <code>Date</code> <code>advance</code> (const <code>Date</code> &amp;, <code>Integer</code> n, <code>TimeUnit</code> unit, <code>BusinessDayConvention</code> convention=Following, bool endOfMonth=false) const </p>
<p> <code>Date</code> <code>advance</code> (const <code>Date</code> &amp;date, const <code>Period</code> &amp;period, <code>BusinessDayConvention</code> convention=Following, bool endOfMonth=false) const </p>
<p> <code>BigInteger</code> <code>businessDaysBetween</code> (const <code>Date</code> &amp;from, const <code>Date</code> &amp;to, bool includeFirst=true, bool includeLast=false) const </p>
<p> static std::vector&lt; <code>Date</code> &gt; <code>holidayList</code> (const <code>Calendar</code> &amp;calendar, const <code>Date</code> &amp;from, const <code>Date</code> &amp;to, bool includeWeekEnds=false)<br />
 <i>Returns the holidays between two dates. </i></p>
<h2>Detailed Description</h2>
<p>calendar class </p>
<p> This class provides methods for determining whether a date is a business day or a holiday for a given market, and for incrementing/decrementing a date of a given number of business days. </p>
<p> The Bridge pattern is used to provide the base behavior of the calendar, namely, to determine whether a date is a business day. </p>
<p> A calendar should be defined for specific exchange holiday schedule or for general country holiday schedule. Legacy city holiday schedule calendars will be moved to the exchange/country convention. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the methods for adding and removing holidays are tested by inspecting the calendar before and after their invocation.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, <code>Repo.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Calendar</code> ()</h3>
<p>The default constructor returns a calendar with a null implementation, which is therefore unusable except as a placeholder.</p>
<h2>Member Function Documentation</h2>
<h3>std::string name () const</h3>
<p>Returns the name of the calendar. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This method is used for output and comparison between calendars. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<h3>bool isBusinessDay (const <code>Date</code> &amp; d) const</h3>
<p>Returns true iff the date is a business day for the given market.</p>
<h3>bool isHoliday (const <code>Date</code> &amp; d) const</h3>
<p>Returns true iff the date is a holiday for the given market.</p>
<h3>bool isWeekend (<code>Weekday</code> w) const</h3>
<p>Returns true iff the weekday is part of the weekend for the given market.</p>
<h3>bool isEndOfMonth (const <code>Date</code> &amp; d) const</h3>
<p>Returns true iff the date is last business day for the month in given market.</p>
<h3>void addHoliday (const <code>Date</code> &amp;)</h3>
<p>Adds a date to the set of holidays for the given calendar.</p>
<h3>void removeHoliday (const <code>Date</code> &amp;)</h3>
<p>Removes a date from the set of holidays for the given calendar.</p>
<h3><code>Date</code> adjust (const <code>Date</code> &amp;, <code>BusinessDayConvention</code> convention = Following) const</h3>
<p>Adjusts a non-business day to the appropriate near business day with respect to the given convention. </p>
<p> <code>Examples: </code> <code>Bonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>FittedBondCurve.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h3><code>Date</code> advance (const <code>Date</code> &amp;, <code>Integer</code> n, <code>TimeUnit</code> unit, <code>BusinessDayConvention</code> convention = Following, bool endOfMonth = false) const</h3>
<p>Advances the given date of the given number of business days and returns the result. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The input date is not modified.</dl>
<p> <code>Examples: </code> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h3><code>Date</code> advance (const <code>Date</code> &amp; date, const <code>Period</code> &amp; period, <code>BusinessDayConvention</code> convention = Following, bool endOfMonth = false) const</h3>
<p>Advances the given date as specified by the given period and returns the result. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The input date is not modified.</dl>
<h3><code>BigInteger</code> businessDaysBetween (const <code>Date</code> &amp; from, const <code>Date</code> &amp; to, bool includeFirst = true, bool includeLast = false) const</h3>
<p>Calculates the number of business days between two given dates and returns the result.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;) [related]</h3>
<p>Returns true iff the two calendars belong to the same derived class.</p>
<h3>bool operator!= (const <code>Calendar</code> &amp;, const <code>Calendar</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Calendar</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
