---
title: "stdchronoutc_clockto_sys(3)"
name: "stdchronoutc_clockto_sys"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoutc_clockto_sys/"
description: "std::chrono::utc_clock::to_sys – std::chrono::utc_clock::to_sys"
---

<p>std::chrono::utc_clock::to_sys &#8211; std::chrono::utc_clock::to_sys</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;

static std::chrono::sys_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;(since C++ 20)

    to_sys(const std::chrono::utc_time&lt;Duration&gt; &amp;t);</code></pre>
<p>Converts a utc_time t to a sys_time representing the same point in time (if possible).<br />
If t represents a time point during a leap second insertion, the last representable value of sys_time prior to the insertion of the leap second is returned. In all other cases, utc_clock::from_sys(utc_clock::to_sys(t)) == t. </p>
<h2>Return value</h2>
<p>A sys_time representing the same point in time as t, or the last representable value prior to the insertion of the leap second if t represents a time point during a leap second insertion. </p>
<h2>See also</h2>
<p>from_sys converts sys_time to utc_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
