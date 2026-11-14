---
title: "stdshared_timed_mutextry_lock_shared_until(3)"
name: "stdshared_timed_mutextry_lock_shared_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_timed_mutextry_lock_shared_until/"
---

std::shared_timed_mutex::try_lock_shared_until - std::shared_timed_mutex::try_lock_shared_until

<h2>Synopsis</h2>

<pre><code>template &lt;class Clock, class Duration&gt;
(since C++ 14)

    bool try_lock_shared_until(const std::chrono::time_point&lt;Clock, Duration&gt; &amp;timeout_time);</code></pre> 
Tries to lock the mutex in shared mode. Blocks until specified timeout_time has been reached or the lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. 
If timeout_time has already passed, this function behaves like try_lock_shared(). 
The clock tied to timeout_time is used, which means that adjustments of the clock are taken into account. Thus, the maximum duration of the block might, but might not, be less or more than timeout_time - Clock::now() at the time of the call, depending on the direction of the adjustment. The function also may block for longer than until after timeout_time has been reached due to scheduling or resource contention delays. 
As with try_lock_shared(), this function is allowed to fail spuriously and return false even if the mutex was not locked by any other thread at some point before timeout_time. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. 
If try_lock_shared_until is called by a thread that already owns the mutex in any mode (shared or exclusive), the behavior is undefined. 

<h2>Parameters</h2>

timeout_time - maximum time point to block until

<h2>Return value</h2>

true if the shared lock ownership was acquired successfully, otherwise false. 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex has been 
try_lock_until unavailable until specified time point has been reached 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex is not available 
try_lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex has been 
try_lock_shared_for unavailable for the specified timeout duration 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
