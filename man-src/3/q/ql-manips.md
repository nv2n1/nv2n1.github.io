---
title: "ql-manips(3)"
name: "ql-manips"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-manips/"
description: "Output manipulators –"
---

<p>Output manipulators &#8211;</p>
<h3>Functions</h3>
<p>detail::short_date_holder <code>short_date</code> (const Date &amp;)<br />
 <i>output dates in short format (mm/dd/yyyy) </i><br />
 detail::long_date_holder <code>long_date</code> (const Date &amp;)<br />
 <i>output dates in long format (Month ddth, yyyy) </i><br />
 detail::iso_date_holder <code>iso_date</code> (const Date &amp;)<br />
 <i>output dates in ISO format (yyyy-mm-dd) </i><br />
 detail::long_period_holder <code>long_period</code> (const Period &amp;)<br />
 <i>output periods in long format (e.g. &#8216;2 weeks&#8217;) </i><br />
 detail::short_period_holder <code>short_period</code> (const Period &amp;)<br />
 <i>output periods in short format (e.g. &#8216;2w&#8217;) </i><br />
 detail::long_weekday_holder <code>long_weekday</code> (Weekday)<br />
 <i>output weekdays in long format </i><br />
 detail::short_weekday_holder <code>short_weekday</code> (Weekday)<br />
 <i>output weekdays in short format (three letters) </i><br />
 detail::shortest_weekday_holder <code>shortest_weekday</code> (Weekday)<br />
 <i>output weekdays in shortest format (two letters) </i><br />
 template&lt;typename T &gt; detail::null_checker&lt; T &gt; <code>checknull</code> (T)<br />
 <i>check for nulls before output </i><br />
 detail::ordinal_holder <code>ordinal</code> (Size)<br />
 <i>outputs naturals as 1st, 2nd, 3rd&#8230; </i><br />
 template&lt;typename T &gt; detail::power_of_two_holder&lt; T &gt; <code>power_of_two</code> (T)<br />
 <i>output integers as powers of two </i><br />
 detail::percent_holder <code>percent</code> (Real)<br />
 <i>output reals as percentages </i><br />
 detail::percent_holder <code>rate</code> (Rate)<br />
 <i>output rates and spreads as percentages </i><br />
 detail::percent_holder <code>volatility</code> (Volatility)<br />
 <i>output volatilities as percentages </i></p>
<h2>Detailed Description</h2>
<p>Helper functions for creating formatted output.</p>
<h2>Function Documentation</h2>
<h3>detail::short_date_holder QuantLib::io::short_date (const Date &amp;)</h3>
<p>output dates in short format (mm/dd/yyyy)</p>
<h3>detail::long_date_holder QuantLib::io::long_date (const Date &amp;)</h3>
<p>output dates in long format (Month ddth, yyyy)</p>
<h3>detail::iso_date_holder QuantLib::io::iso_date (const Date &amp;)</h3>
<p>output dates in ISO format (yyyy-mm-dd)</p>
<h3>detail::long_period_holder QuantLib::io::long_period (const Period &amp;)</h3>
<p>output periods in long format (e.g. &#8216;2 weeks&#8217;)</p>
<h3>detail::short_period_holder QuantLib::io::short_period (const Period &amp;)</h3>
<p>output periods in short format (e.g. &#8216;2w&#8217;)</p>
<h3>detail::long_weekday_holder QuantLib::io::long_weekday (Weekday)</h3>
<p>output weekdays in long format</p>
<h3>detail::short_weekday_holder QuantLib::io::short_weekday (Weekday)</h3>
<p>output weekdays in short format (three letters)</p>
<h3>detail::shortest_weekday_holder QuantLib::io::shortest_weekday (Weekday)</h3>
<p>output weekdays in shortest format (two letters)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
