---
title: "stdchronotai_clock(3)"
name: "stdchronotai_clock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotai_clock/"
description: "std::chrono::tai_clock – std::chrono::tai_clock"
---

<p>std::chrono::tai_clock &#8211; std::chrono::tai_clock</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
class tai_clock; <i>(since C++20)</i><br />
The clock std::chrono::tai_clock is a Clock that represents International Atomic Time (TAI). It measures time since 00:00:00, 1 January 1958, and is offset 10 seconds ahead of UTC at that date (i.e., its epoch, 1958-01-01 00:00:00 TAI, is 1957-12-31 23:59:50 UTC).<br />
Leap seconds are not inserted into TAI. Thus, every time a leap second is inserted into UTC, UTC falls another second behind TAI. As of December 2017, UTC is 37 seconds behind TAI, reflecting the 10-second initial offset and the 27 leap seconds inserted between 1958 and 2017. Thus, 2018-01-01 00:00:00 UTC is equivalent to 2018-01-01 00:00:37 TAI.<br />
tai_clock meets the Clock requirements. It does not meet the TrivialClock requirements unless the implementation can guarantee that now() does not throw an exception.<br />
Time point family </p>
<pre><code>Defined in namespace std::chrono

template&lt;class Duration&gt;                                                     (since C++20)

using tai_time = std::chrono::time_point&lt;std::chrono::tai_clock, Duration&gt;;

using tai_seconds = tai_time&lt;std::chrono::seconds&gt;;                          (since C++20)

</code></pre>
<p>operator&lt;&lt;_(std::chrono::tai_time) performs stream output on a tai_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20)<br />
from_stream_(std::chrono::tai_time) parses a tai_time from a stream according to the provided format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20)<br />
to_stream_(std::chrono::tai_time) outputs a tai_time into a stream according to the provided format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
<h2>Member types</h2>
<p>Member type Definition<br />
rep signed arithmetic type representing the number of ticks in the clock&#8217;s duration<br />
period a std::ratio type representing the tick period of the clock, in seconds<br />
duration std::chrono::duration&lt;rep, period&gt;, capable of representing negative durations<br />
time_point std::chrono::time_point&lt;std::chrono::tai_clock&gt;</p>
<h2>Member constants</h2>
<p>constexpr bool is_steady true if the time between ticks is always constant, i.e. calls to now() return values that increase monotonically even in case of some external clock adjustment, otherwise false<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>now returns a std::chrono::time_point representing the current point in time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>to_utc converts tai_time to utc_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>from_utc converts utc_time to tai_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
