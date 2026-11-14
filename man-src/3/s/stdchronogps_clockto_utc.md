---
title: "stdchronogps_clockto_utc(3)"
name: "stdchronogps_clockto_utc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronogps_clockto_utc/"
description: "std::chrono::gps_clock::to_utc – std::chrono::gps_clock::to_utc"
---

<p>std::chrono::gps_clock::to_utc &#8211; std::chrono::gps_clock::to_utc</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;

static std::chrono::utc_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;(since C++ 20)

    to_utc(const std::chrono::gps_time&lt;Duration&gt; &amp;t) noexcept;</code></pre>
<p>Converts the gps_time t to a utc_time representing the same point in time. </p>
<h2>Return value</h2>
<p>A std::chrono::utc_time representing the same point in time as t, computed as if by constructing a value of the return type from t.time_since_epoch() and adding 315964809s. (315964809 is the number of seconds between the epochs of the two clocks: 1980-01-06 00:00:00 UTC for gps_clock and 1970-01-01 00:00:00 UTC for utc_clock.) </p>
<h2>See also</h2>
<p>from_utc converts a utc_time to gps_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
