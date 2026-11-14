---
title: "date(3)"
name: "date"
section: "3"
letter: "d"
url: "/docs/linux/man/3-date/"
description: "ql/time/date.hpp – date- and time-related classes, typedefs and enumerations"
---

<h2 class="name">NAME</h2>
<p> ql/time/date.hpp &#8211; date- and time-related classes, typedefs and enumerations </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/time/period.hpp&gt;<br />
 #include &lt;ql/time/weekday.hpp&gt;<br />
 #include &lt;ql/types.hpp&gt;<br />
 #include &lt;utility&gt;<br />
 #include &lt;functional&gt; </p>
<h3>Classes</h3>
<p> class <code>Date</code><br />
 <i>Concrete date class. </i></p>
<h3>Typedefs</h3>
<p> typedef Integer <code>Day</code><br />
 <i>Day number. </i><br />
 typedef Integer <code>Year</code><br />
 <i>Year number. </i></p>
<h3>Enumerations</h3>
<p> enum <code>Month</code> { <code>January</code> = 1, <code>February</code> = 2, <code>March</code> = 3, <code>April</code> = 4, <code>May</code> = 5, <code>June</code> = 6, <code>July</code> = 7, <code>August</code> = 8, <code>September</code> = 9, <code>October</code> = 10, <code>November</code> = 11, <code>December</code> = 12, <code>Jan</code> = 1, <code>Feb</code> = 2, <code>Mar</code> = 3, <code>Apr</code> = 4, <code>Jun</code> = 6, <code>Jul</code> = 7, <code>Aug</code> = 8, <code>Sep</code> = 9, <code>Oct</code> = 10, <code>Nov</code> = 11, <code>Dec</code> = 12 }<br />
 <i>Month names. </i></p>
<h3>Functions</h3>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const short_date_holder &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const long_date_holder &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const iso_date_holder &amp;) </p>
<p> detail::short_date_holder <code>short_date</code> (const Date &amp;)<br />
 <i>output dates in short format (mm/dd/yyyy) </i><br />
 detail::long_date_holder <code>long_date</code> (const Date &amp;)<br />
 <i>output dates in long format (Month ddth, yyyy) </i><br />
 detail::iso_date_holder <code>iso_date</code> (const Date &amp;)<br />
 <i>output dates in ISO format (yyyy-mm-dd) </i><br />
 BigInteger <code>operator-</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator==</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator!=</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator&lt;</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator&lt;=</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator&gt;</code> (const Date &amp;d1, const Date &amp;d2) </p>
<p> bool <code>operator&gt;=</code> (const Date &amp;d1, const Date &amp;d2) </p>
<h2>Detailed Description</h2>
<p> date- and time-related classes, typedefs and enumerations </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
