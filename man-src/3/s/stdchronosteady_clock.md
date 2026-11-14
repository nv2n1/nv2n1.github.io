---
title: "stdchronosteady_clock(3)"
name: "stdchronosteady_clock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronosteady_clock/"
description: "std::chrono::steady_clock – std::chrono::steady_clock"
---

<p>std::chrono::steady_clock &#8211; std::chrono::steady_clock</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;chrono&gt;<br />
class steady_clock; <i>(since C++11)</i><br />
Class std::chrono::steady_clock represents a monotonic clock. The time points of this clock cannot decrease as physical time moves forward and the time between ticks of this clock is constant. This clock is not related to wall clock time (for example, it can be time since last reboot), and is most suitable for measuring intervals.<br />
std::chrono::steady_clock meets the requirements of TrivialClock. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
rep arithmetic type representing the number of ticks in the clock&#8217;s duration<br />
period a std::ratio type representing the tick period of the clock, in seconds<br />
duration std::chrono::duration&lt;rep, period&gt;<br />
time_point std::chrono::time_point&lt;std::chrono::steady_clock&gt;</p>
<h2>Member constants</h2>
<p>constexpr bool is_steady steady clock flag, always true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>now returns a time_point representing the current value of the clock<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>See also</h2>
<p>system_clock wall clock time from the system-wide realtime clock<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++11)</i><br />
high_resolution_clock the clock with the shortest tick period available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++11)</i> </p>
