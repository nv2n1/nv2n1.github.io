---
title: "stdchronogps_clockfrom_utc(3)"
name: "stdchronogps_clockfrom_utc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronogps_clockfrom_utc/"
description: "std::chrono::gps_clock::from_utc – std::chrono::gps_clock::from_utc"
---

<p>std::chrono::gps_clock::from_utc &#8211; std::chrono::gps_clock::from_utc</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;

static std::chrono::gps_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;(since C++ 20)

    from_utc(const std::chrono::utc_time&lt;Duration&gt; &amp;) noexcept;</code></pre>
<p>Converts the utc_time t to a gps_time representing the same point in time. </p>
<h2>Return value</h2>
<p>A std::chrono::gps_time representing the same point in time as t, computed as if by constructing a value of the return type from t.time_since_epoch() and subtracting 315964809s. (315964809 is the number of seconds between the epochs of the two clocks: 1980-01-06 00:00:00 UTC for gps_clock and 1970-01-01 00:00:00 UTC for utc_clock.) </p>
<h2>See also</h2>
<p>to_utc converts a gps_time to utc_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
