---
title: "stdchronofile_clock(3)"
name: "stdchronofile_clock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronofile_clock/"
description: "std::chrono::file_clock – std::chrono::file_clock"
---

<p>std::chrono::file_clock &#8211; std::chrono::file_clock</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;chrono&gt;

using file_clock = /* see below */;  (since C++20)</code></pre>
<p>std::chrono::file_clock is an alias for the clock used for std::filesystem::file_time_type. Its epoch is unspecified.<br />
file_clock meets the TrivialClock requirements.<br />
Time point family </p>
<pre><code>Defined in namespace std::chrono

template&lt;class Duration&gt;                                                       (since C++20)

using file_time = std::chrono::time_point&lt;std::chrono::file_clock, Duration&gt;;

</code></pre>
<p>operator&lt;&lt;_(std::chrono::file_time) performs stream output on a file_time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20)<br />
from_stream_(std::chrono::file_time) parses a file_time from a stream according to the provided format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20)<br />
to_stream_(std::chrono::file_time) outputs a file_time into a stream according to the provided format<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
<h2>Member types</h2>
<p>Member type Definition<br />
rep signed arithmetic type representing the number of ticks in the clock&#8217;s duration<br />
period a std::ratio type representing the tick period of the clock, in seconds<br />
duration std::chrono::duration&lt;rep, period&gt;, capable of representing negative durations<br />
time_point std::chrono::time_point&lt;std::chrono::file_clock&gt;</p>
<h2>Member constants</h2>
<p>constexpr bool is_steady true if the time between ticks is always constant, i.e. calls to now() return values that increase monotonically even in case of some external clock adjustment, otherwise false<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>file_clock provides exactly one of the following two pairs of static member functions: </p>
<p>* to_utc and from_utc; or<br />
* to_sys and from_sys. </p>
<p>now returns a std::chrono::time_point representing the current point in time<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>to_utc converts between file_time and utc_time<br />
from_utc <i>(public static member function)</i> </p>
<p><code>[static]</code> (optional) </p>
<p>to_sys converts between file_time and sys_time<br />
from_sys <i>(public static member function)</i> </p>
<p><code>[static]</code> (optional)</p>
