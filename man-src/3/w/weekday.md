---
title: "weekday(3)"
name: "weekday"
section: "3"
letter: "w"
url: "/docs/linux/man/3-weekday/"
description: "ql/time/weekday.hpp – Weekday enumeration."
---

<p>ql/time/weekday.hpp &#8211; Weekday enumeration. </p>
<h2>Synopsis</h2>
<pre><code>enum Weekday { Sunday =  1, Monday =  2, Tuesday =  3, Wednesday =  4, Thursday =  5, Friday =  6, Saturday =  7, Sun =  1, Mon =  2, Tue =  3, Wed =  4, Thu =  5, Fri =  6, Sat =  7 }



Functions</code></pre>
<h3>Enumerations</h3>
<pre><code>enum Weekday { Sunday =  1, Monday =  2, Tuesday =  3, Wednesday =  4, Thursday =  5, Friday =  6, Saturday =  7, Sun =  1, Mon =  2, Tue =  3, Wed =  4, Thu =  5, Fri =  6, Sat =  7 }



Functions</code></pre>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const long_weekday_holder &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const short_weekday_holder &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const shortest_weekday_holder &amp;) </p>
<p> detail::long_weekday_holder <code>long_weekday</code> (Weekday)<br />
 <i>output weekdays in long format </i><br />
 detail::short_weekday_holder <code>short_weekday</code> (Weekday)<br />
 <i>output weekdays in short format (three letters) </i><br />
 detail::shortest_weekday_holder <code>shortest_weekday</code> (Weekday)<br />
 <i>output weekdays in shortest format (two letters) </i></p>
<h2>Detailed Description</h2>
<p>Weekday enumeration.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
