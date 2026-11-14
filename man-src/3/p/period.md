---
title: "period(3)"
name: "period"
section: "3"
letter: "p"
url: "/docs/linux/man/3-period/"
description: "ql/time/period.hpp – period- and frequency-related classes and enumerations"
---

<p>ql/time/period.hpp &#8211; period- and frequency-related classes and enumerations </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/time/frequency.hpp&gt;

#include &lt;ql/time/timeunit.hpp&gt;

#include &lt;ql/types.hpp&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>Period</code></p>
<h3>Functions</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const long_period_holder &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const short_period_holder &amp;) </p>
<p> detail::long_period_holder <code>long_period</code> (const Period &amp;)<br />
 <i>output periods in long format (e.g. &#8216;2 weeks&#8217;) </i><br />
 detail::short_period_holder <code>short_period</code> (const Period &amp;)<br />
 <i>output periods in short format (e.g. &#8216;2w&#8217;) </i><br />
 template&lt;typename T &gt; Period <code>operator*</code> (T n, TimeUnit units) </p>
<p> template&lt;typename T &gt; Period <code>operator*</code> (TimeUnit units, T n) </p>
<p> Period <code>operator-</code> (const Period &amp;p) </p>
<p> Period <code>operator*</code> (Integer n, const Period &amp;p) </p>
<p> Period <code>operator*</code> (const Period &amp;p, Integer n) </p>
<p> bool <code>operator==</code> (const Period &amp;p1, const Period &amp;p2) </p>
<p> bool <code>operator!=</code> (const Period &amp;p1, const Period &amp;p2) </p>
<p> bool <code>operator&gt;</code> (const Period &amp;p1, const Period &amp;p2) </p>
<p> bool <code>operator&lt;=</code> (const Period &amp;p1, const Period &amp;p2) </p>
<p> bool <code>operator&gt;=</code> (const Period &amp;p1, const Period &amp;p2)</p>
<h2>Detailed Description</h2>
<p>period- and frequency-related classes and enumerations</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
