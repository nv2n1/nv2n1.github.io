---
title: "stdunique_locktry_lock_for(3)"
name: "stdunique_locktry_lock_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_locktry_lock_for/"
---

std::unique_lock&lt;Mutex&gt;::try_lock_for - std::unique_lock&lt;Mutex&gt;::try_lock_for

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep, class Period&gt;
(since C++ 11)

    bool try_lock_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;timeout_duration);</code></pre> 
Tries to lock the associated mutex. Blocks until specified timeout_duration has elapsed or the lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. Effectively calls mutex()-&gt;try_lock_for(timeout_duration). 
This function may block for longer than timeout_duration due to scheduling or resource contention delays. 
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments. 
std::system_error is thrown if there is no associated mutex or if the mutex is already locked by this std::unique_lock. 

<h2>Parameters</h2>

timeout_duration - maximum duration to block for

<h2>Return value</h2>

true if the ownership of the mutex has been acquired successfully, false otherwise. 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;try_lock_for(timeout_duration) 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the mutex is already locked, std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the associated mutex 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated TimedLockable mutex, returns if the mutex has been unavailable until specified time point has been reached 
try_lock_until <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
