---
title: "stdthis_threadsleep_until(3)"
name: "stdthis_threadsleep_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthis_threadsleep_until/"
---

std::this_thread::sleep_until - std::this_thread::sleep_until

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;thread&gt;

    template &lt;class Clock, class Duration&gt;
    (since C++ 11)

        void sleep_until(const std::chrono::time_point&lt;Clock, Duration&gt; &amp;sleep_time);</code></pre> 
Blocks the execution of the current thread until specified sleep_time has been reached. 
The clock tied to sleep_time is used, which means that adjustments of the clock are taken into account. Thus, the duration of the block might, but might not, be less or more than sleep_time - Clock::now() at the time of the call, depending on the direction of the adjustment. The function also may block for longer than until after sleep_time has been reached due to scheduling or resource contention delays. 

<h2>Parameters</h2>

sleep_time - time to block until

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

Any exception thrown by Clock or Duration (clocks and durations provided by the standard library never throw)

<h2>See also</h2>

sleep_for stops the execution of the current thread for a specified time duration 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
