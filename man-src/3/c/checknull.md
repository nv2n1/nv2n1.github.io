---
title: "checknull(3)"
name: "checknull"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checknull/"
description: "ql/utilities/dataformatters.hpp – output manipulators"
---

<h2 class="name">NAME</h2>
<p> ql/utilities/dataformatters.hpp &#8211; output manipulators </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/utilities/null.hpp&gt;<br />
 #include &lt;ostream&gt; </p>
<h3>Functions</h3>
<p> template&lt;typename T &gt; std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const null_checker&lt; T &gt; &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const ordinal_holder &amp;) </p>
<p> template&lt;typename T &gt; std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const power_of_two_holder&lt; T &gt; &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const percent_holder &amp;) </p>
<p> template&lt;typename T &gt; detail::null_checker&lt; T &gt; <code>checknull</code> (T)<br />
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
<p> output manipulators </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
