---
title: "stdchronoutc_clockfrom_sys(3)"
name: "stdchronoutc_clockfrom_sys"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoutc_clockfrom_sys/"
description: "std::chrono::utc_clock::from_sys – std::chrono::utc_clock::from_sys"
---

<p>std::chrono::utc_clock::from_sys &#8211; std::chrono::utc_clock::from_sys</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;

static std::chrono::utc_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;(since C++ 20)

    from_sys(const std::chrono::sys_time&lt;Duration&gt; &amp;t);</code></pre>
<p>Converts a sys_time t to a utc_time u that represents the same point in time.<br />
u.time_since_epoch() &#8211; t.time_since_epoch() is equal to the number of leap seconds that was inserted between t and 1 January 1970. If t is the exact date of a leap second insertion, that leap second is counted as inserted. </p>
<h2>Return value</h2>
<p>A utc_time representing the same point in time as t. </p>
<h2>See also</h2>
<p>to_sys converts utc_time to sys_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
