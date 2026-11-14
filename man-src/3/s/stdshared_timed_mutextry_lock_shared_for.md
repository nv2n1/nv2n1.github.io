---
title: "stdshared_timed_mutextry_lock_shared_for(3)"
name: "stdshared_timed_mutextry_lock_shared_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_timed_mutextry_lock_shared_for/"
---

std::shared_timed_mutex::try_lock_shared_for - std::shared_timed_mutex::try_lock_shared_for

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep, class Period&gt;
(since C++ 14)

    bool try_lock_shared_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;timeout_duration);</code></pre> 
Tries to lock the mutex in shared mode. Blocks until specified timeout_duration has elapsed or the shared lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. 
If timeout_duration is less or equal timeout_duration.zero(), the function behaves like try_lock_shared(). 
This function may block for longer than timeout_duration due to scheduling or resource contention delays. 
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments. 
As with try_lock_shared(), this function is allowed to fail spuriously and return false even if the mutex was not locked by any other thread at some point during timeout_duration. 
Prior unlock() operation on the same mutex synchronizes-with (as defined in std::memory_order) this operation if it returns true. 
If try_lock_shared_for is called by a thread that already owns the mutex in any mode (shared or exclusive), the behavior is undefined. 

<h2>Parameters</h2>

timeout_duration - maximum duration to block for

<h2>Return value</h2>

true if the lock was acquired successfully, otherwise false. 

<h2>Exceptions</h2>

Any exception thrown by clock, time_point, or duration during the execution (clocks, time points, and durations provided by the standard library never throw)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex is not available 
try_lock_shared <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex for shared ownership, returns if the mutex has been 
try_lock_shared_until unavailable until specified time point has been reached 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the mutex, returns if the mutex has been 
try_lock_for unavailable for the specified timeout duration 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
