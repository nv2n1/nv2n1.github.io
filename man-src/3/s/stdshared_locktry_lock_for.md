---
title: "stdshared_locktry_lock_for(3)"
name: "stdshared_locktry_lock_for"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_locktry_lock_for/"
---

std::shared_lock&lt;Mutex&gt;::try_lock_for - std::shared_lock&lt;Mutex&gt;::try_lock_for

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep, class Period&gt;
(since C++ 14)

    bool try_lock_for(const std::chrono::duration&lt;Rep, Period&gt; &amp;timeout_duration);</code></pre> 
Tries to lock the associated mutex in shared mode. Blocks until specified timeout_duration has elapsed or the lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. Effectively calls mutex()-&gt;try_lock_shared_for(timeout_duration). 
This function may block for longer than timeout_duration due to scheduling or resource contention delays. 
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments. 
std::system_error is thrown if there is no associated mutex or if the mutex is already locked. 

<h2>Parameters</h2>

timeout_duration - maximum duration to block for

<h2>Return value</h2>

true if the ownership of the mutex has been acquired successfully, false otherwise. 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;try_lock_shared_for(timeout_duration) 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the mutex is already locked, std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attempts to lock the associated TimedLockable mutex, returns if the mutex has been unavailable for the specified time duration 
try_lock_for <i>(public member function of std::unique_lock&lt;Mutex&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the associated mutex 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, until a specified time point 
try_lock_until <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
