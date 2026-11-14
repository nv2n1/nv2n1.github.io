---
title: "stdunique_locktry_lock_until(3)"
name: "stdunique_locktry_lock_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_locktry_lock_until/"
---

std::unique_lock&lt;Mutex&gt;::try_lock_until - std::unique_lock&lt;Mutex&gt;::try_lock_until

<h2>Synopsis</h2>

<pre><code>template &lt;class Clock, class Duration&gt;
(since C++ 11)

    bool try_lock_until(const std::chrono::time_point&lt;Clock, Duration&gt; &amp;timeout_time);</code></pre> 
Tries to lock the associated mutex. Blocks until specified timeout_time has been reached or the lock is acquired, whichever comes first. On successful lock acquisition returns true, otherwise returns false. May block for longer than until timeout_time has been reached. 
Effectively calls mutex()-&gt;try_lock_until(timeout_time) 
std::system_error is thrown if there is no associated mutex or if the mutex is already locked. 

<h2>Parameters</h2>

timeout_time - maximum time point to block until

<h2>Return value</h2>

true if the ownership of the mutex has been acquired successfully, false otherwise. 

<h2>Exceptions</h2>

* Any exceptions thrown by mutex()-&gt;try_lock_until(timeout_time) 

 

 
* If there is no associated mutex, std::system_error with an error code of std::errc::operation_not_permitted 

 

 
* If the mutex is already locked, std::system_error with an error code of std::errc::resource_deadlock_would_occur

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locks the associated mutex 
lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tries to lock the associated mutex, returns if the mutex is not available 
try_lock <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;attempts to lock the associated TimedLockable mutex, returns if the mutex has been unavailable for the specified time duration 
try_lock_for <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlocks the associated mutex 
unlock <i>(public member function)</i> 
